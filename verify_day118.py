"""Final verification of Day 118 update"""
import re, sys, codecs, os
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

print('=== Stats ===')
for stat in ['dayCount', 'kmCount', 'locationCount', 'currentLocation']:
    m = re.search(r'id="' + stat + r'"[^>]*>([^<]+)<', c)
    print(f'  {stat}: {m.group(1) if m else "NOT FOUND"}')

print()
print('=== Latest 5 days ===')
days = re.findall(r'<span class="day-number">(\d+)</span>\s*<span class="day-date">([^<]+)</span>', c)
for d in days[-5:]:
    print(' ', d)

print()
print('=== Day 118 Entry ===')
day118_pos = c.find('day-number">118</span>')
print('Day 118 marker pos:', day118_pos)
if day118_pos > 0:
    # Get day card
    day_card_start = c.rfind('<div class="day-card">', 0, day118_pos)
    day_card_end = c.find('<div class="day-card">', day118_pos)
    if day_card_end == -1:
        day_card_end = c.find('<div class="footer">')
    entry = c[day_card_start:day_card_end]
    print(f'Day 118 entry length: {len(entry)} bytes')
    # Count tips
    tip_count = entry.count('<div class="tip">')
    p_count = entry.count('<p>')
    photo_count = entry.count('<div class="photo-placeholder">')
    print(f'  Tips: {tip_count}')
    print(f'  <p> tags: {p_count}')
    print(f'  Photos: {photo_count}')
    # Show first 500 chars
    # Try to extract title
    title_m = re.search(r'<div class="day-title">([^<]+)</div>', entry)
    if title_m:
        print(f'  Title: {title_m.group(1)}')
    # Date line
    date_m = re.search(r'<span class="day-date">([^<]+)</span>', entry)
    if date_m:
        print(f'  Date: {date_m.group(1)}')

print()
print('=== Footer ===')
m = re.search(r'最后更新：([^<]+)<', c)
print('Last update:', m.group(1) if m else 'NOT FOUND')

# Find footer tip title
m = re.search(r'<p style="font-size: 14px; margin-bottom: 10px;">([^<]+)</p>', c)
if m:
    print('Footer title:', m.group(1))

print()
print('=== Content Sanity ===')
checks = [
    '中山陵',  # Day 118 main spot
    '明孝陵',  # Day 118 second spot
    '秦淮河',  # Day 118 third spot
    '总统府',  # Day 118 fourth spot
    '夫子庙',  # Day 118
    '玄武湖',  # Day 118
    '鸡鸣寺',  # Day 118
    '老门东',  # Day 118
    '鸭血粉丝',  # Day 118 food
    '盐水鸭',  # Day 118 food
    '小雨转阴 28/22',  # Day 118 weather
    '220km',  # Day 118 distance
    'G42',  # Day 118 highway
    '2500年',  # Nanjing historical claim
]
for keyword in checks:
    found = keyword in c
    print(f'  "{keyword}": {"YES" if found else "NO ❌"}')

# Check that Day 117 (苏州) entry still has its content
day117_checks = [
    '拙政园',
    '留园',
    '苏州博物馆',
    '平江路',
    '寒山寺',
]
print()
print('=== Day 117 content preservation ===')
for keyword in day117_checks:
    found = keyword in c
    print(f'  "{keyword}": {"YES" if found else "NO ❌"}')

# Old dayCount, kmCount, locationCount should be replaced
# Verify new values
assert 'id="dayCount">119<' in c, 'dayCount not 119'
assert 'id="kmCount">16115<' in c, 'kmCount not 16115'
assert 'id="locationCount">126<' in c, 'locationCount not 126'
print()
print('=== All assertions passed ===')
print('New file size:', os.path.getsize('index.html'), 'bytes')

# Check brace balance
open_braces = c.count('{')
close_braces = c.count('}')
print(f'Braces: open={open_braces}, close={close_braces}, balanced={open_braces == close_braces}')

# Check basic HTML structure
print(f'<div> count: {c.count("<div>")}')
print(f'</div> count: {c.count("</div>")}')
