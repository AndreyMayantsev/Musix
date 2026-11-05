from pydantic_settings import BaseSettings, SettingsConfigDict

class Mu6Settings(BaseSettings):

    app_name: str
    debug: bool = False
    music_path: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Mu6Settings()