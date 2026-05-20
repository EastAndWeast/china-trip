# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, json, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('厦门鼓浪屿旅游攻略 2026年4月 最新', '厦门'),
    ('厦门环岛路 曾厝垵 南普陀寺 攻略 2026年4月', '厦门景点'),
    ('厦门美食攻略 2026 沙茶面 海鲜', '厦门美食'),
]

all_results = []

for query, name in queries:
    encoded_query = urllib.parse.quote(query)
    url = f'https://html.duckduckgo.com/html/?q={encoded_query}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
    try:
        response = urllib.request.urlopen(req, timeout=15)
        html = response.read().decode('utf-8')
        pattern = r'class="result__a"[^>]*>([^<]*)</a>'
        results = re.findall(pattern, html)
        print(f'=== {name}: {len(results)} results ===')
        for r in results[:5]:
            print(f'  {r.strip()[:80]}')
        all_results.append({'query': query, 'name': name, 'results': [{'title': r.strip()[:100]} for r in results[:5]]})
    except Exception as e:
        print(f'Error for {name}: {e}')
        all_results.append({'query': query, 'name': name, 'results': []})
    print()

output = {'updated': '2026-04-20', 'queries': all_results}
with open('C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
print('Saved search_results_latest.json')
