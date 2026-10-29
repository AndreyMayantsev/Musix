import datetime
import logging
import os.path
import time

from musix_app.core.music_scanner import MusicScanner
from musix_app.core.app_settings import Settings

log = logging.getLogger("musix.server")


class MusicService:

    def __init__(self, music_folder=None):
        if music_folder:
            self.track_list = {}
            self.folder = os.path.join(music_folder)
            if not os.path.exists(self.folder):
                raise FileNotFoundError(f"DIRECTORY_NOT_FOUND: {self.folder}\nPlease check your settings in ~/.Musix")
            self.set_music_folder(music_folder)

    def set_music_folder(self, music_folder):

        self.folder = os.path.join(music_folder)
        if not os.path.exists(self.folder):
            raise FileNotFoundError(f"DIRECTORY_NOT_FOUND: {self.folder}\nPlease check your settings in ~/.Musix")

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
