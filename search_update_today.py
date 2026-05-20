# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, sys, json, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('泉州旅游攻略 2026年4月 开元寺 清净寺 古城', '泉州古城'),
    ('泉州美食攻略 2026 姜母鸭 肉粽 面线糊', '泉州美食'),
    ('厦门鼓浪屿旅游攻略 2026年4月', '厦门鼓浪屿'),
]

results = {}
for q, name in queries:
    try:
        encoded = urllib.parse.quote(q)
        url = 'https://lite.duckduckgo.com/lite/?q=' + encoded
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=10)
        html = resp.read().decode('utf-8')
        titles = re.findall(r'class="result-link"[^>]*>([^<]+)</a>', html)
        print('=== ' + name + ' (' + str(len(titles)) + ' results) ===')
        for t in titles[:5]:
            print('  ' + t)
        results[name] = titles[:5]
    except Exception as e:
        print('Error for ' + name + ': ' + str(e))
        results[name] = []

output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump({'updated': '2026-04-25', 'queries': [{'name': k, 'results': [{'title': r} for r in v]} for k, v in results.items()]}, f, ensure_ascii=False, indent=2)
print('Saved to ' + output_path)