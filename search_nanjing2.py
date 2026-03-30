# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import json
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

proxy = "http://127.0.0.1:7890"
proxy_handler = urllib.request.ProxyHandler({'http': proxy, 'https': proxy})

queries = [
    '南京旅游攻略 2026年3月 中山陵 夫子庙 秦淮河',
    '南京3月底4月初樱花 梅花山 2026',
    '扬州到南京交通 高铁 2026年3月'
]

all_results = {}

for query in queries:
    encoded_query = urllib.parse.quote(query)
    url = 'https://lite.duckduckgo.com/lite/?q=' + encoded_query
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html',
    })
    try:
        opener = urllib.request.build_opener(proxy_handler)
        response = opener.open(req, timeout=15)
        html = response.read().decode('utf-8')
        
        # Extract result titles
        links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]*)</a>', html)
        results = []
        for href, text in links:
            text = text.strip()
            if text and 'uddg' in href and len(text) > 10:
                results.append(text)
        
        print('=== ' + query + ' ===')
        for i, r in enumerate(results[:5]):
            print(str(i+1) + '. ' + r[:80])
        print()
        
        all_results[query] = [{'title': r} for r in results[:5]]
    except Exception as e:
        print('Error for ' + query + ': ' + str(e))
        all_results[query] = []

output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_nanjing.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print('Saved to ' + output_path)
