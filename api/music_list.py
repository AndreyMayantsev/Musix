import json
from .composer import ResponseType, compose_response
from baseapp.system_info import get_system_info


class MusicList:

    def __init__(self, music_server):
        self.system = get_system_info()
        self.server = music_server

    def make_response(self):
        try:
            resp = self.server.get_track_list()
            return compose_response(ResponseType.OK, resp)
        except SystemError as error:
            return compose_response(ResponseType.SystemError, error)
        except Exception as error:
            return compose_response(ResponseType.UndefinedError, error)
