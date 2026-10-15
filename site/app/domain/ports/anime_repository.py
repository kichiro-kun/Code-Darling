# -*- coding: utf-8 -*-

"""
Repository Port (Interface) for Anime.

Defines the contract that any data-access implementation
(in-memory, SQL, NoSQL, Redis…) must fulfill.
The domain layer knows ONLY about this interface —
it never imports concrete adapters.
"""

from abc import ABC, abstractmethod

from app.domain.entities.anime import Anime


class AnimeRepository(ABC):
    """Abstract base — the 'port' the application code depends on."""

    @abstractmethod
    def get_all(self) -> list[Anime]:
        """Return all anime records."""
        ...

    @abstractmethod
    def get_by_id(self, anime_id: int) -> Anime | None:
        """Return a single anime by its primary key, or None."""
        ...

    @abstractmethod
    def search(self, query: str) -> list[Anime]:
        """Search anime by title (Russian or English)."""
        ...

    @abstractmethod
    def by_genre(self, genre: str) -> list[Anime]:
        """Return anime filtered by a specific genre."""
        ...
