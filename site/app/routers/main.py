from fastapi import APIRouter, Request, Query
from app.services.anime_service import anime_service

router = APIRouter()


@router.get("/")
def index(request: Request):
    """Главная страница — список аниме."""
    animes = anime_service.get_all()
    return request.app.state.templates.TemplateResponse(
        "index.html",
        {"request": request, "animes": animes},
    )


@router.get("/search")
def search(request: Request, q: str = Query("", description="Поисковый запрос")):
    """Поиск по названию."""
    animes = anime_service.search(q) if q else anime_service.get_all()
    return request.app.state.templates.TemplateResponse(
        "index.html",
        {"request": request, "animes": animes, "query": q},
    )
