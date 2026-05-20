# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find stats
dc = re.search(r'id="dayCount"[^>]*>(\d+)<', content)
lc = re.search(r'id="locationCount"[^>]*>(\d+)<', content)
km = re.search(r'id="kmCount"[^>]*>(\d+)<', content)
loc = re.search(r'id="currentLocation"[^>]*>([^<]+)<', content)
update = re.search(r'最后更新：([^<]+)', content)
print(f'Stats: Day {dc.group(1) if dc else "N/A"}, Location {lc.group(1) if lc else "N/A"}, KM {km.group(1) if km else "N/A"}')
print(f'Current Location: {loc.group(1) if loc else "N/A"}')
print(f'Last Update: {update.group(1) if update else "N/A"}')

# Find all day numbers and dates
days = re.findall(r'<span class="day-number">第(\d+)天</span>', content)
print(f'\nDays found: {len(days)}')
print(f'Day numbers (first 10): {days[:10]}')
print(f'Day numbers (last 10): {days[-10:]}')

# Find the day-card for day 41 (should be the first one)
pattern = r'<span class="day-number">第41天</span>(.*?)(?=day-card|$)'
match = re.search(pattern, content, re.DOTALL)
if match:
    print('\n--- Day 41 Content (first 500 chars) ---')
    print(match.group(0)[:500])
