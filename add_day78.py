# -*- coding: utf-8 -*-
"""环游中国 - Day 78 更新脚本
日期: 2026-05-06 (Day 78 内容：九江 · 休整 + 出发武汉)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 77
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated dayCount -> 78')

# 2. Update km (~330km from九江到武汉)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 330) + '<',
    content)
print('Updated kmCount -> 9203 (added 330km)')

# 3. Update location count (+1 武汉)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated locationCount -> 48')

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">武汉 · 江城风光<',
    content)
print('Updated currentLocation -> 武汉 · 江城风光')

# 5. Day 78 entry (2026-05-06)
day78_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第78天</span>
                    <span class="day-date">2026-05-06 · 四月初九</span>
                </div>
                <div class="day-title">🚄 九江 → 武汉 · 江城风光</div>
                <div class="day-content">
                    <p>🚗 清晨从九江出发，沿福银高速向南，约3.5小时抵达武汉。</p>
                    <p>🛤️ 行驶路线：九江 → 福银高速 → 沪渝高速 → 武汉市区</p>
                    <p>🌉 武汉：长江与汉江交汇处，九省通衢</p>
                    <p>🏛️ 黄鹤楼：江南名楼，"昔人已乘黄鹤去，此地空余黄鹤楼"</p>
                    <p>🌸 樱花大道：武汉大学周边，5月虽过樱花季，但校园风景依然</p>
                    <p>🍜 午餐：武汉特色早餐（热干面、糊汤粉）</p>
                    <p>🥟 武汉鸭脖：精武路鸭脖，周黑鸭品牌发源地</p>
                    <p>🦐 武昌鱼：长江武昌鱼，清蒸最佳</p>
                    <p>🌉 长江大桥：万里长江第一桥，钢铁巨龙</p>
                    <p>🌃 晚上：汉正街/江汉路步行街，感受江城夜生活</p>
                    <p>📅 明日预告：武汉 · 东湖 + 湖北省博物馆</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏛️</div>
                    <div class="photo-placeholder">🌉</div>
                    <div class="photo-placeholder">🍜</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🏛️</span>
                        <span class="tip-text">黄鹤楼门票约70元，地铁可直达。推荐傍晚登楼，可欣赏武汉两江四岸灯光秀</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🍜</span>
                        <span class="tip-text">武汉早餐文化丰富，粮道街/吉庆街是本地人最爱的早餐去处，热干面3-5元/碗</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🦐</span>
                        <span class="tip-text">武昌鱼是武汉特产各大酒楼均有，清蒸鱼肉鲜嫩，约68元/份</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day78_entry + '\n' + footer_marker)
print('Added Day 78 entry: 九江 → 武汉 · 江城风光')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年5月6日</p>')
    print('Updated footer timestamp to 2026年5月6日')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 78')
print('Location: 武汉')
print('Date: 2026-05-06 (四月初九)')
print('KM added: 330 (total: ~9203)')
print('Location count: 48')