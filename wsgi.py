from api import about, music_list
from flask import Flask


# making http server
server = Flask("Musix")


@server.route("/system")
def about_system():
    return about.SystemInfo().make_response()


@server.route("/build")
def get_files():
    return music_list.MusicList().make_response()
