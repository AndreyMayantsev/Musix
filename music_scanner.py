from baseapp import base_filesystem
from music_track_loader import MusicTrackLoader


class MusicScanner:

    def __init__(self):
        self.bfs = base_filesystem.BaseFilesystem()

    def scan_folder(self, folder):
        """ Returns music list in json """
        files_list = self.bfs.get_all_objects_in_folder_list(folder, mask=".mp3")
        tracks_list = {}
        track_id = 0

        for file in files_list:
            _mtl = MusicTrackLoader(file)
            tracks_list[track_id] = _mtl.get_track_as_json()
            track_id += 1

        return tracks_list

