# -*- coding: utf-8 -*-
"""
环游中国 - Day 75 更新脚本
日期: 2026-05-02 (Day 75 内容：景德镇 · 瓷都之旅)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 74
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated dayCount -> 75')

# 2. Update km (~90km from婺源到景德镇)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 90) + '<',
    content)
print('Updated kmCount -> ~8863')

# 3. Update location count (+1 景德镇)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated locationCount -> 45')

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">景德镇 · 瓷都<',
    content)
print('Updated currentLocation -> 景德镇 · 瓷都')

# 5. Day 75 entry (2026-05-02)
day75_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第75天</span>
                    <span class="day-date">2026-05-02 · 四月初五</span>
                </div>
                <div class="day-title">🏺 景德镇 · 瓷都之旅</div>
                <div class="day-content">
                    <p>🚗 从婺源出发，沿杭长高速向北，约1.5小时抵达景德镇。</p>
                    <p>🛤️ 行驶路线：婺源 → 杭长高速 → 景德镇南互通 → 市区</p>
                    <p>🏺 景德镇：中国瓷都，千年窑火不灭</p>
                    <p>🏛️ 景德镇中国陶瓷博物馆：免费参观，了解景德镇陶瓷史</p>
                    <p>🔥 古窑民俗博览区：AAAAA级景区，观看传统制瓷工艺</p>
                    <p>🧡 陶溪川文创街区：老工厂改造，文艺气息浓厚</p>
                    <p>🍜 午餐：景德镇特色小吃</p>
                    <p>🥢 冷粉：景德镇第一名小吃，拌粉配花生豆</p>
                    <p>🥟 饺子粑：薄皮糯米糍粑，内馅丰富</p>
                    <p>🍖 牛骨粉：牛骨熬汤配米粉，回味无穷</p>
                    <p>🌆 下午：逛陶溪川创意市集，感受瓷都新活力</p>
                    <p>🏠 晚上：住景德镇市区酒店</p>
                    <p>📅 明日预告：庐山 · 匡庐奇秀</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏺</div>
                    <div class="photo-placeholder">🔥</div>
                    <div class="photo-placeholder">🍜</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🎫</span>
                        <span class="tip-text">景德镇中国陶瓷博物馆免费，需预约；古窑民俗博览区门票95元，关注"景德镇文旅"可享优惠</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🛍️</span>
                        <span class="tip-text">陶溪川周五周六有创意市集，适合淘特色陶瓷手工艺品，价格从几十到几百不等</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🅿️</span>
                        <span class="tip-text">自驾进入景德镇市区需注意限行规定，周末和节假日外地车牌不受限</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day75_entry + '\n' + footer_marker)
print('Added Day 75 entry: 景德镇 · 瓷都之旅')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年5月2日</p>')
    print('Updated footer timestamp to 2026年5月2日')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 75')
print('Location: 景德镇')
print('Date: 2026-05-02 (四月初五)')
print('KM added: 90 (total: ~8863)')
print('Location count: 45')