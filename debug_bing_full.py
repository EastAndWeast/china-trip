# -*- coding: utf-8 -*-
"""Debug Bing full response"""
import urllib.request, urllib.parse, re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

query = '西递古村 门票'
encoded = urllib.parse.quote(query)
url = 'https://www.bing.com/search?q=' + encoded + '&mkt=zh-CN'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}
req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req, timeout=15)
html = resp.read().decode('utf-8', errors='ignore')
print('Total length:', len(html))

# Find all class attributes with "result"
result_classes = re.findall(r'class="([^"]*)"', html)
unique_classes = sorted(set(result_classes))
print('\nUnique class values (first 30):')
for c in unique_classes[:30]:
    print('  ' + c)

# Find all divs with content
print('\n\nSearching for search result containers...')
for pattern in [r'<li[^>]*class="[^"]*b_algo[^"]*"', r'<div[^>]*class="[^"]*result[^"]*"']:
    matches = re.findall(pattern, html)
    print(pattern[:50] + ': ' + str(len(matches)) + ' matches')