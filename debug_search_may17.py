# -*- coding: utf-8 -*-
"""Check what's happening with search - debug"""
import urllib.request, urllib.parse, re, json, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Test different search endpoints
tests = [
    ('Bing direct', 'https://www.bing.com/search?q=%E5%AE%89%E5%BE%BD%E6%B8%A3%E5%B7%9E&mkt=zh-CN'),
    ('DuckDuckGo', 'https://html.duckduckgo.com/html/?q=%E5%AE%89%E5%BE%BD%E6%B8%A3%E5%B7%9E'),
    ('DuckDuckGo Lite', 'https://lite.duckduckgo.com/lite/?q=%E5%AE%89%E5%BE%BD%E6%B8%A3%E5%B7%9E'),
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

for name, url in tests:
    print('=== ' + name + ' ===')
    try:
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=15)
        html = resp.read().decode('utf-8', errors='ignore')
        print('Status:', resp.status)
        print('Length:', len(html))
        # Look for results
        if 'result' in html.lower() or 'search' in html.lower():
            print('Contains search results')
        print()
    except Exception as e:
        print('Error:', str(e))
        print()