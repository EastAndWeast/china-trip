# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

query = '苏州旅游攻略 2026'
encoded_query = urllib.parse.quote(query)
url = 'https://lite.duckduckgo.com/lite/?q=' + encoded_query
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html',
})
response = urllib.request.urlopen(req, timeout=15)
html = response.read().decode('utf-8')

# Find result links from lite version
pattern = '<a class="result-link" href="([^"]+)"[^>]*>([^<]+)</a>'
results = re.findall(pattern, html)
print(f'Lite results: {len(results)}')
for r in results[:10]:
    print(r)
