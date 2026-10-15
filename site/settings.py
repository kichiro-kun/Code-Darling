# -*- coding: utf-8 -*-

"""
Copyright 2026 kichiro-kun (Kei)
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    'settings'
]

__author__ = 'kichiro-kun (Kei)'
__version__ = '0.2.0'


# _______________________________________________________________________________________
class Settings:
    APP_TITLE: str = "Code: Darling"
    APP_DESCRIPTION: str = "Сайт для просмотра аниме"
    APP_VERSION: str = "0.1.0"
    TEMPLATE_DIR: str = "app/interfaces/templates"
    STATIC_DIR: str = "app/interfaces/static"
    BASE_URL: str = "http://127.0.0.1:8000"
    IS_DEV: bool = True

    # -----------------------------------------------------------------------------------
    @property
    def docs_url(self) -> str | None:
        return "/api/docs" if self.IS_DEV else None

    # -----------------------------------------------------------------------------------
    @property
    def redoc_url(self) -> str | None:
        return "/api/redoc" if self.IS_DEV else None

    # -----------------------------------------------------------------------------------
    @property
    def openapi_url(self) -> str | None:
        return "/api/openapi.json" if self.IS_DEV else None


settings = Settings()
