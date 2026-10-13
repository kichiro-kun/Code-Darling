from app.models.anime import Anime
from datetime import date

# ── Заглушка данных (позже заменим на БД) ──────────────────
_ANIME_DB: list[Anime] = [
    Anime(
        id=1,
        title="Атака Титанов",
        title_en="Attack on Titan",
        description="Человечество живёт в городах за стенами от огромных титанов. Эрен Йегер клянётся уничтожить всех титанов после того, как они уничтожают его город.",
        poster_url="https://picsum.photos/seed/aoe/300/450",
        year=2013,
        genres=["боевик", "драма", "фэнтези"],
        rating=9.1,
        episodes_count=89,
        is_released=True,
        status="released"
    ),
    Anime(2, "Стальной алхимик", "Fullmetal Alchemist: Brotherhood",
          "Братья Элрик стремятся вернуть свои тела после провалившегося алхимического эксперимента, используя власть алхимии.",
          "https://picsum.photos/seed/fma/300/450", 2009,
          ["приключения", "фэнтези", "боевик"], 9.2, 64, True, "released"),
    Anime(3, "Ван-Пис", "One Piece",
          "Путь Шанка Усоппа — стать Королём Пиратов. Он собирает команду и отправляется на поиски легендарного сокровища One Piece.",
          "https://picsum.photos/seed/op/300/450", 1999,
          ["приключения", "комедия", "суперспособность"], 9.0, 1100, False, "airing"),
    Anime(4, "Моб Псайко 100", "Mob Psycho 100",
          "13-летний Шигару Мори, обладатель сильнейших экстрасенсорных способностей, пытается вести обычную жизнь.",
          "https://picsum.photos/seed/mp/300/450", 2016,
          ["суперспособность", "комедия", "боевик"], 8.8, 37, False, "airing"),
    Anime(5, "Реванш", "Vivy: Fluorite Eye's Song",
          "ИИ-певица с бессмертием обретает свободу воли и пытается изменить своё прошлое, спасая людей.",
          "https://picsum.photos/seed/vivy/300/450", 2021,
          ["меха", "драма", "фантастика"], 8.4, 13, True, "released"),
    Anime(6, "Соломенный пират", "Solo Leveling",
          "Самый слабый охотник получает уникальную систему, позволяющую становиться сильнее без ограничений.",
          "https://picsum.photos/seed/sl/300/450", 2024,
          ["фэнтези", "боевик", "приключения"], 8.9, 25, False, "airing"),
    Anime(7, "Магическая битва", "Jujutsu Kaisen",
          "Юдзи Итадори проглатывает проклятие Сугуру — и втягивается в мир магов и проклятий.",
          "https://picsum.photos/seed/jjk/300/450", 2020,
          ["боевик", "фэнтези", "суперспособность"], 8.7, 47, False, "airing"),
    Anime(8, "Шин Гоку", "Shin Gokukan",
          "Боец-самурай с необычными способностями бросает вызов самым сильным мастерам боевых искусств.",
          "https://picsum.photos/seed/sgk/300/450", 2024,
          ["боевик", "приключения"], 8.5, 13, False, "upcoming"),
]


class AnimeService:
    """Простой сервис — позже заменим на SQL/Redis."""

    def get_all(self) -> list[Anime]:
        return list(_ANIME_DB)

    def get_by_id(self, anime_id: int) -> Anime | None:
        return next((a for a in _ANIME_DB if a.id == anime_id), None)

    def search(self, query: str) -> list[Anime]:
        q = query.lower()
        return [a for a in _ANIME_DB
                if q in a.title.lower() or q in a.title_en.lower()]

    def by_genre(self, genre: str) -> list[Anime]:
        return [a for a in _ANIME_DB if genre in a.genres]


anime_service = AnimeService()
