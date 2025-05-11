from baseapp import logging
from baseapp import app_settings
from music_scanner import MusicScanner
from wsgi import server

import json

if __name__ == "__main__":

    # Activate logging function
    log = logging.Log("MAIN")
    log.write_info("Start logging")
    # Activate settings mechanism
    settings = app_settings.Settings()
    # Trying to start web server
    music_list = MusicScanner().scan_folder("D:\\musoc\\mp3")

    log.write_info(f"{len(music_list)} tracks was founded")
    print(json.dumps(music_list))

    # try:
    #     server.run()
    # except Exception as ServerRunError:
    #     log.write_error(f"Error caused while service running, {ServerRunError}")
