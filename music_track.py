from dataclasses import dataclass


@dataclass
class MusicTrack:
    file_path: str
    artist: str
    album: str
    title: str
    bit_rate: int
    length: int

    def get_track_info(self):
        return {
            "file": self.file_path,
            "artist": self.artist,
            "album": self.album,
            "title": self.title,
            "bit_rate": self.bit_rate,
            "length": self.length
        }