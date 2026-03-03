from flask import Flask
from flask_cors import cross_origin, CORS
from app.tracks.routes import tracks_bp
from app.system.routes import system_bp
from app.baseapp import app_settings, logging
from app.services.music_server import MusicServer


def create_app():
    # Flask run
    http_server = Flask('MU6')

    CORS(http_server)

    http_server.register_blueprint(tracks_bp)
    http_server.register_blueprint(system_bp)

    music_folder = 'D:\\musoc\\mp3'

    # Application settings manager
    settings = app_settings.Settings()
    if settings.get_setting('HomePath'):
        music_folder = settings.get_setting('HomePath')

    # Music server manager
    http_server.music_server = MusicServer(music_folder)

    print("*" * 30)
    print(http_server.music_server.get_track_list())
    print("*" * 30)

    log = logging.Log("main")

    return http_server
