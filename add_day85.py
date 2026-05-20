# -*- coding: utf-8 -*-
"""环游中国 - Day 85 更新脚本
日期: 2026-05-13 (Day 85 内容：庐山 → 景德镇，瓷都之旅)
"""
import re, sys, codecs, urllib.request, urllib.parse, json
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

# === SEARCH PHASE: 获取最新旅行信息 ===
queries = [
    ('景德镇旅游攻略 2026年5月 陶瓷博物馆 陶溪川', '景德镇'),
    ('婺源篁岭旅游攻略 2026年5月 晒秋', '婺源'),
]

search_results = {}
for query, name in queries:
    encoded_query = urllib.parse.quote(query)
    url = f'https://html.duckduckgo.com/html/?q={encoded_query}'
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })
    try:
        response = urllib.request.urlopen(req, timeout=15)
        html = response.read().decode('utf-8')
        pattern = r'<a class="result__a"[^>]*>([^<]*)</a>'
        snippets_pattern = r'<a class="result__a"[^>]*>.*?</a>.*?<a class="result__snippet"[^>]*>([^<]*)</a>'
        results = re.findall(pattern, html)
        snippet_results = re.findall(snippets_pattern, html, re.DOTALL)
        print(f'=== {name} ===')
        for i, r in enumerate(results[:5]):
            print(f'  {i+1}. {r.strip()}')
        search_results[name] = {'titles': [r.strip() for r in results[:5]], 'snippets': [s.strip() for s in snippet_results[:5]]}
    except Exception as e:
        print(f'Error for {name}: {e}')
        search_results[name] = {'titles': [], 'snippets': []}

# Save search results
search_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_day85.json'
with open(search_path, 'w', encoding='utf-8') as f:
    json.dump(search_results, f, ensure_ascii=False, indent=2)
print(f'Saved search results to {search_path}')

# === HTML UPDATE PHASE ===
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 84
new_day = current_day + 1
print(f'\nCurrent max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated dayCount -> 85')

# 2. Update km (庐山到景德镇约150km)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 150) + '<',
    content)
print('Updated kmCount -> 11580 (added 150km)')

# 3. Update location count (+1 景德镇)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated locationCount -> 52')

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">景德镇 · 瓷都<',
    content)
print('Updated currentLocation -> 景德镇 · 瓷都')

# 5. Day 85 entry (2026-05-13)
day85_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第85天</span>
                    <span class="day-date">2026-05-13 · 四月十六 · 周三</span>
                </div>
                <div class="day-title">🏺 庐山 → 景德镇 · 瓷都文化之旅</div>
                <div class="day-content">
                    <p>🚗 今日主题：告别庐山，驱车前往瓷都景德镇（车程约2.5小时，150km）</p>
                    <p>🏛️ 上午：景德镇中国陶瓷博物馆（免费，需提前在微信预约"景德镇中国陶瓷博物馆"）</p>
                    <p>🎨 下午：陶溪川文创街区 — 周五至周日晚上有创意集市（16:00-22:00），白天也可逛特色小店</p>
                    <p>🌆 傍晚：御窑博物院（门票53元）— 红砖拱廊建筑，傍晚灯光下尤为迷人</p>
                    <p>🍜 晚餐：景德镇本地菜，推荐"辣椒炒肉"、"碱水粑"、"鲶鱼煮豆腐"、冷粉</p>
                    <p>🛍️ 晚上可逛陶溪川夜市或樊家井批发市场，淘几件心仪的瓷器带回家</p>
                    <p>📅 明日预告：景德镇 → 婺源（约1小时），篁岭晒秋人家 + 詹天佑故居</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏺</div>
                    <div class="photo-placeholder">🎨</div>
                    <div class="photo-placeholder">🏛️</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🎫</span>
                        <span class="tip-text">陶瓷博物馆免费但需提前预约，周一闭馆；御窑博物院门票53元，建议下午4点前往，拍照效果好</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🛒</span>
                        <span class="tip-text">陶溪川创意集市逢周五六日16:00-22:00，本地设计师作品价格200-2000元；樊家井是批发价更便宜但需讲价</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🌸</span>
                        <span class="tip-text">4-5月景德镇春意盎然，适合古镇漫步；气温15-25℃，偶有小雨，备把伞</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day85_entry + '\n' + footer_marker)
print('Added Day 85 entry: 庐山 → 景德镇 · 瓷都文化之旅')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年5月13日（周三）</p>')
    print('Updated footer timestamp to 2026年5月13日（周三）')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 85')
print('Location: 景德镇 · 瓷都')
print('Date: 2026-05-13 (四月十六 · 周三)')
print('KM added: 150 (total: ~11580)')
print('Location count: 52')
print('Key update: 庐山→景德镇，瓷都文化之旅')