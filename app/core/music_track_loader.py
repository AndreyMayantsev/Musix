import logging
import os
import music_tag

from app.core.fix_codepage import fix_track_tag
from app.models.music_track import MusicTrack

log = logging.getLogger("musix.loader")


class MusicTrackLoader:

    def __init__(self, track_absolute_path: str):
        log.info(f"Loading: {track_absolute_path}")
        _f = music_tag.load_file(track_absolute_path)

        artist = fix_track_tag(str(_f['artist'])) or "Unknown Artist"
        album = fix_track_tag(str(_f['album'])) or "Unknown Album"
        title = fix_track_tag(str(_f['title'])) or os.path.basename(track_absolute_path)

        bit_rate = _f['#bitrate']
        length = _f['#length']

        self.music_track = MusicTrack(
            file=track_absolute_path,
            artist=artist,
            album=album,
            title=title,
            bitrate=bit_rate,
            duration=length
        )
