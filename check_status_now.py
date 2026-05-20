# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check current state
day = re.search(r'id="dayCount"[^>]*>(\d+)<', content)
km = re.search(r'id="kmCount"[^>]*>(\d+)<', content)
lc = re.search(r'id="locationCount"[^>]*>(\d+)<', content)
loc = re.search(r'id="currentLocation"[^>]*>([^<]+)<', content)
print('Current - Days:', day.group(1) if day else '?', 'km:', km.group(1) if km else '?', 'locs:', lc.group(1) if lc else '?', 'location:', loc.group(1) if loc else '?')

# Check last day in timeline
last_days = re.findall(r'class="day-number">第(\d+)天', content)
print('Last days in timeline:', last_days[-5:] if last_days else 'none')
print('Total day entries:', len(last_days))