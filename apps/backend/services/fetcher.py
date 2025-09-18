"""Channel ingestion scheduler (placeholder)."""

from __future__ import annotations

from datetime import datetime
from typing import Iterable

from ..core.config import get_settings


class FetchJobResult(dict):
    """Lightweight structure describing fetch job outcomes."""


def run_fetch_cycle(channels: Iterable[int]) -> FetchJobResult:
    """Mock implementation of a fetch cycle."""

    settings = get_settings()
    return FetchJobResult(
        channels=list(channels),
        fetched_messages=0,
        started_at=datetime.utcnow().isoformat(),
        cron_minutes=settings.cron_fetch_minutes,
    )
