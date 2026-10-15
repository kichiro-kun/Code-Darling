# -*- coding: utf-8 -*-
"""Domain layer — core entities and repository ports."""

from app.domain.exceptions import (
    DomainError,
    AnimeNotFoundError,
    InvalidSearchQueryError,
    GenreNotFoundError,
)

__all__ = [
    "DomainError",
    "AnimeNotFoundError",
    "InvalidSearchQueryError",
    "GenreNotFoundError",
]
