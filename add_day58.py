# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update day count 57 -> 58
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 2. Update location count (+2: 江岭 + 庆源)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 2) + '<',
    content)

# 3. Update km (北线各村间约60km)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 60) + '<',
    content)

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">婺源 · 东线<',
    content)

print('Updated stats: Day 58, km +60, location -> 婺源东线')

# 5. Add Day 58 entry before footer
day58_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第58天</span>
                    <span class="day-date">2026-04-15 · 三月十八</span>
                </div>
                <div class="day-title">🏘️ 婺源东线 · 江岭梯田·庆源古村</div>
                <div class="day-content">
                    <p>婺源第三天！开启东线深度游——江岭梯田与庆源古村，感受"中国最美乡村"的另一面！</p>
                    <p>🚗 今日路线：县城→江岭（约40km，1小时）→庆源（约30km，40分钟）→返程或前往下一站</p>
                    <p>🌾 上午：江岭梯田（通票景点）</p>
                    <p>江岭——婺源最壮观的梯田景区，海拔约500-800米，层层叠叠的油菜花海与白墙黛瓦相映成趣！</p>
                    <p>🌼 江岭梯田：婺源油菜花的"终极目的地"，10万亩梯田油菜花海，被誉为"全球十大最美梯田"之一</p>
                    <p>4月中旬虽已过盛花期，但高海拔梯田仍有金黄残花，云雾缭绕时宛如仙境，摄影爱好者天堂！</p>
                    <p>📸 江岭日出：清晨日出时分，晨雾+油菜花+徽派建筑，光影绝佳，建议清晨5-6点前往</p>
                    <p>🏘️ 中午：庆源古村（单独购票，约50元/人）</p>
                    <p>庆源——被誉为"婺源最后的世外桃源"，1300年历史古村，小桥流水人家，宁静古朴</p>
                    <p>🏛️ 庆源古村：始建于唐僖宗年间（公元874年），千年古村保存完好，没有过度商业化，难得的宁静之地</p>
                    <p>村中有明清古建筑、青石板路、古樟树，漫步其中仿佛穿越时光，感受最原汁原味的婺源</p>
                    <p>🍜 午餐：庆源农家乐，品尝地道婺源风味</p>
                    <p>🌿 下午：根据时间和体力，可选择：</p>
                    <p>① 前往下一站：武夷山（婺源→武夷山，约200km，3小时车程）</p>
                    <p>② 继续游览东线：汪口、月亮湾（县城附近）</p>
                    <p>📊 今日行程：婺源东线深度游，江岭+庆源，车程约90公里</p>
                    <p>🌧️ 天气提醒：4月婺源多雨，备好雨具，江岭海拔较高早晚温差大</p>
                    <p>📍 明日计划：离开婺源前往武夷山（福建），开启新一段旅程！</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌾</div>
                    <div class="photo-placeholder">🏘️</div>
                    <div class="photo-placeholder">🌼</div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day58_entry + '\n' + footer_marker)
print('Added Day 58 entry for 婺源东线')

# 6. Update travel tips
old_footer_pattern = r'<div class="footer">.*?<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月14日</p>.*?</div>'

new_footer = '''<div class="footer">
            <p>🚗 环游中国 · 房车日记</p>
            <p>记录每一天的所见所闻</p>
            <div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年4月中旬婺源东线旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🌾 江岭梯田：通票景点，婺源最壮观梯田，"全球十大最美梯田"之一，4月中旬仍有残花可赏</li>
                    <li>📸 江岭日出：建议清晨5-6点前往，晨雾+油菜花+古村光影绝佳，摄影爱好者天堂</li>
                    <li>🏘️ 庆源古村：单独购票约50元，1300年历史，"婺源最后的世外桃源"，宁静古朴无过度商业化</li>
                    <li>🎫 婺源通票：180元/人/5天，含江岭、晓起、江湾、思溪延村、彩虹桥、灵岩洞、石城等12个景点</li>
                    <li>🌧️ 4月婺源多雨：提前备好雨具，早晚温差大（约12-22°C），江岭海拔较高注意保暖</li>
                    <li>🚗 东线路况：柏油路为主，路况良好，县城到江岭约40km/1小时，家用轿车无压力</li>
                    <li>📅 下一站：武夷山（江西婺源→福建武夷山，约200km，3小时车程），或杭州方向</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月15日</p>
            </div>
        </div>'''

new_content = re.sub(old_footer_pattern, new_footer, content, flags=re.DOTALL)
if new_content != content:
    print('Updated travel tips to Wuyuan East Line')
else:
    print('WARNING: Could not find old footer to replace')

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('\n=== Update Complete ===')
print('Day: 58')
print('Location: 婺源 · 东线')
print('Date: 2026-04-15')
