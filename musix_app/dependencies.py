from musix_app.app_server import AppServer
from musix_app.services.music_service import MusicService
from musix_app.services.apps_service import AppService
from musix_app.services.system_service import SystemService
from settings import settings


_server = AppServer(
    music_service=MusicService(settings.music_path),
    app_service=AppService(),
    system_service=SystemService(),
    app_settings=settings
)


def get_server() -> AppServer:
    return _server