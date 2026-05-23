# -*- coding: utf-8 -*-
import re

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all day-date spans
date_pattern = r'<span class="day-date">(\d{4}-\d{2}-\d{2})'
dates = re.findall(date_pattern, content)
print(f'All dates found: {dates}')

# Find the last date position
last_date = dates[-1] if dates else None
if last_date:
    span_pattern = f'<span class="day-date">{last_date}'
    span_pos = content.find(span_pattern)
    print(f'Last date: {last_date} at position {span_pos}')
    print(f'Context around span (100 chars after):')
    print(repr(content[span_pos:span_pos+200]))

    # Search for day-content near this
    search_from = span_pos
    dc = content.find('<div class="day-content">', search_from)
    print(f'day-content found at: {dc}')
    if dc > 0:
        print(f'Distance from span: {dc - span_pos}')
        print(f'Content preview: {repr(content[dc:dc+200])}')