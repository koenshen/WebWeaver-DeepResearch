"""Shared, external input/output adaptation for benchmark runners."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

from benchmark.benchmark_stats import write_stats
from benchmark.llm_trace import export as export_llm_trace


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
            handle.write(json.dumps({"question": question, "answer": ""}, ensure_ascii=False) + "\n")
    return mapping


def run_inference(staging_file: Path, output_base: Path, model: str, max_workers: int, temperature: float, presence_penalty: float) -> Path:
    """Invoke the existing runner through the optional Tavily plugin wrapper."""
    relative_dataset = staging_file.relative_to(INFERENCE)
    command = [
        sys.executable, str(ROOT / "benchmark" / "run_tavily_react.py"),
        "--dataset", str(relative_dataset), "--output", str(output_base.resolve()),
        "--model", model, "--max_workers", str(max_workers),
        "--temperature", str(temperature), "--presence_penalty", str(presence_penalty),
        "--roll_out_count", "1",
    ]
    env = os.environ.copy()
    env["BENCHMARK_LLM_TRACE_DIR"] = str((output_base.parent / ".llm_traces").resolve())
    subprocess.run(command, cwd=ROOT, check=True, env=env)
    model_name = Path(model.rstrip("/")).name
    return output_base.resolve() / f"{model_name}_sglang" / relative_dataset / "iter1.jsonl"


def read_results(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Expected inference output was not created: {path}")
    # JSON strings may legally contain U+2028/U+2029.  str.splitlines() treats
    # those characters as record separators, while JSONL is delimited by LF.
    return [json.loads(line) for line in path.read_text(encoding="utf-8").split("\n") if line.strip()]


def export_lrb(results: list[dict[str, Any]], mapping: dict[str, dict[str, Any]], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for result in results:
        task = mapping.get(result.get("question", ""))
        if task is None:
            # A stable run name may have raw results from a previously larger
            # target cohort.  They are valid history, but not part of this
            # invocation's requested prefix.
            continue
        qid = str(task["qid"])
        (output_dir / f"qid_{qid}_report.md").write_text(str(result.get("prediction", "")), encoding="utf-8")
        write_stats(output_dir / f"qid_{qid}_stats.json", result, {"qid": qid, "query": task["prompt"]})
        export_llm_trace(result.get("question", ""), output_dir / f"qid_{qid}_llm_trace.jsonl", output_dir / ".llm_traces")


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
        export_llm_trace(result.get("question", ""), artifact_dir / f"id_{task_id}_llm_trace.jsonl", artifact_dir / ".llm_traces")
    output_file.write_text(
        "".join(json.dumps(records_by_id[record_id], ensure_ascii=False) + "\n" for record_id in record_order),
        encoding="utf-8",
    )
