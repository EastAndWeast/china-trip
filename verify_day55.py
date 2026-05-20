# -*- coding: utf-8 -*-
import re

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Stats
dc = re.search(r'id="dayCount"[^>]*>(\d+)<', content)
km = re.search(r'id="kmCount"[^>]*>(\d+)<', content)
loc = re.search(r'id="currentLocation"[^>]*>([^<]+)<', content)
days_since = re.search(r'出发日期.*?(\d{4})年(\d{1,2})月(\d{1,2})日', content)

print('=== 环游中国网站状态 ===')
print('Day:', dc.group(1) if dc else 'N/A')
print('KM:', km.group(1) if km else 'N/A')
print('Location:', loc.group(1) if loc else 'N/A')

# Count day cards
day_cards = len(re.findall(r'class="day-card"', content))
print('Day cards in HTML:', day_cards)

# Last update in footer
start = content.find('最后更新：')
print('Footer:', content[start:start+40])

# Day 55 check
m55 = re.search(r'第55天.*?2026-04-12', content)
print('Day 55 (Apr 12):', 'Found' if m55 else 'Missing')

# Search results
import json
try:
    with open('C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json', 'r', encoding='utf-8') as f:
        sr = json.load(f)
    print('\n=== 搜索结果 ===')
    print('Updated:', sr.get('updated', 'N/A'))
    for item in sr.get('queries', []):
        print(f'  {item["name"]}: {len(item.get("results", []))} results')
except:
    pass
