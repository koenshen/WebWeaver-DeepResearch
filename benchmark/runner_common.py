"""Shared, external input/output adaptation for benchmark runners."""

from __future__ import annotations

import json
import os
import signal
import subprocess
import sys
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Callable

from benchmark.benchmark_stats import write_stats
from benchmark.llm_trace import export as export_llm_trace
from benchmark.llm_trace import load_events
from benchmark.runtime_log import log


ROOT = Path(__file__).resolve().parents[1]
INFERENCE = ROOT / "inference"

EN_REPORT_SUFFIX = """

Deliver only a comprehensive Markdown research report. Cite important factual claims with accessible source URLs, and include a References section with the full URLs. Do not describe your tool use or search process.""".strip()
ZH_REPORT_SUFFIX = """

请只交付一份完整的 Markdown 深度研究报告。关键事实后必须附可访问的来源 URL，并在文末提供含完整 URL 的“参考资料”部分。不要描述工具调用或搜索过程。""".strip()


def benchmark_question(prompt: str, language: str | None = None) -> str:
    suffix = ZH_REPORT_SUFFIX if language == "zh" else EN_REPORT_SUFFIX
    return f"{prompt.rstrip()}\n\n{suffix}"


def write_input(tasks: list[dict[str, Any]], staging_file: Path) -> dict[str, dict[str, Any]]:
    """Write the exact existing-runner contract and retain an external ID map."""
    staging_file.parent.mkdir(parents=True, exist_ok=True)
    mapping: dict[str, dict[str, Any]] = {}
    with staging_file.open("w", encoding="utf-8") as handle:
        for task in tasks:
            question = benchmark_question(task["prompt"], task.get("language"))
            if question in mapping:
                raise ValueError("Duplicate benchmark prompt after normalization; cannot safely map async output")
            mapping[question] = task
            benchmark_kind = "id" if "id" in task else "qid"
            handle.write(json.dumps({
                "question": question, "answer": "", "_benchmark_id": str(task.get("id", task.get("qid", "?")),),
                "_benchmark_id_kind": benchmark_kind,
            }, ensure_ascii=False) + "\n")
    return mapping


