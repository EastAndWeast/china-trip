# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Search for travel info for next destination
queries = [
    '黄山 旅游攻略 2026年3月',
    '宏村 西递 旅游攻略 2026',
    '江西 婺源 油菜花 2026年3月',
    '黄山 千岛湖 旅游',
]

all_results = {}

for query in queries:
    encoded_query = urllib.parse.quote(query)
    url = f'https://html.duckduckgo.com/html/?q={encoded_query}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    try:
        response = urllib.request.urlopen(req, timeout=10)
        html = response.read().decode('utf-8')
        results = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html)
        print(f'=== {query} ===')
        for i, r in enumerate(results[:5]):
            print(f'{i+1}. {r}')
        print()
        all_results[query] = results[:5]
    except Exception as e:
        print(f'Error for {query}: {e}')
        all_results[query] = []

# Save results
output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

print(f'Results saved to {output_path}')
