# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

query = '黄山旅游攻略 2026'
encoded_query = urllib.parse.quote(query)
url = 'https://html.duckduckgo.com/html/?q=' + encoded_query
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})
response = urllib.request.urlopen(req, timeout=15)
html = response.read().decode('utf-8')

# Try different patterns
patterns = [
    r'<a class="result__a"[^>]*>([^<]*)</a>',
    r'<a class=result__a[^>]*>([^<]*)</a>',
    r'class="result__a"[^>]*>([^<]+)</a>',
    r'result__a.*?>([^<]+)<',
]
for p in patterns:
    m = re.findall(p, html)
    print('Pattern:', p[:40], '->', len(m), 'matches')
    if m:
        for x in m[:3]:
            print('   ', x[:60])

# Also look for any result links
result_a = re.findall(r'<a [^>]*class="result__a"[^>]*>', html)
print('\nFound result__a tags:', len(result_a))
if result_a:
    print('First one:', result_a[0][:100])

# Check for any Chinese content
cn_pattern = re.findall(r'[\u4e00-\u9fff].{5,50}', html)
print('\nChinese text found:', len(cn_pattern))
if cn_pattern:
    for x in cn_pattern[:5]:
        print('  ', x[:60])
