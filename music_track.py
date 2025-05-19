class MusicTrack:

    def __init__(self, file_path, artist, album, title, bit_rate, length):
        # base information about track
        self.file_path: str = file_path
        self.artist: str = artist
        self.album: str = album
        self.title: str = title
        # technical details (const)
        self.bit_rate: int = bit_rate
        self.length: int = length

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
