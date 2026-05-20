# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, json, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('杭州西湖旅游攻略 2026年5月', '杭州'),
    ('杭州灵隐寺旅游攻略 2026', '灵隐寺'),
]
results = {}
for q, name in queries:
    encoded = urllib.parse.quote(q)
    url = 'https://html.duckduckgo.com/html/?q=' + encoded
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        html = resp.read().decode('utf-8', errors='ignore')
        titles = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html)
        clean = [re.sub(r'<[^>]+>', '', t).strip() for t in titles]
        print('=== ' + name + ': ' + str(len(clean)) + ' results ===')
        for t in clean[:3]: print('  - ' + t[:80])
        results[name] = clean[:5]
    except Exception as e:
        print('Error', name, e)
        results[name] = []

output = {'updated': '2026-05-19', 'day91': {'destination': '杭州西湖', 'results': results}}
with open('C:/Users/admin/.openclaw/workspace/china-trip/search_results_day91.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
print('Saved search_results_day91.json')