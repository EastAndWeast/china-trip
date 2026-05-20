# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import json
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('南昌旅游攻略 2026年5月 滕王阁', '南昌'),
    ('衡山旅游攻略 2026年5月', '衡山'),
    ('长沙到南昌自驾路线 2026', '长沙南昌'),
    ('南昌美食攻略 2026', '南昌美食'),
]

all_results = {}

for query, name in queries:
    encoded_query = urllib.parse.quote(query)
    url = 'https://html.duckduckgo.com/html/?q=' + encoded_query
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
    try:
        response = urllib.request.urlopen(req, timeout=15)
        html = response.read().decode('utf-8')
        pattern = '<a rel="nofollow" class="result__a" href="[^"]*">([^<]+)</a>'
        results = re.findall(pattern, html)
        results = [r.strip() for r in results if len(r.strip()) > 5][:5]
        print('=== ' + name + ' (' + str(len(results)) + ' results) ===')
        for r in results:
            print('  ' + r[:80])
        print()
        all_results[name] = results
    except Exception as e:
        print('Error for ' + name + ': ' + str(e))
        all_results[name] = []

output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print('Saved to ' + output_path)