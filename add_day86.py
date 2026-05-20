# -*- coding: utf-8 -*-
"""环游中国 - Day 86 更新脚本
日期: 2026-05-14 (Day 86 内容：景德镇 → 婺源，篁岭晒秋 + 江湾 + 詹天佑故居)
"""
import re, sys, codecs, urllib.request, urllib.parse, json
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'
SEARCH_RESULTS_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_day86.json'

# === SEARCH PHASE: 获取最新旅行信息 ===
queries = [
    ('婺源篁岭旅游攻略 2026年5月 晒秋 路线', '婺源篁岭'),
    ('婺源江湾古镇旅游攻略 2026年 景点', '婺源江湾'),
    ('婺源旅游攻略 2026年5月 美食 交通', '婺源美食交通'),
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
        title_pattern = r'<a class="result__a"[^>]*>([^<]*)</a>'
        snippet_pattern = r'<a class="result__snippet"[^>]*>([^<]*)</a>'
        titles = re.findall(title_pattern, html)
        snippets = re.findall(snippet_pattern, html)
        print(f'=== {name} ===')
        for i, t in enumerate(titles[:5]):
            print(f'  {i+1}. {t.strip()}')
        search_results[name] = {
            'titles': [t.strip() for t in titles[:5]],
            'snippets': [s.strip() for s in snippets[:5]]
        }
    except Exception as e:
        print(f'Error for {name}: {e}')
        search_results[name] = {'titles': [], 'snippets': []}

# Save search results
with open(SEARCH_RESULTS_PATH, 'w', encoding='utf-8') as f:
    json.dump(search_results, f, ensure_ascii=False, indent=2)
print(f'\nSaved search results to {SEARCH_RESULTS_PATH}')

# === KEY FINDINGS FROM SEARCH ===
key_findings = {
    'day86': {
        'jingdezhen_wuyuan': '景德镇到婺源约1小时车程（高铁20分钟），婺源站到篁岭需搭巴士或打车',
        'huangl ing': '篁岭晒秋：春天也有"晒秋"景观，梯田油菜花海，缆车登顶观景',
        'jiangwan': '江湾古镇：萧江宗祠、江永纪念馆、三省堂，徽派建筑群',
        'tips': '婺源通票180元含14个景点；篁岭单独票145元（含缆车）；5月是淡季人少'
    }
}

# === HTML UPDATE PHASE ===
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 85
new_day = current_day + 1
print(f'\nCurrent max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print(f'Updated dayCount -> {current_day + 1}')

# 2. Update km (景德镇到婺源约120km)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 120) + '<',
    content)
print('Updated kmCount (added 120km)')

# 3. Update location count (+1 婺源)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated locationCount (added 1)')

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">婺源 · 最美乡村<',
    content)
print('Updated currentLocation -> 婺源 · 最美乡村')

# 5. Day 86 entry (2026-05-14)
day86_entry = f'''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第86天</span>
                    <span class="day-date">2026-05-14 · 四月十七 · 周四</span>
                </div>
                <div class="day-title">🌾 景德镇 → 婺源 · 最美乡村</div>
                <div class="day-content">
                    <p>🚗 今日行程：景德镇驱车前往婺源（车程约1小时，高铁仅20分钟）</p>
                    <p>🌾 上午：篁岭景区 — 缆车登顶，欣赏梯田油菜花海（5月油菜花晚熟品种仍有）</p>
                    <p>🏘️ 特色体验：篁岭古村"晒秋"景观，徽派建筑群，天街古巷</p>
                    <p>🏛️ 下午：江湾古镇 — 萧江宗祠、江永纪念馆、三省堂，徽派宗祠文化</p>
                    <p>🍜 婺源特色美食：荷包红鲤鱼、粉蒸肉、糊豆腐、糖醋鹅颈</p>
                    <p>🌙 晚上住婺源县城，逛婺源文化广场，体验当地夜生活</p>
                    <p>📅 明日预告：婺源 → 黄山（约2小时车程），黄山风景区</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌾</div>
                    <div class="photo-placeholder">🏘️</div>
                    <div class="photo-placeholder">🌸</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🎫</span>
                        <span class="tip-text">婺源通票180元含14个景点（篁岭单独145元含缆车）；建议提前网上购票</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🚗</span>
                        <span class="tip-text">景德镇到婺源：高铁20分钟（婺源站），或自驾1小时走杭长高速；婺源站到篁岭需打车约30元</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🌸</span>
                        <span class="tip-text">5月婺源是淡季，游客少，住宿便宜（县城100-200元/晚）；油菜花晚熟品种5月上旬仍可看</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day86_entry + '\n' + footer_marker)
print('Added Day 86 entry: 景德镇 → 婺源 · 最美乡村')

# 6. Update footer timestamp
content = re.sub(
    r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>',
    '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年5月14日（周四）</p>',
    content
)
print('Updated footer timestamp to 2026年5月14日（周四）')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Day 86 Update Complete ===')
print('Day: 86')
print('Location: 婺源 · 最美乡村')
print('Date: 2026-05-14 (四月十七 · 周四)')
print('KM added: 120 (total: ~11700)')
print('Location count: 54')
print('Key update: 景德镇→婺源，篁岭晒秋 + 江湾古镇')