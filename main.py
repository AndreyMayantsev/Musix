import logging

from fastapi import FastAPI

from musix_app.app_server import AppServer
from musix_app.core.logger import setup_logging
from musix_app.services.apps_service import AppService
from musix_app.services.system_service import SystemService
from musix_app.core.app_settings import Settings
from musix_app.services.music_service import MusicService

# --- initialize logging first ---
setup_logging()
logger = logging.getLogger("musix")

from musix_app.api.tracks.routes import tracks_router
from musix_app.api.system.routes import system_router


"""
Use 'uvicorn main:app --reload' to local run 
"""
app = FastAPI()
app.state
server_instance = AppServer(
    music_service=MusicService(),
    app_service=AppService(),
    system_service=SystemService(),
    app_settings=Settings()
)

app.state.app_server = server_instance

# --- include routes ---
app.include_router(tracks_router)
app.include_router(system_router)
