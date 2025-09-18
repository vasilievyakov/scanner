"""FastAPI application entrypoint for the Telegram Intelligence Platform backend."""

from fastapi import FastAPI

from .api import api_router
from .core.config import get_settings
from .core.logger import configure_logging

configure_logging()
settings = get_settings()

app = FastAPI(
    title="Telegram Intelligence Platform API",
    description="Backend services for the tg-intel MVP.",
    version="0.1.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

app.include_router(api_router, prefix="/api")


@app.get("/healthz", tags=["internal"])
async def health_check() -> dict[str, str]:
    """Lightweight readiness probe."""
    return {"status": "ok", "env": settings.environment}
