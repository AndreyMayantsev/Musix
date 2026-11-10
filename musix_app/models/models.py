from sqlmodel import SQLModel, Field


"""
Folder models
"""
class FolderModelBase(SQLModel):
    id: str = Field(description="FolderID", primary_key=True)


class FolderModelPublic(FolderModelBase):
    pass


class FolderModel(FolderModelBase, table=True):
    __tablename__ = "folders"

    path: str = Field(description="Full path to folder")


"""
MusicTrack models
"""
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


"""
Application models
"""
class ApplicationModel(SQLModel, table=True):
    __tablename__ = "applications"

    id: str = Field(description="ApplicationID", primary_key=True)
    os: str | None = Field(default=None, description="Operation System")
    name: str | None = Field(default=None, description="Operation System")
    info: str | None = Field(default=None, description="HW info")