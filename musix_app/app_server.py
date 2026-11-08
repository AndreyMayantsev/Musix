import logging

from pathlib import Path
from musix_app.core.logger import setup_logging
from musix_app.services.apps_service import AppService
from musix_app.services.music_service import MusicService
from musix_app.services.system_service import SystemService
from settings import Mu6Settings


class AppServer:

    server_counter = 0

    def __init__(
            self,
            music_service: MusicService,
            app_service: AppService,
            system_service: SystemService,
            app_settings: Mu6Settings
    ):
        self.server_counter += 1
        setup_logging()
        self.logger = logging.getLogger("mu6.app.server")
        self.app_settings = app_settings
        self.home_path = app_settings.music_path
        self.music_service = music_service
        # self.music_service.set_music_folder(self.home_path)
        self.app_service = app_service
        self.system_service = system_service
        self.logger.info(f"AppServer init [{self.server_counter}]")

    def __load_settings_home_path(self):
        _home_path = self.app_settings.get_setting("HomePath")
        home_path = _home_path if _home_path else "F:\\MUSIC"
        return Path(home_path)