# -*- coding: utf-8 -*-

"""
API Router — outermost presentation layer.

Translates HTTP requests into use-case calls and renders responses.
Depends on application use cases (NOT directly on repositories).
"""

from fastapi import APIRouter, Request, Query, HTTPException
from fastapi.responses import JSONResponse

from app.application.use_cases import (
    GetAnimeByIdUseCase,
    GetAllAnimeUseCase,
    SearchAnimeUseCase,
    GetAnimeByGenreUseCase,
)
from app.domain.exceptions import AnimeNotFoundError
from app.interfaces.schemas.anime import AnimeResponse

router = APIRouter()

# ── HTML pages ──────────────────────────────────────────────────────


@router.get("/", name="index")
def index(request: Request):
    """Главная страница — каталог аниме."""
    animes = request.app.state.use_cases.get_all.execute()
    return request.app.state.templates.TemplateResponse(
        "index.html",
        {"request": request, "animes": animes},
    )


@router.get("/search", name="search")
def search(request: Request, q: str = Query("", description="Поисковый запрос")):
    """Поиск по названию (RU или EN)."""
    animes = request.app.state.use_cases.search.execute(q)
    return request.app.state.templates.TemplateResponse(
        "index.html",
        {"request": request, "animes": animes, "query": q},
    )


@router.get("/anime/{anime_id}", name="anime_detail")
def anime_detail(request: Request, anime_id: int):
    """Страница отдельного тайтла."""
    try:
        anime = request.app.state.use_cases.get_by_id.execute(anime_id)
    except AnimeNotFoundError:
        raise HTTPException(status_code=404, detail=f"Аниме с id={anime_id} не найдено")
    return request.app.state.templates.TemplateResponse(
        "anime_detail.html",
        {"request": request, "anime": anime},
    )


# ── JSON API ────────────────────────────────────────────────────────

@router.get("/api/anime", response_model=list[AnimeResponse], name="api_anime_list")
def api_anime_list(
    request: Request,
    q: str = Query(None, description="Поиск по названию"),
    genre: str = Query(None, description="Фильтр по жанру"),
):
    """Каталог / поиск / фильтр по жанру (JSON)."""
    if q:
        animes = request.app.state.use_cases.search.execute(q)
    elif genre:
        animes = request.app.state.use_cases.by_genre.execute(genre)
    else:
        animes = request.app.state.use_cases.get_all.execute()
    return [AnimeResponse.model_validate(a) for a in animes]


@router.get("/api/anime/{anime_id}", response_model=AnimeResponse, name="api_anime_detail")
def api_anime_detail(request: Request, anime_id: int):
    """Одно аниме по id (JSON)."""
    try:
        anime = request.app.state.use_cases.get_by_id.execute(anime_id)
    except AnimeNotFoundError as e:
        return JSONResponse(status_code=404, content={"detail": str(e)})
    return AnimeResponse.model_validate(anime)
