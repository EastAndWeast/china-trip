# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 29 content for March 17, 2026
day_29 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第29天</span>
                    <span class="day-date">2026-03-17 · 二月廿八</span>
                </div>
                <div class="day-title">🏔️ 启程黄山 · 五岳归来不看山</div>
                <div class="day-content">
                    <p>今天从婺源出发，前往中国最著名的山脉——黄山！"五岳归来不看山，黄山归来不看岳"。</p>
                    <p>🏔️ 黄山：世界文化与自然双重遗产，以奇松、怪石、云海、温泉著称</p>
                    <p>上午驱车约150公里，从婺源到黄山风景区，沿途欣赏皖南山水风光。</p>
                    <p>🏨 下午抵达黄山脚下，入住汤口镇特色民宿，为明天登山做准备。</p>
                    <p>下午在黄山景区周边游览，参观翡翠谷、九龙瀑等景点。</p>
                    <p>🌊 翡翠谷：又称"情人谷"，溪水清澈见底，潭潭相连</p>
                    <p>🍜 晚上品尝了黄山特色美食：黄山炖鸽、徽州毛豆腐、臭鳜鱼</p>
                    <p>今晚早点休息，明早5点出发乘坐云谷寺索道上山，欣赏日出云海！</p>
                    <p>📊 今日行程：从婺源到黄山，约150公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏔️</div>
                    <div class="photo-placeholder">🌅</div>
                    <div class="photo-placeholder">🍜</div>
                </div>
            </div>
'''

# Find Day 28 position and insert Day 29 after it
pattern = r'(<span class="day-number">第28天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    # Insert Day 29 after Day 28
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_29 + content[insert_pos:]
    
    # Update stats
    # Update day count
    new_content = re.sub(r'<div class="stat-value" id="dayCount">(\d+)</div>', 
                        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>', 
                        new_content)
    
    # Update km count (add ~150km for today)
    new_content = re.sub(r'<div class="stat-value" id="kmCount">(\d+)</div>', 
                        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 150}</div>', 
                        new_content)
    
    # Update location count (add 1 for 黄山)
    new_content = re.sub(r'<div class="stat-value" id="locationCount">(\d+)</div>', 
                        lambda m: f'<div class="stat-value" id="locationCount">{int(m.group(1)) + 1}</div>', 
                        new_content)
    
    # Update current location
    new_content = new_content.replace(
        'id="currentLocation">婺源 · 李坑',
        'id="currentLocation">黄山 · 汤口镇'
    )
    
    # Update travel tips
    tips_content = '''<div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年3月安徽旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏔️ 黄山：春季云海较多，建议提前关注天气预报，穿好防滑鞋</li>
                    <li>🌅 看日出：光明顶是最佳观赏点，需早起排队占位置</li>
                    <li>🚠 索道：云谷寺/玉屏索道上山，建议提前购票</li>
                    <li>🏔️ 黄山四绝：奇松、怪石、云海、温泉，各有特色</li>
                    <li>🍜 徽州美食：毛豆腐、臭鳜鱼、黄山炖鸽、徽州石鸡</li>
                    <li>🏘️ 宏村西递：黄山附近的徽派古村落，世界文化遗产</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年3月17日</p>
            </div>'''
    
    # Replace old tips
    old_tips_pattern = r'<div style="margin-top: 20px; padding: 15px; background: rgba\(255,255,255,0\.1\); border-radius: 10px; text-align: left;">.*?</div>\s*</div>\s*</div>\s*</div>\s*</body>'
    new_content = re.sub(old_tips_pattern, tips_content + '\n        </div>\n    </div>\n</body>', new_content, re.DOTALL)
    
    # Write back to file
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully updated index.html with Day 29!')
    print('Updated stats: dayCount +1 (28->29), kmCount +150 (3285->3435)')
    print('Updated locationCount: 19->20')
    print('Current location changed to: 黄山 · 汤口镇')
    print('Travel tips updated to March 17, 2026')
else:
    print('Could not find Day 28 position!')
