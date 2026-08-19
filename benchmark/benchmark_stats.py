"""Same statistics contract as ../gpt-researcher/benchmark_stats.py."""
import json
from pathlib import Path
from typing import Any
try:
    import tiktoken
except ImportError:
    tiktoken = None

_CURRENT_STATS = None

class ResearchStats:
    def __init__(self):
        self.llm_calls=[]; self.search_calls=[]; self.visit_calls=[]
        self.total_input_tokens=0; self.total_output_tokens=0
        self.total_search_count=0; self.total_search_results=0
        self.total_visit_count=0; self.total_visit_success=0; self.total_visit_failed=0
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
    def on_visit_call(self, url, status, attempts, content_length, duration_seconds):
        detail={
            'url':url,
            'retriever':'jina',
            'status':status,
            'attempts':attempts,
            'content_length':content_length,
            'duration_seconds':duration_seconds,
            'summary_status':'not_started',
        }
        self.visit_calls.append(detail)
        self.total_visit_count+=1
        if status == 'success': self.total_visit_success+=1
        else: self.total_visit_failed+=1
        if url: self.source_urls.add(url)
        return detail
    def on_visit_summary(self, url, status, duration_seconds, summary_length, input_tokens=0, output_tokens=0, error=None):
        detail=next((item for item in reversed(self.visit_calls) if item['url']==url and item['summary_status']=='not_started'),None)
        if detail is None: return
        detail.update({
            'summary_status':status,
            'summary_duration_seconds':duration_seconds,
            'summary_length':summary_length,
            'summary_input_tokens':input_tokens,
            'summary_output_tokens':output_tokens,
        })
        if error: detail['summary_error']=error
    def get_summary(self):
        return {'total_llm_calls':len(self.llm_calls),'total_input_tokens':self.total_input_tokens,'total_output_tokens':self.total_output_tokens,'total_tokens':self.total_input_tokens+self.total_output_tokens,'total_search_count':self.total_search_count,'total_search_results':self.total_search_results,'total_visit_count':self.total_visit_count,'total_visit_success':self.total_visit_success,'total_visit_failed':self.total_visit_failed,'llm_calls_detail':self.llm_calls,'search_calls_detail':self.search_calls,'visit_calls_detail':self.visit_calls,'source_urls_count':len(self.source_urls)}

def set_current(stats):
    global _CURRENT_STATS
    _CURRENT_STATS = stats

def current():
    return _CURRENT_STATS

def clear_current():
    global _CURRENT_STATS
    _CURRENT_STATS = None

def usage_dict(usage):
    return {'input_tokens':getattr(usage,'prompt_tokens',0) or 0,'output_tokens':getattr(usage,'completion_tokens',0) or 0}

def write_stats(path: Path, result: dict[str,Any], metadata: dict[str,Any]):
    if '_benchmark_stats' not in result: raise RuntimeError('Missing runtime benchmark statistics')
    data=dict(result['_benchmark_stats']); data.update(metadata)
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
