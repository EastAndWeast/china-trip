# -*- coding: utf-8 -*-
"""Search for travel info for next destinations"""
import urllib.request
import urllib.parse
import re
import json

searches = [
    ('武夷山旅游', 'wuyishan'),
    ('福建自驾游', 'fujian'),
    ('霞浦滩涂', 'xiapu'),
]

all_results = {}

for query, key in searches:
    url = 'https://html.duckduckgo.com/html/?q=' + urllib.parse.quote(query)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        resp = urllib.request.urlopen(req, timeout=15)
        html = resp.read().decode('utf-8')
        
        # Try different patterns
        results = re.findall(r'<a class="result__a"[^>]*>([^<]+)</a>', html)
        all_results[key] = results[:5] if results else []
        
        print(f'=== {query} ===')
        for i, r in enumerate(all_results[key]):
            print(f'{i+1}. {r}')
        print()
    except Exception as e:
        all_results[key] = []
        print(f'{query}: Error - {e}')
        print()

# Save to file
with open('search_results.json', 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

print('Results saved to search_results.json')
