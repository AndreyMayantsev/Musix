from baseapp import base_filesystem
from uuid import uuid4
import hashlib
from music_track_loader import MusicTrackLoader


class MusicScanner:

    def __init__(self):
        self.bfs = base_filesystem.BaseFilesystem()

    def scan_folder(self, folder):
        """ Returns music list in json """
        files_list = self.bfs.get_all_objects_in_folder_list(folder, mask=".mp3")
        tracks_list = {}

        for file in files_list:
            # get filepath as string
            _id_fname = str(file)
            # hashing for make stable id for files
            _id = hashlib.sha256(_id_fname.encode('utf-8')).hexdigest()
            # get track information
            _mtl = MusicTrackLoader(file)
            # add track to list with stable id
            tracks_list[_id] = _mtl.get_track_as_json()

        return tracks_list

