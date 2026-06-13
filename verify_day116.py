# -*- coding: utf-8 -*-
"""验证 Day 116 更新"""
import re, sys, codecs, os
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = r'C:\Users\admin\.openclaw\workspace\china-trip\index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Find Day 116 entry
day116_match = re.search(
    r'<div class="day-card">\s*<div class="day-header">\s*<span class="day-number">116</span>\s*<span class="day-date">([^<]+)</span>.*?</div>\s*</div>',
    content, re.DOTALL)

if day116_match:
    print('=== Day 116 Entry Verified ===')
    print('Date line:', day116_match.group(1).strip())
    # Find title
    title_match = re.search(
        r'<span class="day-number">116</span>.*?<div class="day-title">([^<]+)</div>',
        content, re.DOTALL)
    if title_match:
        print('Title:', title_match.group(1).strip())
else:
    print('ERROR: Day 116 entry not found!')

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

# Check day range in comments
day_range_match = re.search(r'第\s*(\d+)\s*天\s*[-–~]\s*第\s*(\d+)\s*天', content)
if day_range_match:
    print(f'Day range in comment: {day_range_match.group(1)} - {day_range_match.group(2)}')

# Check subtitle
subtitle_match = re.search(r'<p class="subtitle">([^<]+)</p>', content)
if subtitle_match:
    print(f'Subtitle: {subtitle_match.group(1).strip()}')

# Day cards sorted
day_cards = re.findall(r'<div class="day-card">\s*<div class="day-header">\s*<span class="day-number">(\d+)</span>\s*<span class="day-date">([^<]+)</span>', content, re.DOTALL)
day_nums = [int(d[0]) for d in day_cards]
print(f'\nTotal day cards: {len(day_cards)}')
print(f'Day numbers: {sorted(set(day_nums))[:5]}...{sorted(set(day_nums))[-5:]}')
print(f'Min: {min(day_nums)}, Max: {max(day_nums)}')
print(f'All unique: {len(set(day_nums))} == {len(day_nums)} ({len(set(day_nums)) == len(day_nums)})')

# Check latest 5 day cards
print('\n=== Latest 5 days ===')
for d in day_cards[-5:]:
    print(f'  Day {d[0]}: {d[1].strip()}')

# Check footer
print('\n=== Footer last update ===')
footer_match = re.search(r'最后更新：([^<]+)<', content)
if footer_match:
    print(f'Last update: {footer_match.group(1).strip()}')

# Verify tips count
day116_tips = content[content.find('day-number">116</span>'):content.find('day-number">116</span>')+30000]
tip_count = day116_tips.count('<div class="tip">')
print(f'\nDay 116 tips count: {tip_count}')

# Check the section-title at top  
# Look for "第X天" pattern at top
top_title_match = re.search(r'<h1[^>]*>.*?</h1>', content, re.DOTALL)
if top_title_match:
    print(f'\n=== Top h1 ===\n{top_title_match.group(0)[:200]}')

# File size
print(f'\nFile size: {os.path.getsize(HTML_PATH)} bytes')

# Validate the new location
print(f'\ncurrentLocation contains 乌镇: {"乌镇" in cur_match.group(1) if cur_match else False}')
print(f'currentLocation contains 西栅: {"西栅" in cur_match.group(1) if cur_match else False}')

# Footer check
footer_section = content[content.find('<div class="footer">'):]
print(f'\nFooter contains 乌镇: {"乌镇" in footer_section}')
print(f'Footer contains 2026年6月13日: {"2026年6月13日" in footer_section}')
print(f'Footer contains 木心美术馆: {"木心美术馆" in footer_section}')
print(f'Footer contains 茅盾: {"茅盾" in footer_section}')
