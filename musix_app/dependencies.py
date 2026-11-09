from musix_app.app_server import AppServer
from musix_app.services.music_service import MusicService
from musix_app.services.apps_service import AppService
from musix_app.services.system_service import SystemService
from musix_app.services.database_service import db_service
from settings import settings


_server = AppServer(
    music_path=settings.music_path,
    music_service=MusicService(settings.music_path),
    database_service=db_service,
    app_service=AppService(),
    system_service=SystemService(),
    app_settings=settings
)


def get_server() -> AppServer:
    return _server