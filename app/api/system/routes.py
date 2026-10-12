from fastapi import APIRouter, Response, HTTPException
from app.api.about import SystemInfo
from app.api.composer import BaseResponse

system_router = APIRouter()

@system_router.get("/system", response_model=BaseResponse[dict])
def about_system():
    return SystemInfo().make_response()

@system_router.get("/favicon.ico", include_in_schema=False)
def get_favicon():
    with open("icon.png", 'rb') as _favicon:
        favicon = _favicon.read()

    return Response(content=favicon, media_type="image/png")
