# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, json, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    '南京旅游攻略 2026年3月 中山陵 夫子庙 秦淮河',
    '扬州到南京高铁交通 2026年3月',
    '南京3月底4月初旅游 樱花 梅花山 2026'
]

all_results = {}
for query in queries:
    encoded = urllib.parse.quote(query)
    url = 'https://html.duckduckgo.com/html/?q=' + encoded
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        html = resp.read().decode('utf-8')
        results = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html)
        print('=== ' + query + ' ===')
        for i, r in enumerate(results[:5]):
            print(str(i+1) + '. ' + r)
        print()
        all_results[query] = results[:5]
    except Exception as e:
        print('Error for ' + query + ': ' + str(e))
        all_results[query] = []

output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_nanjing.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print('Saved to ' + output_path)
