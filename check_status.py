# -*- coding: utf-8 -*-
import re
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Check index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find stats
dc = re.search(r'id="dayCount"[^>]*>(\d+)<', content)
lc = re.search(r'id="locationCount"[^>]*>(\d+)<', content)
km = re.search(r'id="kmCount"[^>]*>(\d+)<', content)
loc = re.search(r'id="currentLocation"[^>]*>([^<]+)<', content)
update = re.search(r'最后更新：([^<]+)', content)
print(f'=== Current Website Stats ===')
print(f'Day: {dc.group(1) if dc else "N/A"}')
print(f'Location #: {lc.group(1) if lc else "N/A"}')
print(f'KM: {km.group(1) if km else "N/A"}')
print(f'Current Location: {loc.group(1) if loc else "N/A"}')
print(f'Last Update: {update.group(1) if update else "N/A"}')

# Get day 40 content (second entry)
day40_pattern = r'<span class="day-number">第40天</span>.*?</div>\s*</div>\s*</div>'
day40_match = re.search(day40_pattern, content, re.DOTALL)
if day40_match:
    print('\n--- Day 40 (truncated) ---')
    print(day40_match.group(0)[:800])

# Check search results
with open('search_results_latest.json', 'r', encoding='utf-8') as f:
    search_data = json.load(f)
print(f'\n=== Search Results ===')
print(f'Updated: {search_data.get("updated", "N/A")}')
for query, results in search_data.items():
    if query != 'updated' and isinstance(results, list) and len(results) > 0:
        print(f'\nQuery: {query}')
        for r in results[:2]:
            print(f'  - {r.get("title", "N/A")[:60]}')
