import json

from api import about, music_list
from baseapp import logging
from baseapp import app_settings
from music_server import MusicServer
from flask import Flask
from flask_socketio import SocketIO, emit

settings = app_settings.Settings()

music_server = MusicServer('D:\\musoc\\mp3')
http_server = Flask('MU6')

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
    # Отправить файл по WebSocket
    file_path = music_server.get_track_path(path)
    with open(file_path, "rb") as f:
        chunk_size = 1024  # Размер кусочка в байтах
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            emit("stream_file", chunk)


@http_server.route("/")
def root():
    return """
    <h1>Welcome to Mu6 api router</h1>
    <h2>«Winamp, it really whips the llama's ass!»</h2>
    <br>
    <b>/system</b> - system info<br>
    <b>/tracklist</b> - list of all tracks in json<br>
    """


http_server.run()
