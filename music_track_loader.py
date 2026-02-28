import json

import music_tag
import ftfy
import fix_codepage
from music_track import MusicTrack


class MusicTrackLoader:

    def __init__(self, track_absolute_path: str):
        _f = music_tag.load_file(track_absolute_path)
        # base information about track
        artist: str = self.__check_string_param(_f['artist'])
        album: str = self.__check_string_param(_f['album'])
        title: str = self.__check_string_param(_f['title'])
        # technical details (const)
        bit_rate: str = self.__check_string_param(_f['#bitrate'])
        length = self.__check_string_param(_f['#length'])
        self.music_track = MusicTrack(track_absolute_path, artist, album, title, bit_rate, length)

    def __check_string_param(self, param):
        if param:
            return str(param)
        else:
            return "Unknown"

    def get_track(self):
        return self.music_track

    def get_track_as_json(self):
        _json = {
            "file": self.music_track.file_path,
            "artist": fix_codepage.fix_track_tag(self.music_track.artist),
            "album": fix_codepage.fix_track_tag(self.music_track.album),
            "title": fix_codepage.fix_track_tag(self.music_track.title),
            "bitrate": int(self.music_track.bit_rate),
            "duration": float(self.music_track.length)
        }
        return _json
