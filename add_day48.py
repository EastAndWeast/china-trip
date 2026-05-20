# -*- coding: utf-8 -*-
import re
import sys
import json
from datetime import datetime, timedelta

sys.stdout.reconfigure(encoding='utf-8')

# Read the index.html file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 48 content - continuing Suzhou, visiting 拙政园 and preparing to head to Shanghai
day_48 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第48天</span>
                    <span class="day-date">2026-04-05 · 三月初八</span>
                </div>
                <div class="day-title">🌸 苏州 · 拙政园与平江路美食</div>
                <div class="day-content">
                    <p>🌸 清明假期第二天！苏州天气晴好，游客比平日多了不少。</p>
                    <p>🏛️ 拙政园：早晨六点半入园，避开了人流高峰</p>
                    <p>拙政园始建于明正德年间，是中国四大名园之首，占地约78亩</p>
                    <p>🌺 4月的拙政园最美！玉兰、海棠、樱花竞相绽放，倒影与亭台楼阁相映成趣</p>
                    <p>📸 拍摄了经典的"与谁同坐轩"景点，倚栏听风，太惬意了</p>
                    <p>🍜 中午在平江路品尝了苏州特色美食：松鼠桂鱼、苏式汤面、桂花糕</p>
                    <p>平江路的桃花开了，粉白相间，走在古街上仿佛穿越回了旧时光</p>
                    <p>🚗 下午在观前街采购了一些苏州特产：碧螺春茶叶、丝绸围巾</p>
                    <p>📊 今日行程：在苏州市区游览，步行约12公里</p>
                    <p>📍 明日计划：启程前往上海，游览外滩与豫园</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌺</div>
                    <div class="photo-placeholder">🏛️</div>
                    <div class="photo-placeholder">🍜</div>
                </div>
            </div>
'''

# Find Day 47 position and insert Day 48 after it
# Use a pattern to find Day 47's closing div
pattern = r'(<span class="day-number">第47天</span>.*?</div>\s*</div>\s*</div>\s*)'

match = re.search(pattern, content, re.DOTALL)

if match:
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_48 + content[insert_pos:]
    
    # Update day count
    new_content = re.sub(
        r'<div class="stat-value" id="dayCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>',
        new_content
    )
    
    # Update km count (estimate +120km for day trip)
    new_content = re.sub(
        r'<div class="stat-value" id="kmCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 120}</div>',
        new_content
    )
    
    # Update location count if new location
    new_content = re.sub(
        r'<div class="stat-value" id="locationCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="locationCount">{int(m.group(1))}</div>',
        new_content
    )
    
    # Update current location
    new_content = re.sub(
        r'id="currentLocation">([^<]+)</strong>',
        'id="currentLocation">苏州 · 拙政园</strong>',
        new_content
    )
    
    # Update last updated date
    new_content = re.sub(
        r'最后更新：\d+年\d+月\d+日',
        '最后更新：2026年4月5日',
        new_content
    )
    
    # Write back
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully updated index.html with Day 48!')
    print('Day count: 47 -> 48')
    print('km count: +120km')
    print('Current location: 苏州 · 拙政园')
else:
    print('Could not find Day 47 position!')
    print('Trying alternative pattern...')
    # Try another pattern
    alt_pattern = r'(第47天.*?photo-placeholder.*?</div>\s*</div>\s*)'
    match2 = re.search(alt_pattern, content, re.DOTALL)
    if match2:
        insert_pos = match2.end()
        new_content = content[:insert_pos] + day_48 + content[insert_pos:]
        new_content = re.sub(r'id="dayCount">(\d+)</div>', lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>', new_content)
        new_content = re.sub(r'id="kmCount">(\d+)</div>', lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 120}</div>', new_content)
        with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('Updated using alternative pattern!')
    else:
        print('Could not find insertion point. Manual intervention needed.')
