import logging
import os.path
import time

from musix_app.core.hash_id import get_id, get_hex_id
from musix_app.core.music_scanner import MusicScanner
from pathlib import Path


log = logging.getLogger("music.service")


class MusicService:

    def __init__(self, music_folder=None):

        self.subfolders = {}
        self.tracks = {}
        self.home_path = Path(music_folder)

        if not music_folder:
            raise FileNotFoundError(f"DIRECTORY_NOT_SET: {self.folder}")

        if music_folder:
            self.track_list = {}
            self.folder = os.path.join(music_folder)
            if not os.path.exists(self.folder):
                raise FileNotFoundError(f"DIRECTORY_NOT_FOUND: {self.folder}")
            self.set_music_folder(music_folder)
            self.__get_music_subfolders()

    def __get_music_subfolders(self):

        all_directories = [str(p) for p in self.home_path.rglob('*') if p.is_dir()]
        for dir in all_directories:
            _path = str(dir)
            _folder_id = get_hex_id(_path)
            print(f"Scanning dir: {dir} / {_folder_id}")
            self.subfolders[_folder_id] = {"id": _folder_id, "path": _path}
        print(f"PATHS:\n{self.subfolders}")

    def set_music_folder(self, music_folder):

        self.folder = os.path.join(music_folder)
        if not os.path.exists(self.folder):
            raise FileNotFoundError(f"DIRECTORY_NOT_FOUND: {self.folder}")

        begin_time = time.time()
        log.info(f"Scanning music folder: {self.folder}")
        self.track_list = MusicScanner().scan_folder(self.folder)
        execution_time = round((time.time() - begin_time), 3)
        log.info(f"Scan complete: {len(self.track_list)} tracks founded. Operation has complete in: { execution_time } sec.")

    def update_track_list(self):
        self.track_list = MusicScanner().scan_folder(self.folder)
        log.info(f"Track list updated: {len(self.track_list)} tracks")

    def get_track_list(self):
        return self.track_list

    def get_track(self, track_id):
        return self.track_list.get(int(track_id))

    def get_track_path(self, track_id):
        t = self.get_track(track_id)
        try:
            return t.file
        except (KeyError, TypeError):
            return None
