# -*- coding: utf-8 -*-
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Read file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 40 content - Yangzhou continued exploration
day_40 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第40天</span>
                    <span class="day-date">2026-03-28 · 三月十一</span>
                </div>
                <div class="day-title">🏯 扬州 · 个园与大明寺</div>
                <div class="day-content">
                    <p>扬州第三天！继续探索这座"淮左名都"的历史与文化！</p>
                    <p>🌿 上午游览个园，这是中国四大名园之一，以竹石见长！</p>
                    <p>🎋 个园：建于清代嘉庆年间，因园中多竹而得名，有"城市山林"之誉</p>
                    <p>个园的四季假山尤为著名，用不同石料营造出春夏秋冬四季景色。</p>
                    <p>🏛️ 下午前往大明寺，这座千年古刹是扬州最著名的寺庙！</p>
                    <p>🗼 大明寺：始建于南朝宋孝武帝年间，栖灵塔高耸入云</p>
                    <p>登塔远眺，扬州城尽收眼底，瘦西湖隐约可见！</p>
                    <p>🍜 午餐品尝扬州早茶：翡翠烧麦、蟹黄包、千层糕</p>
                    <p>☕ 扬州是中国四大菜系之一——淮扬菜的发源地</p>
                    <p>🌙 傍晚在南河下历史文化街区漫步，感受老扬州的市井生活</p>
                    <p>📊 今日行程：个园 + 大明寺 + 南河下，步行约10公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">🌿</div>
                    <div class="photo-placeholder">🌙</div>
                </div>
            </div>
'''

# Find Day 39 position and insert Day 40 after it
pattern = r'(<span class="day-number">第39天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_40 + content[insert_pos:]
    
    # Update statistics
    new_content = re.sub(
        r'<div class="stat-value" id="dayCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>',
        new_content
    )
    
    # Update km count (Yangzhou city walking ~10km, minimal travel)
    new_content = re.sub(
        r'<div class="stat-value" id="kmCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 10}</div>',
        new_content
    )
    
    # Update location count (staying in Yangzhou, no new location)
    # Skip location count update - still in Yangzhou
    
    # Update current location (still in Yangzhou, now 个园)
    new_content = new_content.replace(
        'id="currentLocation">扬州 · 瘦西湖',
        'id="currentLocation">扬州 · 个园'
    )
    
    # Update last update time
    new_content = re.sub(
        r'最后更新：\d+年\d+月\d+日',
        '最后更新：2026年3月28日',
        new_content
    )
    
    # Write back
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully added Day 40!')
    print('Day 40: 扬州 · 个园与大明寺 (2026-03-28)')
    print('Stats: dayCount +1, kmCount +10')
    print('Current location: 扬州 · 个园')
else:
    print('Could not find Day 39 position!')
    day_matches = re.findall(r'<span class="day-number">(第\d+天)</span>', content)
    print(f'Found days: {day_matches[-5:] if day_matches else "none"}')
