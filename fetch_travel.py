# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import json
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Try a different approach with DDG
queries = [
    '杭州 西湖 春季 旅游 攻略 2026',
    '苏州 园林 春季 旅游 2026',
    '上海 3月 旅游 攻略 2026',
]

all_results = {}

for query in queries:
    # Use the /d.js endpoint which is simpler
    encoded_query = urllib.parse.quote(query)
    url = f'https://lite.duckduckgo.com/lite/?q={encoded_query}'
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    })
    try:
        response = urllib.request.urlopen(req, timeout=15)
        html = response.read().decode('utf-8')
        # Find results
        results = re.findall(r'<a class="result__a"[^>]*href="([^"]*)"[^>]*>([^<]*)</a>', html)
        snippets = re.findall(r'<a class="result__snippet"[^>]*>([^<]*)</a>', html)
        print(f'=== {query} ===')
        for i, r in enumerate(results[:5]):
            snip = snippets[i] if i < len(snippets) else ''
            print(f'{i+1}. {r[1]} | {snip[:80]}')
        print()
        all_results[query] = [{'title': r[1], 'url': r[0], 'snippet': snippets[i] if i < len(snippets) else ''} for i, r in enumerate(results[:5])]
    except Exception as e:
        print(f'Error for {query}: {e}')
        all_results[query] = []

output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

print(f'Results saved to {output_path}')
