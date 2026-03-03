import os

from flask import Blueprint, Response, current_app, jsonify
from app.api.music_list import MusicList

tracks_bp = Blueprint('tracks', __name__)


@tracks_bp.route("/tracklist")
def get_files():

    return MusicList(current_app.music_server).make_response()


@tracks_bp.route("/stream/<path:path>")
def stream_file(path):
    print(f"LOADING ID: {path}")
    file_path = current_app.music_server.get_track_path(path)

    def generate():
        chunk_size = 1024 * 16
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                yield chunk

    # get size
    file_size = os.path.getsize(file_path)

    # get MIME-type
    mime_type = "audio/mpeg"

    # send file
    response = Response(generate(), mimetype=mime_type)
    response.headers['Content-Length'] = file_size
    response.headers['Accept-Ranges'] = 'bytes'

    return response
