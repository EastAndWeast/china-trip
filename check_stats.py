# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

loc_match = re.search(r'id="currentLocation"[^>]*>([^<]+)<', content)
if loc_match:
    print('Location:', loc_match.group(1))

day_match = re.search(r'id="dayCount"[^>]*>(\d+)<', content)
if day_match:
    print('Day count:', day_match.group(1))

km_match = re.search(r'id="kmCount"[^>]*>(\d+)<', content)
if km_match:
    print('KM:', km_match.group(1))

date_match = re.findall(r'class="day-date">(\d{4}-\d{2}-\d{2})', content)
if date_match:
    print('Last dates:', date_match[-3:])