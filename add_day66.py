# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 65
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 2. Update km (~80km for day trip)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 80) + '<',
    content)

# 3. Update location count (same city, new spots)
# No change to location count

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">漳州 · 芗城区<',
    content)

print('Updated stats: Day 66, km +80, location -> 漳州 · 芗城区')

# 5. Day 66 entry
day66_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第66天</span>
                    <span class="day-date">2026-04-23 · 三月廿六</span>
                </div>
                <div class="day-title">🏯 漳州古城深度游 · 文庙 · 尚书探花府</div>
                <div class="day-content">
                    <p>漳州古城第二天！深度探索闽南文化心脏。</p>
                    <p>🏛️ 上午：漳州文庙——福建省现存最大的文庙建筑群</p>
                    <p>📜 文庙免费开放，祭祀孔子，传承儒家文化</p>
                    <p>🏠 尚书探花府：明清古宅，探花第主人官邸，闽南红砖文化代表</p>
                    <p>🛤️ 香港路步行街：古城商业街，骑楼建筑群，片仔癀发源地</p>
                    <p>🍜 早餐：古城阿芳卤面（漳州特色，来古城必吃）</p>
                    <p>🌿 午餐：老国三角粿（地道漳州小吃，外酥里嫩）</p>
                    <p>📚 下午：漳州博物馆（免费，周二至周日 9:00-17:00）</p>
                    <p>🛁 傍晚：休整，为明天前往福州做准备</p>
                    <p>🚗 明日行程：漳州 → 福州（约220km，预计2.5小时）</p>
                    <p>📅 明日预告：福州三坊七巷 · 西湖公园 · 闽江夜景</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏛️</div>
                    <div class="photo-placeholder">🏠</div>
                    <div class="photo-placeholder">🍜</div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day66_entry + '\n' + footer_marker)
print('Added Day 66 entry: 漳州古城深度游 · 文庙 · 尚书探花府')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月23日</p>')
    print('Updated footer timestamp to 2026年4月23日')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 66')
print('Location: 漳州 · 芗城区')
print('Date: 2026-04-23')
print('KM added: 80 (total: ~7203)')
