# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

days = re.findall(r'class="day-number">第(\d+)天', content)
print('Total days in website:', len(days))
print('Day numbers:', sorted(set(int(d) for d in days)))

day_dates = re.findall(r'class="day-number">第(\d+)天.*?class="day-date">([^<]+)', content, re.DOTALL)
print('Last 5 days with dates:')
for d, date in day_dates[-5:]:
    print('  Day ' + d + ': ' + date)

dc = re.search(r'id="dayCount"[^>]*>(\d+)<', content)
print('Day count stat:', dc.group(1) if dc else 'N/A')
km = re.search(r'id="kmCount"[^>]*>(\d+)<', content)
print('KM stat:', km.group(1) if km else 'N/A')
lc = re.search(r'id="locationCount"[^>]*>(\d+)<', content)
print('Location count stat:', lc.group(1) if lc else 'N/A')
loc = re.search(r'id="currentLocation"[^>]*>([^<]+)<', content)
print('Current location:', loc.group(1) if loc else 'N/A')
footer = re.search(r'最后更新：([^<]+)', content)
print('Footer update:', footer.group(1) if footer else 'N/A')
