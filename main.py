import json
import os
from api import about, music_list
from baseapp import logging
from baseapp import app_settings
from music_server import MusicServer
from flask import Flask, Response
from flask_cors import cross_origin, CORS


music_folder = 'D:\\musoc\\mp3'

# Application settings manager
settings = app_settings.Settings()
if settings.get_setting('HomePath'):
    music_folder = settings.get_setting('HomePath')

# Music server manager
music_server = MusicServer(music_folder)
# Flask run
http_server = Flask('MU6')
CORS(http_server)

print("*" * 30)
print(music_server.get_track_list())
print("*" * 30)


@http_server.route("/system")
def about_system():
    return about.SystemInfo().make_response()


@http_server.route("/tracklist")
def get_files():
    return music_list.MusicList(music_server).make_response()


@http_server.route("/stream/<path:path>")
def stream_file(path):
    print(f"LOADING ID: {path}")
    file_path = music_server.get_track_path(path)

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


@http_server.route("/")
def root():
    return """
    <h1>Welcome to Mu6 api router</h1>
    <h2>«Winamp, it really whips the llama's ass!»</h2>
    <br>
    <b>/system</b> - system info<br>
    <b>/tracklist</b> - list of all tracks in json<br>
    <b>/stream/<:id></b> - get track by ID<br>
    """


http_server.run()
