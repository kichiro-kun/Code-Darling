from dataclasses import dataclass, field
from typing import Optional
from datetime import date


@dataclass
class Anime:
    id: int
    title: str
    title_en: str
    description: str
    poster_url: str
    year: int
    genres: list[str] = field(default_factory=list)
    rating: float = 0.0
    episodes_count: int = 0
    is_released: bool = True
    status: str = "released"  # released | airing | upcoming
    created_at: date = date.today()
