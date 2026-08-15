"""Same statistics contract as ../gpt-researcher/benchmark_stats.py."""
import json
import threading
from pathlib import Path
from typing import Any
try:
    import tiktoken
except ImportError:
    tiktoken = None

_LOCAL = threading.local()

class ResearchStats:
    def __init__(self):
        self.llm_calls=[]; self.search_calls=[]
        self.total_input_tokens=0; self.total_output_tokens=0
        self.total_search_count=0; self.total_search_results=0
        self.source_urls=set()
        self._encoder=tiktoken.get_encoding('cl100k_base') if tiktoken else None
    def _count_tokens(self, text):
        return len(self._encoder.encode(str(text))) if self._encoder else len(str(text))//4
    def on_llm_call(self, model, messages, response, usage_metadata=None):
        if usage_metadata and usage_metadata.get('input_tokens',0)>0:
            inp=usage_metadata['input_tokens']; out=usage_metadata['output_tokens']
        else:
            inp=self._count_tokens('\n'.join(str(m.get('content','')) for m in messages)); out=self._count_tokens(response)
        self.llm_calls.append({'model':model,'input_tokens':inp,'output_tokens':out,'total_tokens':inp+out,'message_count':len(messages)})
        self.total_input_tokens+=inp; self.total_output_tokens+=out
    def on_search_call(self, query, effective_query, retriever, num_results, source_urls=None):
        self.search_calls.append({'query':query,'effective_query':effective_query,'retriever':retriever,'num_results':num_results})
        self.total_search_count+=1; self.total_search_results+=num_results
        self.source_urls.update(url for url in (source_urls or []) if url)
    def get_summary(self):
        return {'total_llm_calls':len(self.llm_calls),'total_input_tokens':self.total_input_tokens,'total_output_tokens':self.total_output_tokens,'total_tokens':self.total_input_tokens+self.total_output_tokens,'total_search_count':self.total_search_count,'total_search_results':self.total_search_results,'llm_calls_detail':self.llm_calls,'search_calls_detail':self.search_calls,'source_urls_count':len(self.source_urls)}

def set_current(stats): _LOCAL.stats=stats
def current(): return getattr(_LOCAL,'stats',None)
def clear_current(): _LOCAL.stats=None

def usage_dict(usage):
    return {'input_tokens':getattr(usage,'prompt_tokens',0) or 0,'output_tokens':getattr(usage,'completion_tokens',0) or 0}

def write_stats(path: Path, result: dict[str,Any], metadata: dict[str,Any]):
    if '_benchmark_stats' not in result: raise RuntimeError('Missing runtime benchmark statistics')
    data=dict(result['_benchmark_stats']); data.update(metadata)
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
