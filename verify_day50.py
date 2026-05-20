# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check counts
day = re.search(r'id="dayCount">(\d+)</div>', content)
km = re.search(r'id="kmCount">(\d+)</div>', content)
loc = re.search(r'id="locationCount">(\d+)</div>', content)
curr = re.search(r'id="currentLocation">([^<]+)</strong>', content)
updated = re.search(r'最后更新：(\d+年\d+月\d+日)', content)

print(f'Day count: {day.group(1) if day else "NOT FOUND"}')
print(f'km count: {km.group(1) if km else "NOT FOUND"}')
print(f'location count: {loc.group(1) if loc else "NOT FOUND"}')
print(f'current location: {curr.group(1) if curr else "NOT FOUND"}')
print(f'last updated: {updated.group(1) if updated else "NOT FOUND"}')

# Check Day 50 exists
day50 = re.search(r'第50天', content)
print(f'Day 50 present: {"YES" if day50 else "NO"}')

# Print Day 50 title
day50_m = re.search(r'<span class="day-number">第50天</span>.*?<div class="day-title">(.*?)</div>', content, re.DOTALL)
if day50_m:
    print(f'Day 50 title: {day50_m.group(1)}')
