# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import json
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('苏州旅游攻略 2026年3月 拙政园 平江路', '苏州旅游'),
    ('扬州旅游攻略 2026年3月 烟花三月', '扬州旅游'),
    ('南京旅游攻略 2026年3月 中山陵 夫子庙', '南京旅游'),
    ('无锡灵山拈花湾旅游攻略 2026年春季', '无锡旅游'),
    ('黄山旅游攻略 2026年3月 宏村西递', '黄山旅游'),
]

all_results = {}

for query, name in queries:
    encoded_query = urllib.parse.quote(query)
    url = f'https://html.duckduckgo.com/html/?q={encoded_query}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    try:
        response = urllib.request.urlopen(req, timeout=10)
        html = response.read().decode('utf-8')
        pattern = r'<a class="result__a"[^>]*>([^<]*)</a>'
        results = re.findall(pattern, html)
        print(f'=== {name}: {query} ===')
        for i, r in enumerate(results[:5]):
            print(f'{i+1}. {r}')
        print()
        all_results[query] = [{'title': r} for r in results[:5]]
    except Exception as e:
        print(f'Error for {query}: {e}')
        all_results[query] = []

# Save results
output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print(f'Saved to {output_path}')
