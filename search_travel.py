# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import json

# 搜索武夷山旅行信息
query = '武夷山 旅行 2026年3月 旅游攻略'
encoded_query = urllib.parse.quote(query)
url = f'https://html.duckduckgo.com/html/?q={encoded_query}'

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req, timeout=10)
html = response.read().decode('utf-8')

# 简单提取标题和链接
results = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html)
print("武夷山旅行搜索结果:")
for i, r in enumerate(results[:5]):
    print(f'{i+1}. {r}')

# 搜索福州旅行信息
print("\n\n福州旅行搜索结果:")
query2 = '福州 旅行 2026年3月 旅游'
encoded_query2 = urllib.parse.quote(query2)
url2 = f'https://html.duckduckgo.com/html/?q={encoded_query2}'
req2 = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
response2 = urllib.request.urlopen(req2, timeout=10)
html2 = response2.read().decode('utf-8')
results2 = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html2)
for i, r in enumerate(results2[:5]):
    print(f'{i+1}. {r}')
