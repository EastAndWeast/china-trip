# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 66
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 2. Update km (~220km from 漳州 to 福州)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 220) + '<',
    content)

# 3. Update location count (+1 for new city)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">福州 · 鼓楼区<',
    content)

print('Updated stats: Day 67, km +220, location count +1, location -> 福州 · 鼓楼区')

# 5. Day 67 entry
day67_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第67天</span>
                    <span class="day-date">2026-04-24 · 三月廿七</span>
                </div>
                <div class="day-title">🏙️ 福州 · 三坊七巷与闽江夜色</div>
                <div class="day-content">
                    <p>漳州出发，车程约2.5小时，抵达福建省会福州！</p>
                    <p>🛤️ 上午：驱车前往福州，沿着G15沈海高速一路向北</p>
                    <p>🏯 下午：三坊七巷——中国十大历史文化名街之一</p>
                    <p>📜 三坊七巷：始于晋代，成于唐宋，盛于明清</p>
                    <p>是福州的历史之源、文化之根，被誉为"里坊制度活化石"</p>
                    <p>🗼 游览顺序：南后街 → 三坊 → 七巷 → 林则徐纪念馆</p>
                    <p>🍜 午餐：福州鱼丸（连江鱼丸） + 肉燕（燕皮馄饨）</p>
                    <p>🌿 下午：西湖公园——福建省历史最悠久的园林</p>
                    <p>🏛️ 西湖公园：免费开放，始建于晋太康三年（282年）</p>
                    <p>福建省博物馆（免费，周二至周日 9:00-17:00）就在湖畔</p>
                    <p>🌙 傍晚：闽江畔散步，欣赏福州夜景</p>
                    <p>闽江夜游是福州经典项目，两岸灯光璀璨</p>
                    <p>🚗 明日行程：福州继续游览，探访鼓山与马尾</p>
                    <p>📅 明日预告：鼓山登山 · 马尾船政文化 · 烟台山历史文化街区</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">🌿</div>
                    <div class="photo-placeholder">🌙</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">💡</span>
                        <span class="tip-text">三坊七巷免费开放，建议16:00后前往避开人潮</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🅿️</span>
                        <span class="tip-text">停车建议：福州城市规划展示馆停车场（地下）</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day67_entry + '\n' + footer_marker)
print('Added Day 67 entry: 福州 · 三坊七巷与闽江夜色')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月24日</p>')
    print('Updated footer timestamp to 2026年4月24日')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 67')
print('Location: 福州 · 鼓楼区')
print('Date: 2026-04-24')
print('KM added: 220 (total: ~7423)')
print('Location count: 39')