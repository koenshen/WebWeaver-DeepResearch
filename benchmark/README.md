# Benchmark plugin

This directory adapts the unmodified ReAct inference implementation to
LiveResearchBench and DeepResearch Bench. It does not edit files under
`inference/`.

Configure the repository-root `.env`. Set `ONLY_TAVILY=true` to use the
runtime Tavily plugin; set it to `false` to preserve the original Serper and
Google Scholar behavior. The Tavily fields in `.env.example` deliberately use
the same names as `../gpt-researcher/.env`.

For an OpenAI-compatible primary model (without local weights), also set
`USE_OPENAI_COMPATIBLE_MAIN_MODEL=true` and the three
`OPENAI_COMPATIBLE_API_*` / `OPENAI_COMPATIBLE_MODEL` fields. This is another
runtime-only plugin and does not require local vLLM servers.

With local weights, start the existing vLLM servers first. With the external
main-model plugin, no local vLLM server is needed. Then run one task, for example:

```bash
python benchmark/run_liveresearch_bench.py --num-questions 1
python benchmark/run_deepresearch_bench.py --num-questions 1
```

Both commands invoke the existing `inference/run_multi_react.py` with one
rollout, export evaluator-ready reports, and write a per-task `*_stats.json`.
Use `--num-questions 0` to inspect resumable progress. The generated report
directories can be passed to each benchmark's official evaluator.
