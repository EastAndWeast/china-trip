# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Check current stats
day_match = re.search(r'id="dayCount"[^>]*>(\d+)<', content)
km_match = re.search(r'id="kmCount"[^>]*>(\d+)<', content)
loc_match = re.search(r'id="locationCount"[^>]*>(\d+)<', content)
cur_match = re.search(r'id="currentLocation"[^>]*>([^<]+)<', content)
print('Current: dayCount=%s, kmCount=%s, locationCount=%s, location=%s' % (
    day_match.group(1) if day_match else '?',
    km_match.group(1) if km_match else '?',
    loc_match.group(1) if loc_match else '?',
    cur_match.group(1) if cur_match else '?'
))

# Find the last day number
day_nums = re.findall(r'class="day-number">(\d+)<', content)
print('Last day numbers:', day_nums[-3:] if day_nums else 'none')

# Find current date context - check last day entry
last_day_match = re.findall(r'class="day-number">(\d+)<', content)
if last_day_match:
    last_day = int(last_day_match[-1])
    print(f'Last day in HTML: {last_day}')
    
# Check the date of last entry
last_date_match = re.search(r'(\d{4}-\d{2}-\d{2})</span>\s*</div>\s*<div class="day-title">', content)
if last_date_match:
    print(f'Last entry date: {last_date_match.group(1)}')