def run_inference(staging_file: Path, output_base: Path, model: str, max_workers: int, temperature: float, presence_penalty: float, on_success: Callable[[dict[str, Any]], None] | None = None) -> Path:
    """Run each pending benchmark question in an isolated, time-bounded child."""
    relative_dataset = staging_file.relative_to(INFERENCE)
    items = [json.loads(line) for line in staging_file.read_text(encoding="utf-8").split("\n") if line.strip()]
    if max_workers != 1:
        raise ValueError("Benchmark hard-timeout mode currently requires --max-workers 1")
    command_prefix = [
        sys.executable, str(ROOT / "benchmark" / "run_tavily_react.py"),
        "--dataset", str(relative_dataset), "--output", str(output_base.resolve()),
        "--model", model, "--max_workers", str(max_workers),
        "--temperature", str(temperature), "--presence_penalty", str(presence_penalty),
        "--roll_out_count", "1",
    ]
    model_name = Path(model.rstrip("/")).name
    raw_results = output_base.resolve() / f"{model_name}_sglang" / relative_dataset / "iter1.jsonl"
    failed_dir = output_base.parent / "failed"
    inflight_dir = failed_dir / ".inflight"
    timeout_seconds = int(os.getenv("BENCHMARK_QUESTION_TIMEOUT_SECONDS", "1800"))

    def stop_child(process: subprocess.Popen, reason: str) -> None:
        """Terminate the isolated question and every descendant it started."""
        if process.poll() is not None:
            return
        # Ctrl+C can arrive again while the parent is waiting for the child to
        # exit.  Do not let that second interrupt skip the SIGKILL fallback and
        # leave the separate child process group running in the terminal.
        old_mask = None
        if hasattr(signal, "pthread_sigmask"):
            old_mask = signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGINT})
        try:
            log(f'[question child] STOP reason={reason} pid={process.pid}')
            try:
                os.killpg(process.pid, signal.SIGTERM)
            except ProcessLookupError:
                return
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                log(f'[question child] KILL reason={reason} pid={process.pid}')
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    return
                process.wait()
        finally:
            if old_mask is not None:
                signal.pthread_sigmask(signal.SIG_SETMASK, old_mask)

    def write_raw_failure(item: dict[str, Any], reason: str, trace_path: Path, elapsed: float, error: str | None = None) -> None:
        events = load_events(trace_path)
        final_messages = events[-1].get("input", {}).get("messages", []) if events else []
        timestamp = datetime.now().astimezone()
        item_id = str(item.get("_benchmark_id", "?"))
        payload = {
            "question": item["question"], "answer": item.get("answer", ""),
            "error": error or reason, "failure_reason": reason,
            "elapsed_seconds": round(elapsed, 3), "messages": final_messages,
        }
        raw_results.parent.mkdir(parents=True, exist_ok=True)
        with raw_results.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
        failure = {
            "id": item_id, "status": "failed", "reason": reason,
            "timestamp": timestamp.isoformat(), "elapsed_seconds": round(elapsed, 3),
            "question": item["question"], "error": error,
            "final_messages": final_messages, "llm_trace": events,
        }
        failed_dir.mkdir(parents=True, exist_ok=True)
        id_kind = item.get("_benchmark_id_kind", "id")
        filename = f"{id_kind}_{item_id}_{timestamp:%Y%m%d-%H%M%S-%f}_{reason}.json"
        (failed_dir / filename).write_text(json.dumps(failure, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if trace_path.exists(): trace_path.unlink()
        log(f'[question child] FAILED reason={reason} elapsed={elapsed:.1f}s artifact={failed_dir / filename}')

    for position, item in enumerate(items, start=1):
        # The original runner uses the dataset pathname as its output namespace.
        # Rewriting this one-row manifest preserves that namespace while making
        # one question a killable OS process.
        staging_file.write_text(json.dumps(item, ensure_ascii=False) + "\n", encoding="utf-8")
        session_id = uuid.uuid4().hex
        trace_path = inflight_dir / f"{__import__('hashlib').sha256(item['question'].encode('utf-8')).hexdigest()}_{session_id}.jsonl"
        env = os.environ.copy()
        env.update({
            "BENCHMARK_LLM_TRACE_DIR": str(inflight_dir.resolve()),
            "BENCHMARK_TRACE_SESSION_ID": session_id,
            "BENCHMARK_QUESTION_LABEL": f"question {position}/{len(items)} id={item.get('_benchmark_id', '?')}",
        })
        log(f'[question child] START position={position}/{len(items)} id={item.get("_benchmark_id", "?")} timeout={timeout_seconds}s')
        started = time.monotonic()
        # A separate process group lets Ctrl+C and the hard timeout terminate
        # this child plus anything it spawned, without leaving orphaned tools.
        process = subprocess.Popen(command_prefix, cwd=ROOT, env=env, start_new_session=True)
        timed_out = False
        next_heartbeat = 30
        try:
            while process.poll() is None:
                elapsed = time.monotonic() - started
                if elapsed >= timeout_seconds:
                    timed_out = True
                    stop_child(process, "question_timeout")
                    break
                if elapsed >= next_heartbeat:
                    log(f'[question child] WAITING elapsed={elapsed:.1f}s')
                    next_heartbeat += 30
                time.sleep(1)
            if not timed_out:
                process.wait()
        except KeyboardInterrupt:
            stop_child(process, "keyboard_interrupt")
            raise
        elapsed = time.monotonic() - started
        if timed_out:
            write_raw_failure(item, "question_timeout", trace_path, elapsed)
            continue
        if process.returncode != 0:
            write_raw_failure(item, "child_process_error", trace_path, elapsed, f"child exit code {process.returncode}")
            continue
        # The original runner converts task exceptions into error JSON records.
        # Turn that terminal error into the requested self-contained artifact.
        matching_error = None
        matching_result = None
        if raw_results.exists():
            for line in reversed(raw_results.read_text(encoding="utf-8").split("\n")):
                if not line.strip(): continue
                try: record = json.loads(line)
                except json.JSONDecodeError: continue
                if record.get("question") == item["question"]:
                    matching_result = record
                    if record.get("error"): matching_error = str(record["error"])
                    break
        if matching_error:
            if "LLMResponseRetriesExhausted" in matching_error or "exhausted 10 attempts" in matching_error:
                reason = "llm_response_retries_exhausted"
            elif "no successful Tavily search" in matching_error:
                reason = "no_tavily_search"
            else:
                reason = "question_execution_error"
            write_raw_failure(item, reason, trace_path, elapsed, matching_error)
        else:
            if matching_result is not None and on_success is not None:
                on_success(matching_result)
            log(f'[question child] END status=success elapsed={elapsed:.1f}s')
    return raw_results


def read_results(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Expected inference output was not created: {path}")
    # JSON strings may legally contain U+2028/U+2029.  str.splitlines() treats
    # those characters as record separators, while JSONL is delimited by LF.
    return [json.loads(line) for line in path.read_text(encoding="utf-8").split("\n") if line.strip()]


def export_lrb(results: list[dict[str, Any]], mapping: dict[str, dict[str, Any]], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for result in results:
        if result.get("error"):
            continue
        task = mapping.get(result.get("question", ""))
        if task is None:
            # A stable run name may have raw results from a previously larger
            # target cohort.  They are valid history, but not part of this
            # invocation's requested prefix.
            continue
        qid = str(task["qid"])
        (output_dir / f"qid_{qid}_report.md").write_text(str(result.get("prediction", "")), encoding="utf-8")
        write_stats(output_dir / f"qid_{qid}_stats.json", result, {"qid": qid, "query": task["prompt"]})
        trace_source = result.get("_benchmark_trace_path")
        export_llm_trace(result.get("question", ""), output_dir / f"qid_{qid}_llm_trace.jsonl", source_path=trace_source)
        if trace_source and Path(trace_source).exists(): Path(trace_source).unlink()


def export_drb(results: list[dict[str, Any]], mapping: dict[str, dict[str, Any]], output_file: Path, artifact_dir: Path) -> None:
    artifact_dir.mkdir(parents=True, exist_ok=True)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    records_by_id: dict[Any, dict[str, Any]] = {}
    record_order: list[Any] = []
    if output_file.exists():
        for line in output_file.read_text(encoding="utf-8").split("\n"):
            if line.strip():
                record = json.loads(line)
                record_id = record.get("id")
                records_by_id[record_id] = record
                record_order.append(record_id)
    for result in results:
        if result.get("error"):
            continue
        task = mapping.get(result.get("question", ""))
        if task is None:
            # Ignore valid historical raw results outside the current target
            # prefix (for example after reducing --num-questions).
            continue
        task_id = task["id"]
        article = str(result.get("prediction", ""))
        if task_id not in records_by_id:
            record_order.append(task_id)
        records_by_id[task_id] = {"id": task_id, "prompt": task["prompt"], "article": article}
        (artifact_dir / f"id_{task_id}_report.md").write_text(article, encoding="utf-8")
        write_stats(artifact_dir / f"id_{task_id}_stats.json", result, {"id": task_id, "prompt": task["prompt"], "language": task.get("language"), "topic": task.get("topic")})
        trace_source = result.get("_benchmark_trace_path")
        export_llm_trace(result.get("question", ""), artifact_dir / f"id_{task_id}_llm_trace.jsonl", source_path=trace_source)
        if trace_source and Path(trace_source).exists(): Path(trace_source).unlink()
    output_file.write_text(
        "".join(json.dumps(records_by_id[record_id], ensure_ascii=False) + "\n" for record_id in record_order),
        encoding="utf-8",
    )
