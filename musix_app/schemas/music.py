import datetime
from enum import Enum
from typing import Generic, TypeVar, Dict
from pydantic import BaseModel, Field, field_validator


class ResponseType(Enum):
    OK = "success"
    SystemError = "error"
    NetworkError = "error"
    UndefinedError = "error"


T = TypeVar('T')


class BaseResponse(BaseModel, Generic[T]):
    type: ResponseType = ResponseType.OK
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.now)
    data: T


class TrackInfo(BaseModel):
    file: str = Field(description="Полный путь к файлу")
    artist: str = Field(description="Исполнитель")
    album: str = Field(description="Альбом")
    title: str = Field(description="Название трека")
    bitrate: int = Field(description="Битрейт в bps")
    duration: float = Field(description="Длительность в секундах")

    @field_validator('bitrate', mode='before')
    def clean_bitrate(cls, v):
        if isinstance(v, str):
            v = ''.join(filter(str.isdigit, v))
        return int(v) if v else 0

    @field_validator('duration', mode='before')
    def clean_duration(cls, v):
        try:
            return float(v)
        except (ValueError, TypeError):
            return 0.0


MusicListData = Dict[int, TrackInfo]
