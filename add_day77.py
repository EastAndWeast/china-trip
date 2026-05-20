# -*- coding: utf-8 -*-
"""
环游中国 - Day 77 更新脚本
日期: 2026-05-04 (Day 77 内容：九江 · 长江沿岸)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 76
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated dayCount -> 77')

# 2. Update km (~80km from庐山到九江)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 80) + '<',
    content)
print('Updated kmCount -> 9073')

# 3. Update location count (+1 九江)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated locationCount -> 47')

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">九江 · 长江沿岸<',
    content)
print('Updated currentLocation -> 九江 · 长江沿岸')

# 5. Day 77 entry (2026-05-04)
day77_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第77天</span>
                    <span class="day-date">2026-05-04 · 四月初七</span>
                </div>
                <div class="day-title">🌉 九江 · 长江沿岸</div>
                <div class="day-content">
                    <p>🚗 从庐山出发，沿福银高速向东北，约1.5小时抵达九江市区。</p>
                    <p>🛤️ 行驶路线：庐山 → 福银高速 → 九江长江大桥 → 九江市区</p>
                    <p>🌉 九江：长江与鄱阳湖交汇处，江南鱼米之乡</p>
                    <p>🏛️ 浔阳楼：江南名楼，"落霞与孤鹜齐飞，秋水共长天一色"</p>
                    <p>🌊 长江沿岸：欣赏长江壮阔，远处可见庐山轮廓</p>
                    <p>🦐 午餐：九江特色江鲜</p>
                    <p>🥟 浔阳楼特色菜：特色鱼宴、回鱼两吃</p>
                    <p>🧂 鄱阳湖螃蟹：湖区特产，肥美鲜嫩</p>
                    <p>🍜 庐山云雾茶：高山云雾茶，回味悠长</p>
                    <p>🌄 下午：沿长江大堤漫步，感受江南水乡风情</p>
                    <p>🏠 晚上：九江市区住宿，品尝当地夜宵</p>
                    <p>📅 明日预告：武汉 · 江城风光</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌉</div>
                    <div class="photo-placeholder">🌊</div>
                    <div class="photo-placeholder">🦐</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🚢</span>
                        <span class="tip-text">九江是长江重要的港口城市，可乘坐渡轮游览长江风光，欣赏庐山与长江的壮丽景色</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🦀</span>
                        <span class="tip-text">鄱阳湖螃蟹是九江特产，5月正是吃蟹的好时节，清蒸最为鲜美</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🏛️</span>
                        <span class="tip-text">浔阳楼门票约40元，是九江标志性建筑，登楼可俯瞰长江与市区全景</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day77_entry + '\n' + footer_marker)
print('Added Day 77 entry: 九江 · 长江沿岸')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年5月5日</p>')
    print('Updated footer timestamp to 2026年5月5日')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 77')
print('Location: 九江')
print('Date: 2026-05-04 (四月初七)')
print('KM added: 80 (total: ~9073)')
print('Location count: 47')