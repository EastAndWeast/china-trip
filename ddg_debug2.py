# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

url = 'https://html.duckduckgo.com/html/?q=%E9%95%BF%E6%B2%99%E6%97%85%E6%B8%B8%E6%94%BB%E7%95%A5%202026'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
response = urllib.request.urlopen(req, timeout=15)
html = response.read().decode('utf-8')

with open('C:/Users/admin/.openclaw/workspace/china-trip/ddg_debug_output.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Written')