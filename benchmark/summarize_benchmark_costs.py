#!/usr/bin/env python3
"""Summarize completed LiveResearch and DeepResearch benchmark costs."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Any

import tiktoken
from rich import box
from rich.console import Console
from rich.table import Table


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LIVE_DIR = PROJECT_ROOT / "benchmark_outputs" / "liveresearch-20260816-1535"
DEFAULT_DEEP_DIR = PROJECT_ROOT / "benchmark_outputs" / "deepresearch-20260816-1535"
REQUIRED_NUMERIC_FIELDS = (
    "total_input_tokens",
    "total_output_tokens",
    "total_tokens",
    "total_search_count",
    "total_search_results",
    "duration_seconds",
)


@dataclass(frozen=True)
class BenchmarkTotals:
    question_count: int
    input_tokens: int
    output_tokens: int
    total_tokens: int
    tavily_calls: int
    tavily_results: int
    duration_seconds: float
    report_characters: int
    report_tokens: int

    def mean(self, value: int | float) -> float:
        return value / self.question_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live-dir", type=Path, default=DEFAULT_LIVE_DIR)
    parser.add_argument("--deep-dir", type=Path, default=DEFAULT_DEEP_DIR)
    parser.add_argument(
        "--encoding",
        default="cl100k_base",
        help="tiktoken encoding used to count final-report tokens",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read valid JSON from {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return value


def require_number(stats: dict[str, Any], field: str, path: Path) -> int | float:
    value = stats.get(field)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"Missing or non-numeric {field!r} in {path}")
    return value


def collect(directory: Path, encoding: tiktoken.Encoding) -> BenchmarkTotals:
    directory = directory.resolve()
    if not directory.is_dir():
        raise ValueError(f"Benchmark output directory does not exist: {directory}")

    stats_paths = sorted(directory.glob("*_stats.json"))
    if not stats_paths:
        raise ValueError(f"No *_stats.json files found in {directory}")

    sums: dict[str, int | float] = {field: 0 for field in REQUIRED_NUMERIC_FIELDS}
    report_characters = 0
    report_tokens = 0

    for stats_path in stats_paths:
        stats = load_json(stats_path)
        values = {
            field: require_number(stats, field, stats_path)
            for field in REQUIRED_NUMERIC_FIELDS
        }
        if values["total_tokens"] != (
            values["total_input_tokens"] + values["total_output_tokens"]
        ):
            raise ValueError(
                f"total_tokens is not input + output in {stats_path}: "
                f"{values['total_tokens']} != {values['total_input_tokens']} + "
                f"{values['total_output_tokens']}"
            )

        detail = stats.get("search_calls_detail")
        if isinstance(detail, list) and len(detail) != values["total_search_count"]:
            raise ValueError(
                f"total_search_count does not match search_calls_detail in {stats_path}"
            )

        report_path = stats_path.with_name(
            stats_path.name.removesuffix("_stats.json") + "_report.md"
        )
        if not report_path.is_file():
            raise ValueError(f"Missing report paired with {stats_path}: {report_path}")
        report = report_path.read_text(encoding="utf-8")
        if "report_length" in stats and stats["report_length"] != len(report):
            raise ValueError(
                f"report_length does not match the report file in {stats_path}: "
                f"{stats['report_length']} != {len(report)}"
            )

        for field, value in values.items():
            sums[field] += value
        report_characters += len(report)
        report_tokens += len(encoding.encode(report))

    return BenchmarkTotals(
        question_count=len(stats_paths),
        input_tokens=int(sums["total_input_tokens"]),
        output_tokens=int(sums["total_output_tokens"]),
        total_tokens=int(sums["total_tokens"]),
        tavily_calls=int(sums["total_search_count"]),
        tavily_results=int(sums["total_search_results"]),
        duration_seconds=float(sums["duration_seconds"]),
        report_characters=report_characters,
        report_tokens=report_tokens,
    )


def format_minutes(mean_seconds: float) -> str:
    rounded_seconds = int(
        Decimal(str(mean_seconds)).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    )
    minutes, seconds = divmod(rounded_seconds, 60)
    return f"约 {minutes} 分 {seconds} 秒"


def format_average(total: int | float, count: int) -> str:
    average = Decimal(str(total)) / Decimal(count)
    rounded = average.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"{rounded:,.2f}"


def result_rows(totals: BenchmarkTotals) -> list[tuple[str, str]]:
    mean_duration = totals.mean(totals.duration_seconds)
    return [
        ("成功完成题数", f"{totals.question_count:,}"),
        ("平均输入 token/题", format_average(totals.input_tokens, totals.question_count)),
        ("平均输出 token/题", format_average(totals.output_tokens, totals.question_count)),
        ("平均总 token/题", format_average(totals.total_tokens, totals.question_count)),
        ("平均 Tavily 调用/题", format_average(totals.tavily_calls, totals.question_count)),
        ("平均 Tavily 搜索结果/题", format_average(totals.tavily_results, totals.question_count)),
        ("平均耗时/题", f"{format_average(totals.duration_seconds, totals.question_count)} 秒"),
        ("换算为分钟", format_minutes(mean_duration)),
        (
            "平均结果数/Tavily 调用",
            format_average(totals.tavily_results, totals.tavily_calls),
        ),
        ("平均最终报告字符数", format_average(totals.report_characters, totals.question_count)),
        ("平均最终报告 token 数", format_average(totals.report_tokens, totals.question_count)),
    ]


def total_rows(totals: BenchmarkTotals) -> list[tuple[str, str]]:
    return [
        ("总输入 token", f"{totals.input_tokens:,}"),
        ("总输出 token", f"{totals.output_tokens:,}"),
        ("总 token", f"{totals.total_tokens:,}"),
        ("Tavily 总调用数", f"{totals.tavily_calls:,}"),
        ("Tavily 总结果数", f"{totals.tavily_results:,}"),
        ("总耗时", f"{totals.duration_seconds:,.2f} 秒"),
        ("最终报告总字符数", f"{totals.report_characters:,}"),
        ("最终报告总 token 数", f"{totals.report_tokens:,}"),
    ]


def print_comparison(
    console: Console,
    first_column: str,
    live_rows: list[tuple[str, str]],
    deep_rows: list[tuple[str, str]],
) -> None:
    if [label for label, _ in live_rows] != [label for label, _ in deep_rows]:
        raise ValueError("Comparison rows do not have matching labels")
    table = Table(box=box.HEAVY_HEAD, show_lines=True, pad_edge=False)
    table.add_column(first_column, no_wrap=True)
    table.add_column("LiveResearch", justify="right", no_wrap=True)
    table.add_column("DeepResearch", justify="right", no_wrap=True)
    for (label, live_value), (_, deep_value) in zip(live_rows, deep_rows):
        table.add_row(label, live_value, deep_value)
    console.print(table)


def main() -> None:
    args = parse_args()
    try:
        encoding = tiktoken.get_encoding(args.encoding)
        live = collect(args.live_dir, encoding)
        deep = collect(args.deep_dir, encoding)
    except (OSError, ValueError) as exc:
        raise SystemExit(f"error: {exc}") from exc

    console = Console()
    console.print("[bold]## 统计结果[/bold]")
    console.print()
    print_comparison(console, "指标", result_rows(live), result_rows(deep))
    console.print()
    console.print("[bold]## 聚合分子[/bold]")
    console.print()
    console.print("为了方便复算，两个 benchmark 的总量如下：")
    console.print()
    print_comparison(console, "总量", total_rows(live), total_rows(deep))


if __name__ == "__main__":
    main()
