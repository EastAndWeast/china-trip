# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 64
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 2. Update km (~100km for day trip)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 100) + '<',
    content)

# 3. Update location count (new location: 漳州)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">漳州 · 芗城区<',
    content)

print('Updated stats: Day 65, km +100, location -> 漳州 · 芗城区')

# 5. Day 65 entry
day65_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第65天</span>
                    <span class="day-date">2026-04-22 · 三月廿五</span>
                </div>
                <div class="day-title">🏛️ 集美学村 · 陈嘉庚纪念馆 · 告别厦门</div>
                <div class="day-content">
                    <p>厦门之旅最后一天！上午参访集美学村，下午告别厦门前往漳州。</p>
                    <p>🚄 上午：集美学村——嘉庚建筑群，中西合璧的教育圣地</p>
                    <p>🏛️ 陈嘉庚纪念馆：了解"华侨旗帜、民族光辉"陈嘉庚的传奇一生</p>
                    <p>📜 纪念馆免费开放，周二至周日 9:00-17:00，周一闭馆</p>
                    <p>🎓 集美大学：嘉庚建筑风格的百年学府，校园景色优美</p>
                    <p>🌳 鳌园：陈嘉庚先生陵墓，闽南石雕艺术精华</p>
                    <p>🛤️ 中午：龙舟池畔散步，欣赏学村建筑与湖光山色</p>
                    <p>🍜 午餐：集美学村附近大社沙茶面（地道厦门味道，价格实惠）</p>
                    <p>🚗 下午：驾车约1.5小时（70km）前往漳州古城</p>
                    <p>🛣️ 路线：厦门岛 → 厦门大桥 → 沈海高速 → 漳州出口 → 芗城区</p>
                    <p>🏨 傍晚：入住漳州古城附近酒店，休整后夜游古城</p>
                    <p>🌙 夜游：漳州古城夜景，片仔癀博物馆外立面灯光秀</p>
                    <p>📊 今日行程：集美学村 + 陈嘉庚纪念馆 + 漳州古城</p>
                    <p>🚗 交通：全程约100km，厦门大桥出岛较拥堵，建议16:00前离岛</p>
                    <p>📅 明日预告：漳州古城深度游——文庙、尚书探花府、古城夜景</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏛️</div>
                    <div class="photo-placeholder">🎓</div>
                    <div class="photo-placeholder">🌙</div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day65_entry + '\n' + footer_marker)
print('Added Day 65 entry: 集美学村 · 陈嘉庚纪念馆 · 漳州')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月22日</p>')
    print('Updated footer timestamp to 2026年4月22日')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 65')
print('Location: 漳州 · 芗城区')
print('Date: 2026-04-22')
print('KM added: 100 (total: ~7123)')