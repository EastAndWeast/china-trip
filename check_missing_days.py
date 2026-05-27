# -*- coding: utf-8 -*-
import re, sys, codecs, json
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Get all day numbers
all_days = re.findall(r'<span class="day-number">第(\d+)天</span>', content)
unique_days = sorted(set(int(d) for d in all_days))
print(f'Unique days in timeline: {len(unique_days)} days (from {unique_days[0]} to {unique_days[-1]})')
print(f'Day count stat shows: 98')

# Calculate what days are missing
missing = []
for i in range(unique_days[0], unique_days[-1] + 1):
    if i not in unique_days:
        missing.append(i)
print(f'Missing days: {missing}')

# Find current location
loc = re.search(r'id="currentLocation">([^<]+)<', content)
print(f'Current location in stats: {loc.group(1) if loc else "not found"}')

# Check what day 91 content says about next destination
pattern = r'<span class="day-number">第91天</span>.*?(?=<span class="day-number">第92天|<div class="footer")'
match = re.search(pattern, content, re.DOTALL)
if match:
    # Look for "明日预告" or similar
    tomorrow = re.search(r'明日预告：([^<]+)</p>', match.group(0))
    if tomorrow:
        print(f'Day 91 says tomorrow: {tomorrow.group(1)}')