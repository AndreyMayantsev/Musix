from pydantic import BaseModel, Field, field_validator


class MusicTrack(BaseModel):
    file: str = Field(description="Полный путь к файлу")
    artist: str = Field(description="Исполнитель")
    album: str = Field(description="Альбом")
    title: str = Field(description="Название трека")
    bitrate: int = Field(description="Битрейт в bps")
    duration: float = Field(description="Длительность в секундах")

    # Валидатор: если битрейт или длительность пришли строкой, 
    # Pydantic сам попытается их сконвертировать, но мы можем подстраховаться
    @field_validator('bitrate', mode='before')
    def clean_bitrate(cls, v):
        if isinstance(v, str):
            # Убираем пробелы или kbps, если они есть, и берем только цифры
            v = ''.join(filter(str.isdigit, v))
        return int(v) if v else 0

    @field_validator('duration', mode='before')
    def clean_duration(cls, v):
        try:
            return float(v)
        except (ValueError, TypeError):
            return 0.0