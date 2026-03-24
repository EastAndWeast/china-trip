# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

queries = [
    '婺源 江岭 油菜花 2026年3月',
    '江西婺源 旅游攻略 篁岭',
    '婺源 李坑 晓起 景点'
]

for query in queries:
    encoded = urllib.parse.quote(query)
    url = f'https://html.duckduckgo.com/html/?q={encoded}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        resp = urllib.request.urlopen(req, timeout=15)
        html = resp.read().decode('utf-8', errors='ignore')
        results = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html)
        print(f'=== {query} ===')
        for i, r in enumerate(results[:5]):
            print(f'{i+1}. {r}')
        print()
    except Exception as e:
        print(f'Error for {query}: {e}')
        print()
