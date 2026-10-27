from app.core import base_filesystem
from app.core.music_track_loader import MusicTrackLoader
# Импортируем наш алиас типа из предыдущего шага для аннотации
from app.schemas.music import MusicListData


class MusicScanner:

    def __init__(self):
        self.bfs = base_filesystem.BaseFilesystem()

    def scan_folder(self, folder) -> MusicListData:
        """ Возвращает словарь, где значения — это Pydantic-модели TrackInfo """
        _id_num = 0
        files_list = self.bfs.get_all_objects_in_folder_list(folder, mask=".mp3")
        tracks_list = {}

        for file in files_list:
            _mtl = MusicTrackLoader(file)
            tracks_list[_id_num] = _mtl.music_track
            _id_num += 1

        return tracks_list

