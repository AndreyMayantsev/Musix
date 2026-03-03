from app.baseapp import base_filesystem
from uuid import uuid4
import hashlib
from app.services.music_track_loader import MusicTrackLoader


class MusicScanner:

    def __init__(self):
        self.bfs = base_filesystem.BaseFilesystem()

    def scan_folder(self, folder):
        """ Returns music list in json """
        _id_num = 0
        files_list = self.bfs.get_all_objects_in_folder_list(folder, mask=".mp3")
        tracks_list = {}

        for file in files_list:
            # get filepath as string
            # _id_fname = str(file)
            # hashing for make stable id for files
            # _id = hashlib.sha256(_id_fname.encode('utf-8')).hexdigest()
            # get track information
            _mtl = MusicTrackLoader(file)
            # add track to list with stable id
            tracks_list[str(_id_num)] = _mtl.get_track_as_json()
            _id_num += 1

        return tracks_list

