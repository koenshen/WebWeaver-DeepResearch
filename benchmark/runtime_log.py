"""Small benchmark-only logger with operation heartbeats."""
from __future__ import annotations

import os
import time
from datetime import datetime


def label() -> str:
    return os.getenv("BENCHMARK_QUESTION_LABEL", "question=?")


def log(message: str, *, stream=None) -> None:
    print(f"[{datetime.now().astimezone():%Y-%m-%d %H:%M:%S}] [{label()}] {message}", file=stream, flush=True)


def preview(title: str, content: str, limit: int = 500) -> None:
    text = content[:limit]
    log(f"{title} output_chars={len(content)}")
    print("\n==================== LLM OUTPUT PREVIEW BEGIN ====================", flush=True)
    print(text, flush=True)
    if len(content) > limit:
        print(f"... [truncated {len(content) - limit} characters]", flush=True)
    print("===================== LLM OUTPUT PREVIEW END =====================\n", flush=True)


def heartbeat(description: str, interval_seconds: int = 30):
    """Return an elapsed-time callback without creating a background thread."""
    started = time.monotonic()

    def stop() -> float:
        return time.monotonic() - started

    return stop
