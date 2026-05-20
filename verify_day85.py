# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

day = re.search(r'id="dayCount">(\d+)</div>', content)
km = re.search(r'id="kmCount">(\d+)</div>', content)
loc = re.search(r'id="currentLocation">([^<]+)</strong>', content)

print('Day:', day.group(1) if day else 'N/A')
print('KM:', km.group(1) if km else 'N/A')
print('Location:', loc.group(1) if loc else 'N/A')

day_numbers = re.findall(r'class="day-number">第(\d+)天', content)
print('Last days:', sorted([int(d) for d in day_numbers], reverse=True)[:5])

# Check Day 85 content
day85 = re.search(r'第85天.*?<div class="day-title">(.*?)</div>', content, re.DOTALL)
if day85:
    print('Day 85 title:', day85.group(1)[:50])