from musix_app.core.logger import get_logger
from pydantic import BaseModel, Field


log = get_logger("mu6.appservice")


class AppInfo(BaseModel):
    id: str
    name: str
    info: str


class AppService:

    def __init__(self):
        self.registered_apps = {}

    def register_app(self, app_id: str, app_info: str):
        self.registered_apps[app_id] = app_info

    def get_registered_app(self, app_id: str):
        if app_id not in self.registered_apps:
            log.error(f" >>> Unknown app {app_id}, apps: {self.registered_apps}")
        return self.registered_apps.get(app_id)