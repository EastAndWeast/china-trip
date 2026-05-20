# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('南昌旅游攻略 2026年5月', '南昌'),
    ('岳阳楼旅游攻略 2026', '岳阳'),
    ('长沙到南昌自驾路线', '长沙南昌'),
    ('衡山旅游攻略 2026年5月', '衡山'),
]

all_results = {}

for q in queries:
    name = q[1] if len(q) > 1 else q[0]
    query_str = q[0] if len(q) > 1 else q
    encoded_query = urllib.parse.quote(query_str)
    url = 'https://lite.duckduckgo.com/lite/?q=' + encoded_query
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    try:
        response = urllib.request.urlopen(req, timeout=15)
        html = response.read().decode('utf-8')
        pattern = '<a class="result-link" href="([^"]+)"[^>]*>([^<]+)</a>'
        results = re.findall(pattern, html)
        print('=== ' + name + ' (' + str(len(results)) + ' results) ===')
        for r in results[:5]:
            print('  ' + r[1][:80])
        print()
        all_results[name] = [{'title': r[1].strip()} for r in results[:5]]
    except Exception as e:
        print('Error for ' + name + ': ' + str(e))
        all_results[name] = []

output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print('Saved to ' + output_path)