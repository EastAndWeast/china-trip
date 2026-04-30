# -*- coding: utf-8 -*-
"""
环游中国 - Day 73 更新脚本
日期: 2026-04-30 (Day 73 内容：三清山 · 道教仙山)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 72
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated dayCount -> 73')

# 2. Update km (~300km from武夷山到三清山)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 300) + '<',
    content)
print('Updated kmCount -> ~8653')

# 3. Location count increases by 1
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated locationCount -> 44')

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">上饶 · 三清山<',
    content)
print('Updated currentLocation -> 上饶 · 三清山')

# 5. Day 73 entry
day73_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第73天</span>
                    <span class="day-date">2026-04-30 · 四月初四</span>
                </div>
                <div class="day-title">🏔️ 三清山 · 道教仙山</div>
                <div class="day-content">
                    <p>从武夷山出发，沿宁上高速、沪昆高速向北，约3小时抵达三清山景区。</p>
                    <p>🛤️ 行驶路线：武夷山 → 宁上高速 → 沪昆高速 → 三清山</p>
                    <p>🏔️ 三清山：道教名山，有"江南第一仙峰"之誉</p>
                    <p>⛰️ 玉京峰：三清山最高峰，海拔1819.9米</p>
                    <p>🌲 巨蟒出山：三清山标志性景观，垂直高度128米</p>
                    <p>🪨 东方女神：三清山代表景观，天然形成酷似女神</p>
                    <p>🍜 午餐：三清山当地特色美食</p>
                    <p>🥢 清明果：江西特色小吃，艾草糯米制成</p>
                    <p>🐟 粉蒸肉：江西传统名菜，糯软可口</p>
                    <p>🌿 下午：西海岸景区高空栈道漫步</p>
                    <p>🌅 西海岸栈道：全长约4公里，平均海拔1600米</p>
                    <p>🌄 阳光海岸：东海岸高空栈道，看日出日落绝佳</p>
                    <p>📅 明日预告：婺源 · 中国最美乡村</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏔️</div>
                    <div class="photo-placeholder">🌲</div>
                    <div class="photo-placeholder">🍜</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">💡</span>
                        <span class="tip-text">三清山建议住在山上，便于看日出日落，索道下山后游览更轻松</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">⛰️</span>
                        <span class="tip-text">巨蟒出山和东方女神是必打卡景点，拍照最佳位置在对应观景台</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🥾</span>
                        <span class="tip-text">山上步道较多，建议穿防滑鞋，舒适背包，准备雨衣（山区天气多变）</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day73_entry + '\n' + footer_marker)
print('Added Day 73 entry: 三清山 · 道教仙山')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月30日</p>')
    print('Updated footer timestamp to 2026年4月30日')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 73')
print('Location: 三清山')
print('Date: 2026-04-30')
print('KM added: 300 (total: ~8653)')
print('Location count: 44')