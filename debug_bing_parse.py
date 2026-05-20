# -*- coding: utf-8 -*-
"""Debug Bing search result parsing"""
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

# Try different patterns
patterns = [
    (r'<h2[^>]*><a[^>]*>([^<]+)</a></h2>', 'h2>a pattern'),
    (r'<h3[^>]*><a[^>]*>([^<]+)</a></h3>', 'h3>a pattern'),
    (r'class="b_title"[^>]*>([^<]+)', 'b_title'),
    (r'class="title"[^>]*>([^<]+)', 'title'),
    (r'<a [^>]*class="[^"]*result[^"]*"[^>]*>([^<]+)</a>', 'result-link'),
    (r'class="[^"]*headline[^"]*"[^>]*>([^<]+)', 'headline'),
]

for pat, desc in patterns:
    matches = re.findall(pat, html)
    print(desc + ': ' + str(len(matches)) + ' matches')
    for m in matches[:3]:
        print('  ' + m[:80])

# Write a portion of HTML for inspection
with open('C:/Users/admin/.openclaw/workspace/china-trip/bing_search_sample.html', 'w', encoding='utf-8') as f:
    # Find around where results might be
    idx = html.find('西递')
    if idx > 0:
        f.write(html[max(0,idx-200):idx+500])
    else:
        f.write(html[30000:35000])
print('Wrote sample to bing_search_sample.html')