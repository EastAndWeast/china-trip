# -*- coding: utf-8 -*-
"""Add Day 46 - 苏州 Day 1 - 出发前往苏州"""
import re, sys, codecs, json, os
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Use existing search data for 苏州
search_data = {
    "苏州旅游": [
        {"title": "2026苏州旅游攻略：苏州园林+平江路+金鸡湖三日经典路线", "url": "https://zhuanlan.zhihu.com/p/1890444732850762196", "snippet": "4月份计划来苏州的姐妹，大多都比较关心4月苏州天气该穿什么/苏州园林哪些值得去..."},
        {"title": "2026苏杭保姆级旅游攻略，吃住行全覆盖，人挤人也不踩坑!", "url": "https://www.sohu.com/a/1002860166_122614299", "snippet": "2026苏杭保姆级旅游攻略：吃住行全覆盖..."},
        {"title": "2026苏州国际旅游年·苏州春天旅游季启幕", "url": "https://www.suzhou.gov.cn/szsrmzf/szyw/202603/9f49bb7865df4f088c86b354c32c9a85.shtml", "snippet": "苏州春天旅游季携春日新福利、新活动、新产品、新品牌、新灵感焕新而来"},
        {"title": "2026苏州三天两晚深度旅行攻略，体会江南古城千年风雅人文", "url": "https://www.youxiake.com/gonglue/view?id=4558", "snippet": "苏州三天两晚深度旅行攻略"},
        {"title": "2026苏州旅游攻略,4月苏州自助游/自驾/出游/自由行/游玩攻略", "url": "https://you.ctrip.com/place/suzhou11.html", "snippet": "2026苏州旅游攻略，苏州自助游攻略"}
    ],
    "updated": "2026年4月3日"
}

search_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
try:
    with open(search_path, 'r', encoding='utf-8') as f:
        existing = json.load(f)
    existing.update(search_data)
    search_data = existing
except Exception as e:
    print(f'Could not load existing search data: {e}')

with open(search_path, 'w', encoding='utf-8') as f:
    json.dump(search_data, f, ensure_ascii=False, indent=2)
print('Search results updated with Suzhou data!')

# Read index.html
index_path = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check if Day 46 already exists
if '第46天' in content:
    print('Day 46 already exists!')
    sys.exit(0)

# Day 46 content
day_46 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第46天</span>
                    <span class="day-date">2026-04-03 · 三月十七</span>
                </div>
                <div class="day-title">🚗 扬州 → 苏州 · 出发！</div>
                <div class="day-content">
                    <p>🌅 告别扬州！今天踏上前往苏州的旅程！</p>
                    <p>🚗 上午退房，收拾行李，从扬州出发沿高速前往苏州</p>
                    <p>全程约100公里，约1.5小时车程，一路江南水乡风光</p>
                    <p>🏯 中午抵达苏州，先去观前街品尝苏州地道美食</p>
                    <p>🍜 苏州美食：松鼠桂鱼、碧螺虾仁、清炒虾仁、苏式汤面</p>
                    <p>🛤️ 下午漫步平江路——保存最完整的苏州古街</p>
                    <p>🏠 平江路：800米长的历史街区，小桥流水人家，免费开放</p>
                    <p>🎋 两旁的评弹茶馆、竹编店、丝绸店，充满苏州风情</p>
                    <p>🌙 晚上在金鸡湖畔看夜景，摩天轮灯光秀璀璨</p>
                    <p>📊 今日行程：扬州→苏州高速100km + 观前街/平江路/金鸡湖，步行约8公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🚗</div>
                    <div class="photo-placeholder">🛤️</div>
                    <div class="photo-placeholder">🌙</div>
                </div>
            </div>
'''

# Find Day 45 position and insert Day 46 after it
pattern = r'(<span class="day-number">第45天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_46 + content[insert_pos:]
    
    # Update statistics
    new_content = re.sub(
        r'<div class="stat-value" id="dayCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>',
        new_content
    )
    
    # Update km count (driving ~100km + walking ~8km)
    new_content = re.sub(
        r'<div class="stat-value" id="kmCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 108}</div>',
        new_content
    )
    
    # Update location
    new_content = re.sub(
        r'id="currentLocation">[^<]+',
        'id="currentLocation">苏州 · 金鸡湖',
        new_content
    )
    
    # Update location count (苏州 is a new location)
    new_content = re.sub(
        r'<div class="stat-value" id="locationCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="locationCount">{int(m.group(1)) + 1}</div>',
        new_content
    )
    
    # Update last update time
    new_content = re.sub(
        r'最后更新：\d+年\d+月\d+日',
        '最后更新：2026年4月3日',
        new_content
    )
    
    # Write back
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('\n✅ Successfully added Day 46!')
    print('Day 46: 扬州 → 苏州 · 出发！ (2026-04-03)')
    print('Stats: dayCount 45→46, kmCount +108, locationCount 28→29')
    print('Current location: 苏州 · 金鸡湖')
    print('Last update: 2026年4月3日')
else:
    print('Could not find Day 45 position!')
    sys.exit(1)
