# -*- coding: utf-8 -*-
"""
环游中国 - Day 70 更新脚本
日期: 2026-04-27 (Day 70 内容：崇武古城 · 惠安女文化)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 69
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 2. Update km (~80km from泉州到崇武)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 80) + '<',
    content)

# 3. Location count increases by 1 (new location: 崇武)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">泉州 · 惠安县 · 崇武镇<',
    content)

print('Updated stats: Day 70, km +80, location -> 泉州 · 惠安县 · 崇武镇')

# 5. Day 70 entry
day70_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第70天</span>
                    <span class="day-date">2026-04-27 · 四月初一</span>
                </div>
                <div class="day-title">🏰 崇武古城 · 惠安女的传奇</div>
                <div class="day-content">
                    <p>清晨从泉州出发，驱车约50公里抵达崇武镇。</p>
                    <p>🏰 上午：崇武古城——明代海防要塞</p>
                    <p>🏯 崇武古城：建于1387年，600年历史的海防古城</p>
                    <p>🧱 城墙：花岗岩砌筑，周长约2.5公里，保存完好</p>
                    <p>🗿 古城内石雕：200多尊石雕，人物、动物、器物精美</p>
                    <p>🧑‍🦱 抗战历史：崇武是抗战遗址，曾发生"崇武抗战"激烈战斗</p>
                    <p>👩 下午：惠安女文化探访</p>
                    <p>👗 惠安女：福建三大渔女之一，以奇特服饰闻名</p>
                    <p>🪢 惠安女服饰：封建头、民主肚、节约衣、浪费裤</p>
                    <p>🏠 崇武渔港：福建省最大渔港之一，海鲜新鲜便宜</p>
                    <p>🦐 崇武海鲜：正宗野生小鱿鱼、海蛎煎、鱼丸汤</p>
                    <p>🌅 傍晚：崇武海岸线骑行</p>
                    <p>🛤️ 半月湾：崇武最美海滩，半月形沙滩细腻</p>
                    <p>🌊 潮汐花园：海边礁石区，拍照绝佳</p>
                    <p>📅 明日预告：出发前往福州 · 三坊七巷</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏰</div>
                    <div class="photo-placeholder">👗</div>
                    <div class="photo-placeholder">🌅</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">💡</span>
                        <span class="tip-text">惠安女服饰体验可在崇武古城周边村落预约</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🦐</span>
                        <span class="tip-text">崇武渔港下午4点左右渔船回港，海鲜最鲜活</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🛵</span>
                        <span class="tip-text">古城内建议租电动车游览，停车方便</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day70_entry + '\n' + footer_marker)
print('Added Day 70 entry: 崇武古城 · 惠安女文化')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月27日</p>')
    print('Updated footer timestamp to 2026年4月27日')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 70')
print('Location: 泉州 · 惠安县 · 崇武镇')
print('Date: 2026-04-27')
print('KM added: 80 (total: ~7803)')
print('Location count: 41')
