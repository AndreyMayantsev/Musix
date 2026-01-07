import json
from dataclasses import dataclass
from baseapp.system_info import get_system_info


@dataclass
class MusicList:

    def __init__(self, music_server):
        system: str = get_system_info()


    def make_response(self):
        folder = self.music_server
        resp = {
            "home_folder": {folder},
            "files": {}
        }
        return json.dumps(resp)
