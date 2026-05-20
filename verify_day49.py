# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find Day 49
m = re.search(r'第49天.*?<div class="day-card">', content, re.DOTALL)
if m:
    print('Day 49 found!')
    # Get Day 49 content
    start = m.start()
    # Find the end of Day 49's day-card div
    # Count nested divs
    depth = 0
    i = content.find('<div class="day-card">', start)
    end = i
    while end < len(content):
        if content[end:end+16] == '<div class="day-c':
            depth += 1
        elif content[end:end+6] == '</div>':
            depth -= 1
            if depth == 0:
                end += 6
                break
        end += 1
    
    day49_html = content[i:end]
    print(f'Day 49 HTML length: {len(day49_html)}')
    print('\nTitle line:')
    title_m = re.search(r'day-title">(.*?)</div>', day49_html, re.DOTALL)
    if title_m:
        print(title_m.group(1))
    print('\nFirst 500 chars of content:')
    content_m = re.search(r'day-content">(.*?)</div>', day49_html, re.DOTALL)
    if content_m:
        # Strip HTML tags
        text = re.sub(r'<[^>]+>', '', content_m.group(1))
        print(text[:500])
else:
    print('Day 49 not found!')
