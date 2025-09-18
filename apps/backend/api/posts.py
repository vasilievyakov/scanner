"""Post endpoints providing feed and search capabilities."""

from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Query
from pydantic import BaseModel, Field

router = APIRouter(prefix="/channels", tags=["posts"])


class PostResponse(BaseModel):
    """API representation of a Telegram post."""

    id: int
    channel_id: int
    tg_message_id: int
    posted_at: datetime
    text: str
    has_media: bool = Field(description="Whether the original message contains media attachments.")


class PostListResponse(BaseModel):
    """Paginated response payload for posts."""

    items: List[PostResponse]
    page: int
    page_size: int
    total: int


_FAKE_POSTS: List[PostResponse] = [
    PostResponse(
        id=1,
        channel_id=1,
        tg_message_id=101,
        posted_at=datetime.fromisoformat("2024-09-18T10:15:00"),
        text="Welcome to the tg-intel MVP skeleton!",
        has_media=False,
    ),
    PostResponse(
        id=2,
        channel_id=1,
        tg_message_id=102,
        posted_at=datetime.fromisoformat("2024-09-18T11:00:00"),
        text="Search and AI summarisation will be wired in upcoming iterations once the PostgreSQL layer and AI services are connected.",
        has_media=False,
    ),
]


@router.get("/{channel_id}/posts", response_model=PostListResponse)
async def list_posts(
    channel_id: int,
    query: Optional[str] = Query(default=None, description="Full-text search query."),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
) -> PostListResponse:
    """Return posts for the requested channel.

    The current implementation filters the in-memory placeholder dataset. Replace with a
    PostgreSQL query using full-text search once the database layer is ready.
    """

    filtered = [post for post in _FAKE_POSTS if post.channel_id == channel_id]
    if query:
        filtered = [post for post in filtered if query.lower() in post.text.lower()]

    total = len(filtered)
    start = (page - 1) * page_size
    end = start + page_size
    items = filtered[start:end]

    return PostListResponse(items=items, page=page, page_size=page_size, total=total)
