# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 30 content for March 18, 2026
day_30 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第30天</span>
                    <span class="day-date">2026-03-18 · 二月廿九</span>
                </div>
                <div class="day-title">🏔️ 黄山之巅 · 光明顶日出</div>
                <div class="day-content">
                    <p>今天起了个大早，5点出发前往光明顶看日出！</p>
                    <p>🌅 光明顶：黄山的第二高峰，海拔1860米，是观赏日出的最佳地点</p>
                    <p>清晨5点半抵达光明顶观景台，已经有不少游客在等待了。</p>
                    <p>6点15分左右，太阳从东方缓缓升起，金色的光芒洒在云海之上，美不胜收！</p>
                    <p>🌊 云海：黄山云海素有"五海"之称，今天运气特别好，看到了壮观的云海</p>
                    <p>上午游览了北海景区，观赏了著名的始信峰、梦笔生花等奇松怪石。</p>
                    <p>🌲 北海景区：以北海宾馆周围的松林为核心，是黄山的精华景区</p>
                    <p>下午乘坐玉屏索道下山，游览了玉屏楼、迎客松等景点。</p>
                    <p>🌲 迎客松：黄山的标志性景观，树龄已超过千年</p>
                    <p>傍晚回到汤口镇，泡了温泉放松身心，结束了完美的黄山之行！</p>
                    <p>🍜 晚上品尝了最后一顿徽州美食：黄山双石、石耳炖鸡</p>
                    <p>明天将启程前往宏村，感受徽派古村落的魅力！</p>
                    <p>📊 今日行程：黄山景区一日游，步行约20公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌅</div>
                    <div class="photo-placeholder">🌊</div>
                    <div class="photo-placeholder">🌲</div>
                </div>
            </div>
'''

# Find Day 29 position and insert Day 30 after it
pattern = r'(<span class="day-number">第29天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    # Insert Day 30 after Day 29
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_30 + content[insert_pos:]
    
    # Update stats
    # Update day count
    new_content = re.sub(r'<div class="stat-value" id="dayCount">(\d+)</div>', 
                        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>', 
                        new_content)
    
    # Update km count (add ~20km for hiking)
    new_content = re.sub(r'<div class="stat-value" id="kmCount">(\d+)</div>', 
                        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 20}</div>', 
                        new_content)
    
    # Update travel tips
    tips_content = '''<div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年3月安徽旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏔️ 黄山：春季云海较多，建议提前关注天气预报，穿好防滑鞋</li>
                    <li>🌅 看日出：光明顶是最佳观赏点，需早起排队占位置，建议4:30到达</li>
                    <li>🚠 索道：云谷寺/玉屏索道上山，建议提前在官网购票</li>
                    <li>🏔️ 黄山四绝：奇松、怪石、云海、温泉，各有特色</li>
                    <li>🍜 徽州美食：毛豆腐、臭鳜鱼、黄山炖鸽、徽州石鸡</li>
                    <li>🏘️ 宏村西递：黄山附近的徽派古村落，世界文化遗产</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年3月18日</p>
            </div>'''
    
    # Replace old tips
    old_tips_pattern = r'<div style="margin-top: 20px; padding: 15px; background: rgba\(255,255,255,0\.1\); border-radius: 10px; text-align: left;">.*?</div>\s*</div>\s*</div>\s*</div>\s*</body>'
    new_content = re.sub(old_tips_pattern, tips_content + '\n        </div>\n    </div>\n</body>', new_content, re.DOTALL)
    
    # Write back to file
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully updated index.html with Day 30!')
    print('Updated stats: dayCount +1 (29->30), kmCount +20 (3435->3455)')
    print('Travel tips updated to March 18, 2026')
else:
    print('Could not find Day 29 position!')
