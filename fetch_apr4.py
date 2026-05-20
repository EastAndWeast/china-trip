# -*- coding: utf-8 -*-
"""Fetch April 4 travel info for Suzhou"""
import urllib.request, urllib.parse, re, json, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('苏州旅游攻略 2026年4月 拙政园 金鸡湖', '苏州4月'),
    ('苏州平江路观前街美食攻略 2026年4月', '苏州美食'),
    ('苏州旅游4月最新活动 2026年春季', '苏州活动'),
]
results = {}
for query, name in queries:
    encoded = urllib.parse.quote(query)
    url = f'https://html.duckduckgo.com/html/?q={encoded}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        html = resp.read().decode('utf-8')
        titles = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html)
        snippets = re.findall(r'<a class="result__snippet"[^>]*>([^<]*)</a>', html)
        results[name] = {
            'titles': titles[:5],
            'snippets': [re.sub(r'<[^>]+>', '', s) for s in snippets[:5]]
        }
        print(f'=== {name} ===')
        for i, t in enumerate(titles[:5]):
            print(f'  {i+1}. {t}')
        print()
    except Exception as e:
        print(f'Error {name}: {e}')
        results[name] = {'titles': [], 'snippets': []}

# Save
out_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_apr4.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f'Saved to {out_path}')
