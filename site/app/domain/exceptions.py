# -*- coding: utf-8 -*-
"""
Domain exceptions — pure business errors, no framework dependencies.
"""


class DomainError(Exception):
    """Base class for all domain-level business errors."""
    pass


class AnimeNotFoundError(DomainError):
    """Raised when an anime with the given id does not exist."""

    def __init__(self, anime_id: int) -> None:
        self.anime_id = anime_id
        super().__init__(f"Аниме с id={anime_id} не найдено")


class InvalidSearchQueryError(DomainError):
    """Raised when a search query is invalid."""

    def __init__(self, query: str) -> None:
        self.query = query
        super().__init__(f"Некорректный поисковый запрос: {query!r}")


class GenreNotFoundError(DomainError):
    """Raised when a genre filter is not recognized."""

    def __init__(self, genre: str) -> None:
        self.genre = genre
        super().__init__(f"Жанр {genre!r} не найден")