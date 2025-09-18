"""Telegram client helpers (placeholder)."""

from __future__ import annotations

from typing import List, Tuple


async def resolve_channel(tg_url: str) -> Tuple[int, str]:
    """Resolve a Telegram channel URL into internal identifiers."""

    # Real implementation will rely on Telethon API calls.
    return 123456789, "Placeholder Channel"


async def fetch_history(tg_id: int, limit: int = 200) -> List[dict]:
    """Fetch channel history."""

    # Telethon-powered implementation goes here.
    return [
        {"tg_message_id": 100 + index, "text": f"Placeholder message #{index}"}
        for index in range(1, min(limit, 3) + 1)
    ]
