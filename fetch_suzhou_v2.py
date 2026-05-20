# -*- coding: utf-8 -*-
"""Fetch travel info using alternative approach"""
import urllib.request, urllib.parse, re, json, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Try Bing API-style search
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

queries = [
    ('苏州 2026年4月 旅游攻略 景点', '苏州旅游'),
]

for query, name in queries:
    encoded = urllib.parse.quote(query)
    # Try Bing search
    url = f'https://www.bing.com/search?q={encoded}&mkt=zh-CN'
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        html = resp.read().decode('utf-8', errors='ignore')
        # Find search results
        titles = re.findall(r'<h2[^>]*><a[^>]*>([^<]+)</a></h2>', html)
        print(f'=== {name} (Bing) ===')
        for t in titles[:5]:
            clean = re.sub(r'<[^>]+>', '', t)
            print(f'  {clean}')
        
        # Save raw for inspection
        with open('C:/Users/admin/.openclaw/workspace/china-trip/bing_test.html', 'w', encoding='utf-8') as f:
            f.write(html[:5000])
        print(f'Saved raw to bing_test.html')
    except Exception as e:
        print(f'Error {name}: {e}')
