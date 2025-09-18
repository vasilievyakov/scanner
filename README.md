# tg-intel

Monorepository skeleton for the **Telegram Intelligence Platform** MVP.

## Structure

```
apps/
  backend/      # FastAPI + Telethon service (Railway)
  frontend/     # Next.js client (Vercel)
infra/          # Infrastructure-as-code and deployment manifests
```

The repository intentionally starts lightweight so that the team can iterate during the MVP implementation. Use the [`prd_telegram_intelligence_platform_mvp_consolidated_v_1.md`](prd_telegram_intelligence_platform_mvp_consolidated_v_1.md) document as the product source of truth.

## Getting started

1. Duplicate `.env.example` into `.env` and populate the secrets from Supabase, Telegram, Railway and Vercel.
2. See `apps/backend/README.md` and `apps/frontend/README.md` for service-specific instructions once those components are implemented.
3. CI is provided as a placeholder GitHub Action (`.github/workflows/ci.yml`). Extend it with linting, testing and deployment steps as the codebase evolves.

> **Note:** Actions that require external services (Vercel, Railway, Supabase) cannot be executed inside this development container. Track their configuration status in project management tools.
