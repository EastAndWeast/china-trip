# -*- coding: utf-8 -*-
import re, codecs, sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    c = f.read()
days = re.findall(r'<span class="day-number">(第\d+天)</span>', c)
print('Days found:', len(days))
print('Day numbers:', days)
m = re.search(r'最后更新：(\d+年\d+月\d+日)', c)
print('Last updated:', m.group(1) if m else 'not found')
m2 = re.search(r'id="currentLocation">([^<]+)', c)
print('Current location:', m2.group(1) if m2 else 'not found')
# Check day 42 and 43 exist
print('Day 42 found:', '第42天' in c)
print('Day 43 found:', '第43天' in c)
print('南京 found:', '南京' in c)
print('玄武湖 found:', '玄武湖' in c)
