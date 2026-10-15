# -*- coding: utf-8 -*-

"""
Use Cases for Anime.

Application layer — orchestrates domain entities via repository ports.
Depends ONLY on the domain layer (entities + ports).
"""

from app.domain.entities.anime import Anime
from app.domain.ports.anime_repository import AnimeRepository
from app.domain.exceptions import AnimeNotFoundError


class GetAnimeByIdUseCase:
    """Сценарий: получить аниме по id."""

    def __init__(self, repository: AnimeRepository) -> None:
        self._repo = repository

    def execute(self, anime_id: int) -> Anime:
        anime = self._repo.get_by_id(anime_id)
        if anime is None:
            raise AnimeNotFoundError(anime_id)
        return anime


class GetAllAnimeUseCase:
    """Сценарий: получить весь каталог аниме."""

    def __init__(self, repository: AnimeRepository) -> None:
        self._repo = repository

    def execute(self) -> list[Anime]:
        return self._repo.get_all()


class SearchAnimeUseCase:
    """Сценарий: поиск аниме по названию (RU или EN)."""

    def __init__(self, repository: AnimeRepository) -> None:
        self._repo = repository

    def execute(self, query: str) -> list[Anime]:
        if not query or not query.strip():
            return self._repo.get_all()
        return self._repo.search(query.strip())


class GetAnimeByGenreUseCase:
    """Сценарий: фильтровать каталог по жанру."""

    def __init__(self, repository: AnimeRepository) -> None:
        self._repo = repository

    def execute(self, genre: str) -> list[Anime]:
        if not genre or not genre.strip():
            return self._repo.get_all()
        return self._repo.by_genre(genre.strip())
