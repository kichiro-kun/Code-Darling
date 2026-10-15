# -*- coding: utf-8 -*-

"""
Copyright 2026 kichiro-kun (Kei)
Apache license, version 2.0 (Apache-2.0 license)
"""

__author__ = 'kichiro-kun (Kei)'
__version__ = '0.1.0'


import logging
from typing import Dict

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from settings import settings

# ── Clean Architecture wiring ───────────────────────────────────────
from app.domain.ports.anime_repository import AnimeRepository
from app.application.use_cases import (
    GetAnimeByIdUseCase,
    GetAllAnimeUseCase,
    SearchAnimeUseCase,
    GetAnimeByGenreUseCase,
)
from app.infrastructure.adapters.anime_repository_in_memory import InMemoryAnimeRepository


class UseCaseContainer:
    """Simple DI container — holds all use-case instances."""

    def __init__(self, repo: AnimeRepository) -> None:
        self.get_by_id = GetAnimeByIdUseCase(repo)
        self.get_all = GetAllAnimeUseCase(repo)
        self.search = SearchAnimeUseCase(repo)
        self.by_genre = GetAnimeByGenreUseCase(repo)


def create_app() -> FastAPI:
    """Application factory — builds and wires the FastAPI app."""
    application = FastAPI(
        title=settings.APP_TITLE,
        description=settings.APP_DESCRIPTION,
        version=settings.APP_VERSION,
        docs_url=settings.docs_url,
        redoc_url=settings.redoc_url,
        openapi_url=settings.openapi_url,
        debug=settings.IS_DEV,
    )

    # ── DI: concrete adapter → use cases → app state ────────────────
    repository = InMemoryAnimeRepository()
    application.state.use_cases = UseCaseContainer(repository)

    # ── Static & templates ──────────────────────────────────────────
    application.mount(
        path="/static",
        app=StaticFiles(directory=settings.STATIC_DIR),
        name="static",
    )
    application.state.templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)

    # ── Routes ──────────────────────────────────────────────────────
    from app.interfaces.api.router import router as main_router
    application.include_router(router=main_router)

    # ── Health ──────────────────────────────────────────────────────
    @application.get("/health")
    async def health() -> Dict[str, str]:
        return {"status": "ok"}

    # ── Global exception handler ────────────────────────────────────
    @application.exception_handler(Exception)
    async def unhandled_exception_handler(request, exc):
        from fastapi.responses import JSONResponse
        return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

    return application


app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
