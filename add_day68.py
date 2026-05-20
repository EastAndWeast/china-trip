# -*- coding: utf-8 -*-
"""
环游中国 - Day 68 更新脚本
日期: 2026-04-25 (覆盖 Day 68 内容：福州第二天)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 67
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 2. Update km (~250km from 福州 to 泉州)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 250) + '<',
    content)

# 3. Update location count (+1 for new city)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">泉州 · 鲤城区<',
    content)

print('Updated stats: Day 68, km +250, location count +1, location -> 泉州 · 鲤城区')

# 5. Day 68 entry
day68_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第68天</span>
                    <span class="day-date">2026-04-25 · 三月廿八</span>
                </div>
                <div class="day-title">🏯 福州 · 鼓山与马尾船政文化</div>
                <div class="day-content">
                    <p>福州第二天，继续探索这座历史文化名城！</p>
                    <p>🌄 上午：鼓山登山——福州标志性风景区</p>
                    <p>🧗 鼓山登山道：全长约 5 公里，登山时间约 1.5-2 小时</p>
                    <p>🚠 可乘坐鼓山缆车（单程 50 元）直达山顶</p>
                    <p>🏯 山顶涌泉寺：福州最古老的寺庙之一，始建于五代</p>
                    <p>📸 观景台可俯瞰整个福州全景，天气好时能看到闽江入海口</p>
                    <p>🍜 午餐：福州聚春园（闽菜代表，荔枝肉/佛跳墙）</p>
                    <p>⚓ 下午：马尾船政文化之旅</p>
                    <p>📚 马尾船政文化是中国近代海军发源地</p>
                    <p>🔧 船政文化遗址包括：船政衙门、轮机厂、钟楼</p>
                    <p>🏛️ 中国船政文化博物馆（免费，周二至周日 9:00-17:00）</p>
                    <p>🛥️ 马尾：这里是洋务运动的重要历史见证</p>
                    <p>🌆 傍晚：烟台山历史文化街区漫步</p>
                    <p>🏠 烟台山：福州最美老街，汇集了各国领事馆旧址</p>
                    <p>📷 走在百年老建筑群中，仿佛穿越到近代历史</p>
                    <p>🚗 明日行程：前往海上丝绸之路起点——泉州</p>
                    <p>📅 明日预告：开元寺 · 清净寺 · 泉州古城 · 闽南文化</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌄</div>
                    <div class="photo-placeholder">⚓</div>
                    <div class="photo-placeholder">🏠</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">💡</span>
                        <span class="tip-text">鼓山建议清晨出发，8点前到达可避开人流</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🚠</span>
                        <span class="tip-text">不想爬山可乘缆车，建议下午乘车上山看日落</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day68_entry + '\n' + footer_marker)
print('Added Day 68 entry: 福州 · 鼓山与马尾船政文化')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月25日</p>')
    print('Updated footer timestamp to 2026年4月25日')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 68')
print('Location: 泉州 · 鲤城区 (明日)')
print('Date: 2026-04-25')
print('KM added: 250 (total: ~7673)')
print('Location count: 40')