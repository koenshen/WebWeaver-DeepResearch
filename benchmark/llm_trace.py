"""Interruption-safe, per-question traces for benchmark LLM API calls."""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import threading
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

_LOCAL = threading.local()
_WRITE_LOCK = threading.Lock()


def _trace_path(question: str) -> Path | None:
    root = os.getenv("BENCHMARK_LLM_TRACE_DIR", "").strip()
    if not root:
        return None
    digest = hashlib.sha256(question.encode("utf-8")).hexdigest()
    return Path(root) / f"{digest}.jsonl"


def begin(question: str) -> None:
    _LOCAL.question = question
    _LOCAL.session_id = uuid.uuid4().hex
    _LOCAL.call_index = 0
    _LOCAL.call_groups = {}


def finish() -> None:
    for name in ("question", "session_id", "call_index", "call_groups"):
        if hasattr(_LOCAL, name):
            delattr(_LOCAL, name)


def next_call_group(purpose: str) -> int:
    groups = getattr(_LOCAL, "call_groups", None)
    if groups is None:
        return 1
    groups[purpose] = groups.get(purpose, 0) + 1
    return groups[purpose]


def record(
    *,
    purpose: str,
    call_group: int,
    attempt: int,
    model: str,
    temperature: Any,
    messages: list[dict[str, Any]],
    status: str,
    duration_seconds: float,
    response: str | None = None,
    usage: dict[str, int] | None = None,
    error: BaseException | None = None,
) -> None:
    question = getattr(_LOCAL, "question", "")
    path = _trace_path(question) if question else None
    if path is None:
        return
    _LOCAL.call_index = getattr(_LOCAL, "call_index", 0) + 1
    has_tool_call = bool(response and "<tool_call>" in response and "</tool_call>" in response)
    has_answer = bool(response and "<answer>" in response and "</answer>" in response)
    valid_protocol_response = (
        has_tool_call or has_answer if purpose == "main_agent" else bool(response)
    )
    event = {
        "session_id": getattr(_LOCAL, "session_id", ""),
        "call_index": _LOCAL.call_index,
        "purpose": purpose,
        "call_group": call_group,
        "attempt": attempt,
        "model": model,
        "temperature": temperature,
        "status": status,
        "timestamp": datetime.now().astimezone().isoformat(),
        "duration_seconds": round(duration_seconds, 3),
        "input": {"messages": messages},
        "output": None if response is None else {"content": response},
        "usage": usage or {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0},
        "classification": {
            "has_tool_call": has_tool_call,
            "has_answer": has_answer,
            "valid_protocol_response": valid_protocol_response,
        },
    }
    if error is not None:
        event["error_type"] = type(error).__name__
        event["error"] = str(error)
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(event, ensure_ascii=False) + "\n"
    with _WRITE_LOCK, path.open("a", encoding="utf-8") as handle:
        handle.write(encoded)
        handle.flush()


def export(question: str, destination: Path, source_root: Path | None = None) -> None:
    if source_root is None:
        source = _trace_path(question)
    else:
        digest = hashlib.sha256(question.encode("utf-8")).hexdigest()
        source = source_root / f"{digest}.jsonl"
    if source is None or not source.exists():
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
