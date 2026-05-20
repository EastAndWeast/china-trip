# -*- coding: utf-8 -*-
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find Day 54
m = re.search(r'第54天.*?2026-04-11', content)
print('Day 54 found:', m is not None)

# Find footer
start = content.find('最后更新：')
print('Footer last update:', content[start:start+30])

# Check stats
dc = re.search(r'id="dayCount"[^>]*>(\d+)<', content)
print('Day count:', dc.group(1) if dc else 'N/A')
km = re.search(r'id="kmCount"[^>]*>(\d+)<', content)
print('KM:', km.group(1) if km else 'N/A')
loc = re.search(r'id="currentLocation"[^>]*>([^<]+)<', content)
print('Location:', loc.group(1) if loc else 'N/A')

# Check day 54 content
day54_start = content.find('第54天')
if day54_start > 0:
    print('\nDay 54 snippet:')
    print(content[day54_start:day54_start+200])
