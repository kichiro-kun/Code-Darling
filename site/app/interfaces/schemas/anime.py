# -*- coding: utf-8 -*-

"""
Pydantic schemas — API response contracts (presentation layer).
Maps domain entities to JSON for the OpenAPI / JSON endpoints.
"""

from datetime import date

from pydantic import BaseModel


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

    model_config = {"from_attributes": True}
