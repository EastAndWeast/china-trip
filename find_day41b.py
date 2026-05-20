# -*- coding: utf-8 -*-
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find day 41 with better pattern
# Day cards start with <div class="day-card"> and end before the next <div class="day-card">
day_pattern = r'<div class="day-card">\s*<div class="day-header">\s*<span class="day-number">(第\d+天)</span>\s*<span class="day-date">([^<]+)</span>'
matches = list(re.finditer(day_pattern, content))
print(f'Total day entries: {len(matches)}')

# Find day 41
for m in matches:
    day_num = m.group(1)
    if '41' in day_num:
        day_date = m.group(2)
        print(f'\nFound Day 41: {day_num} - {day_date}')
        # Extract the full day card content
        start = m.start()
        # Find the end - next day-card or end of timeline
        next_match = None
        for i, dm in enumerate(matches):
            if dm.start() > start:
                next_match = dm
                break
        if next_match:
            end = next_match.start()
        else:
            end = content.find('</div>\s*</div>\s*</div>\s*</div>\s*</div>', start)
        print(f'\n--- Day 41 Content ---')
        print(content[start:end][:1000])
        
# Show first 5 and last 5 day entries
print('\n--- First 5 days (most recent) ---')
for m in matches[:5]:
    print(f'{m.group(1)}: {m.group(2)}')
    
print('\n--- Last 5 days (oldest) ---')
for m in matches[-5:]:
    print(f'{m.group(1)}: {m.group(2)}')
