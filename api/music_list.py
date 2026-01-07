import json
from dataclasses import dataclass
from baseapp.system_info import get_system_info


class MusicList:

    def __init__(self, music_server):
        self.system = get_system_info()
        self.server = music_server

    def make_response(self):
        resp = self.server.get_track_list()
        return json.dumps(resp)
