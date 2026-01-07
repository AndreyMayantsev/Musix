from music_scanner import MusicScanner


class MusicServer:

    def __init__(self, music_folder):
        self.folder = music_folder
        self.track_list = MusicScanner().scan_folder(self.folder)

    def update_track_list(self):
        self.track_list = MusicScanner().scan_folder(self.folder)

    def get_track_list(self):
        return self.track_list

    def get_track(self, track_id):
        return self.track_list.get(track_id)

    def get_track_path(self, track_id):
        t = self.get_track(track_id)
        return t['file']
