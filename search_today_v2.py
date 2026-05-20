# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import sys
import codecs
import json

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('武夷山旅游攻略 2026年4月 九曲溪', '武夷山'),
    ('婺源江岭庆源古村旅游攻略 2026年4月', '婺源东线'),
    ('扬州瘦西湖个园旅游攻略 2026年4月', '扬州'),
    ('黄山宏村西递旅游攻略 2026年4月', '黄山宏村'),
    ('杭州西湖龙井村旅游攻略 2026年4月', '杭州'),
]

all_results = []

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
        print('=== ' + name + ': ' + str(len(results)) + ' results ===')
        query_results = []
        for title in results[:5]:
            title_clean = title.strip()
            print('  ' + title_clean[:70])
            query_results.append({'title': title_clean})
        print()
        all_results.append({'query': query, 'name': name, 'results': query_results})
    except Exception as e:
        print('Error for ' + name + ': ' + str(e))
        all_results.append({'query': query, 'name': name, 'results': []})

# Save with today's date
output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump({'updated': '2026-04-15', 'queries': all_results}, f, ensure_ascii=False, indent=2)
print('Saved to ' + output_path)
