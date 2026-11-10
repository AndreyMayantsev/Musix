import logging
from musix_app.core.logger import setup_logging

setup_logging()
logger = logging.getLogger("musix")

from musix_app.api.tracks.routes import tracks_router
from musix_app.api.system.routes import system_router
from fastapi import FastAPI

"""
Use 'uvicorn main:app --reload' to local run 
"""
# --- Make FastAPI ---
app = FastAPI()

# --- include routes ---
app.include_router(tracks_router)
app.include_router(system_router)
