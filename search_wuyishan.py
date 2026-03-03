# -*- coding: utf-8 -*-
from duckduckgo_search import DDGS
import json

ddgs = DDGS()

# 搜索武夷山旅行信息
print("=== 搜索武夷山旅行信息 ===")
results = list(ddgs.text('武夷山旅游 2026 旅行攻略 景点', max_results=5))
for r in results:
    print(f"Title: {r['title']}")
    print(f"URL: {r['href']}")
    print(f"Body: {r['body']}")
    print('---')

print("\n=== 搜索福州到武夷山交通 ===")
results2 = list(ddgs.text('福州到武夷山交通 高铁 自驾 2026', max_results=3))
for r in results2:
    print(f"Title: {r['title']}")
    print(f"URL: {r['href']}")
    print(f"Body: {r['body']}")
    print('---')
