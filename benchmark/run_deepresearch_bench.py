#!/usr/bin/env python3
"""External DeepResearch Bench adapter for the unmodified ReAct inference stack.

python benchmark/run_deepresearch_bench.py \
    --run-name deepresearch-20260816-1020 \
    --num-questions 5 \
    --max-workers 1
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from benchmark.runner_common import INFERENCE, ROOT, export_drb, read_results, run_inference, write_input


DEFAULT_QUERY = ROOT.parent / "deep_research_bench" / "data" / "prompt_data" / "query.jsonl"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-name", default=f"deepresearch-{datetime.now():%Y%m%d-%H%M%S}")
    parser.add_argument("--query-file", type=Path, default=DEFAULT_QUERY)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--output-file", type=Path)
    parser.add_argument("--num-questions", type=int, default=-1, help="0=progress only, -1=all pending, N=first N")
    parser.add_argument("--no-resume", action="store_true")
    parser.add_argument("--skip-inference", action="store_true")
    parser.add_argument("--raw-results", type=Path)
    parser.add_argument("--model", default=os.getenv("OPENAI_COMPATIBLE_MODEL") or os.getenv("MODEL_PATH", ""))
    parser.add_argument("--max-workers", type=int, default=int(os.getenv("MAX_WORKERS", "1")))
    parser.add_argument("--temperature", type=float, default=float(os.getenv("TEMPERATURE", "0.85")))
    parser.add_argument("--presence-penalty", type=float, default=float(os.getenv("PRESENCE_PENALTY", "1.1")))
    return parser.parse_args()


def main() -> None:
    load_dotenv(ROOT / ".env", override=False)
    args = parse_args()
    output_dir = args.output_dir or ROOT / "benchmark_outputs" / args.run_name
    output_file = args.output_file or output_dir / "results.jsonl"
    tasks = [json.loads(line) for line in args.query_file.read_text(encoding="utf-8").split("\n") if line.strip()]
    completed = set()
    if output_file.exists() and not args.no_resume:
        completed = {json.loads(line).get("id") for line in output_file.read_text(encoding="utf-8").split("\n") if line.strip()}
    target = tasks if args.num_questions == -1 else tasks[:max(args.num_questions, 0)]
    completed_in_target = 0 if args.no_resume else sum(task["id"] in completed for task in target)
    to_run = len(target) if args.no_resume else len(target) - completed_in_target
    print(
        f"DeepResearchBench: total={len(tasks)}, target={len(target)}, "
        f"complete_in_target={completed_in_target}, to_run={to_run}"
    )
    if args.num_questions == 0 or not target or to_run == 0:
        return

    staging = INFERENCE / "eval_data" / "benchmark_staging" / args.run_name / "drb_tasks.jsonl"
    # Keep the complete target cohort in staging so the inference runner can
    # recognize prior raw results and execute only newly added questions.
    mapping = write_input(target, staging)
    if args.skip_inference:
        if not args.raw_results:
            raise SystemExit("--skip-inference requires --raw-results")
        raw_results = args.raw_results
    else:
        if not args.model:
            raise SystemExit("MODEL_PATH in .env or --model is required")
        raw_results = run_inference(staging, output_dir / "raw_runs", args.model, args.max_workers, args.temperature, args.presence_penalty)
    export_drb(read_results(raw_results), mapping, output_file, output_dir)
    print(f"Evaluator-ready JSONL: {output_file}")


if __name__ == "__main__":
    main()
