"""Channel endpoints for the tg-intel backend."""

from __future__ import annotations

from typing import List

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field, HttpUrl

router = APIRouter(prefix="/channels", tags=["channels"])


class ChannelCreateRequest(BaseModel):
    """Request body for registering a new Telegram channel."""

    tg_url: HttpUrl = Field(description="Public URL to the Telegram channel.")


class ChannelResponse(BaseModel):
    """API representation of a channel."""

    id: int = Field(description="Internal channel identifier.")
    title: str = Field(description="Human-readable channel title.")
    tg_url: HttpUrl = Field(description="Public URL to the Telegram channel.")
    status: str = Field(description="Ingestion status for the channel (e.g. active, pending, error).")


# In-memory placeholder store to keep the skeleton self-contained.
_FAKE_CHANNELS: List[ChannelResponse] = [
    ChannelResponse(id=1, title="Example Channel", tg_url="https://t.me/example", status="pending"),
]


@router.post("", response_model=ChannelResponse, status_code=status.HTTP_201_CREATED)
async def create_channel(payload: ChannelCreateRequest) -> ChannelResponse:
    """Register a channel for ingestion.

    The real implementation will persist the channel in PostgreSQL and enqueue a background fetch job.
    """

    if any(channel.tg_url == payload.tg_url for channel in _FAKE_CHANNELS):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Channel already exists")

    channel = ChannelResponse(
        id=len(_FAKE_CHANNELS) + 1,
        title="Placeholder title",
        tg_url=payload.tg_url,
        status="pending",
    )
    _FAKE_CHANNELS.append(channel)
    return channel


@router.get("", response_model=List[ChannelResponse])
async def list_channels() -> List[ChannelResponse]:
    """Return the list of known channels.

    Replace with a database-backed query during full implementation.
    """

    return _FAKE_CHANNELS
