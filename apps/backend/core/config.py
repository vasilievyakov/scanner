"""Application configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache
from typing import Optional


@dataclass(frozen=True)
class Settings:
    """Runtime configuration loaded from environment variables."""

    environment: str = os.getenv("ENVIRONMENT", "development")
    supabase_url: Optional[str] = os.getenv("SUPABASE_URL")
    supabase_anon_key: Optional[str] = os.getenv("SUPABASE_ANON_KEY")
    supabase_service_role_key: Optional[str] = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    supabase_db_url: Optional[str] = os.getenv("SUPABASE_DB_URL")
    backend_port: int = int(os.getenv("BACKEND_PORT", "8000"))
    cron_fetch_minutes: int = int(os.getenv("CRON_FETCH_MINUTES", "5"))
    ai_summary_endpoint: Optional[str] = os.getenv("AI_SUMMARY_ENDPOINT")
    ai_summary_model_id: Optional[str] = os.getenv("AI_SUMMARY_MODEL_ID")
    tg_api_id: Optional[str] = os.getenv("TG_API_ID")
    tg_api_hash: Optional[str] = os.getenv("TG_API_HASH")
    tg_session_path: str = os.getenv("TG_SESSION_PATH", "./.secrets/telethon.session")
    tg_proxy_url: Optional[str] = os.getenv("TG_PROXY_URL")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return cached settings instance."""

    return Settings()
