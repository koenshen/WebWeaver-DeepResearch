"""Tavily replacement for the inference ``search`` tool.

This module is intentionally external to ``inference/``.  Its public contract
matches the existing Search tool: ``call({"query": [..]}) -> str``.
"""

from __future__ import annotations

import json
import os
import re
from typing import Optional, Union

import requests
from qwen_agent.tools.base import BaseTool
from benchmark.benchmark_stats import current


class TavilyUsageLimitExceeded(BaseException):
    """Stop a benchmark when the Tavily plan usage limit is exhausted."""


_fatal_error: TavilyUsageLimitExceeded | None = None


def raise_if_fatal() -> None:
    """Re-raise a fatal Tavily error outside WebWeaver's bare tool exception."""
    if _fatal_error is not None:
        raise _fatal_error


def _overflow_log(message: str) -> None:
    """Make Tavily query-length handling conspicuous in terminal output."""
    print(f"\033[91m[Tavily overflow] {message}\033[0m", flush=True)


def _quota_log(message: str) -> None:
    """Make Tavily quota exhaustion and key rotation conspicuous."""
    print(f"\033[91m[Tavily quota] {message}\033[0m", flush=True)


class TavilySearchTool(BaseTool):
    name = "search"
    description = "Performs batched Tavily web searches."
    parameters = {
        "type": "object",
        "properties": {
            "query": {
                "type": "array",
                "items": {"type": "string"},
                "minItems": 1,
                "description": "The list of search queries.",
            }
        },
        "required": ["query"],
    }

    def __init__(self, cfg: Optional[dict] = None):
        super().__init__(cfg)
        raw_keys = os.getenv("TAVILY_API_KEY", "")
        self._api_keys = list(dict.fromkeys(
            key.strip() for key in raw_keys.split(",") if key.strip()
        ))
        self._api_key_index = 0

    @staticmethod
    def _max_results() -> int:
        return int(os.getenv("MAX_SEARCH_RESULTS_PER_QUERY", "10"))

    @staticmethod
    def _compress_query(query: str) -> str:
        """Mirror GPT Researcher's configurable Tavily overflow policy."""
        limit = int(os.getenv("TAVILY_QUERY_MAX_LENGTH", "399"))
        if len(query) <= limit:
            return query
        mode = os.getenv("TAVILY_OVERFLOW_LENGTH", "truncate").lower()
        _overflow_log(f"mode={mode}, length={len(query)}, limit={limit}")
        if mode != "summary":
            _overflow_log(f"force-truncated original query to {limit} characters")
            return query[:limit]

        # The optional summary path deliberately uses GPT Researcher's env names.
        # If it cannot be configured or fails, fall back to deterministic truncate.
        model = os.getenv("STRATEGIC_LLM", "").split(":", 1)[-1]
        key = os.getenv("OPENAI_API_KEY", "")
        base_url = os.getenv("OPENAI_BASE_URL", "")
        if not (model and key):
            _overflow_log("summary model is not configured; falling back to truncation")
            return query[:limit]
        try:
            from openai import OpenAI

            client = OpenAI(api_key=key, base_url=base_url or None)
            attempts = int(os.getenv("TAVILY_OVERFLOW_MAX_SUMMARY_ATTEMPTS", "20"))
            current = query
            for attempt in range(1, attempts + 1):
                _overflow_log(
                    f"LLM summary attempt {attempt}/{attempts}, input_length={len(current)}"
                )
                response = client.chat.completions.create(
                    model=model,
                    temperature=0,
                    max_tokens=1000,
                    messages=[{
                        "role": "user",
                        "content": (
                            f"Compress this into one web search query under {limit} "
                            "characters. Return only the query:\n\n" + current
                        ),
                    }],
                )
                current = (response.choices[0].message.content or "").strip()
                _overflow_log(f"LLM summary output_length={len(current)}")
                if len(current) <= limit:
                    _overflow_log(f"LLM summary succeeded on attempt {attempt}")
                    return current
        except Exception as exc:
            _overflow_log(f"LLM summary failed: {exc}; falling back to truncation")
        _overflow_log(f"force-truncated original query to {limit} characters")
        return query[:limit]

    def _search_one(self, query: str) -> str:
        if not self._api_keys:
            return "[Search] Tavily API key is not configured."
        effective_query = self._compress_query(query)
        while True:
            key_number = self._api_key_index + 1
            key_count = len(self._api_keys)
            payload = {
                "query": effective_query,
                "search_depth": "basic",
                "topic": "general",
                "days": 2,
                "include_answer": False,
                "include_raw_content": False,
                "max_results": self._max_results(),
                "include_domains": None,
                "exclude_domains": None,
                "include_images": False,
                "api_key": self._api_keys[self._api_key_index],
                "use_cache": True,
            }
            try:
                response = requests.post(
                    "https://api.tavily.com/search",
                    data=json.dumps(payload),
                    headers={"Content-Type": "application/json"},
                    timeout=100,
                )
                if response.status_code in (403, 432, 433):
                    _quota_log(
                        f"key {key_number}/{key_count} exhausted: "
                        f"HTTP {response.status_code}: {response.text}"
                    )
                    if self._api_key_index + 1 < key_count:
                        self._api_key_index += 1
                        _quota_log(
                            f"switching from key {key_number}/{key_count} to "
                            f"key {self._api_key_index + 1}/{key_count}; "
                            "retrying the same query"
                        )
                        continue
                    _quota_log(f"all {key_count} Tavily keys are exhausted; aborting benchmark")
                    if current():
                        current().on_search_call(query, effective_query, "tavily", 0)
                    global _fatal_error
                    _fatal_error = TavilyUsageLimitExceeded(response.text)
                    raise _fatal_error
                response.raise_for_status()
                results = response.json().get("results", [])
                break
            except Exception as exc:
                if current(): current().on_search_call(query, effective_query, 'tavily', 0)
                return f"[Search] Tavily request failed for {query!r}: {exc}"

        if current():
            current().on_search_call(
                query,
                effective_query,
                "tavily",
                len(results),
                [item.get("url") for item in results],
            )

        entries = []
        for index, item in enumerate(results, start=1):
            title = item.get("title") or item.get("url") or "Untitled"
            url = item.get("url", "")
            content = item.get("content", "")
            entries.append(f"{index}. [{title}]({url})\n{content}")
        if not entries:
            return f"No results found for {query!r}. Try a more general query."
        return (
            f"A Tavily search for {query!r} found {len(entries)} results:\n\n"
            "## Web Results\n" + "\n\n".join(entries)
        )

    def call(self, params: Union[str, dict], **kwargs) -> str:
        if not isinstance(params, dict) or "query" not in params:
            return "[Search] Invalid request format: expected a query field."
        queries = params["query"]
        if isinstance(queries, str):
            queries = [queries]
        if not isinstance(queries, list) or not all(isinstance(q, str) for q in queries):
            return "[Search] Invalid query: expected a string or a list of strings."
        return "\n=======\n".join(self._search_one(query) for query in queries)


class DisabledScholarTool:
    """A no-network replacement that prevents accidental Serper Scholar calls."""

    name = "google_scholar"

    def call(self, params: Union[str, dict], **kwargs) -> str:
        return (
            "[google_scholar] Disabled for this Tavily-only benchmark run. "
            "Use the search tool instead."
        )


def tavily_only_prompt(base_prompt: str) -> str:
    """Remove Scholar from the original prompt without editing prompt.py."""
    lines = [line for line in base_prompt.splitlines() if '"name": "google_scholar"' not in line]
    prompt = "\n".join(lines)
    return prompt.replace(
        "Perform Google web searches then returns a string of the top search results.",
        "Perform Tavily web searches and return a string of the top search results.",
    )
