# -*- coding: utf-8 -*-
import re, codecs, sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

for day in [66, 67]:
    pattern = '<span class="day-number">第' + str(day) + '天</span>'
    idx = content.find(pattern)
    if idx >= 0:
        print(f'Day {day} found at position {idx}')
        print(content[idx:idx+400])
        print('---')
    else:
        print(f'Day {day} NOT FOUND')
