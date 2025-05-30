from baseapp import logging
from baseapp import app_settings
from music_scanner import MusicScanner
from wsgi import server

import json

if __name__ == "__main__":
    home_path = 'D:\\musoc\\mp3'
    # Activate logging function
    log = logging.Log("MAIN")
    log.write_info("Start logging")
    # Activate settings mechanism
    settings = app_settings.Settings()
    if settings.get_setting('HomePath'):
        home_path = settings.get_setting('HomePath')
    else:
        print(f"Setting HomePath not founded, set default folder: {home_path} ")
        log.write_warning(f"Setting HomePath not founded, set default folder: {home_path} ")

    # Trying to start web server
    music_list = MusicScanner().scan_folder("D:\\musoc\\mp3")

    log.write_info(f"{len(music_list)} tracks was founded")
    log.write_info(json.dumps(music_list))

    # try:
    #     server.run()
    # except Exception as ServerRunError:
    #     log.write_error(f"Error caused while service running, {ServerRunError}")
