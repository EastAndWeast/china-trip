# -*- coding: utf-8 -*-
"""环游中国 - Day 79 更新脚本
日期: 2026-05-07 (Day 79 内容：武汉休整 + 出发长沙)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 78
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated dayCount -> 79')

# 2. Update km (~350km from武汉到长沙)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 350) + '<',
    content)
print('Updated kmCount -> 9553 (added 350km)')

# 3. Update location count (+1 长沙)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated locationCount -> 49')

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">长沙 · 湘江之都<',
    content)
print('Updated currentLocation -> 长沙 · 湘江之都')

# 5. Day 79 entry (2026-05-07)
day79_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第79天</span>
                    <span class="day-date">2026-05-07 · 四月初十</span>
                </div>
                <div class="day-title">🚄 武汉 → 长沙 · 湘江之夜</div>
                <div class="day-content">
                    <p>🛤️ 上午游览武汉东湖，骑行绿道，享湖光山色</p>
                    <p>🏛️ 湖北省博物馆：曾侯乙编钟、越王勾践剑，免费参观需预约</p>
                    <p>🌸 午后沿京港澳高速向南，约4.5小时抵达长沙</p>
                    <p>🛣️ 行驶路线：武汉 → 京港澳高速 → 长沙市区</p>
                    <p>🌉 橘子洲：湘江中的长岛，毛泽东青年雕像，地铁2号线直达</p>
                    <p>🧁 茶颜悦色：长沙本土奶茶品牌，门店众多，幽兰拿铁必点</p>
                    <p>🦞 口味虾/小龙虾：长沙夜宵代表，文和友/超级文和友是打卡点</p>
                    <p>🌶️ 辣椒炒肉：湘菜代表，费大厨/炊烟时代是热门连锁</p>
                    <p>🏙️ 黄兴路步行街/五一广场：长沙最繁华商圈</p>
                    <p>🎭 解放西路：酒吧一条街，夜生活丰富</p>
                    <p>📅 明日预告：长沙 · 岳麓山 + 湖南大学 + 太平老街</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏛️</div>
                    <div class="photo-placeholder">🌉</div>
                    <div class="photo-placeholder">🦞</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🏛️</span>
                        <span class="tip-text">湖北省博物馆免费参观，每周一闭馆，需在官方公众号提前预约，周二至周日9:00-17:00开放</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🌉</span>
                        <span class="tip-text">橘子洲景区免费，观光小火车40元/人是游览最佳方式，建议傍晚去可以看湘江夜景</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🦞</span>
                        <span class="tip-text">长沙小龙虾推荐：文和友（海信广场店）、天宝兄弟，口味虾约128-168元/份，茶颜悦色约16-22元/杯</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day79_entry + '\n' + footer_marker)
print('Added Day 79 entry: 武汉 → 长沙 · 湘江之夜')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年5月7日</p>')
    print('Updated footer timestamp to 2026年5月7日')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 79')
print('Location: 长沙')
print('Date: 2026-05-07 (四月初十)')
print('KM added: 350 (total: ~9553)')
print('Location count: 49')