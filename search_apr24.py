# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, codecs, sys, json
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('福州三坊七巷旅游攻略2026年4月', '福州三坊七巷'),
    ('福州西湖公园闽江旅游攻略2026', '福州景点'),
    ('漳州到福州自驾旅游2026年4月', '福州交通'),
]

all_results = {}

for query, name in queries:
    encoded = urllib.parse.quote(query)
    url = f'https://html.duckduckgo.com/html/?q={encoded}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        html = resp.read().decode('utf-8')
        results = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html)
        print(f'=== {name} ===')
        for i, r in enumerate(results[:8]):
            print(f'{i+1}. {r}')
        all_results[name] = results[:8]
    except Exception as e:
        print(f'Error for {name}: {e}')
        all_results[name] = []
    print()

# Save results
output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_apr24.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print(f'Saved to {output_path}')
