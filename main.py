from fastapi import FastAPI
from app.api.tracks.routes import tracks_router
from app.api.system.routes import system_router
from app.baseapp.app_settings import Settings
from app.baseapp.logging import Log
from app.services.music_server import MusicServer

"""
Use 'uvicorn main:app --reload' to local run 
"""

# --- initialize ---
app = FastAPI()
app.settings = Settings()
app.log = Log("MUSIX", debug=True)
app.log.write_info(f"Settings: {app.settings}")

# --- Loading server ---
_home_path = app.settings.get_setting("HomePath")
home_path = _home_path if _home_path else "F:\\БАКАПЫ\\musoc"
app.log.write_info(f"Set HOMEPATH to: {home_path}")
app.state.music_server = MusicServer(home_path)

# --- include routes ---
app.include_router(tracks_router)
app.include_router(system_router)
