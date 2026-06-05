# -*- coding: utf-8 -*-
import re
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
# Search all day-number patterns
m1 = re.findall(r'class="day-number">(\d+)<', c)
print('Numeric style:', len(m1), 'matches, first 5:', m1[:5], 'last 5:', m1[-5:])
# Also look for 第N天 style
day_cn = re.findall(r'第(\d+)天', c)
print('第N天 style:', len(day_cn), 'matches, last 5:', day_cn[-5:] if day_cn else 'none')
# day-cards
cards = re.findall(r'class="day-card"', c)
print('Total day-card divs:', len(cards))
