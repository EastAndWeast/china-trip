# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, json, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('千岛湖旅游攻略 2026年5月', '千岛湖'),
    ('黄山旅游攻略 2026年5月', '黄山'),
    ('宏村西递旅游攻略 2026年5月', '宏村'),
    ('扬州旅游攻略 2026年5月', '扬州'),
    ('杭州西湖旅游攻略 2026年5月', '杭州'),
]

all_results = {}

for query, name in queries:
    encoded_query = urllib.parse.quote(query)
    url = f'https://html.duckduckgo.com/html/?q={encoded_query}'
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })
    try:
        response = urllib.request.urlopen(req, timeout=15)
        html = response.read().decode('utf-8')
        pattern = r'<a class="result__a"[^>]*>([^<]*)</a>'
        results = re.findall(pattern, html)
        print(f'=== {name}: {len(results)} results ===')
        for i, r in enumerate(results[:5]):
            print(f'{i+1}. {r.strip()}')
        all_results[query] = [{'title': r.strip()} for r in results[:5]]
    except Exception as e:
        print(f'Error for {query}: {e}')
        all_results[query] = []

output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print(f'Saved to {output_path}')