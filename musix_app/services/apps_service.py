from pydantic import BaseModel, Field
from typing import Dict
import uuid


class AppInfo(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str
    info: str


class BaseResponse(BaseModel):
    reg_status: bool
    app: AppInfo


# Хранилище в памяти: ключ — UUID приложения
_apps_store: Dict[uuid.UUID, AppInfo] = {}


class AppService:

    def __init__(self):
        print("AppService")