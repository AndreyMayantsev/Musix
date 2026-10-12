import datetime
from enum import Enum
from typing import Generic, TypeVar, Any
from pydantic import BaseModel, Field


class ResponseType(Enum):
    OK = "success"
    SystemError = "error"
    NetworkError = "error"
    UndefinedError = "error"


T = TypeVar('T')


class BaseResponse(BaseModel, Generic[T]):
    type: ResponseType = ResponseType.OK
    # По умолчанию автоматически подставится текущее время UTC
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    data: T
