# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

query = '苏州旅游攻略 2026'
encoded_query = urllib.parse.quote(query)
url = f'https://html.duckduckgo.com/html/?q={encoded_query}'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
})
response = urllib.request.urlopen(req, timeout=15)
html = response.read().decode('utf-8')

# Find results - look for the result__a class
pattern = r'<a class="result__a"[^>]*href="([^"]+)"[^>]*>([^<]+)</a>'
results = re.findall(pattern, html)
print(f'Results found: {len(results)}')
for r in results[:10]:
    print(r)
