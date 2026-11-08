import json
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
        self.track_list = {}
        self.flat_track_list = {}
        self.music_scanner = MusicScanner()

        if not music_folder:
            raise FileNotFoundError(f"DIRECTORY_NOT_SET: {music_folder}")
        else:
            self.home_path = Path(music_folder)

            if not os.path.exists(self.home_path):
                raise FileNotFoundError(f"DIRECTORY_NOT_FOUND: {self.home_path}")

            self.__get_music_subfolders()
            log.info(f">>>>>>>>>> {self.subfolders}")
            self.__get_tracks_in_folders()
            log.info(f">>>>>>>>>> {self.track_list}")
            self.__build_flat_track_list()
            log.info(f">>>>>>>>>> {self.flat_track_list}")

    def __get_music_subfolders(self):

        all_directories = [str(p) for p in self.home_path.rglob('*') if p.is_dir()]
        for _dir in all_directories:
            _path = str(_dir)
            _folder_id = get_hex_id(_path)
            print(f"Scanning dir: {_dir} / {_folder_id}")
            self.subfolders[_folder_id] = {"name": _dir, "path": _path}

    def __get_tracks_in_folders(self):

        for sf, sd in self.subfolders.items():
            log.info(f'Scanning folder {sf} | {sd}')
            self.track_list[sf] = self.music_scanner.scan_folder(sd.get('path'))

    def __build_flat_track_list(self):
        track_counter = 0
        for id, track in self.track_list.items():
            self.flat_track_list[track_counter] = track.dump_model()
            track_counter += 1


    # def set_music_folder(self, music_folder):
    #
    #     self.folder = os.path.join(music_folder)
    #     if not os.path.exists(self.folder):
    #         raise FileNotFoundError(f"DIRECTORY_NOT_FOUND: {self.folder}")
    #
    #     begin_time = time.time()
    #     log.info(f"Scanning music folder: {self.folder}")
    #     self.track_list = MusicScanner().scan_folder(self.folder)
    #     execution_time = round((time.time() - begin_time), 3)
    #     log.info(f"Scan complete: {len(self.track_list)} tracks founded. Operation has complete in: { execution_time } sec.")

    def update_track_list(self):
        self.track_list = MusicScanner().scan_folder(self.folder)
        log.info(f"Track list updated: {len(self.track_list)} tracks")

    def get_track_list(self):
        return self.track_list

    def get_flat_track_list(self):
        return self.flat_track_list

    def get_track(self, track_id):
        return self.track_list.get(int(track_id))

    def get_track_path(self, track_id):
        t = self.get_track(track_id)
        try:
            return t.file
        except (KeyError, TypeError):
            return None
