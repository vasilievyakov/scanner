"""API routers for the tg-intel backend."""

from fastapi import APIRouter

from . import channels, posts, summaries

api_router = APIRouter()
api_router.include_router(channels.router)
api_router.include_router(posts.router)
api_router.include_router(summaries.router)
