# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read the index.html file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 50 content - from Shanghai to Wuzhen, experiencing the ancient water town
day_50 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第50天</span>
                    <span class="day-date">2026-04-07 · 三月初十</span>
                </div>
                <div class="day-title">🌾 乌镇 · 江南水乡的春日画卷</div>
                <div class="day-content">
                    <p>🌤️ 清明假期后的第一个工作日，避开人流，独自漫游乌镇</p>
                    <p>🚗 早晨从上海出发，走沪昆高速约120公里，约1.5小时抵达桐乡乌镇</p>
                    <p>🏘️ 乌镇：1300年建镇史，国家5A级景区，首批中国历史文化名镇</p>
                    <p>🌼 4月的乌镇郊外，大片油菜花海正值盛放，金黄一片映衬白墙黛瓦</p>
                    <p>📸 清晨的油菜花田是拍摄春日大片绝佳地点，建议日出或黄昏时分前往</p>
                    <p>🛶 上午游览西栅：乌镇大剧院→木心美术馆→草木本色染坊→喜庆堂</p>
                    <p>🏛️ 木心美术馆：纪念艺术家木心的私人美术馆，建筑本身就是一件艺术品</p>
                    <p>🌉 西栅桥里桥茶楼品茶，俯瞰水道，感受江南水乡的静谧时光</p>
                    <p>🚣 乘坐乌篷船穿行于水巷，体会"船在水中走，人在画中游"的意境</p>
                    <p>🏯 下午游览东栅：原汁原味的水乡生活，百米廊棚下感受市井烟火</p>
                    <p>📮 乌镇邮局寄出一张明信片，将这份江南春色传递给远方的朋友</p>
                    <p>🌆 傍晚的乌镇红灯笼亮起，拍摄古桥与倒影，记录最美的水乡夜景</p>
                    <p>📊 今日行程：乌镇西栅+东栅，车程约250公里，游览约8小时</p>
                    <p>📍 明日计划：从乌镇前往杭州，西湖春色+灵隐寺祈福</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌼</div>
                    <div class="photo-placeholder">🛶</div>
                    <div class="photo-placeholder">🌆</div>
                </div>
            </div>
'''

# Find Day 49 ending pattern - the photo placeholders of Day 49 followed by closing divs
# Day 49 has photo placeholders: 🏯 🌆 🚢
pattern = r'(<span class="day-number">第49天</span>.*?photo-placeholder">🚢</div>\s*</div>\s*</div>\s*)'

match = re.search(pattern, content, re.DOTALL)

if match:
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_50 + content[insert_pos:]
    print(f'Found Day 49 at position {insert_pos}')
    
    # Update day count: 49 -> 50
    new_content = re.sub(
        r'id="dayCount">(\d+)</div>',
        lambda m: f'id="dayCount">{int(m.group(1)) + 1}</div>',
        new_content
    )
    
    # Update km count: estimate +250km
    new_content = re.sub(
        r'id="kmCount">(\d+)</div>',
        lambda m: f'id="kmCount">{int(m.group(1)) + 250}</div>',
        new_content
    )
    
    # Update location count: 30 -> 31 (Wuzhen is new location)
    new_content = re.sub(
        r'id="locationCount">(\d+)</div>',
        lambda m: f'id="locationCount">{int(m.group(1)) + 1}</div>',
        new_content
    )
    
    # Update current location
    new_content = re.sub(
        r'id="currentLocation">([^<]+)</strong>',
        'id="currentLocation">乌镇 · 西栅</strong>',
        new_content
    )
    
    # Update last updated date
    new_content = re.sub(
        r'最后更新：\d+年\d+月\d+日',
        '最后更新：2026年4月7日',
        new_content
    )
    
    # Write back
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully updated index.html with Day 50!')
    print('Day count: 49 -> 50')
    print('km count: +250km (4964 -> 5214)')
    print('Location count: 30 -> 31')
    print('Current location: 乌镇 · 西栅')
else:
    print('Could not find Day 49 position!')
    print('Trying alternative patterns...')
    
    # Try simpler pattern
    alt_pattern = r'(第49天.*?photo-placeholder">🚢</div>\s*</div>\s*)'
    match2 = re.search(alt_pattern, content, re.DOTALL)
    if match2:
        print(f'Found Day 49 (alt) at position {match2.end()}')
    else:
        print('Alternative pattern not found either')
