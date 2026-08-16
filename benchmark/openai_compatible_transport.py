"""Runtime transport for using an OpenAI-compatible API as the main agent LLM."""

from __future__ import annotations

import os
import time
from typing import Any

from openai import APIConnectionError, APIError, APITimeoutError, OpenAI
from benchmark.benchmark_stats import current, usage_dict
from benchmark.llm_trace import next_call_group, record as record_llm_trace


NO_SUPPORT_TEMPERATURE_MODELS = {
    "deepseek/deepseek-reasoner", "o1-mini", "o1-mini-2024-09-12",
    "o1", "o1-2024-12-17", "o3-mini", "o3-mini-2025-01-31",
    "o1-preview", "o3", "o3-2025-04-16", "o4-mini",
    "o4-mini-2025-04-16", "gpt-5", "gpt-5-mini",
}


def enabled() -> bool:
    return os.getenv("USE_OPENAI_COMPATIBLE_MAIN_MODEL", "false").strip().lower() == "true"


def install(react_agent_module: Any) -> None:
    """Patch only the loaded module; no file under inference/ is changed."""
    key = os.getenv("OPENAI_COMPATIBLE_API_KEY", "")
    base_url = os.getenv("OPENAI_COMPATIBLE_API_BASE", "")
    model = os.getenv("OPENAI_COMPATIBLE_MODEL", "")
    if not all((key, base_url, model)):
        raise RuntimeError(
            "USE_OPENAI_COMPATIBLE_MAIN_MODEL=true requires "
            "OPENAI_COMPATIBLE_API_KEY, OPENAI_COMPATIBLE_API_BASE, and "
            "OPENAI_COMPATIBLE_MODEL in the root .env"
        )
    timeout = float(os.getenv("OPENAI_COMPATIBLE_TIMEOUT", "600"))

    def call_server(self: Any, msgs: list[dict[str, str]], planning_port: int, max_tries: int = 10) -> str:
        client = OpenAI(api_key=key, base_url=base_url, timeout=timeout)
        call_group = next_call_group("main_agent")
        for attempt in range(max_tries):
            from benchmark.tavily_search_tool import raise_if_fatal
            from benchmark.runtime_stats import raise_if_jina_fatal
            raise_if_fatal()
            raise_if_jina_fatal()
            try:
                temperature = self.llm_generate_cfg.get("temperature", 0.6)
                if attempt >= 1 and model not in NO_SUPPORT_TEMPERATURE_MODELS:
                    temperature = 1
                started = time.monotonic()
                response = client.chat.completions.create(
                    model=model,
                    messages=msgs,
                    stop=["\n<tool_response>", "<tool_response>"],
                    temperature=temperature,
                    top_p=self.llm_generate_cfg.get("top_p", 0.95),
                    max_tokens=10000,
                    presence_penalty=self.llm_generate_cfg.get("presence_penalty", 1.1),
                )
                content = response.choices[0].message.content
                usage = usage_dict(response.usage)
                record_llm_trace(
                    purpose="main_agent", call_group=call_group, attempt=attempt + 1,
                    model=model, temperature=temperature, messages=msgs,
                    status="success" if content and content.strip() else "empty_response",
                    duration_seconds=time.monotonic() - started, response=content or "",
                    usage={**usage, "total_tokens": usage["input_tokens"] + usage["output_tokens"]},
                )
                if content and content.strip():
                    if current():
                        current().on_llm_call(model, msgs, content.strip(), usage)
                    return content.strip()
                print(f"Warning: external API returned an empty response (attempt {attempt + 1}/{max_tries})")
            except (APIError, APIConnectionError, APITimeoutError) as exc:
                record_llm_trace(purpose="main_agent",call_group=call_group,attempt=attempt+1,model=model,temperature=locals().get('temperature'),messages=msgs,status="api_error",duration_seconds=time.monotonic()-locals().get('started',time.monotonic()),error=exc)
                print(f"External API error (attempt {attempt + 1}/{max_tries}): {exc}")
            except Exception as exc:
                record_llm_trace(purpose="main_agent",call_group=call_group,attempt=attempt+1,model=model,temperature=locals().get('temperature'),messages=msgs,status="unexpected_error",duration_seconds=time.monotonic()-locals().get('started',time.monotonic()),error=exc)
                print(f"Unexpected external API error (attempt {attempt + 1}/{max_tries}): {exc}")
            if attempt < max_tries - 1:
                time.sleep(min(2 ** attempt, 30))
        return "vllm server error!!!"

    def count_tokens(self: Any, messages: list[dict[str, str]]) -> int:
        """Avoid loading local model weights merely to estimate context length."""
        text = "\n".join(str(message.get("content", "")) for message in messages)
        try:
            import tiktoken

            return len(tiktoken.get_encoding("cl100k_base").encode(text))
        except Exception:
            return max(1, len(text) // 4) if text else 0

    react_agent_module.MultiTurnReactAgent.call_server = call_server
    react_agent_module.MultiTurnReactAgent.count_tokens = count_tokens
