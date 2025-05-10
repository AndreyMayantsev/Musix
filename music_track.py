import os
import music_tag


class MusicTrack:

    def __init__(self, track_absolute_path: str):
        _f = music_tag.load_file(track_absolute_path)
        # base information about track
        self.file_path: str = self.check_string_param(track_absolute_path)
        self.artist: str = self.check_string_param(_f['artist'])
        self.album: str = self.check_string_param(_f['album'])
        self.title: str = self.check_string_param(_f['title'])
        # technical details (const)
        self.bit_rate: str = self.check_string_param(_f['#bitrate'])
        self.length = self.check_string_param(_f['#length'])

    def check_string_param(self, param):
        if param:
            return str(param)
        else:
            return "Unknown"

    def get_track_info(self):
        track_info = {
            "file": self.file_path,
            "artist": self.artist,
            "album": self.album,
            "title": self.title,
            "bit_rate": self.bit_rate,
            "length": self.length
        }

        return track_info
