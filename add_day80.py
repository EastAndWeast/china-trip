# -*- coding: utf-8 -*-
"""环游中国 - Day 80 更新脚本
日期: 2026-05-08 (Day 80 内容：长沙 → 岳阳 → 长沙/南昌方向)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 79
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated dayCount -> 80')

# 2. Update km (岳阳楼往返约200km + 长沙市内50km)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 250) + '<',
    content)
print('Updated kmCount -> 9803 (added 250km)')

# 3. Location count stays same
print('LocationCount unchanged -> 49')

# 4. Day 80 entry (2026-05-08)
day80_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第80天</span>
                    <span class="day-date">2026-05-08 · 四月十一</span>
                </div>
                <div class="day-title">🚗 长沙 → 岳阳 · 洞庭湖畔</div>
                <div class="day-content">
                    <p>🏔️ 上午游岳麓山：乘索道上山，赏湘江两岸风光，参观岳麓书院（湖南大学）</p>
                    <p>📚 岳麓书院：中国古代四大书院之一，千年学府，门票50元含书院和山</p>
                    <p>🛤️ 午后沿京港澳高速北上，约2小时抵达岳阳</p>
                    <p>🌊 岳阳楼：江南三大名楼之一，临洞庭湖而建，"先天下之忧而忧"名句出处</p>
                    <p>🏞️ 洞庭湖：中国第二大淡水湖，候鸟保护区，岳阳楼下即观湖最佳点</p>
                    <p>🦆 君山岛：洞庭湖中小岛，湘妃竹、柳毅传书典故，渡船往返约70元</p>
                    <p>🐟 岳阳美食：回头鱼（特色鱼火锅）、洞庭湖鲜、银鱼蒸蛋</p>
                    <p>🌉 傍晚返回长沙，或继续前往南昌方向</p>
                    <p>📅 明日预告：南昌 · 滕王阁 · 赣江之夜</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏔️</div>
                    <div class="photo-placeholder">🌊</div>
                    <div class="photo-placeholder">🦆</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🏔️</span>
                        <span class="tip-text">岳麓山索道上山35元/人，下山25元/人，开放时间8:00-18:00，岳麓书院50元/人</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🌊</span>
                        <span class="tip-text">岳阳楼门票70元/人（网络购票65元），景区不大约1-2小时可逛完，登楼望洞庭湖视野极佳</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🦆</span>
                        <span class="tip-text">君山岛船票约40元/人，往返70元，岛上可租电动车骑行，建议预留3-4小时游玩</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day80_entry + '\n' + footer_marker)
print('Added Day 80 entry: 长沙 → 岳阳 · 洞庭湖畔')

# 5. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年5月9日</p>')
    print('Updated footer timestamp to 2026年5月9日')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 80')
print('Location: 长沙 → 岳阳 → 长沙')
print('Date: 2026-05-08 (四月十一)')
print('KM added: 250 (total: ~9803)')
