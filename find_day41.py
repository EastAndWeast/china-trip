# -*- coding: utf-8 -*-
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all day entries with full content
# Pattern: day-number through the end of that day-card
pattern = r'<span class="day-number">(第\d+天)</span>.*?(?=<span class="day-number">|$)'
matches = re.findall(pattern, content, re.DOTALL)
print(f'Total day entries: {len(matches)}')
print('Days found:', [m[0] for m in matches])

# Look for day 41 specifically
day41 = re.search(r'<span class="day-number">第41天</span>(.*?)(?=第40天|day-footer)', content, re.DOTALL)
if day41:
    print('\n--- Day 41 Content (first 600 chars) ---')
    print(day41.group(0)[:600])
else:
    print('\nDay 41 not found in standard pattern')
    
# Try a different approach - find any reference to 41
print('\n--- All 41 references ---')
for m in re.finditer(r'41', content):
    start = max(0, m.start() - 20)
    end = min(len(content), m.end() + 20)
    print(f'...{content[start:end]}...')
