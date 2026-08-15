#!/usr/bin/env python3
"""External LiveResearchBench adapter for the unmodified ReAct inference stack."""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from benchmark.runner_common import INFERENCE, ROOT, export_lrb, read_results, run_inference, write_input


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-name", default=f"liveresearch-{datetime.now():%Y%m%d-%H%M%S}")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--num-questions", type=int, default=-1, help="0=progress only, -1=all pending, N=first N")
    parser.add_argument("--no-resume", action="store_true")
    parser.add_argument("--skip-inference", action="store_true", help="Export an existing raw iter1.jsonl instead")
    parser.add_argument("--raw-results", type=Path)
    parser.add_argument("--model", default=os.getenv("OPENAI_COMPATIBLE_MODEL") or os.getenv("MODEL_PATH", ""))
    parser.add_argument("--max-workers", type=int, default=int(os.getenv("MAX_WORKERS", "1")))
    parser.add_argument("--temperature", type=float, default=float(os.getenv("TEMPERATURE", "0.85")))
    parser.add_argument("--presence-penalty", type=float, default=float(os.getenv("PRESENCE_PENALTY", "1.1")))
    return parser.parse_args()


def main() -> None:
    load_dotenv(ROOT / ".env", override=False)
    args = parse_args()
    sys.path.insert(0, str(ROOT.parent / "LiveResearchBench"))
    from liveresearchbench.common.io_utils import load_liveresearchbench_dataset

    output_dir = args.output_dir or ROOT / "benchmark_outputs" / args.run_name
    data = load_liveresearchbench_dataset(use_realtime=True)
    tasks = [{"qid": qid, "prompt": item["question"], "language": "en"} for qid, item in data.items()]
    completed = {path.stem.removeprefix("qid_").removesuffix("_report") for path in output_dir.glob("qid_*_report.md")}
    pending = tasks if args.no_resume else [task for task in tasks if task["qid"] not in completed]
    selected = pending if args.num_questions == -1 else pending[:args.num_questions]
    print(f"LiveResearchBench: total={len(tasks)}, complete={len(completed)}, selected={len(selected)}")
    if args.num_questions == 0 or not selected:
        return

    staging = INFERENCE / "eval_data" / "benchmark_staging" / args.run_name / "lrb_tasks.jsonl"
    mapping = write_input(selected, staging)
    if args.skip_inference:
        if not args.raw_results:
            raise SystemExit("--skip-inference requires --raw-results")
        raw_results = args.raw_results
    else:
        if not args.model:
            raise SystemExit("MODEL_PATH in .env or --model is required")
        raw_results = run_inference(staging, output_dir / "raw_runs", args.model, args.max_workers, args.temperature, args.presence_penalty)
    export_lrb(read_results(raw_results), mapping, output_dir)
    print(f"Reports and stats written to {output_dir}")


if __name__ == "__main__":
    main()
