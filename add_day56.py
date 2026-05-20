# -*- coding: utf-8 -*-
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Read file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update day count from 55 to 56
content = re.sub(r'id="dayCount"[^>]*>(\d+)<', 
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<' if int(m.group(1)) == 55 else m.group(0),
    content)

# 2. Update location count (add 婺源 = +1, now 32)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<' if int(m.group(1)) == 31 else m.group(0),
    content)

# 3. Update km (西递到婺源约120km)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 120) + '<' if int(m.group(1)) == 5850 else m.group(0),
    content)

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">婺源 · 篁岭<',
    content)

print('Updated stats: Day 55 -> 56, km +120, location -> 婺源篁岭')

# 5. Add Day 56 entry before the closing </div> of timeline
day56_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第56天</span>
                    <span class="day-date">2026-04-13 · 三月十六</span>
                </div>
                <div class="day-title">🏯 婺源篁岭 · 晒秋人家&江湾古韵</div>
                <div class="day-content">
                    <p>离开西递，驱车120公里历时约3小时，终于抵达"中国最美乡村"——婺源！</p>
                    <p>🚗 交通：黟县西递→婺源县城约120公里，走S220转G56高速，3小时车程，路况良好</p>
                    <p>婺源——"中国最美乡村"，4月中旬正值油菜花尾花期，高海拔梯田仍有残花可赏！</p>
                    <p>🌸 花期提醒：平原花海（李坑、思溪延村）已进入尾花期，篁岭梯田油菜花仍可观赏，搭配春雨与古村意境，别有韵味</p>
                    <p>上午抵达后直奔篁岭，乘索道上山，开启"晒秋人家"的春游体验！</p>
                    <p>🏯 篁岭景区：500年历史古村，"中国晒秋第一村""中国版天空之城"，依山而建，梯田环绕，白墙黛瓦错落有致</p>
                    <p>春季的篁岭虽然不是晒秋季节，但油菜花田与古村交相辉映，同样令人惊艳！</p>
                    <p>🎋 篁岭油菜花：梯田花海海拔500-800米，比平原晚开约10天，4月中旬仍有金黄可赏</p>
                    <p>中午在篁岭山下的农家乐享用了地道的婺源美食！</p>
                    <p>🍜 婺源美食：糊豆腐25元/份、荷包红鲤鱼58元、清明果8元/个，篁岭脚下农家乐价格公道</p>
                    <p>下午前往距篁岭约30公里的江湾景区，这里是朱熹故里，萧江氏宗祠气势恢宏！</p>
                    <p>🏛️ 江湾景区：60元/人，朱熹故里，千年古樟树+徽派宗祠群，江氏宗祠保存完好</p>
                    <p>📊 今日行程：黟县西递→婺源篁岭（索道+古村）→江湾（宗祠+古樟），车程约150公里</p>
                    <p>📍 明日计划：婺源北线：思溪延村→彩虹桥→灵岩洞，感受婺源深厚的人文底蕴</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">🌸</div>
                    <div class="photo-placeholder">🏛️</div>
                </div>
            </div>
'''

# Insert Day 56 before footer
footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day56_entry + '\n' + footer_marker)
print('Added Day 56 entry for 婺源篁岭')

# 6. Update travel tips with latest search info
old_footer_pattern = r'<div class="footer">.*?<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月12日</p>.*?</div>'

new_footer = '''<div class="footer">
            <p>🚗 环游中国 · 房车日记</p>
            <p>记录每一天的所见所闻</p>
            <div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年4月中旬婺源旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🌸 花期提醒：4月中旬属婺源油菜花尾花期，高海拔梯田（篁岭、江岭）仍有残花，搭配春雨意境佳</li>
                    <li>🏯 婺源通票：180元/人/5天，含江岭、晓起、江湾、汪口、李坑等10个景点；12景区联票150元/24小时</li>
                    <li>🚠 篁岭索道：需单独购票，建议提前网上订票，山下住宿条件好，旺季需提前1周预订</li>
                    <li>🏛️ 江湾景区：60元/人，朱熹故里，千年古樟+萧江宗祠，徽派宗祠文化浓厚</li>
                    <li>🚗 自驾：婺源各村落间路况良好（柏油/水泥路），家用轿车通行无压力，县内1小时可达所有景区</li>
                    <li>📅 婺源北线：思溪延村、彩虹桥、灵岩洞、石城——婺源最深厚的人文景观线</li>
                    <li>🍜 婺源美食：糊豆腐、荷包红鲤鱼、清明果，县城及景区农家乐价格实惠</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月13日</p>
            </div>
        </div>'''

new_content = re.sub(old_footer_pattern, new_footer, content, flags=re.DOTALL)
if new_content != content:
    print('Updated travel tips')
else:
    print('WARNING: Could not find old footer to replace (already updated?)')

# Write back
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('\n=== Update Complete ===')
print('Day: 56')
print('Location: 婺源 · 篁岭')
print('Date: 2026-04-13')
