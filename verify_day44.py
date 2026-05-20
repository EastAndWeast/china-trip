# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

loc = re.search(r'id="currentLocation">([^<]+)', content)
print('currentLocation:', loc.group(1) if loc else 'not found')
daycnt = re.search(r'id="dayCount">(\d+)</div>', content)
print('dayCount:', daycnt.group(1) if daycnt else 'not found')
loccnt = re.search(r'id="locationCount">(\d+)</div>', content)
print('locationCount:', loccnt.group(1) if loccnt else 'not found')
kmcnt = re.search(r'id="kmCount">(\d+)</div>', content)
print('kmCount:', kmcnt.group(1) if kmcnt else 'not found')
lastup = re.search(r'最后更新：(\d+年\d+月\d+日)', content)
print('Last update:', lastup.group(1) if lastup else 'not found')

# Count total day cards
day_cards = re.findall(r'<span class="day-number">(第\d+天)</span>', content)
print(f'Total day cards found: {len(day_cards)}')
print(f'Day cards: {day_cards[:5]} ... {day_cards[-5:]}')
