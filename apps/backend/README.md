# Backend (FastAPI)

This folder hosts the FastAPI backend powering the Telegram Intelligence Platform. The current version is a skeleton that exposes:

- `GET /healthz` — readiness probe.
- `/api/channels` — placeholder endpoints for registering and listing channels.
- `/api/channels/{id}/posts` — placeholder feed with in-memory posts.
- `/api/posts/{id}/summarize` — mock AI summarisation using a local helper.

## Local development

```bash
uvicorn app:app --reload
```

Populate the required environment variables using the `.env.example` file in the repository root. Real database access, Telethon integration and APScheduler jobs will be added in subsequent iterations.
