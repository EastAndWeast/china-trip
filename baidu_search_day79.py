# -*- coding: utf-8 -*-
"""环游中国 - Day 79 百度搜索更新"""
import urllib.request, urllib.parse, re, json, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('武汉旅游攻略 2026年5月 黄鹤楼 东湖', '武汉旅游'),
    ('长沙旅游攻略 2026年5月 橘子洲 岳麓山', '长沙旅游'),
    ('南昌旅游攻略 2026年5月 滕王阁', '南昌旅游'),
]

all_results = {}

for q, name in queries:
    try:
        encoded = urllib.parse.quote(q)
        url = 'https://www.baidu.com/s?wd=' + encoded
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        resp = urllib.request.urlopen(req, timeout=15)
        html = resp.read().decode('utf-8', errors='ignore')
        
        # Baidu result titles
        titles = re.findall(r'<h3 class="c-title.*?>(.*?)</h3>', html, re.DOTALL)
        if not titles:
            titles = re.findall(r'<h3[^>]*>([^<]+)', html)
        
        clean_titles = []
        for t in titles[:8]:
            ct = re.sub(r'<[^>]+>', '', t).strip()
            ct = re.sub(r'\s+', ' ', ct)
            if ct and len(ct) > 5:
                clean_titles.append(ct)
        
        print(f'=== {name} ({len(clean_titles)} results) ===')
        for i, t in enumerate(clean_titles[:5]):
            print(f'  {i+1}. {t[:80]}')
        print()
        
        all_results[name] = {'query': q, 'titles': clean_titles[:5], 'count': len(clean_titles)}
    except Exception as e:
        print(f'Error for {name}: {e}')
        all_results[name] = {'query': q, 'titles': [], 'error': str(e)}

# Save results
output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_day79.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump({
        'updated': '2026-05-07',
        'day': 79,
        'destination': '长沙',
        'search_results': all_results
    }, f, ensure_ascii=False, indent=2)
print(f'Saved to {output_path}')