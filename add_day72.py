# -*- coding: utf-8 -*-
"""
环游中国 - Day 72 更新脚本
日期: 2026-04-29 (Day 72 内容：武夷山 · 丹山碧水)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 71
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated dayCount -> 72')

# 2. Update km (~350km from福州到武夷山)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 350) + '<',
    content)
print('Updated kmCount -> ~8353')

# 3. Location count increases by 1
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated locationCount -> 43')

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">南平 · 武夷山<',
    content)
print('Updated currentLocation -> 南平 · 武夷山')

# 5. Day 72 entry
day72_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第72天</span>
                    <span class="day-date">2026-04-29 · 四月初三</span>
                </div>
                <div class="day-title">🏔️ 武夷山 · 丹山碧水</div>
                <div class="day-content">
                    <p>从福州出发，沿京台高速向西，约3.5小时抵达武夷山景区。</p>
                    <p>🛤️ 行驶路线：福州 → 京台高速 → 宁上高速 → 武夷山</p>
                    <p>🏔️ 上午：天游峰——武夷山第一峰</p>
                    <p>⛰️ 天游峰：垂直落差约340米，登顶可俯瞰九曲溪全景</p>
                    <p>🛶 九曲溪：武夷山灵魂，竹筏漂流约1.5小时穿越丹霞地貌</p>
                    <p>🌊 大红袍景区：因一棵300年母树闻名，茶香四溢</p>
                    <p>🍜 午餐：武夷山特色美食</p>
                    <p>🐟 稻花鱼：武夷山特产，清蒸红烧皆宜</p>
                    <p>🍜 岚谷熏鹅：武夷山传统名菜，熏制入味</p>
                    <p>🫖 武夷岩茶：大红袍、肉桂、水仙，茶文化之旅</p>
                    <p>🌿 下午：九曲溪竹筏漂流</p>
                    <p>🛶 竹筏漂流：全程约9.5公里，穿越8座滩涂</p>
                    <p>🏔️ 玉女峰：武夷山标志性景观，三姐妹峰之一</p>
                    <p>🛕 水帘洞：武夷山最大洞穴，瀑布飞流直下</p>
                    <p>📅 明日预告：三清山 · 道教名山</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏔️</div>
                    <div class="photo-placeholder">🛶</div>
                    <div class="photo-placeholder">🍵</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">💡</span>
                        <span class="tip-text">九曲溪竹筏建议早班6:40出发，人少景美，避开人流</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🛶</span>
                        <span class="tip-text">竹筏漂流记得提前预约，门票约225元/人</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🍵</span>
                        <span class="tip-text">武夷山岩茶品鉴推荐去茶农家，更正宗</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day72_entry + '\n' + footer_marker)
print('Added Day 72 entry: 武夷山 · 丹山碧水')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月29日</p>')
    print('Updated footer timestamp to 2026年4月29日')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 72')
print('Location: 武夷山')
print('Date: 2026-04-29')
print('KM added: 350 (total: ~8353)')
print('Location count: 43')
