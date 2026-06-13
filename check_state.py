# -*- coding: utf-8 -*-
import re
with open('index.html','r',encoding='utf-8') as f:
    c = f.read()
day = re.search(r'id="dayCount"[^>]*>(\d+)<', c)
km = re.search(r'id="kmCount"[^>]*>(\d+)<', c)
loc = re.search(r'id="locationCount"[^>]*>(\d+)<', c)
cur = re.search(r'id="currentLocation"[^>]*>([^<]+)<', c)
days = re.findall(r'<div class="day-card">\s*<div class="day-header">\s*<span class="day-number">(\d+)</span>\s*<span class="day-date">([^<]+)</span>', c, re.DOTALL)
print('dayCount:', day.group(1) if day else '?')
print('kmCount:', km.group(1) if km else '?')
print('locationCount:', loc.group(1) if loc else '?')
print('currentLocation:', cur.group(1) if cur else '?')
print('Total day cards:', len(days))
print('Last 3 days:')
for d in days[-3:]:
    print(' ', d[0], '|', d[1].strip())
