"""Runtime transport for using an OpenAI-compatible API as the main agent LLM."""

from __future__ import annotations

import os
import time
from typing import Any
import json5

from openai import APIConnectionError, APIError, APITimeoutError, OpenAI
from benchmark.benchmark_stats import current, usage_dict
from benchmark.llm_trace import next_call_group, record as record_llm_trace
from benchmark.runtime_log import heartbeat, log, preview


class LLMResponseRetriesExhausted(RuntimeError):
    """A round exhausted its ten API/format/search-completion attempts."""


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
                temperature = 1
                started = time.monotonic()
                log(f'[main_agent call_group={call_group} attempt={attempt+1}/{max_tries}] START input_messages={len(msgs)} temperature={temperature}')
                stop_waiting = heartbeat(f'main_agent call_group={call_group} attempt={attempt+1}/{max_tries}')
                response = client.chat.completions.create(
                    model=model,
                    messages=msgs,
                    stop=["\n<tool_response>", "<tool_response>"],
                    temperature=temperature,
                    top_p=self.llm_generate_cfg.get("top_p", 0.95),
                    max_tokens=int(os.getenv("OPENAI_COMPATIBLE_MAX_OUTPUT_TOKENS", "131072")),
                    presence_penalty=self.llm_generate_cfg.get("presence_penalty", 1.1),
                )
                duration = stop_waiting()
                content = response.choices[0].message.content
                usage = usage_dict(response.usage)
                has_tool = bool(content and '<tool_call>' in content and '</tool_call>' in content)
                if has_tool:
                    try:
                        json5.loads(content.split('<tool_call>', 1)[1].split('</tool_call>', 1)[0])
                    except Exception:
                        has_tool = False
                has_answer = bool(content and '<answer>' in content and '</answer>' in content)
                valid_protocol = has_tool or has_answer
                missing_search = has_answer and current() is not None and current().total_search_results <= 0
                status = 'success' if content and content.strip() and valid_protocol and not missing_search else ('no_tavily_search' if missing_search else ('invalid_protocol_response' if content and content.strip() else 'empty_response'))
                record_llm_trace(
                    purpose="main_agent", call_group=call_group, attempt=attempt + 1,
                    model=model, temperature=temperature, messages=msgs,
                    status=status, duration_seconds=duration, response=content or "",
                    usage={**usage, "total_tokens": usage["input_tokens"] + usage["output_tokens"]},
                    valid_protocol_response=valid_protocol,
                )
                if content and content.strip() and valid_protocol and not missing_search:
                    log(f'[main_agent call_group={call_group} attempt={attempt+1}/{max_tries}] END status=success duration={duration:.3f}s input_tokens={usage["input_tokens"]} output_tokens={usage["output_tokens"]}')
                    if current():
                        current().on_llm_call(model, msgs, content.strip(), usage)
                    return content.strip()
                reason = 'no successful Tavily search before final answer' if missing_search else ('invalid protocol response' if content and content.strip() else 'empty response')
                log(f'[main_agent call_group={call_group} attempt={attempt+1}/{max_tries}] RETRY reason={reason} duration={duration:.3f}s')
                if content and content.strip(): preview('main_agent invalid', content.strip())
            except (APIError, APIConnectionError, APITimeoutError) as exc:
                if 'stop_waiting' in locals(): stop_waiting()
                record_llm_trace(purpose="main_agent",call_group=call_group,attempt=attempt+1,model=model,temperature=locals().get('temperature'),messages=msgs,status="api_error",duration_seconds=time.monotonic()-locals().get('started',time.monotonic()),error=exc)
                log(f'[main_agent call_group={call_group} attempt={attempt+1}/{max_tries}] API_ERROR {exc}')
            except Exception as exc:
                if 'stop_waiting' in locals(): stop_waiting()
                record_llm_trace(purpose="main_agent",call_group=call_group,attempt=attempt+1,model=model,temperature=locals().get('temperature'),messages=msgs,status="unexpected_error",duration_seconds=time.monotonic()-locals().get('started',time.monotonic()),error=exc)
                log(f'[main_agent call_group={call_group} attempt={attempt+1}/{max_tries}] UNEXPECTED_ERROR {exc}')
            if attempt < max_tries - 1:
                time.sleep(min(2 ** attempt, 30))
        raise LLMResponseRetriesExhausted(f'main_agent call_group={call_group} exhausted {max_tries} attempts')

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
