# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, json, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('南昌旅游攻略 2026年5月 滕王阁 八一广场', '南昌'),
    ('岳阳楼旅游攻略 2026年5月 洞庭湖', '岳阳'),
    ('长沙到南昌自驾路线 2026年5月', '长沙南昌'),
    ('衡山旅游攻略 2026年5月 衡阳', '衡山'),
    ('庐山旅游攻略 2026年5月', '庐山'),
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
        print(f'=== {name}: {query} ===')
        for i, r in enumerate(results[:5]):
            print(f'{i+1}. {r.strip()}')
        print()
        all_results[query] = [{'title': r.strip()} for r in results[:5]]
    except Exception as e:
        print(f'Error for {query}: {e}')
        all_results[query] = []

# Save
output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print(f'Saved to {output_path}')