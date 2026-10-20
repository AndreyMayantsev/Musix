import logging

from fastapi import FastAPI

from app.core.logger import setup_logging

# --- initialize logging first ---
setup_logging()
logger = logging.getLogger("musix")

from app.api.tracks.routes import tracks_router
from app.api.system.routes import system_router
from app.baseapp.app_settings import Settings
from app.services.music_server import MusicServer

"""
Use 'uvicorn main:app --reload' to local run 
"""

# --- initialize ---
app = FastAPI()
app.settings = Settings()
app.state.logger = logger
logger.info(f"Settings: {app.settings}")

# --- Loading server ---
_home_path = app.settings.get_setting("HomePath")
home_path = _home_path if _home_path else "D:\\mp3\\mp3"
logger.info(f"Set HOMEPATH to: {home_path}")
app.state.music_server = MusicServer(home_path)

# --- include routes ---
app.include_router(tracks_router)
app.include_router(system_router)
