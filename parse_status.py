# -*- coding: utf-8 -*-
import re

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

day_match = re.search(r'id="dayCount">(\d+)</div>', content)
km_match = re.search(r'id="kmCount">(\d+)</div>', content)
loc_match = re.search(r'id="currentLocation">([^<]+)</strong>', content)
print('Day count:', day_match.group(1) if day_match else 'N/A')
print('km count:', km_match.group(1) if km_match else 'N/A')
print('Current location:', loc_match.group(1) if loc_match else 'N/A')

day_numbers = re.findall(r'class="day-number">第(\d+)天', content)
print('Last days:', sorted([int(d) for d in day_numbers], reverse=True)[:10])
