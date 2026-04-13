# -*- coding: utf-8 -*-
"""Fetch travel info for Wuyuan North Line Day 57"""
import urllib.request, urllib.parse, re, json, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

# Try Bing with more specific queries for ticket prices, hours, etc.
queries_sixi = [
    ('思溪延村 门票多少钱 游览时间', '思溪延村门票'),
    ('思溪延村 延村 思溪村 历史典故', '思溪延村历史'),
]

queries_caihong = [
    ('婺源彩虹桥 门票 建于 宋代 历史', '彩虹桥历史'),
    ('清华彩虹桥 婺源 游览攻略', '彩虹桥攻略'),
]

queries_lingyan = [
    ('婺源灵岩洞 门票 开放时间', '灵岩洞门票'),
    ('灵岩洞 溶洞 婺源 北线', '灵岩洞介绍'),
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

for section, queries in [('思溪延村', queries_sixi), ('彩虹桥', queries_caihong), ('灵岩洞', queries_lingyan)]:
    print(f'=== {section} ===')
    titles_all = []
    snippets_all = []
    for query, desc in queries:
        titles, snippets = search_bing(query)
        print(f'  [{desc}] {len(titles)} results')
        titles_all.extend(titles[:3])
        snippets_all.extend(snippets[:3])
    all_results[section] = {
        'titles': titles_all[:5],
        'snippets': [re.sub(r'<[^>]+>', '', s)[:200] for s in snippets_all[:5]]
    }
    print()

# Also search for Wuyuan overall info
print('=== 婺源北线总体 ===')
titles, snippets = search_bing('婺源北线 思溪延村 彩虹桥 灵岩洞 石城 联票')
print(f'  {len(titles)} results')
all_results['婺源北线'] = {
    'titles': titles[:5],
    'snippets': [re.sub(r'<[^>]+>', '', s)[:200] for s in snippets[:5]]
}

# Save
output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_day57.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print(f'\nSaved to {output_path}')

# Print summary
print('\n=== SUMMARY ===')
for section, data in all_results.items():
    print(f'\n{section}:')
    for i, title in enumerate(data['titles'][:3]):
        print(f'  - {title}')
        if i < len(data['snippets']):
            print(f'    {data["snippets"][i][:100]}')
