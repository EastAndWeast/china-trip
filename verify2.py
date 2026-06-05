# -*- coding: utf-8 -*-
import re
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
# Find dates of all day cards
# Look for day-date pattern
date_pat = re.findall(r'class="day-date">([^<]+)<', c)
print('Total day-date entries:', len(date_pat))
print('First 3:', date_pat[:3])
print('Last 5:', date_pat[-5:])
# dayCount and kmCount
day_count = re.search(r'id="dayCount"[^>]*>(\d+)<', c)
print('dayCount:', day_count.group(1) if day_count else '?')
# Find first day date
m = re.search(r'开始时间：([^<]+)<', c)
if m:
    print('Start date:', m.group(1))
# Find last update
m2 = re.findall(r'最后更新：([^<]+)<', c)
print('Last update markers:', m2)
# latest day-date
print()
print('Date progression:')
for d in date_pat[-10:]:
    print(' ', d.strip())
