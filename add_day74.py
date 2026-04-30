# -*- coding: utf-8 -*-
"""
环游中国 - Day 74 更新脚本
日期: 2026-05-01 (Day 74 内容：婺源 · 中国最美乡村)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 73
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated dayCount -> 74')

# 2. Update km (~120km from三清山到婺源)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 120) + '<',
    content)
print('Updated kmCount -> ~8773')

# 3. Location count stays the same (same region)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 0) + '<',
    content)
print('LocationCount stays -> 44')

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">上饶 · 婺源<',
    content)
print('Updated currentLocation -> 上饶 · 婺源')

# 5. Day 74 entry (2026-05-01, 劳动节)
day74_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第74天</span>
                    <span class="day-date">2026-05-01 · 劳动节</span>
                </div>
                <div class="day-title">🌼 婺源 · 中国最美乡村</div>
                <div class="day-content">
                    <p>从三清山出发，沿德上高速向南，约1.5小时抵达婺源。</p>
                    <p>🛤️ 行驶路线：三清山 → 德上高速 → 杭长高速 → 婺源</p>
                    <p>🌸 婺源：被誉为"中国最美乡村"，春季油菜花海闻名</p>
                    <p>🏘️ 江湾：婺源最大的村落，萧江氏族聚居地</p>
                    <p>🌿 篁岭：梯田花海，晒秋文化独特景观</p>
                    <p>🛶 彩虹桥：始建于南宋，有"中国最美廊桥"之称</p>
                    <p>🍜 午餐：婺源特色美食</p>
                    <p>🥢 糊豆腐：婺源传统名菜，豆腐肉末糊</p>
                    <p>🍡 清明果：艾草糯米制作，春季时令小吃</p>
                    <p>🥓 婺源红鱼：淡水鱼佳肴，清蒸红烧皆可</p>
                    <p>🌅 下午：思溪延村古村落漫步</p>
                    <p>🏠 思溪延村：《聊斋》取景地，徽派建筑群</p>
                    <p>📅 明日预告：景德镇 · 瓷都之旅</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌼</div>
                    <div class="photo-placeholder">🏘️</div>
                    <div class="photo-placeholder">🍜</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">💡</span>
                        <span class="tip-text">婺源景点分散，建议自驾或包车，东线（江湾、篁岭、李坑）和北线（思溪延村、彩虹桥）分开游览</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🌸</span>
                        <span class="tip-text">5月虽油菜花已谢，但篁岭晒秋和古村建筑仍值得一看，游客比春季少</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🏨</span>
                        <span class="tip-text">婺源住宿推荐住在县城或江湾镇，便于第二日前往各景点</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day74_entry + '\n' + footer_marker)
print('Added Day 74 entry: 婺源 · 中国最美乡村')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年5月1日</p>')
    print('Updated footer timestamp to 2026年5月1日')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 74')
print('Location: 婺源')
print('Date: 2026-05-01 (劳动节)')
print('KM added: 120 (total: ~8773)')
print('Location count: 44')