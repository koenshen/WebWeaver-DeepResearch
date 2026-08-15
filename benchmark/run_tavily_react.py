#!/usr/bin/env python3
"""Run the unmodified multi-ReAct runner, optionally with a Tavily-only plugin.

All arguments are passed through to inference/run_multi_react.py.  The plugin
is activated solely by ONLY_TAVILY=true in the repository-root .env.
"""

from __future__ import annotations

import os
import runpy
import sys
from pathlib import Path

from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parents[1]
INFERENCE = ROOT / "inference"


def main() -> None:
    load_dotenv(ROOT / ".env", override=False)
    sys.path.insert(0, str(ROOT))
    sys.path.insert(0, str(INFERENCE))
    os.chdir(INFERENCE)  # preserve the original shell runner's working directory

    only_tavily = os.getenv("ONLY_TAVILY", "false").strip().lower() == "true"
    use_external_main = os.getenv("USE_OPENAI_COMPATIBLE_MAIN_MODEL", "false").strip().lower() == "true"
    if only_tavily or use_external_main:
        import react_agent
        from benchmark.runtime_stats import install as install_stats
        install_stats(react_agent)

    if use_external_main:
        from benchmark.openai_compatible_transport import install

        install(react_agent)
        print("OpenAI-compatible main-model plugin enabled")

    if only_tavily:
        if not os.getenv("TAVILY_API_KEY"):
            raise SystemExit("ONLY_TAVILY=true requires TAVILY_API_KEY in the root .env")
        import prompt
        from benchmark.tavily_search_tool import DisabledScholarTool, TavilySearchTool, tavily_only_prompt

        react_agent.TOOL_MAP["search"] = TavilySearchTool()
        react_agent.TOOL_MAP["google_scholar"] = DisabledScholarTool()
        react_agent.SYSTEM_PROMPT = tavily_only_prompt(prompt.SYSTEM_PROMPT)
        print("Tavily-only plugin enabled: search=Tavily, google_scholar=disabled")
    elif not use_external_main:
        print("Tavily-only plugin disabled: preserving original inference behavior")

    sys.argv = [str(INFERENCE / "run_multi_react.py"), *sys.argv[1:]]
    runpy.run_path(str(INFERENCE / "run_multi_react.py"), run_name="__main__")


if __name__ == "__main__":
    main()
