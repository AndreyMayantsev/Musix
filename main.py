import logging

from contextlib import asynccontextmanager
from fastapi import FastAPI
from musix_app.core.logger import setup_logging
from musix_app.services.database_service import db_service

setup_logging()
logger = logging.getLogger("musix")

from musix_app.api.tracks.routes import tracks_router
from musix_app.api.system.routes import system_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("--------- start ----------")
    db_service.create_db_and_tables()

    yield

    print("--------- stop ----------")
    db_service.engine.dispose()


"""
Use 'uvicorn main:app --reload' to local run 
"""
# --- Make FastAPI ---
app = FastAPI(lifespan=lifespan)

# --- include routes ---
app.include_router(tracks_router)
app.include_router(system_router)
