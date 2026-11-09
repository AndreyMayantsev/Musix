import logging
import os
import music_tag

from musix_app.core.fix_codepage import fix_track_tag
from musix_app.core.hash_id import get_hex_id
from musix_app.models.models import MusicTrackModel

log = logging.getLogger("mu6.loader")


class MusicTrackLoader:

    def __init__(self, track_absolute_path: str):
        log.info(f"Loading: {track_absolute_path}")
        _f = music_tag.load_file(track_absolute_path)

        artist = fix_track_tag(str(_f['artist'])) or "Unknown Artist"
        album = fix_track_tag(str(_f['album'])) or "Unknown Album"
        title = fix_track_tag(str(_f['title'])) or os.path.basename(track_absolute_path)

        bit_rate = _f['#bitrate'].value
        length = _f['#length'].value

        self.music_track = MusicTrackModel(
            id=get_hex_id(track_absolute_path),
            file=track_absolute_path,
            artist=artist,
            album=album,
            title=title,
            bitrate=bit_rate,
            duration=length
        )
