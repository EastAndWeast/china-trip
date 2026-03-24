# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import json
import sys
import codecs

# 设置UTF-8输出
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# 搜索泉州湄洲岛旅行信息
query = '泉州 湄洲岛 妈祖 旅行 旅游攻略'
encoded_query = urllib.parse.quote(query)
url = f'https://html.duckduckgo.com/html/?q={encoded_query}'

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    response = urllib.request.urlopen(req, timeout=10)
    html = response.read().decode('utf-8')
    
    results = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html)
    print('=== 泉州/湄洲岛旅行搜索结果 ===')
    for i, r in enumerate(results[:5]):
        print(f'{i+1}. {r}')
except Exception as e:
    print(f'搜索出错: {e}')

# 搜索福州
print()
query2 = '福州 三坊七巷 鼓山 旅行'
encoded_query2 = urllib.parse.quote(query2)
url2 = f'https://html.duckduckgo.com/html/?q={encoded_query2}'

try:
    req2 = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    response2 = urllib.request.urlopen(req2, timeout=10)
    html2 = response2.read().decode('utf-8')
    results2 = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html2)
    print('=== 福州旅行搜索结果 ===')
    for i, r in enumerate(results2[:5]):
        print(f'{i+1}. {r}')
except Exception as e:
    print(f'搜索出错: {e}')

print()
print('=== 搜索完成 ===')
