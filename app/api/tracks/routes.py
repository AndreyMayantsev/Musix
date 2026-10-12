import os
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import StreamingResponse

from app.api.composer import BaseResponse
from app.api.music_list import MusicList
from app.schemas.music import MusicListData

tracks_router = APIRouter()

@tracks_router.get("/tracks", response_model=BaseResponse[MusicListData])
async def get_files(request: Request):
    music_server = request.app.state.music_server
    return MusicList(music_server).make_response()


@tracks_router.get(
    "/stream/{path:path}",
    response_class=StreamingResponse,
    responses={
        200: {
            "content": {"audio/mpeg": {}},
            "description": "Успешное воспроизведение аудио-трека",
        }
    }
)
async def stream_file(path: str, request: Request):
    print(f"..> streaming track: {path}")

    music_server = request.app.state.music_server
    file_path = music_server.get_track_path(path)
    print(file_path)

    if not file_path:
        raise HTTPException(status_code=404, detail="Track not found! Check ID and try again.")

    def generate():
        chunk_size = 1024 * 16
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                yield chunk

    file_size = os.path.getsize(file_path)
    mime_type = "audio/mpeg"

    headers = {
        'Content-Length': str(file_size),
        'Accept-Ranges': 'bytes'
    }

    return StreamingResponse(generate(), media_type=mime_type, headers=headers)