from baseapp import base_filesystem
from uuid import uuid4
from music_track_loader import MusicTrackLoader


class MusicScanner:

    def __init__(self):
        self.bfs = base_filesystem.BaseFilesystem()

    def scan_folder(self, folder):
        """ Returns music list in json """
        files_list = self.bfs.get_all_objects_in_folder_list(folder, mask=".mp3")
        tracks_list = {}

        for file in files_list:
            _mtl = MusicTrackLoader(file)
            tracks_list[str(uuid4())] = _mtl.get_track_as_json()

        return tracks_list

