# -*- coding: utf-8 -*-
"""
环游中国 - Day 71 更新脚本
日期: 2026-04-28 (Day 71 内容：福州 · 三坊七巷)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 70
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 2. Update km (~200km from崇武到福州)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 200) + '<',
    content)

# 3. Location count increases by 1 (new location: 福州)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">福州 · 鼓楼区<',
    content)

print('Updated stats: Day 71, km +200, location -> 福州 · 鼓楼区')

# 5. Day 71 entry
day71_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第71天</span>
                    <span class="day-date">2026-04-28 · 四月初二</span>
                </div>
                <div class="day-title">🏛️ 福州 · 有福之州</div>
                <div class="day-content">
                    <p>从崇武出发，沿沈海高速向北，约2.5小时抵达福州。</p>
                    <p>🛤️ 行驶路线：崇武 → 泉州环城高速 → 福厦高速 → 福州</p>
                    <p>🏛️ 上午：三坊七巷——明清古建筑博物馆</p>
                    <p>🛤️ 三坊七巷：起于晋代，完善于唐代，鼎盛于明清</p>
                    <p>🏠 南后街：主街，连接三坊七巷，全长约1公里</p>
                    <p>🛕 衣锦坊：最古老的坊，寓意"衣锦还乡"</p>
                    <p>🏠 文儒坊：因历代文儒聚集而得名</p>
                    <p>🛕 光禄坊：因光禄卿任职过而得名</p>
                    <p>🍜 午餐：福州传统小吃</p>
                    <p>🥧 佛跳墙：闽菜之王，福州名菜</p>
                    <p>🍜 福州鱼丸：鲜嫩Q弹，以鳗鱼、鲨鱼为馅</p>
                    <p>🥮 芋泥：福州甜品代表，香甜软糯</p>
                    <p>🌳 下午：福州城市漫步</p>
                    <p>⛰️ 鼓山：福州标志，登山看夜景</p>
                    <p>🌉 解放大桥：闽江夜景，福州最美</p>
                    <p>🌿 西湖公园：福州最古老的公园，1700年历史</p>
                    <p>📅 明日预告：武夷山 · 丹山碧水</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏛️</div>
                    <div class="photo-placeholder">🥧</div>
                    <div class="photo-placeholder">⛰️</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">💡</span>
                        <span class="tip-text">三坊七巷建议下午4点后游玩，傍晚灯光亮起最美</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🥧</span>
                        <span class="tip-text">佛跳墙推荐"聚春园"，福州最老字号</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">⛰️</span>
                        <span class="tip-text">鼓山可以坐缆车上山，山顶可俯瞰福州全景</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day71_entry + '\n' + footer_marker)
print('Added Day 71 entry: 福州 · 三坊七巷')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月28日</p>')
    print('Updated footer timestamp to 2026年4月28日')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 71')
print('Location: 福州 · 鼓楼区')
print('Date: 2026-04-28')
print('KM added: 200 (total: ~8003)')
print('Location count: 42')
