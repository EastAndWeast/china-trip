# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import json
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

def search(query):
    encoded_query = urllib.parse.quote(query)
    url = 'https://lite.duckduckgo.com/lite/?q=' + encoded_query
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    })
    response = urllib.request.urlopen(req, timeout=15)
    html = response.read().decode('utf-8')
    
    # Parse results
    pattern = '<a class="result-link" href="([^"]+)"[^>]*>([^<]+)</a>'
    results = re.findall(pattern, html)
    titles = [r[1].strip() for r in results[:5]]
    return titles

queries = [
    '南京旅游攻略 2026年3月',
    '黄山旅游攻略 2026年3月 宏村西递',
    '无锡灵山拈花湾旅游攻略 2026年春季',
]

all_results = {}
for q in queries:
    try:
        titles = search(q)
        print(f'=== {q} ===')
        for i, t in enumerate(titles):
            print(f'{i+1}. {t}')
        print()
        all_results[q] = titles
    except Exception as e:
        print(f'Error for {q}: {e}')
        all_results[q] = []

# Save
output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print(f'Saved to {output_path}')
