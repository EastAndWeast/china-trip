# -*- coding: utf-8 -*-
"""Add Day 44 - Nanjing to Yangzhou"""
import re, sys, codecs, json, urllib.request, urllib.parse

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Step 1: Search for Yangzhou travel info
queries = [
    ('扬州旅游攻略 2026年4月 烟花三月 瘦西湖', '扬州旅游'),
    ('南京到扬州交通 2026年4月', '交通'),
    ('扬州瘦西湖 个园 大明寺 2026', '扬州景点'),
]

all_results = {}
for query, name in queries:
    try:
        encoded = urllib.parse.quote(query)
        url = f'https://html.duckduckgo.com/html/?q={encoded}'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=15)
        html = resp.read().decode('utf-8')
        results = re.findall(r'<a class="result__a"[^>]*>([^<]*)</a>', html)
        print(f'=== {name} ===')
        for i, r in enumerate(results[:5]):
            print(f'{i+1}. {r}')
        all_results[name] = results[:5]
    except Exception as e:
        print(f'Error: {e}')
        all_results[name] = []

# Save search results
with open('C:/Users/admin/.openclaw/workspace/china-trip/search_yangzhou.json', 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

# Step 2: Add Day 44 to index.html
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

day_44 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第44天</span>
                    <span class="day-date">2026-04-01 · 三月十五</span>
                </div>
                <div class="day-title">🚄 南京→扬州 · 烟花三月下扬州</div>
                <div class="day-content">
                    <p>🎉 四月第一天！告别南京，乘坐高铁前往扬州！"烟花三月下扬州"——终于等到这个季节！</p>
                    <p>🚄 交通：南京南→扬州，约40分钟，宁启铁路极为便捷</p>
                    <p>🏯 上午抵达扬州后，首先游览瘦西湖！这是江南最著名的园林湖泊之一。</p>
                    <p>🌸 瘦西湖：著名的"两岸花柳全依水，一路楼台只问山"，春季垂柳如丝、桃红柳绿</p>
                    <p>🌉 瘦西湖五亭桥、二十四桥、白塔等景点，一步一景，美不胜收！</p>
                    <p>🍜 午餐品尝扬州经典早茶：蟹黄包、烫干丝、虾仁蒸饺，扬州早茶名不虚传！</p>
                    <p>🏛️ 下午游览大明寺，千年古刹，鉴真大师东渡的起点！</p>
                    <p>🛕 大明寺：始建于南朝，历代高僧辈出，登上栖灵塔可俯瞰扬州城全景</p>
                    <p>🌙 傍晚漫步东关街——扬州最具代表性的历史老街！</p>
                    <p>🏮 东关街：全长1200米，汇集了扬州老字号店铺，夜晚灯火阑珊</p>
                    <p>📊 今日行程：南京到扬州高铁40分钟，瘦西湖+大明寺+东关街，步行约12公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🚄</div>
                    <div class="photo-placeholder">🌸</div>
                    <div class="photo-placeholder">🏮</div>
                </div>
            </div>
'''

# Find Day 43 position and insert Day 44 after it
pattern = r'(<span class="day-number">第43天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_44 + content[insert_pos:]
    
    # Update statistics
    new_content = re.sub(
        r'<div class="stat-value" id="dayCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>',
        new_content
    )
    
    # Update km count (Yangzhou walking ~12km + high speed rail ~100km)
    new_content = re.sub(
        r'<div class="stat-value" id="kmCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 112}</div>',
        new_content
    )
    
    # Update location count (add Yangzhou)
    new_content = re.sub(
        r'<div class="stat-value" id="locationCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="locationCount">{int(m.group(1)) + 1}</div>',
        new_content
    )
    
    # Update current location
    new_content = re.sub(
        r'id="currentLocation">[^<]+',
        'id="currentLocation">扬州 · 东关街',
        new_content
    )
    
    # Update last update time
    new_content = re.sub(
        r'最后更新：\d+年\d+月\d+日',
        '最后更新：2026年4月1日',
        new_content
    )
    
    # Write back
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('\nSuccessfully added Day 44!')
    print('Day 44: 南京→扬州 · 烟花三月下扬州 (2026-04-01)')
    print('Stats: dayCount +1, kmCount +112, locationCount +1')
    print('Current location: 扬州 · 东关街')
    print('Last update: 2026年4月1日')
else:
    print('Could not find Day 43 position!')
    day_matches = re.findall(r'<span class="day-number">(第\d+天)</span>', content)
    print('Found days: ' + str(day_matches[-5:] if day_matches else 'none'))
