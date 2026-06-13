# -*- coding: utf-8 -*-
"""验证 Day 117 更新"""
import re, sys, codecs, os
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = r'C:\Users\admin\.openclaw\workspace\china-trip\index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Find Day 117 entry
day117_match = re.search(
    r'<div class="day-card">\s*<div class="day-header">\s*<span class="day-number">117</span>\s*<span class="day-date">([^<]+)</span>.*?</div>\s*</div>',
    content, re.DOTALL)

if day117_match:
    print('=== Day 117 Entry Verified ===')
    print('Date line:', day117_match.group(1).strip())
    title_match = re.search(
        r'<span class="day-number">117</span>.*?<div class="day-title">([^<]+)</div>',
        content, re.DOTALL)
    if title_match:
        print('Title:', title_match.group(1).strip())
else:
    print('ERROR: Day 117 entry not found!')

# Check all stats
print()
print('=== Stats ===')
day_match = re.search(r'id="dayCount"[^>]*>(\d+)<', content)
km_match = re.search(r'id="kmCount"[^>]*>(\d+)<', content)
loc_match = re.search(r'id="locationCount"[^>]*>(\d+)<', content)
cur_match = re.search(r'id="currentLocation"[^>]*>([^<]+)<', content)
print(f'dayCount: {day_match.group(1) if day_match else "?"}')
print(f'kmCount: {km_match.group(1) if km_match else "?"}')
print(f'locationCount: {loc_match.group(1) if loc_match else "?"}')
print(f'currentLocation: {cur_match.group(1) if cur_match else "?"}')

# Check subtitle
subtitle_match = re.search(r'<p class="subtitle">([^<]+)</p>', content)
if subtitle_match:
    print(f'Subtitle: {subtitle_match.group(1).strip()}')

# Day cards
day_cards = re.findall(r'<div class="day-card">\s*<div class="day-header">\s*<span class="day-number">(\d+)</span>\s*<span class="day-date">([^<]+)</span>', content, re.DOTALL)
day_nums = [int(d[0]) for d in day_cards]
print(f'\nTotal day cards: {len(day_cards)}')
print(f'Min: {min(day_nums)}, Max: {max(day_nums)}')
print(f'All unique: {len(set(day_nums))} == {len(day_nums)} ({len(set(day_nums)) == len(day_nums)})')

print('\n=== Latest 5 days ===')
for d in day_cards[-5:]:
    print(f'  Day {d[0]}: {d[1].strip()}')

# Check footer
print('\n=== Footer last update ===')
footer_match = re.search(r'最后更新：([^<]+)<', content)
if footer_match:
    print(f'Last update: {footer_match.group(1).strip()}')

# Day 117 tips count
day117_tips = content[content.find('day-number">117</span>'):content.find('day-number">117</span>')+30000]
tip_count = day117_tips.count('<div class="tip">')
print(f'\nDay 117 tips count: {tip_count}')

# File size
print(f'\nFile size: {os.path.getsize(HTML_PATH)} bytes')

# Verify content includes key Suzhou landmarks
print('\n=== Content checks ===')
print(f'currentLocation contains 苏州: {"苏州" in (cur_match.group(1) if cur_match else "")}')
print(f'Footer contains 苏州: {"苏州" in content[content.find("<div class=\"footer\">"):]}')
print(f'Footer contains 2026年6月14日: {"2026年6月14日" in content}')
print(f'Footer contains 拙政园: {"拙政园" in content}')
print(f'Footer contains 寒山寺: {"寒山寺" in content}')
print(f'Footer contains 平江路: {"平江路" in content}')

# Verify the new location
print(f'currentLocation contains 拙政园: {"拙政园" in (cur_match.group(1) if cur_match else "")}')

# Verify title and date line
day117_title = re.search(
    r'<span class="day-number">117</span>\s*<span class="day-date">([^<]+)</span>.*?<div class="day-title">([^<]+)</div>',
    content, re.DOTALL)
if day117_title:
    print(f'\nDay 117 date: {day117_title.group(1).strip()}')
    print(f'Day 117 title: {day117_title.group(2).strip()}')
