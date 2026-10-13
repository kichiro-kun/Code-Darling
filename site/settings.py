# -*- coding: utf-8 -*-

"""
Copyright 2026 kichiro-kun (Kei)
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    'settings'
]

__author__ = 'kichiro-kun (Kei)'
__version__ = '0.1.0'


# _______________________________________________________________________________________
class Settings:
    APP_NAME: str = "Code: Darling"
    APP_DESCRIPTION: str = "Сайт для просмотра аниме"
    TEMPLATE_DIR: str = "app/templates"
    STATIC_DIR: str = "app/static"
    BASE_URL: str = "http://127.0.0.1:8000"


settings = Settings()
