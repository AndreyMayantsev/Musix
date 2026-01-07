from baseapp import logging
from baseapp import app_settings
from music_server import MusicServer
from flask import Flask

import json


# making http server
server = Flask("Musix")

log = logging.Log('main')
# Default home_path
home_path = 'D:\\musoc\\mp3'

# Load settings and making scan home_path
settings = app_settings.Settings()
if settings.get_setting('HomePath'):
    home_path = settings.get_setting('HomePath')
else:
    print(f"Setting HomePath not founded, using default folder: {home_path} ")

# Load MusicServer
music_server = MusicServer(home_path)
tracks = music_server.get_track_list()

print(json.dumps(music_server.get_track_list()))

for track in tracks:
    print(tracks[track])

try:
    server.run()
except Exception as ServerRunError:
    log.write_error(f"Error caused while service running, {ServerRunError}")
