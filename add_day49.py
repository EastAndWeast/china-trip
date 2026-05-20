# -*- coding: utf-8 -*-
import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

# Read the index.html file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 49 content - moving from Suzhou to Shanghai, visiting Yuyuan Garden and the Bund
day_49 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第49天</span>
                    <span class="day-date">2026-04-06 · 三月初九</span>
                </div>
                <div class="day-title">🌆 上海 · 豫园与外滩夜色</div>
                <div class="day-content">
                    <p>🌤️ 清明假期最后一天！从苏州出发，驱车约100公里抵达上海</p>
                    <p>🚗 上午从苏州出发，走沪宁高速，约1.5小时抵达上海市区</p>
                    <p>🏯 第一站：豫园 — 上海最著名的古典园林，始建于明代嘉靖年间</p>
                    <p>🏮 豫园与城隍庙相邻，4月的豫园春意盎然，玉兰和海棠正值花期</p>
                    <p>🍜 中午在城隍庙品尝上海特色小吃：南翔小笼包、蟹壳黄、葱油拌面</p>
                    <p>上海老城厢保留了明清风格的街巷，走在其中仿佛穿越回旧时光</p>
                    <p>🌆 下午在外滩漫步，欣赏万国建筑博览群的雄伟与黄浦江的壮阔</p>
                    <p>📸 4月傍晚的外滩光线柔和，是拍摄陆家嘴天际线的最佳时机</p>
                    <p>🌃 夜幕降临，陆家嘴摩天大楼灯光璀璨 — 东方明珠、环球金融中心、上海中心大厦</p>
                    <p>🚢 乘坐浦江游览船，从水上欣赏外滩与浦东的绝美夜景</p>
                    <p>📊 今日行程：上海市区游览，步行约15公里，车程约200公里往返</p>
                    <p>📍 明日计划：从上海前往乌镇或西塘水乡，体验江南水墨风情</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">🌆</div>
                    <div class="photo-placeholder">🚢</div>
                </div>
            </div>
'''

# Find Day 48 position (after its closing tags)
# Pattern: find the end of Day 48's day-card div
pattern = r'(<span class="day-number">第48天</span>.*?photo-placeholder">🍜</div>\s*</div>\s*</div>\s*)'

match = re.search(pattern, content, re.DOTALL)

if match:
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_49 + content[insert_pos:]
    print(f'Found Day 48 at position {insert_pos}')
    
    # Update day count: 48 -> 49
    new_content = re.sub(
        r'id="dayCount">(\d+)</div>',
        lambda m: f'id="dayCount">{int(m.group(1)) + 1}</div>',
        new_content
    )
    
    # Update km count: estimate +200km for day trip
    new_content = re.sub(
        r'id="kmCount">(\d+)</div>',
        lambda m: f'id="kmCount">{int(m.group(1)) + 200}</div>',
        new_content
    )
    
    # Update location count: 29 -> 30 (Shanghai is a new location)
    new_content = re.sub(
        r'id="locationCount">(\d+)</div>',
        lambda m: f'id="locationCount">{int(m.group(1)) + 1}</div>',
        new_content
    )
    
    # Update current location
    new_content = re.sub(
        r'id="currentLocation">([^<]+)</strong>',
        'id="currentLocation">上海 · 外滩</strong>',
        new_content
    )
    
    # Update last updated date
    new_content = re.sub(
        r'最后更新：\d+年\d+月\d+日',
        '最后更新：2026年4月6日',
        new_content
    )
    
    # Write back
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully updated index.html with Day 49!')
    print('Day count: 48 -> 49')
    print('km count: +200km (4764 -> 4964)')
    print('Location count: 29 -> 30')
    print('Current location: 上海 · 外滩')
else:
    print('Could not find Day 48 position!')
    print('Trying alternative pattern...')
    # Alternative: find the last occurrence of Day 48 closing
    alt_pattern = r'(第48天.*?photo-placeholder">🚢</div>\s*</div>\s*)'
    match2 = re.search(alt_pattern, content, re.DOTALL)
    if match2:
        insert_pos = match2.end()
        new_content = content[:insert_pos] + day_49 + content[insert_pos:]
        new_content = re.sub(r'id="dayCount">(\d+)</div>', lambda m: f'id="dayCount">{int(m.group(1)) + 1}</div>', new_content)
        new_content = re.sub(r'id="kmCount">(\d+)</div>', lambda m: f'id="kmCount">{int(m.group(1)) + 200}</div>', new_content)
        new_content = re.sub(r'id="locationCount">(\d+)</div>', lambda m: f'id="locationCount">{int(m.group(1)) + 1}</div>', new_content)
        new_content = re.sub(r'id="currentLocation">([^<]+)</strong>', 'id="currentLocation">上海 · 外滩</strong>', new_content)
        new_content = re.sub(r'最后更新：\d+年\d+月\d+日', '最后更新：2026年4月6日', new_content)
        with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('Updated using alternative pattern!')
    else:
        print('Could not find insertion point. Trying to find Day 47...')
        # Find Day 47 position
        day47_pattern = r'(<span class="day-number">第47天</span>.*?</div>\s*</div>\s*</div>\s*)'
        match3 = re.search(day47_pattern, content, re.DOTALL)
        if match3:
            print(f'Found Day 47 at position {match3.end()}')
            # Insert after Day 47 instead
            insert_pos = match3.end()
            new_content = content[:insert_pos] + day_49 + content[insert_pos:]
            new_content = re.sub(r'id="dayCount">(\d+)</div>', lambda m: f'id="dayCount">{int(m.group(1)) + 1}</div>', new_content)
            new_content = re.sub(r'id="kmCount">(\d+)</div>', lambda m: f'id="kmCount">{int(m.group(1)) + 200}</div>', new_content)
            new_content = re.sub(r'id="locationCount">(\d+)</div>', lambda m: f'id="locationCount">{int(m.group(1)) + 1}</div>', new_content)
            new_content = re.sub(r'id="currentLocation">([^<]+)</strong>', 'id="currentLocation">上海 · 外滩</strong>', new_content)
            new_content = re.sub(r'最后更新：\d+年\d+月\d+日', '最后更新：2026年4月6日', new_content)
            with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print('Updated after Day 47!')
        else:
            print('Could not find any insertion point. Manual intervention needed.')
