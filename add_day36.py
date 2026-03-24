# -*- coding: utf-8 -*-
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Read file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 36 content
day_36 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第36天</span>
                    <span class="day-date">2026-03-24 · 三月初七</span>
                </div>
                <div class="day-title">🌸 杭州 · 灵隐寺祈福与龙井问茶</div>
                <div class="day-content">
                    <p>在杭州的第二天，上午前往灵隐寺，这座千年古刹是杭州最著名的佛教寺院！</p>
                    <p>🏯 灵隐寺：始建于东晋年间，距今已有1700多年历史，香火鼎盛</p>
                    <p>🙏 在灵隐寺祈福请愿，感受佛教文化的博大精深</p>
                    <p>🪷 寺内有著名的飞来峰、永福寺等景点，建议预留半天时间</p>
                    <p>下午前往龙井村，这里是西湖龙井茶的发源地！</p>
                    <p>🍵 龙井村：被誉为"茶乡第一村"，盛产西湖龙井茶</p>
                    <p>在茶农家品尝了正宗的明前龙井，茶香四溢，回甘绵长</p>
                    <p>傍晚在西湖边散步，欣赏雷峰塔夜景，结束充实的一天</p>
                    <p>📊 今日行程：灵隐寺 + 龙井村 + 西湖，步行约15公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">🍵</div>
                    <div class="photo-placeholder">🌸</div>
                </div>
            </div>
'''

# Find the last day card position and insert Day 36
# Look for Day 35 which has day-number >第35天<
pattern = r'(<span class="day-number">第35天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_36 + content[insert_pos:]
    
    # Update statistics
    new_content = re.sub(
        r'<div class="stat-value" id="dayCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>',
        new_content
    )
    
    # Update km count (estimate: 0 km - staying in Hangzhou)
    new_content = re.sub(
        r'<div class="stat-value" id="kmCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1))}</div>',
        new_content
    )
    
    # Update current location
    new_content = new_content.replace(
        'id="currentLocation">杭州 · 西湖景区',
        'id="currentLocation">杭州 · 灵隐寺'
    )
    
    # Update last update time
    new_content = re.sub(
        r'最后更新：\d+年\d+月\d+日',
        '最后更新：2026年3月25日',
        new_content
    )
    
    # Write back
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully added Day 36!')
    print('Location: 杭州 · 灵隐寺')
    print('Stats: dayCount 35->36')
else:
    print('Could not find Day 35 position!')
    # Try to find any day card
    day_matches = re.findall(r'<span class="day-number">(第\d+天)</span>', content)
    print(f'Found days: {day_matches[-5:] if day_matches else "none"}')
