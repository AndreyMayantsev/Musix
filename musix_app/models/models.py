from sqlmodel import SQLModel, Field


class FolderModel(SQLModel, table=True):
    __tablename__ = "folders"

    id: str = Field(description="FolderID", primary_key=True)
    path: str = Field(description="Full path to folder")


class MusicTrackBase(SQLModel):

    id: str = Field(description="TrackID", primary_key=True)
    folder_id: str | None = Field(default=None, foreign_key="folders.id", description="Folder ID")
    artist: str | None = Field(default=None, description="Artist")
    album: str | None = Field(default=None, description="Album")
    title: str | None = Field(default=None, description="Track title")
    bitrate: int | None = Field(default=None, description="bitrate bps")
    duration: float | None = Field(default=None, description="sec")

class MusicTrackModel(MusicTrackBase, table=True):
    __tablename__ = "music_tracks"
    file: str = Field(description="File path")

class MusicTrackPublic(MusicTrackBase):
    pass