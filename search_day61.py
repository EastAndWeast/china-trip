# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import sys
import codecs
import json

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('武夷山虎啸岩一线天旅游攻略 2026年4月', '武夷山深度游'),
    ('福州厦门泉州旅游攻略 2026年4月', '福建之旅'),
]

all_results = {}

for query, name in queries:
    encoded_query = urllib.parse.quote(query)
    url = 'https://html.duckduckgo.com/html/?q=' + encoded_query
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })
    try:
        response = urllib.request.urlopen(req, timeout=15)
        html = response.read().decode('utf-8')
        pattern = r'class="result__a"[^>]*>([^<]+)</a>'
        results = re.findall(pattern, html)
        print('=== ' + name + ' ===')
        for title in results[:5]:
            print('  ' + title.strip()[:80])
        print()
        all_results[name] = {'query': query, 'results': [t.strip() for t in results[:5]]}
    except Exception as e:
        print('Error for ' + name + ': ' + str(e))
        all_results[name] = {'query': query, 'results': []}

output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_day61.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump({'day': 61, 'date': '2026-04-18', 'results': all_results}, f, ensure_ascii=False, indent=2)
print('Saved to ' + output_path)
