from pydantic import BaseModel
from datetime import date
from typing import Optional


class AnimeBase(BaseModel):
    title: str
    title_en: str
    description: str
    poster_url: str
    year: int
    genres: list[str]
    rating: float
    episodes_count: int
    status: str = "released"


class AnimeResponse(AnimeBase):
    id: int

    class Config:
        from_attributes = True
