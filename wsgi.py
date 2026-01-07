from api import about, music_list
from flask import Flask
from main import music_server, server


@server.route("/system")
def about_system():
    return about.SystemInfo().make_response()


@server.route("/build")
def get_files():
    return music_list.MusicList(music_server).make_response()
