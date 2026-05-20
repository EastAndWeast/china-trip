# -*- coding: utf-8 -*-
"""环游中国 - 搜索武汉/长沙/南昌最新旅行信息"""
import urllib.request, urllib.parse, re, json, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('武汉旅游攻略 2026年5月 黄鹤楼 东湖', '武汉旅游'),
    ('长沙旅游攻略 2026年5月 橘子洲 岳麓山', '长沙旅游'),
    ('南昌旅游攻略 2026年5月 滕王阁 八一广场', '南昌旅游'),
    ('武汉到长沙自驾 2026年5月 路线', '武汉长沙自驾'),
    ('长沙美食 茶颜悦色 文和友 2026', '长沙美食'),
]

all_results = {}

for query, name in queries:
    encoded_query = urllib.parse.quote(query)
    # Try DuckDuckGo HTML
    url = f'https://html.duckduckgo.com/html/?q={encoded_query}'
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    })
    try:
        response = urllib.request.urlopen(req, timeout=15)
        html = response.read().decode('utf-8', errors='replace')
        # Multiple patterns to extract results
        patterns = [
            r'<a class="result__a"[^>]*>([^<]+)</a>',
            r'class="result__title"[^>]*>([^<]+)</a>',
        ]
        results = []
        for pat in patterns:
            results = re.findall(pat, html)
            if results:
                break
        results = [r.strip() for r in results if len(r.strip()) > 5][:8]
        print(f'=== {name} ({query}) ===')
        for i, r in enumerate(results):
            print(f'  {i+1}. {r}')
        print()
        all_results[name] = {'query': query, 'results': results, 'count': len(results)}
    except Exception as e:
        print(f'Error for {query}: {e}')
        all_results[name] = {'query': query, 'results': [], 'error': str(e)}

# Save
output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_day79.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print(f'Saved {len(all_results)} query results to {output_path}')