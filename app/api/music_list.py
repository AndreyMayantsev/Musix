class MusicList:
    # List of tracks

    def __init__(self, music_server):
        self.server = music_server

    def make_response(self):
        try:
            resp = self.server.get_track_list()
            return {"data": resp}
        except SystemError as error:
            return {"data": error}
        except Exception as error:
            return {"data": error}
