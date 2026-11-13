import uuid

from sqlmodel import Session

from musix_app.core.hash_id import get_hex_id
from musix_app.core.logger import get_logger
from pydantic import BaseModel, Field

from musix_app.models.models import ApplicationModel
from musix_app.services.database_service import DataBaseService

log = get_logger("mu6.appservice")


class AppService:

    def __init__(self):
        self.database_service = None
        self.registered_apps = {}

    def set_database_service(self, database_svc: DataBaseService):
        self.database_service = database_svc

    def register_app(self, os: str, name: str, info: str):
        if not self.database_service:
            raise Exception("Database service is None!")
        with Session(self.database_service.engine) as session:
            app_id = str(uuid.uuid4())
            app_fp = get_hex_id(os + name + info)
            existing = session.get(ApplicationModel, app_id)

            if existing:
                existing.os = os
                existing.info = info
                existing.name = info
                session.add(existing)
                session.commit()
                session.refresh(existing)
                return existing

            application = ApplicationModel(id=app_id, os=os, name=name, info=info, finger_print=app_fp)
            session.add(application)
            session.commit()
            session.refresh(application)

            return application.id
