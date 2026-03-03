# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re

# Search for Wuyishan travel info
query = '武夷山 九曲溪 竹筏漂流 2026年3月'
encoded_query = urllib.parse.quote(query)
url = f'https://html.duckduckgo.com/html/?q={encoded_query}'

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
response = urllib.request.urlopen(req, timeout=10)
html = response.read().decode('utf-8')

# Extract titles
results = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html)
print('=== 武夷山旅行搜索结果 ===')
for i, r in enumerate(results[:8]):
    print(f'{i+1}. {r}')

# Also search for next destination
query2 = '福建 旅游景点 2026年3月'
encoded_query2 = urllib.parse.quote(query2)
url2 = f'https://html.duckduckgo.com/html/?q={encoded_query2}'
req2 = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
response2 = urllib.request.urlopen(req2, timeout=10)
html2 = response2.read().decode('utf-8')
results2 = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html2)
print('\n=== 福建旅游景点搜索结果 ===')
for i, r in enumerate(results2[:8]):
    print(f'{i+1}. {r}')
