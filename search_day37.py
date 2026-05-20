# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import json
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    '苏州园林 春季旅游 2026年3月 最新攻略',
    '苏州 拙政园 留园 虎丘 2026 门票 开放时间',
]

all_results = {}

for query in queries:
    encoded_query = urllib.parse.quote(query)
    url = f'https://html.duckduckgo.com/html/?q={encoded_query}'
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    })
    try:
        response = urllib.request.urlopen(req, timeout=15)
        html = response.read().decode('utf-8')
        # Find results
        titles = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html)
        print(f'=== {query} ===')
        for i, t in enumerate(titles[:5]):
            print(f'{i+1}. {t}')
        print()
        all_results[query] = titles[:5]
    except Exception as e:
        print(f'Error for {query}: {e}')
        all_results[query] = []

output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print(f'Results saved')
