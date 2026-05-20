# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open(r'C:\Users\admin\.openclaw\workspace\china-trip\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

days = re.findall(r'class="day-number">第(\d+)天', content)
locs = re.findall(r'class="day-title">([^<]+)<', content)
dates = re.findall(r'class="day-date">([^<]+)<', content)

if days:
    max_day = max([int(d) for d in days])
    print('Last day number:', max_day)
    idx = days.index(str(max_day))
    if idx < len(locs): print('Location:', locs[idx])
    if idx < len(dates): print('Date:', dates[idx])

m = re.search(r'id="dayCount"[^>]*>(\d+)<', content)
if m: print('dayCount:', m.group(1))
m = re.search(r'id="kmCount"[^>]*>(\d+)<', content)
if m: print('kmCount:', m.group(1))
m = re.search(r'id="locationCount"[^>]*>(\d+)<', content)
if m: print('locationCount:', m.group(1))
m = re.search(r'id="currentLocation"[^>]*>([^<]+)<', content)
if m: print('currentLocation:', m.group(1))
m = re.search(r'最后更新：([^<]+)<', content)
if m: print('Last updated:', m.group(1))