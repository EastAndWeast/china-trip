# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find day 91 and next day
pattern = r'<span class="day-number">第91天</span>.*?(?=<span class="day-number">第92天|<div class="footer")'
match = re.search(pattern, content, re.DOTALL)
if match:
    print('=== Day 91 found ===')
    print(match.group(0)[:1500])
else:
    print('Day 91 not found - checking last few days...')
    last_days = re.findall(r'<span class="day-number">第(\d+)天</span>', content)
    print('Last 5 days:', last_days[-5:])
    
    # Find position after last day
    last_day_nums = sorted(set(int(d) for d in last_days))
    if last_day_nums:
        last = last_day_nums[-1]
        pattern2 = r'<span class="day-number">第' + str(last) + r'天</span>.*?(?=<div class="footer")'
        match2 = re.search(pattern2, content, re.DOTALL)
        if match2:
            print(f'Last day ({last}) content:')
            print(match2.group(0)[:1000])