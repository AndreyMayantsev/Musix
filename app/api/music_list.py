from .composer import ResponseType, compose_response


class MusicList:
    # List of tracks

    def __init__(self, music_server):
        self.server = music_server

    def make_response(self):
        try:
            resp = self.server.get_track_list()
            return compose_response(ResponseType.OK, resp)
        except SystemError as error:
            return compose_response(ResponseType.SystemError, error)
        except Exception as error:
            return compose_response(ResponseType.UndefinedError, error)
