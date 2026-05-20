# -*- coding: utf-8 -*-
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Read file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 37 content
day_37 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第37天</span>
                    <span class="day-date">2026-03-25 · 三月初八</span>
                </div>
                <div class="day-title">🏯 苏州 · 园林之城的水乡韵味</div>
                <div class="day-content">
                    <p>告别杭州，乘坐高铁前往苏州，这座被誉为"园林之城"的历史文化名城！</p>
                    <p>🚄 交通：从杭州东站乘坐高铁约1小时到达苏州北站，非常方便</p>
                    <p>🏯 下午游览拙政园，这是中国四大名园之一，始建于明代！</p>
                    <p>🌸 拙政园：占地约78亩，以水为中心，山水萦绕，厅榭精美</p>
                    <p>🌺 春季园林繁花似锦，海棠、玉兰、迎春花开正盛</p>
                    <p>傍晚漫步平江路历史街区，感受古城的水乡风情</p>
                    <p>🚶 平江路：保存完好的宋代古城格局，小桥流水，白墙黛瓦</p>
                    <p>🍜 晚餐品尝苏州特色美食：松鼠桂鱼、苏式汤面、蟹壳黄</p>
                    <p>📊 今日行程：拙政园 + 平江路，步行约8公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">🌸</div>
                    <div class="photo-placeholder">🍜</div>
                </div>
            </div>
'''

# Find the last day card position and insert Day 37
# Look for Day 36 which has day-number >第36天<
pattern = r'(<span class="day-number">第36天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_37 + content[insert_pos:]
    
    # Update statistics
    new_content = re.sub(
        r'<div class="stat-value" id="dayCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>',
        new_content
    )
    
    # Update km count (Hangzhou to Suzhou by train ~150km, city walking ~8km)
    new_content = re.sub(
        r'<div class="stat-value" id="kmCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 150}</div>',
        new_content
    )
    
    # Update location count
    new_content = re.sub(
        r'<div class="stat-value" id="locationCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="locationCount">{int(m.group(1)) + 1}</div>',
        new_content
    )
    
    # Update current location
    new_content = new_content.replace(
        'id="currentLocation">杭州 · 灵隐寺',
        'id="currentLocation">苏州 · 拙政园'
    )
    
    # Update last update time
    new_content = re.sub(
        r'最后更新：\d+年\d+月\d+日',
        '最后更新：2026年3月26日',
        new_content
    )
    
    # Write back
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully added Day 37!')
    print('Location: 苏州 · 拙政园')
    print('Stats: dayCount 36->37, kmCount +150')
else:
    print('Could not find Day 36 position!')
    # Try to find any day card
    day_matches = re.findall(r'<span class="day-number">(第\d+天)</span>', content)
    print(f'Found days: {day_matches[-5:] if day_matches else "none"}')
