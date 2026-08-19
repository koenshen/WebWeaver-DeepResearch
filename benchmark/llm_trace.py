"""Interruption-safe, per-question traces for benchmark LLM API calls."""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

_STATE: dict[str, Any] = {}


def _trace_path(question: str) -> Path | None:
    root = os.getenv("BENCHMARK_LLM_TRACE_DIR", "").strip()
    if not root:
        return None
    digest = hashlib.sha256(question.encode("utf-8")).hexdigest()
    session_id = os.getenv("BENCHMARK_TRACE_SESSION_ID", _STATE.get("session_id", ""))
    suffix = f"_{session_id}" if session_id else ""
    return Path(root) / f"{digest}{suffix}.jsonl"


def begin(question: str) -> None:
    _STATE.update(question=question, session_id=uuid.uuid4().hex, call_index=0, call_groups={})


def finish() -> None:
    _STATE.clear()


def next_call_group(purpose: str) -> int:
    groups = _STATE.get("call_groups")
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
    valid_protocol_response: bool | None = None,
) -> None:
    question = _STATE.get("question", "")
    path = _trace_path(question) if question else None
    if path is None:
        return
    _STATE["call_index"] = _STATE.get("call_index", 0) + 1
    has_tool_call = bool(response and "<tool_call>" in response and "</tool_call>" in response)
    has_answer = bool(response and "<answer>" in response and "</answer>" in response)
    computed_valid_protocol_response = has_tool_call or has_answer if purpose == "main_agent" else bool(response)
    if valid_protocol_response is None:
        valid_protocol_response = computed_valid_protocol_response
    event = {
        "session_id": _STATE.get("session_id", ""),
        "call_index": _STATE["call_index"],
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
    with path.open("a", encoding="utf-8") as handle:
        handle.write(encoded)
        handle.flush()


def export(question: str, destination: Path, source_root: Path | None = None, source_path: str | None = None) -> None:
    if source_path:
        source = Path(source_path)
    elif source_root is None:
        source = _trace_path(question)
    else:
        digest = hashlib.sha256(question.encode("utf-8")).hexdigest()
        candidates = sorted(source_root.glob(f"{digest}_*.jsonl"), key=lambda item: item.stat().st_mtime)
        source = candidates[-1] if candidates else source_root / f"{digest}.jsonl"
    if source is None or not source.exists():
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)


def load_events(path: str | Path) -> list[dict[str, Any]]:
    source = Path(path)
    if not source.exists():
        return []
    events = []
    for line in source.read_text(encoding="utf-8").split("\n"):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return events
