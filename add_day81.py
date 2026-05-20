# -*- coding: utf-8 -*-
"""环游中国 - Day 81 更新脚本
日期: 2026-05-09 (Day 81 内容：长沙出发 → 南昌)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 80
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated dayCount -> 81')

# 2. Update km (长沙到南昌约350km)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 350) + '<',
    content)
print('Updated kmCount -> 10153 (added 350km)')

# 3. Update location count (+1 南昌)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated locationCount -> 50')

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">南昌 · 赣江之都<',
    content)
print('Updated currentLocation -> 南昌 · 赣江之都')

# 5. Day 81 entry (2026-05-09)
day81_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第81天</span>
                    <span class="day-date">2026-05-09 · 四月十二 · 周六</span>
                </div>
                <div class="day-title">🚗 长沙 → 南昌 · 赣江之夜</div>
                <div class="day-content">
                    <p>🌅 早晨从长沙出发，沿京港澳高速/沪昆高速，约4小时抵达南昌</p>
                    <p>🛣️ 行驶路线：长沙 → 沪昆高速 → 南昌绕城高速 → 南昌市区</p>
                    <p>🏯 滕王阁：中国三大名楼之一，"落霞与孤鹜齐飞，秋水共长天一色"名篇出处</p>
                    <p>🌉 八一广场：南昌地标，人民军队诞生地，广场音乐喷泉晚间壮观</p>
                    <p>🏞️ 秋水广场：赣江边亚洲最大音乐喷泉，免费观看（晚间19:30/20:30各一场）</p>
                    <p>🦆 南昌美食：瓦罐汤（标配）、南昌拌粉、藜蒿炒腊肉、白糖糕</p>
                    <p>🏛️ 八一起义纪念馆：免费参观，南昌红色旅游必去，需预约</p>
                    <p>🌃 滕王阁夜游：门票略贵但夜景极美，赣江两岸灯光秀</p>
                    <p>🛶 赣江夜游：乘船游览赣江夜景，欣赏滕王阁和红谷滩CBD灯光</p>
                    <p>📅 明日预告：南昌 · 八一起义纪念馆 + 绳金塔美食</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">🌉</div>
                    <div class="photo-placeholder">🦆</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🏯</span>
                        <span class="tip-text">滕王阁门票50元/人（网络购票45元），主楼共9层，登楼俯瞰赣江和南昌城区，建议傍晚去可以看日落和夜景</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🌉</span>
                        <span class="tip-text">秋水广场音乐喷泉免费，最佳观赏时间19:30-20:00，喷泉面积1.8万平方米，亚洲最大之一</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🦆</span>
                        <span class="tip-text">南昌拌粉3-5元/份，瓦罐汤5-8元/盅，是南昌最实惠的本地美食，万寿宫/船山路是美食街</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day81_entry + '\n' + footer_marker)
print('Added Day 81 entry: 长沙 → 南昌 · 赣江之夜')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年5月9日（周六）</p>')
    print('Updated footer timestamp to 2026年5月9日（周六）')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 81')
print('Location: 南昌 · 赣江之都')
print('Date: 2026-05-09 (四月十二 · 周六)')
print('KM added: 350 (total: ~10153)')
print('Location count: 50')
