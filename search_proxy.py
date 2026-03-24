# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import json
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

proxy = "http://127.0.0.1:7890"
proxy_handler = urllib.request.ProxyHandler({'http': proxy, 'https': proxy})

queries = [
    '杭州西湖旅游攻略 2026年3月',
    '苏州园林旅游攻略 2026年春季',
    '上海旅游攻略 2026年3月',
    '乌镇旅游攻略 2026年春季',
]

all_results = {}

for query in queries:
    encoded_query = urllib.parse.quote(query)
    url = f'https://lite.duckduckgo.com/lite/?q={encoded_query}'
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html',
    })
    try:
        opener = urllib.request.build_opener(proxy_handler)
        response = opener.open(req, timeout=15)
        html = response.read().decode('utf-8')
        
        # Parse results - links are in <a> tags with text content
        links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]*)</a>', html)
        results = []
        snippets = []
        
        # Filter out navigation/social links, keep only result links
        for href, text in links:
            text = text.strip()
            if text and 'uddg' in href and len(text) > 10:
                results.append(text)
        
        # Try to extract snippets from nearby text
        # The snippet is often in a result__snippet class or nearby
        snippet_pattern = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>[^<]*</a>\s*([^<]+)', html)
        
        print(f'=== {query} ===')
        for i, r in enumerate(results[:5]):
            print(f'{i+1}. {r[:80]}')
        print()
        
        all_results[query] = [{'title': r, 'url': ''} for r in results[:5]]
    except Exception as e:
        print(f'Error for {query}: {e}')
        all_results[query] = []

output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

print(f'Results saved to {output_path}')
