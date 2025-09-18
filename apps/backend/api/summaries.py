"""AI summarisation endpoints."""

from __future__ import annotations

from datetime import datetime
from typing import Dict, Optional

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from .posts import PostResponse, _FAKE_POSTS
from ..services.ai import summarize_text

router = APIRouter(prefix="/posts", tags=["summaries"])


class SummarizeRequest(BaseModel):
    """Request body for summarising a post."""

    model_id: Optional[str] = Field(
        default=None, description="Identifier of the AI model to use. Falls back to default from settings."
    )


class SummaryResponse(BaseModel):
    """Response payload for a generated summary."""

    post_id: int
    model_id: str
    summary: str
    created_at: datetime


_SUMMARY_CACHE: Dict[int, SummaryResponse] = {}


@router.post("/{post_id}/summarize", response_model=SummaryResponse)
async def summarize_post(post_id: int, payload: SummarizeRequest) -> SummaryResponse:
    """Generate (or retrieve) a summary for the requested post."""

    post: Optional[PostResponse] = next((item for item in _FAKE_POSTS if item.id == post_id), None)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    if len(post.text) < 80:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Post too short for summarisation")

    if cached := _SUMMARY_CACHE.get(post_id):
        return cached

    model_id = payload.model_id or "mock-model"
    summary_text = summarize_text(post.text, model_id=model_id)
    summary = SummaryResponse(
        post_id=post_id,
        model_id=model_id,
        summary=summary_text,
        created_at=datetime.utcnow(),
    )
    _SUMMARY_CACHE[post_id] = summary
    return summary
