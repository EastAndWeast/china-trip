import re
with open(r'C:\Users\admin\.openclaw\workspace\china-trip\index.html', 'r', encoding='utf-8') as f:
    c = f.read()
# Count all day cards using broader regex
all_cards = re.findall(r'class="day-number">(\d+)<', c)
print('All day-number occurrences:', len(all_cards))
print('First 5:', all_cards[:5])
print('Last 10:', all_cards[-10:])
# Check for day-card divs
small_cards = re.findall(r'<div class="day-card">', c)
print('Total day-card divs:', len(small_cards))
# Check stats
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
# Find largest day number
nums = [int(x) for x in all_cards]
if nums:
    print('Min day:', min(nums), 'Max day:', max(nums))
    # Check for gaps
    from collections import Counter
    cnt = Counter(nums)
    missing = [n for n in range(min(nums), max(nums)+1) if cnt.get(n, 0) == 0]
    duplicates = [n for n, c in cnt.items() if c > 1]
    print('Missing days (in range):', missing[:30] if missing else 'none')
    print('Duplicates:', duplicates[:20] if duplicates else 'none')
