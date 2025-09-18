"""AI summarisation helper functions (mock implementation)."""

from __future__ import annotations

from textwrap import shorten


def summarize_text(text: str, model_id: str) -> str:
    """Return a placeholder summary for the provided text."""

    # Real implementation will call Replicate or Hugging Face Inference API.
    return f"[{model_id}] {shorten(text, width=200, placeholder='…')}"
