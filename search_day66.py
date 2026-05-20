# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, sys, json, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    ('漳州古城旅游攻略 2026年4月 文庙 尚书探花府', '漳州古城'),
    ('福州三坊七巷旅游攻略 2026年4月', '福州旅游'),
    ('武夷山旅游攻略 2026年4月 九曲溪 天游峰', '武夷山'),
]

results = {}
for q, name in queries:
    try:
        encoded = urllib.parse.quote(q)
        url = 'https://www.baidu.com/s?wd=' + encoded
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        resp = urllib.request.urlopen(req, timeout=12)
        html = resp.read().decode('utf-8', errors='ignore')
        titles = re.findall(r'<h3[^>]*>([^<]+)</h3>', html)
        print('=== ' + name + ' (' + str(len(titles)) + ' results) ===')
        for t in titles[:5]:
            clean = re.sub(r'<[^>]+>', '', t).strip()
            if clean:
                print('  ' + clean[:80])
        results[name] = titles[:5]
    except Exception as e:
        print('Error for ' + name + ': ' + str(e))
        results[name] = []

output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump({'updated': '2026-04-23', 'queries': [{'name': k, 'results': [{'title': re.sub(r'<[^>]+>', '', r).strip()[:100]} for r in v]} for k, v in results.items()]}, f, ensure_ascii=False, indent=2)
print('Saved to ' + output_path)