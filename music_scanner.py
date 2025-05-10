import music_tag
import os
from music_track import MusicTrack
from baseapp import base_filesystem


class MusicScanner:

    def __init__(self):
        self.bfs = base_filesystem.BaseFilesystem()

    def scan_folder(self, folder):
        """ Returns music list in json """
        files_list = self.bfs.get_files_list(folder, mask=".mp3")
        tracks_list = {}
        track_id = 0

        for file in files_list:
            _mt = MusicTrack(file)
            tracks_list[track_id] = _mt.get_track_info()
            track_id += 1

        return tracks_list

