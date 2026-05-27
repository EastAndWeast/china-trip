# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the stats section
stats_pattern = r'<div class="stats">(.*?)</div>\s*<div class="trip-info">'
match = re.search(stats_pattern, content, re.DOTALL)
if match:
    print('=== Stats Section ===')
    print(match.group(0))
    print()

# Find current location in trip-info
trip_pattern = r'<div class="trip-info">(.*?)</div>\s*<div class="timeline">'
match2 = re.search(trip_pattern, content, re.DOTALL)
if match2:
    print('=== Trip Info ===')
    print(match2.group(0))