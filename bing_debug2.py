# -*- coding: utf-8 -*-
"""Debug Bing search"""
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
print('HTML length:', len(html))
# Look for patterns
if 'b_paractual' in html:
    print('Found b_paractual!')
    snippets = re.findall(r'<p class="b_paractual"[^>]*>([^<]+)</p>', html)
    print('Snippets:', len(snippets))
    for s in snippets[:3]:
        print('  ', s[:100])
else:
    print('No b_paractual found')
    # Check for other patterns
    if 'class="b_paract' in html:
        print('Found b_paract pattern')
        idx = html.find('b_paract')
        print(html[idx-50:idx+200])
    # Write to file for inspection
    with open('C:/Users/admin/.openclaw/workspace/china-trip/bing_debug.html', 'w', encoding='utf-8') as f:
        f.write(html[:50000])
    print('Wrote first 50k to bing_debug.html')