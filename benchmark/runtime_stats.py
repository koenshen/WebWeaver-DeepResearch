"""Runtime-only instrumentation; does not edit inference source files."""
from __future__ import annotations
import os, time, threading
import requests
from openai import OpenAI
from benchmark.benchmark_stats import ResearchStats,set_current,clear_current,current,usage_dict
from benchmark.llm_trace import begin as begin_llm_trace, finish as finish_llm_trace, next_call_group, record as record_llm_trace

class JinaUsageLimitExceeded(BaseException):
    """Stop a benchmark after every configured Jina Reader key is exhausted."""

_jina_fatal_error=None

def raise_if_jina_fatal():
    if _jina_fatal_error is not None:
        raise _jina_fatal_error

def _jina_quota_log(message):
    print(f'\033[91m[Jina quota] {message}\033[0m',flush=True)

def _jina_log(message):
    print(f'[Jina] {message}',flush=True)

def _jina_summary_log(message):
    print(f'[Jina summary] {message}',flush=True)

def install(react_agent):
    original_run=react_agent.MultiTurnReactAgent._run
    def wrapped_run(self,*args,**kwargs):
        stats=ResearchStats(); set_current(stats)
        data=args[0] if args else kwargs.get('data',{})
        item=data.get('item',{}) if isinstance(data,dict) else {}
        question=item.get('question','')
        begin_llm_trace(question)
        started=time.monotonic()
        try:
            result=original_run(self,*args,**kwargs)
            # The original agent catches BaseException around tool execution.
            # Re-raise a saved Tavily quota error at this plugin boundary.
            from benchmark.tavily_search_tool import raise_if_fatal
            raise_if_fatal()
            raise_if_jina_fatal()
            summary=stats.get_summary()
            summary.update({
                'duration_seconds':time.monotonic()-started,
                'report_length':len(str(result.get('prediction',''))),
                'context_length':len(str(result.get('messages',[]))),
            })
            result['_benchmark_stats']=summary
            return result
        finally:
            clear_current()
            finish_llm_trace()
    react_agent.MultiTurnReactAgent._run=wrapped_run

    visit=react_agent.TOOL_MAP['visit']; original_visit=visit.call_server
    raw_jina_keys=os.getenv('JINA_API_KEYS','')
    jina_keys=list(dict.fromkeys(key.strip() for key in raw_jina_keys.split(',') if key.strip()))
    jina_key_index=0
    visit_context=threading.local()
    if jina_keys:
        def tracked_jina_readpage(url):
            nonlocal jina_key_index
            global _jina_fatal_error
            timeout=50; attempt=0; max_retries=3; started=time.monotonic(); attempts=[]
            visit_context.url=url
            while True:
                key_number=jina_key_index+1; key_count=len(jina_keys)
                request_started=time.monotonic()
                _jina_log(f'fetching with key {key_number}/{key_count}, attempt {attempt+1}/{max_retries}: {url}')
                try:
                    response=requests.get(
                        f'https://r.jina.ai/{url}',
                        headers={'Authorization':f'Bearer {jina_keys[jina_key_index]}'},
                        timeout=timeout,
                    )
                    request_duration=round(time.monotonic()-request_started,3)
                    attempts.append({'attempt':attempt+1,'key_index':key_number,'http_status':response.status_code,'duration_seconds':request_duration})
                    if response.status_code == 200:
                        content_length=len(response.text)
                        _jina_log(f'success: HTTP 200, key {key_number}/{key_count}, {content_length} chars, {request_duration:.3f}s: {url}')
                        if current(): current().on_visit_call(url,'success',attempts,content_length,round(time.monotonic()-started,3))
                        return response.text
                    if response.status_code in (402,403):
                        _jina_quota_log(
                            f'key {key_number}/{key_count} exhausted: '
                            f'HTTP {response.status_code}: {response.text}'
                        )
                        if jina_key_index+1 < key_count:
                            jina_key_index+=1
                            _jina_quota_log(
                                f'switching from key {key_number}/{key_count} to '
                                f'key {jina_key_index+1}/{key_count}; retrying the same URL'
                            )
                            continue
                        _jina_quota_log(
                            f'all {key_count} Jina Reader keys are exhausted; aborting benchmark'
                        )
                        _jina_fatal_error=JinaUsageLimitExceeded(response.text)
                        raise _jina_fatal_error
                    _jina_log(
                        f'failed: HTTP {response.status_code}, key {key_number}/{key_count}, '
                        f'attempt {attempt+1}/{max_retries}, {request_duration:.3f}s: {url}; '
                        f'response={response.text[:500]}'
                    )
                except JinaUsageLimitExceeded:
                    raise
                except Exception as exc:
                    request_duration=round(time.monotonic()-request_started,3)
                    if not attempts or attempts[-1].get('duration_seconds') != request_duration:
                        attempts.append({'attempt':attempt+1,'key_index':key_number,'http_status':None,'duration_seconds':request_duration,'error_type':type(exc).__name__,'error':str(exc)})
                    _jina_log(f'failed: {type(exc).__name__}: {exc}, key {key_number}/{key_count}, attempt {attempt+1}/{max_retries}: {url}')
                attempt+=1
                if attempt >= max_retries:
                    _jina_log(f'giving up after {max_retries} attempts: {url}')
                    if current(): current().on_visit_call(url,'failed',attempts,0,round(time.monotonic()-started,3))
                    return '[visit] Failed to read page.'
                time.sleep(0.5)
        visit.jina_readpage=tracked_jina_readpage

        def tracked_html_readpage_jina(url):
            for _ in range(8):
                content=visit.jina_readpage(url)
                if content and not content.startswith('[visit] Failed to read page.') and content != '[visit] Empty content.' and not content.startswith('[document_parser]'):
                    return content
            return '[visit] Failed to read page.'
        visit.html_readpage_jina=tracked_html_readpage_jina

    def tracked_visit(msgs,max_retries=2):
        key=os.getenv('API_KEY'); base=os.getenv('API_BASE'); model=os.getenv('SUMMARY_MODEL_NAME','')
        if not (key and base and model): return original_visit(msgs,max_retries)
        url=getattr(visit_context,'url','unknown')
        call_group=next_call_group('visit_summary')
        for attempt in range(max_retries):
            started=time.monotonic()
            _jina_summary_log(f'URL {url}, attempt {attempt+1}/{max_retries}, model={model}')
            try:
                response=OpenAI(api_key=key,base_url=base).chat.completions.create(model=model,messages=msgs,temperature=0.0 if attempt == 0 else 1.0,max_tokens=4000)
                content=response.choices[0].message.content or ''
                usage=usage_dict(response.usage); duration=round(time.monotonic()-started,3)
                record_llm_trace(purpose='visit_summary',call_group=call_group,attempt=attempt+1,model=model,temperature=0.0 if attempt == 0 else 1.0,messages=msgs,status='success' if content.strip() else 'empty_response',duration_seconds=duration,response=content,usage={**usage,'total_tokens':usage['input_tokens']+usage['output_tokens']})
                if content.strip():
                    _jina_summary_log(f'success: URL {url}, {len(content.strip())} chars, input_tokens={usage["input_tokens"]}, output_tokens={usage["output_tokens"]}, {duration:.3f}s')
                    if current():
                        current().on_llm_call(model,msgs,content,usage)
                        current().on_visit_summary(url,'success',duration,len(content.strip()),usage['input_tokens'],usage['output_tokens'])
                    return content.strip()
                _jina_summary_log(
                    f'empty response: URL {url}, attempt {attempt+1}/{max_retries}, '
                    f'{time.monotonic()-started:.3f}s'
                )
            except Exception as exc:
                duration=round(time.monotonic()-started,3)
                record_llm_trace(purpose='visit_summary',call_group=call_group,attempt=attempt+1,model=model,temperature=0.0 if attempt == 0 else 1.0,messages=msgs,status='api_error',duration_seconds=duration,error=exc)
                _jina_summary_log(f'failed: URL {url}, {type(exc).__name__}: {exc}, {duration:.3f}s')
                if attempt==max_retries-1:
                    if current(): current().on_visit_summary(url,'failed',duration,0,error=f'{type(exc).__name__}: {exc}')
                    return f'[visit] Summary server error: {exc}'
                time.sleep(1)
        if current(): current().on_visit_summary(url,'failed',0,0,error='Summary server returned empty content.')
        return '[visit] Summary server returned empty content.'
    visit.call_server=tracked_visit
