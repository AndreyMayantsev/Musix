from fastapi import FastAPI
from app.api.tracks.routes import tracks_router
from app.api.system.routes import system_router
from app.baseapp.app_settings import Settings
from app.services.music_server import MusicServer

"""
Use 'uvicorn main:app --reload' to local run 
"""

app = FastAPI()
app.state.music_server = MusicServer("D:\\mp3\\mp3")
app.settings = Settings()

app.include_router(tracks_router)
app.include_router(system_router)