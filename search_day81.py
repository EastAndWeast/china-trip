# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, json, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

queries = [
    ('南昌绳金塔 美食攻略 2026', '绳金塔'),
    ('南昌八一起义纪念馆 预约 开放时间 2026', '纪念馆'),
    ('南昌滕王阁 门票 夜游 2026', '滕王阁'),
    ('武汉旅游 黄鹤楼 东湖 2026年5月', '武汉'),
]

all_results = {}

def search_bing(query):
    encoded = urllib.parse.quote(query)
    url = f'https://www.bing.com/search?q={encoded}&mkt=zh-CN'
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        html = resp.read().decode('utf-8', errors='ignore')
        titles = re.findall(r'<h2[^>]*><a[^>]*>([^<]+)</a></h2>', html)
        snippets = re.findall(r'<p class="b_paractual"[^>]*>([^<]+)</p>', html)
        return titles, snippets
    except Exception as e:
        print(f'  Bing error: {e}')
        return [], []

for query, name in queries:
    print(f'=== {name}: {query} ===')
    titles, snippets = search_bing(query)
    print(f'  {len(titles)} results')
    for t in titles[:3]:
        print(f'  - {t}')
    for s in snippets[:2]:
        clean = re.sub(r'<[^>]+>', '', s).strip()[:100]
        if clean:
            print(f'    {clean}')
    all_results[name] = {'titles': titles[:5], 'snippets': [re.sub(r'<[^>]+>', '', s).strip()[:150] for s in snippets[:5]]}
    print()

output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_day81.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print(f'Saved to {output_path}')