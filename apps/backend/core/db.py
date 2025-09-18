"""Database utilities (placeholder)."""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import AsyncIterator


@asynccontextmanager
async def get_db() -> AsyncIterator[None]:
    """Yield a database connection placeholder.

    Replace with an actual connection pool (asyncpg / SQLAlchemy) when wiring PostgreSQL.
    """

    yield None
