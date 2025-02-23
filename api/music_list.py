import json
import os
from baseapp.system_info import get_system_info
from baseapp.app_settings import Settings


class MusicList():

    def __init__(self):
        self.system = get_system_info()
        self.settings = Settings()

    def make_response(self):
        folder = self.settings.get_setting('music_folder')
        resp = {
            "home_folder": {folder},
            "files": {}
        }
        return json.dumps(resp)
