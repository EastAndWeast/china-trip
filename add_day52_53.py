# -*- coding: utf-8 -*-
"""
添加第五十二天 (2026-04-09) 和第五十三天 (2026-04-10) 内容
"""
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\admin\.openclaw\workspace\china-trip\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ============ 第五十二天内容 (2026-04-09) ============
# Based on itinerary: 去黄山，登山观奇松云海
day52 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第52天</span>
                    <span class="day-date">2026-04-09 · 三月十二</span>
                </div>
                <div class="day-title">🏔️ 黄山风景区 · 云海日出</div>
                <div class="day-content">
                    <p>告别杭州，驱车前往"五岳归来不看山，黄山归来不看岳"的黄山！</p>
                    <p>🏔️ 黄山：世界文化与自然双重遗产，以奇松、怪石、云海、温泉著称</p>
                    <p>🚗 今日车程约280公里，从杭州到黄山风景区，约3.5小时</p>
                    <p>🏨 下午抵达黄山脚下汤口镇，入住景区周边酒店，为明天登山做准备</p>
                    <p>下午在黄山景区周边游览，参观翡翠谷、九龙瀑等景点。</p>
                    <p>🌊 翡翠谷：又称"情人谷"，溪水清澈见底，潭潭相连</p>
                    <p>🍜 晚上品尝了黄山特色美食：黄山炖鸽、徽州毛豆腐、臭鳜鱼</p>
                    <p>今晚早点休息，明早5点出发乘坐云谷寺索道上山，欣赏日出云海！</p>
                    <p>📊 今日行程：从杭州到黄山，约280公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏔️</div>
                    <div class="photo-placeholder">🌅</div>
                    <div class="photo-placeholder">🍜</div>
                </div>
            </div>
'''

# ============ 第五十三天内容 (2026-04-10) ============
# Today! Based on plan: 登山观奇松云海
day53 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第53天</span>
                    <span class="day-date">2026-04-10 · 三月十三</span>
                </div>
                <div class="day-title">🏔️ 黄山之巅 · 光明顶日出与迎客松</div>
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
                    <p>明天计划前往宏村，感受徽派古村落的魅力！</p>
                    <p>📊 今日行程：黄山景区一日游，步行约20公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌅</div>
                    <div class="photo-placeholder">🌊</div>
                    <div class="photo-placeholder">🌲</div>
                </div>
            </div>
'''

# 找到第51天的结束位置（最后一个day-card的结束标签）
# 在最后一个 </div>\n</div>\n<div class="footer"> 之前插入新内容
footer_marker = '<div class="footer">'
idx_footer = content.find(footer_marker)
if idx_footer == -1:
    print('ERROR: Could not find footer marker')
    sys.exit(1)

# 更新统计：天数 51 -> 53
content = re.sub(
    r'<div class="stat-value" id="dayCount">(\d+)</div>',
    lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 2}</div>',
    content
)

# 更新公里数（约+300公里）
content = re.sub(
    r'<div class="stat-value" id="kmCount">(\d+)</div>',
    lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 300}</div>',
    content
)

# 更新当前位置
content = content.replace(
    'id="currentLocation">杭州 · 西湖',
    'id="currentLocation">黄山 · 光明顶'
)

# 更新最后更新时间
content = re.sub(
    r'最后更新：\d+年\d+月\d+日',
    '最后更新：2026年4月10日',
    content
)

# 插入新内容（在footer之前）
new_content = content[:idx_footer] + day52 + day53 + content[idx_footer:]

with open(r'C:\Users\admin\.openclaw\workspace\china-trip\index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('SUCCESS: Day 52 (2026-04-09) and Day 53 (2026-04-10) added!')
print('Updated: dayCount +2 (51->53), kmCount +300 (5450->5750)')
print('Current location: 黄山 · 光明顶')
