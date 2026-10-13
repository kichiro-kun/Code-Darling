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
from app.routers.main import router as main_router
from fastapi import Request
from fastapi.responses import JSONResponse


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s"
)

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
)


@app.get(path="/health")
async def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.exception_handler(exc_class_or_status_code=Exception)
async def unhandled_exception_handler(request, exc) -> JSONResponse:
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})


# Статика и шаблоны
app.mount(path="/static", app=StaticFiles(directory=settings.STATIC_DIR), name="static")
app.state.templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)

# Роуты
app.include_router(router=main_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
