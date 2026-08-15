"""Runtime-only instrumentation; does not edit inference source files."""
from __future__ import annotations
import os, time
from openai import OpenAI
from benchmark.benchmark_stats import ResearchStats,set_current,clear_current,current,usage_dict

def install(react_agent):
    original_run=react_agent.MultiTurnReactAgent._run
    def wrapped_run(self,*args,**kwargs):
        stats=ResearchStats(); set_current(stats)
        started=time.monotonic()
        try:
            result=original_run(self,*args,**kwargs)
            # The original agent catches BaseException around tool execution.
            # Re-raise a saved Tavily quota error at this plugin boundary.
            from benchmark.tavily_search_tool import raise_if_fatal
            raise_if_fatal()
            summary=stats.get_summary()
            summary.update({
                'duration_seconds':time.monotonic()-started,
                'report_length':len(str(result.get('prediction',''))),
                'context_length':len(str(result.get('messages',[]))),
            })
            result['_benchmark_stats']=summary
            return result
        finally: clear_current()
    react_agent.MultiTurnReactAgent._run=wrapped_run

    visit=react_agent.TOOL_MAP['visit']; original_visit=visit.call_server
    def tracked_visit(msgs,max_retries=2):
        key=os.getenv('API_KEY'); base=os.getenv('API_BASE'); model=os.getenv('SUMMARY_MODEL_NAME','')
        if not (key and base and model): return original_visit(msgs,max_retries)
        for attempt in range(max_retries):
            try:
                response=OpenAI(api_key=key,base_url=base).chat.completions.create(model=model,messages=msgs,temperature=0.0 if attempt == 0 else 1.0,max_tokens=4000)
                content=response.choices[0].message.content or ''
                if content.strip():
                    if current(): current().on_llm_call(model,msgs,content,usage_dict(response.usage))
                    return content.strip()
            except Exception as exc:
                if attempt==max_retries-1: return f'[visit] Summary server error: {exc}'
                time.sleep(1)
        return '[visit] Summary server returned empty content.'
    visit.call_server=tracked_visit
