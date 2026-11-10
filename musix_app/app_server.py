from pathlib import Path
from sqlmodel import SQLModel
from musix_app.core.logger import get_logger
from musix_app.services.apps_service import AppService
from musix_app.services.database_service import DataBaseService
from musix_app.services.music_service import MusicService
from musix_app.services.system_service import SystemService
from settings import Mu6Settings


log = get_logger("mu6.service")


class AppServer:

    server_counter = 0

    def __init__(
            self,
            music_path: Path,
            music_service: MusicService,
            database_service: DataBaseService,
            app_service: AppService,
            system_service: SystemService,
            app_settings: Mu6Settings
    ):
        self.__init_database(database_service, music_path)
        self.server_counter += 1
        self.app_settings = app_settings
        self.home_path = app_settings.music_path
        self.music_service = music_service
        self.app_service = app_service
        self.system_service = system_service
        log.info(f"AppServer init [{self.server_counter}]")

    def __init_database(self, database_service: DataBaseService, music_path: Path):
        self.database_service = database_service
        self.database_service.create_db_and_tables()
        self.database_service.sync_subfolders(music_path)
        self.database_service.sync_all_tracks()