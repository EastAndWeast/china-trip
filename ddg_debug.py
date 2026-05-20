# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

query = '长沙旅游攻略 2026'
encoded_query = urllib.parse.quote(query)
url = 'https://html.duckduckgo.com/html/?q=' + encoded_query
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
response = urllib.request.urlopen(req, timeout=15)
html = response.read().decode('utf-8')
print('HTML length:', len(html))

# Find result__a
idx = html.find('result__a')
if idx >= 0:
    print('Found result__a at index', idx)
    print(html[idx-100:idx+300])
else:
    print('No result__a found, looking for other patterns')
    # Check for any interesting class names
    classes = re.findall(r'class="([^"]+)"', html)
    class_counts = {}
    for c in classes:
        class_counts[c] = class_counts.get(c, 0) + 1
    for k, v in sorted(class_counts.items(), key=lambda x: -x[1])[:20]:
        print(f'  {k}: {v}')