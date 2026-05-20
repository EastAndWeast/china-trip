# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all day numbers with context
days = re.findall(r'<span class="day-number">第(\d+)天</span>.*?<span class="day-date">([^<]+)</span>', content, re.DOTALL)
print('Total days found:', len(days))
print('First 3:', days[:3])
print('Last 3:', days[-3:] if len(days) > 3 else '')

# Find stats
dc = re.search(r'id="dayCount"[^>]*>(\d+)<', content)
lc = re.search(r'id="locationCount"[^>]*>(\d+)<', content)
km = re.search(r'id="kmCount"[^>]*>(\d+)<', content)
loc = re.search(r'id="currentLocation"[^>]*>([^<]+)<', content)
print('dayCount:', dc.group(1) if dc else 'N/A')
print('locationCount:', lc.group(1) if lc else 'N/A')
print('kmCount:', km.group(1) if km else 'N/A')
print('currentLocation:', loc.group(1) if loc else 'N/A')

# Find last update time
update = re.search(r'最后更新：([^<]+)', content)
print('Last update:', update.group(1) if update else 'N/A')

# Show last 5 day entries
print('\n--- Last 5 Day Entries ---')
for day_num, day_date in days[-5:]:
    print(f"Day {day_num}: {day_date}")
