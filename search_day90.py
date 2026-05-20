# -*- coding: utf-8 -*-
"""Search for upcoming destinations using DuckDuckGo: 千岛湖"""
import urllib.request, urllib.parse, re, json, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('千岛湖 门票 开放时间 2026年5月', '千岛湖'),
    ('千岛湖旅游攻略 必玩景点 船票', '千岛湖攻略'),
    ('千岛湖鱼头 推荐餐厅 2026', '千岛湖美食'),
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

results = {}
for q, name in queries:
    encoded = urllib.parse.quote(q)
    url = 'https://html.duckduckgo.com/html/?q=' + encoded
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        html = resp.read().decode('utf-8', errors='ignore')
        titles = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html)
        snippets = re.findall(r'<a class="result__snippet"[^>]*>([^<]*)</a>', html)
        clean_titles = [re.sub(r'<[^>]+>', '', t).strip() for t in titles]
        clean_snippets = [re.sub(r'<[^>]+>', '', s).strip()[:200] for s in snippets]
        print('=== ' + name + ': ' + str(len(clean_titles)) + ' titles ===')
        for i, t in enumerate(clean_titles[:5]):
            print('  ' + str(i+1) + '. ' + t[:70])
            if i < len(clean_snippets):
                print('     ' + clean_snippets[i][:80])
        print()
        results[name] = {'titles': clean_titles[:5], 'snippets': clean_snippets[:5]}
    except Exception as e:
        print('Error for ' + name + ': ' + str(e))
        results[name] = {'titles': [], 'snippets': []}

output = {'updated': '2026-05-18', 'day90': {'destination': '千岛湖', 'queries': results}}
with open('C:/Users/admin/.openclaw/workspace/china-trip/search_results_day90.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
print('Saved search_results_day90.json')