from musix_app.app_server import AppServer  # укажите ваш правильный путь к AppServer
from musix_app.services.music_service import MusicService
from musix_app.services.apps_service import AppService
from musix_app.services.system_service import SystemService
from musix_app.core.app_settings import Settings

_server = AppServer(
    music_service=MusicService(),
    app_service=AppService(),
    system_service=SystemService(),
    app_settings=Settings()
)

def get_server() -> AppServer:
    return _server