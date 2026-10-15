# -*- coding: utf-8 -*-

"""
Domain Entity: Anime

This is the innermost layer of Clean Architecture.
It contains pure business entities with NO dependencies
on frameworks, databases, or presentation layers.
"""

from dataclasses import dataclass, field
from datetime import date


@dataclass
class Anime:
    """Core domain entity representing an anime title."""
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
    created_at: date = field(default_factory=date.today)

    def matches_search(self, query: str) -> bool:
        """Domain rule: check if this anime matches a search query."""
        q = query.lower()
        return q in self.title.lower() or q in self.title_en.lower()

    def has_genre(self, genre: str) -> bool:
        """Domain rule: check if this anime belongs to a given genre."""
        return genre in self.genres
