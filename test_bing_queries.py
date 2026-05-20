# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = ['千岛湖旅游 2026', '千岛湖船票 门票', '杭州千岛湖攻略']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

for q in queries:
    encoded = urllib.parse.quote(q)
    url = 'https://www.bing.com/search?q=' + encoded + '&mkt=zh-CN'
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        html = resp.read().decode('utf-8', errors='ignore')
        titles = re.findall(r'<h2[^>]*><a[^>]*>([^<]+)</a></h2>', html)
        print('Query:', q, '-> Results:', len(titles))
        for t in titles[:3]:
            clean = re.sub(r'<[^>]+>', '', t).strip()
            print('  ', clean[:60])
    except Exception as e:
        print('Error:', e)