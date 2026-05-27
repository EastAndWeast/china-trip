# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find day 90 content
pattern = r'day-number">第90天.*?(?=day-number">第91天|<div class="footer")'
match = re.search(pattern, content, re.DOTALL)
if match:
    print('=== Day 90 ===')
    print(match.group(0)[:800])
else:
    print('Day 90 not found')

# Check what comes after day 91
pattern2 = r'day-number">第91天.*?(?=day-number">第92天|<div class="footer")'
match2 = re.search(pattern2, content, re.DOTALL)
if match2:
    text = match2.group(0)
    # Find明日预告
    m = re.search(r'明日预告：([^<]+)</p>', text)
    if m:
        print('\n=== Day 91 tomorrow预告 ===')
        print(m.group(1))
    # Find current location
    loc = re.search(r'currentLocation">([^<]+)<', content)
    print('\nCurrent location:', loc.group(1) if loc else 'not found')