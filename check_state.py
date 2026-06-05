# -*- coding: utf-8 -*-
import re
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
day_nums = re.findall(r'class="day-number">(\d+)<', c)
print('Last 5 day numbers:', day_nums[-5:] if day_nums else 'none')
day_match = re.search(r'id="dayCount"[^>]*>(\d+)<', c)
km_match = re.search(r'id="kmCount"[^>]*>(\d+)<', c)
loc_match = re.search(r'id="locationCount"[^>]*>(\d+)<', c)
cur_match = re.search(r'id="currentLocation"[^>]*>([^<]+)<', c)
print('Stats: dayCount=%s, kmCount=%s, locationCount=%s, location=%s' % (
    day_match.group(1) if day_match else '?',
    km_match.group(1) if km_match else '?',
    loc_match.group(1) if loc_match else '?',
    cur_match.group(1) if cur_match else '?'
))
# Find footer tips
footer_match = re.search(r'<div class="footer">(.*?)(?=</body>|</html>|$)', c, re.DOTALL)
if footer_match:
    text = re.sub(r'<[^>]+>', '', footer_match.group(1))
    text = re.sub(r'\s+', ' ', text)
    print('Footer text (last 500 chars):', text[-500:])
