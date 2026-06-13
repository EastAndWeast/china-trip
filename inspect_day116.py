# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
with open('index.html','r',encoding='utf-8') as f:
    c = f.read()
# Find Day 116 entry
m = re.search(r'(<div class="day-card">\s*<div class="day-header">\s*<span class="day-number">116</span>.*?)(<div class="footer">)', c, re.DOTALL)
if m:
    print('--- Day 116 card structure (first 3000 chars) ---')
    print(m.group(1)[:3000])
    print()
    print('--- end of day 116 (last 1000 chars) ---')
    print(m.group(1)[-1000:])
else:
    print('Day 116 not found')
