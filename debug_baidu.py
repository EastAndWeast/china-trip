# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

q = '厦门鼓浪屿旅游攻略'
encoded = urllib.parse.quote(q)
url = 'https://www.baidu.com/s?wd=' + encoded
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
resp = urllib.request.urlopen(req, timeout=12)
html = resp.read().decode('utf-8', errors='ignore')
print('HTML length:', len(html))
# Look for result patterns
hits = re.findall(r'class="c-title', html)
print('c-title hits:', len(hits))
hits2 = re.findall(r'title.*?</a>', html)
print('title...</a> hits:', len(hits2[:10]))
# Find some text
text = re.findall(r'>([^<]{10,80})<', html)
for t in text[:20]:
    if '厦门' in t or '旅游' in t:
        print('Found:', t)