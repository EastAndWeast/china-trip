# -*- coding: utf-8 -*-
"""
环游中国 - Day 69 更新脚本
日期: 2026-04-26 (Day 69 内容：泉州第一天)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 68
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 2. Update km (~50km within泉州/晋江)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 50) + '<',
    content)

# 3. Location count stays the same (still in 泉州)
# content stays locationCount

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">泉州 · 鲤城区<',
    content)

print('Updated stats: Day 69, km +50, location -> 泉州 · 鲤城区')

# 5. Day 69 entry
day69_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第69天</span>
                    <span class="day-date">2026-04-26 · 三月廿九</span>
                </div>
                <div class="day-title">🏯 泉州 · 海上丝绸之路起点</div>
                <div class="day-content">
                    <p>抵达泉州！这座 UNESCO 认定的东亚文化之都，是宋元时期的国际大都市。</p>
                    <p>🛕 上午：开元寺——福建省内规模最大的佛教寺院</p>
                    <p>🏯 开元寺：始建于唐代 686 年，香火鼎盛</p>
                    <p>🗿 镇国塔：唐代石塔，高 48 米，雕刻精美</p>
                    <p>🌳 桑树古迹：传说中桑开白莲的神树遗址</p>
                    <p>🕌 中午：清净寺——中国现存最古老的伊斯兰教寺之一</p>
                    <p>🕌 清净寺：始建于 1009 年，伊斯兰建筑风格</p>
                    <p>📜 泉州曾是世界最大港口，贸易伙伴遍及亚洲非洲</p>
                    <p>🍜 午餐：泉州面线糊 + 醋肉（老城区网红店）</p>
                    <p>🏛️ 下午：泉州古城漫步</p>
                    <p>🏠 西街：泉州最古老的街区，千年历史</p>
                    <p>🔔 钟楼：泉州市中心地标，民国建筑</p>
                    <p>🌉 洛阳桥：中国现存最早的石桥之一，建于宋代</p>
                    <p>🛶 傍晚：晋江畔看日落</p>
                    <p>🌅 晋江是泉州母亲河，河畔视野开阔</p>
                    <p>🎭 梨园戏：晚间可以欣赏泉州非遗戏曲表演</p>
                    <p>🚗 明日行程：崇武古城 或 惠安海边</p>
                    <p>📅 明日预告：惠安女文化 · 崇武古城 · 泉州美食</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">🕌</div>
                    <div class="photo-placeholder">🌉</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">💡</span>
                        <span class="tip-text">开元寺建议清晨7点前到达，避开旅游团</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🍜</span>
                        <span class="tip-text">西街小吃推荐：面线糊、蚵仔煎、润饼菜、姜母鸭</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🎭</span>
                        <span class="tip-text">梨园戏演出可在"泉州戏曲中心"公众号购票</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day69_entry + '\n' + footer_marker)
print('Added Day 69 entry: 泉州 · 海上丝绸之路起点')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月26日</p>')
    print('Updated footer timestamp to 2026年4月26日')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 69')
print('Location: 泉州 · 鲤城区')
print('Date: 2026-04-26')
print('KM added: 50 (total: ~7723)')
print('Location count: 40 (unchanged)')