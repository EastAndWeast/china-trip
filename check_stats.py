# -*- coding: utf-8 -*-
import re, codecs, sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
m = re.search(r'id="currentLocation">([^<]+)', content)
print('currentLocation:', m.group(1) if m else 'not found')
m2 = re.search(r'<div class="stat-value" id="dayCount">(\d+)</div>', content)
print('dayCount:', m2.group(1) if m2 else 'not found')
m3 = re.search(r'<div class="stat-value" id="locationCount">(\d+)</div>', content)
print('locationCount:', m3.group(1) if m3 else 'not found')
m4 = re.search(r'<div class="stat-value" id="kmCount">(\d+)</div>', content)
print('kmCount:', m4.group(1) if m4 else 'not found')
day41_pattern = r'<span class="day-number">第41天</span>'
m5 = re.search(day41_pattern, content)
print('Day 41 found:', m5 is not None)
