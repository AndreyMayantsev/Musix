import logging

from fastapi import FastAPI
from musix_app.core.logger import setup_logging


# --- initialize logging first ---
setup_logging()
logger = logging.getLogger("musix")

from musix_app.api.tracks.routes import tracks_router
from musix_app.api.system.routes import system_router


"""
Use 'uvicorn main:app --reload' to local run 
"""
# --- Make FastAPI ---
app = FastAPI()

# --- include routes ---
app.include_router(tracks_router)
app.include_router(system_router)
