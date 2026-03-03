import datetime
import json

from app.services.music_scanner import MusicScanner
from app.baseapp.app_settings import Settings


class MusicServer:

    def __init__(self, music_folder):
        self.folder = music_folder
        self.track_list = MusicScanner().scan_folder(self.folder)
        self.settings = Settings(settings_file=".music_cache")
        self.caching()

    def update_track_list(self):
        self.track_list = MusicScanner().scan_folder(self.folder)

    def caching(self):
        self.settings.set_setting('__CACHE_DATE', str(datetime.datetime.now()))
        self.settings.set_setting('__CACHE_LIST', json.dumps(self.track_list))
        self.settings.save_settings()

    def get_track_list(self):
        return self.track_list

    def get_track(self, track_id):
        return self.track_list.get(track_id)

    def get_track_path(self, track_id):
        t = self.get_track(track_id)
        return t['file']
