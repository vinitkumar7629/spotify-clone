from pydantic import BaseModel, ConfigDict


class SongOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    artist: str
    album: str
    audio_file: str
    cover_image: str | None = None