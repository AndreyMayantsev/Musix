import os.path

from musix_app.core.logger import get_logger
from musix_app.core.hash_id import get_id, get_hex_id
# from musix_app.core.music_scanner import MusicScanner
from pathlib import Path


log = get_logger("mu6.service")


class MusicService:

    def __init__(self, root_path: Path):
        self.root_path = Path(root_path)
        # self.music_scanner = MusicScanner()
        if not self.root_path.exists() or not self.root_path.is_dir():
            raise FileNotFoundError(f"DIRECTORY NOT FOUND: {self.root_path}")

    def __get_music_subfolders(self):
        all_directories = [str(p) for p in self.root_path.rglob('*') if p.is_dir()]
        subfolders = {}
        for _dir in all_directories:
            _path = str(_dir)
            _folder_id = get_hex_id(_path)
            subfolders[_folder_id] = {"name": _dir, "path": _path}
        return subfolders

