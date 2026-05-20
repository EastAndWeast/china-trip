# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read the file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 38 content - Suzhou continued exploration
day_38 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第38天</span>
                    <span class="day-date">2026-03-26 · 三月初九</span>
                </div>
                <div class="day-title">🏯 苏州 · 留园与虎丘</div>
                <div class="day-content">
                    <p>在苏州的第二天！今天继续探索苏州古典园林的精华。</p>
                    <p>🌸 上午游览留园，这是中国四大名园之一，以建筑艺术见长！</p>
                    <p>🏯 留园：始建于明代，全园占地约30余亩，分为东、中、西、北四部分</p>
                    <p>留园的假山、池水、花木与建筑完美融合，一步一景，令人陶醉。</p>
                    <p>🍜 中午在观前街品尝了苏州特色美食：生煎包、桂花糕、苏式汤面</p>
                    <p>🗼 下午前往虎丘，这是"吴中第一名胜"，云岩寺塔是世界第二斜塔！</p>
                    <p>虎丘剑池相传为吴王阖闾藏剑之处，虎丘塔更是苏州的城市标志。</p>
                    <p>🌙 傍晚漫步山塘街，感受"最是红尘中一二等富贵风流之地"的古街氛围</p>
                    <p>📊 今日行程：留园 + 虎丘 + 山塘街，步行约12公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">🗼</div>
                    <div class="photo-placeholder">🌙</div>
                </div>
            </div>
'''

# Day 39 content - Heading to Yangzhou
day_39 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第39天</span>
                    <span class="day-date">2026-03-27 · 三月初十</span>
                </div>
                <div class="day-title">🌸 苏州 → 扬州 · 烟花三月下扬州</div>
                <div class="day-content">
                    <p>告别苏州，乘坐高铁前往扬州！"烟花三月下扬州"，正是好时节！</p>
                    <p>🚄 交通：从苏州北站乘坐高铁约1.5小时到达扬州东站</p>
                    <p>🌸 下午抵达扬州后直奔瘦西湖，这是扬州最著名的景区！</p>
                    <p>🏞️ 瘦西湖：全长约4.5公里，因湖面瘦长得名，有"园林之盛，甲于天下"之誉</p>
                    <p>春天的瘦西湖杨柳依依，桃花盛开，二十四桥、五亭桥倒映在碧波之上。</p>
                    <p>🚶 傍晚漫步东关街，这是扬州最具代表性的历史老街！</p>
                    <p>🍜 晚餐品尝扬州特色美食：扬州炒饭、大煮干丝、狮子头、盐水鹅</p>
                    <p>🍵 晚上体验了扬州"皮包水"文化——泡澡堂、喝早茶</p>
                    <p>📊 今日行程：苏州到扬州高铁 + 瘦西湖 + 东关街，步行约8公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌸</div>
                    <div class="photo-placeholder">🏞️</div>
                    <div class="photo-placeholder">🍜</div>
                </div>
            </div>
'''

# Find Day 37 position (after the day-card closing divs) and insert days 38 and 39
# Day 37 ends with 3 closing divs: </div>\n            </div>\n            <div class="day-card">
pattern = r'(<span class="day-number">第37天</span>.*?</div>\s*</div>\s*</div>\s*<div class="day-card">)'

# Actually let's find the end of Day 37 content and insert after
# Day 37 card ends with: </div>\n                </div>\n            </div>\n\n<div class="day-card">
# But before Day 20

# Let's use a different approach - find Day 20 and insert before it (since days are in reverse order)
# Actually, looking at the structure, days are listed newest first (Day 37 before Day 20)
# So we need to insert between Day 37 and Day 20

# The pattern for Day 37 ending
match = re.search(r'(<span class="day-number">第37天</span>.*?</div>\s*</div>\s*</div>\s*)', content, re.DOTALL)

if match:
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_38 + day_39 + content[insert_pos:]
    
    # Update stats - increase day count from 37 to 39
    new_content = re.sub(
        r'<div class="stat-value" id="dayCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 2}</div>',
        new_content
    )
    
    # Update km count (estimate: Suzhou to Yangzhou ~150km高铁 + walking)
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
        'id="currentLocation">苏州 · 拙政园',
        'id="currentLocation">扬州 · 瘦西湖'
    )
    
    # Update last update time
    new_content = re.sub(
        r'最后更新：\d+年\d+月\d+日',
        '最后更新：2026年3月27日',
        new_content
    )
    
    # Write back
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully added Day 38 and Day 39!')
    print('Day 38: 苏州 · 留园与虎丘 (2026-03-26)')
    print('Day 39: 苏州 → 扬州 · 烟花三月下扬州 (2026-03-27)')
    print('Updated stats: dayCount +2, kmCount +150, locationCount +1')
    print('Current location: 扬州 · 瘦西湖')
else:
    print('Could not find Day 37 position!')
    print('Trying alternative pattern...')
    # Try to find the end of Day 37 another way
    match2 = re.search(r'(第37天.*?photo-placeholder">🌸</div>\s*</div>\s*</div>\s*)', content, re.DOTALL)
    if match2:
        print(f'Found alternative pattern at position {match2.end()}')
    else:
        print('Still could not find!')
