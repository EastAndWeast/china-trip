# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

proxy = "http://127.0.0.1:7890"
proxy_handler = urllib.request.ProxyHandler({'http': proxy, 'https': proxy})

query = '杭州西湖旅游攻略'
encoded_query = urllib.parse.quote(query)
url = f'https://lite.duckduckgo.com/lite/?q={encoded_query}'

req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html',
})
try:
    opener = urllib.request.build_opener(proxy_handler)
    response = opener.open(req, timeout=15)
    html = response.read().decode('utf-8')
    
    # Find all links
    print('All links in page:')
    links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]*)</a>', html)
    for href, text in links[:20]:
        if text.strip():
            print(f'  {text.strip()[:80]} -> {href[:60]}')
    
except Exception as e:
    print(f'Error: {e}')
