# -*- coding: utf-8 -*-
"""
环游中国 - Day 76 更新脚本
日期: 2026-05-03 (Day 76 内容：庐山 · 匡庐奇秀)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 75
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated dayCount -> 76')

# 2. Update km (~130km from景德镇到庐山)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 130) + '<',
    content)
print('Updated kmCount -> 8993')

# 3. Update location count (+1 庐山)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated locationCount -> 46')

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">庐山 · 匡庐奇秀<',
    content)
print('Updated currentLocation -> 庐山 · 匡庐奇秀')

# 5. Day 76 entry (2026-05-03)
day76_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第76天</span>
                    <span class="day-date">2026-05-03 · 四月初六</span>
                </div>
                <div class="day-title">🏔️ 庐山 · 匡庐奇秀</div>
                <div class="day-content">
                    <p>🚗 从景德镇出发，沿杭瑞高速向南，约2小时抵达庐山景区。</p>
                    <p>🛤️ 行驶路线：景德镇 → 杭瑞高速 → 庐山大道 → 庐山景区</p>
                    <p>🏔️ 庐山：中国四大名山之一，享有"匡庐奇秀甲天下"美誉</p>
                    <p>🗻 庐山景区：世界地质公园、国家AAAAA级旅游景区</p>
                    <p>🌫️ 如琴湖：形似小提琴，湖光山色，云雾缭绕</p>
                    <p>🏛️ 庐山会议旧址：见证重要历史事件，红色教育基地</p>
                    <p>🌲 花径：白居易赏桃花处，"人间四月芳菲尽，山寺桃花始盛开"</p>
                    <p>🍜 午餐：庐山特色农家菜</p>
                    <p>🥬 石耳炖鸡：庐山特产山珍，滋补养生</p>
                    <p>🥔 庐山土豆：高山土豆，软糯可口</p>
                    <p>🍃 石鱼炒蛋：庐山三石之一，鲜嫩无比</p>
                    <p>🌄 下午：游览仙人洞、御碑亭，感受庐山云海</p>
                    <p>🏠 晚上：住庐山牯岭镇，赏庐山夜色</p>
                    <p>📅 明日预告：九江 · 长江沿岸</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏔️</div>
                    <div class="photo-placeholder">🌫️</div>
                    <div class="photo-placeholder">🍜</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🎫</span>
                        <span class="tip-text">庐山门票160元/人，景区巴士70元/人（必买）；自驾车需停在山脚换乘中心，不能直接开上山</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🧥</span>
                        <span class="tip-text">庐山海拔1474米，山上气温比山下低10度左右，即使5月也建议带外套，云雾天气注意防滑</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🏨</span>
                        <span class="tip-text">庐山牯岭镇住宿选择多，建议住镇上便于游览各景点，节假日需提前订房</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day76_entry + '\n' + footer_marker)
print('Added Day 76 entry: 庐山 · 匡庐奇秀')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年5月4日</p>')
    print('Updated footer timestamp to 2026年5月4日')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 76')
print('Location: 庐山')
print('Date: 2026-05-03 (四月初六)')
print('KM added: 130 (total: ~8993)')
print('Location count: 46')