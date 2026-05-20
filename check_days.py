# -*- coding: utf-8 -*-
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all day numbers
day_nums = re.findall(r'<span class="day-number">(第\d+天)</span>', content)
print(f"Total days found: {len(day_nums)}")
for d in day_nums:
    print(d)

# Check what's around the last day number
last_pos = content.rfind('<span class="day-number">')
print(f"\nLast day number position: {last_pos}")
print(content[last_pos:last_pos+200])
