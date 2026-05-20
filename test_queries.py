# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = ['千岛湖旅游 2026', '千岛湖船票 门票', '杭州千岛湖攻略']
for q in queries:
    encoded = urllib.parse.quote(q)
    url = 'https://html.duckduckgo.com/html/?q=' + encoded
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        html = resp.read().decode('utf-8', errors='ignore')
        titles = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html)
        print('Query:', q, '-> Results:', len(titles))
        for t in titles[:3]:
            print('  ', t.strip()[:60])
    except Exception as e:
        print('Error:', e)