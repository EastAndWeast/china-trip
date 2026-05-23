# -*- coding: utf-8 -*-
import re

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Find current stats
day_match = re.search(r'id="dayCount"[^>]*>(\d+)<', content)
km_match = re.search(r'id="kmCount"[^>]*>(\d+)<', content)
loc_match = re.search(r'id="locationCount"[^>]*>(\d+)<', content)
cur_match = re.search(r'id="currentLocation"[^>]*>([^<]+)<', content)

print(f"Current dayCount: {day_match.group(1) if day_match else 'not found'}")
print(f"Current kmCount: {km_match.group(1) if km_match else 'not found'}")
print(f"Current locationCount: {loc_match.group(1) if loc_match else 'not found'}")
print(f"Current location: {cur_match.group(1) if cur_match else 'not found'}")

# Find latest day
day_nums = re.findall(r'class="day-number">(\d+)<', content)
print(f"Last day numbers: {day_nums[-5:] if day_nums else 'none'}")

# Find dates
dates = re.findall(r'<span class="day-date">(\d{4}-\d{2}-\d{2})', content)
print(f"Last dates: {dates[-5:] if dates else 'none'}")

# Find current location in stats
current = re.search(r'id="currentLocation"[^>]*>([^<]+)<', content)
if current:
    print(f"Current location: {current.group(1)}")
