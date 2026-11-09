from pathlib import Path
from typing import Dict

import musix_app.models.models as models
from musix_app.core.hash_id import get_hex_id
from musix_app.core.logger import get_logger
from sqlmodel import SQLModel, create_engine, Session, select

from musix_app.core.music_track_loader import MusicTrackLoader

log = get_logger("mu6.database")


class DataBaseService:

    def __init__(self):
        sqlite_url = "sqlite:///./database.db"
        log.info(f"Connecting to database: {sqlite_url}")
        self.engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

    def create_db_and_tables(self):
        log.info("Making Database tables")
        SQLModel.metadata.create_all(self.engine)

    def get_session(self):
        with Session(self.engine) as session:
            yield session

    def sync_subfolders(self, root_directory: Path):
        log.info(f"Making folders structure in DB")
        root = Path(root_directory)
        with Session(self.engine) as session:
            for item in root.rglob("*"):
                if item.is_dir():
                    full_path = str(item.resolve())  # Реальный путь, например: "D:\Music\Linkin Park"
                    folder_id = get_hex_id(full_path)
                    exists = session.get(models.FolderModel, folder_id)
                    if not exists:
                        folder_record = models.FolderModel(
                            id=folder_id,
                            path=full_path
                        )
                        session.add(folder_record)

            session.commit()

    def sync_all_tracks(self, root_directory: Path = None):
        with Session(self.engine) as session:
            folders = session.exec(select(models.FolderModel)).all()
            existing_track_ids = set(session.exec(select(models.MusicTrackModel.id)).all())
            added_count = 0

            for folder in folders:
                folder_path = Path(folder.path)
                if not folder_path.exists():
                    continue

                for file_path in folder_path.glob("*.mp3"):
                    abs_path = str(file_path.resolve())
                    track_id = get_hex_id(abs_path)

                    if track_id in existing_track_ids:
                        continue

                    try:
                        loader = MusicTrackLoader(abs_path)
                        track_model = loader.music_track
                        track_model.folder_id = folder.id
                        session.add(track_model)
                        existing_track_ids.add(track_id)
                        added_count += 1

                    except Exception as e:
                        log.error(f"File loading error >>> {abs_path}: {e}")

            if added_count > 0:
                session.commit()
                log.info(f"DB updated, added {added_count} tracks")
            else:
                log.info("No new tracks founded")

    def get_all_tracks(self):
        with Session(self.engine) as session:
             return session.exec(select(models.MusicTrackModel)).all()

    def get_track(self, track_id: str):
        with Session(self.engine) as session:
             return session.get(models.MusicTrackModel, track_id)

# Service instance
db_service = DataBaseService()