# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update day count 56 -> 57
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 2. Update location count (+2: 思溪延村 + 彩虹桥/灵岩洞 = +2 or +3, keep +2 for now)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 2) + '<',
    content)

# 3. Update km (篁岭到思溪延村约50km, 到彩虹桥约15km)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 80) + '<',
    content)

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">婺源 · 北线<',
    content)

print('Updated stats: Day 57, km +80, location -> 婺源北线')

# 5. Add Day 57 entry before footer
day57_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第57天</span>
                    <span class="day-date">2026-04-14 · 三月十七</span>
                </div>
                <div class="day-title">🏘️ 婺源北线 · 思溪延村·彩虹桥·灵岩洞</div>
                <div class="day-content">
                    <p>婺源第二天，开启北线深度游！昨天篁岭江湾，今日北线三杰——思溪延村、彩虹桥、灵岩洞！</p>
                    <p>🚗 今日路线：篁岭→思溪延村（约50km，1小时）→清华彩虹桥（约15km）→灵岩洞（约20km）→县城住宿</p>
                    <p>🏘️ 上午：思溪延村（通票景点，单独60元/人）</p>
                    <p>思溪延村——"中国最美乡村"代表，百年古建群+明清古宅，徽商文化活化石！</p>
                    <p>📜 思溪延村历史：始建于南宋庆元年间（1195-1200），已有800多年历史，明清古建群保存完好</p>
                    <p>延村保留了大量清代及民国时期的徽派建筑，有"徽州古建博物馆"之誉。</p>
                    <p>🎋 特色：百年古井+石板巷道+精美木雕，徽商文化浓厚，《聊斋》取景地</p>
                    <p>🏯 中午：清华彩虹桥（通票景点，单独60元/人）</p>
                    <p>彩虹桥——婺源标志性古桥，南宋（1137年）建造，千年历史，八墩九孔廊桥！</p>
                    <p>🌉 彩虹桥建于南宋距今约890年，是婺源最古老、规模最大的廊桥，有"中国最美的廊桥"之称</p>
                    <p>全长约140米，宽约7米，八墩九孔，桥上有廊亭，可避雨休憩。</p>
                    <p>🍜 午餐：清华镇农家乐，地道婺源风味</p>
                    <p>🕳️ 下午：灵岩洞（通票景点，单独60元/人）</p>
                    <p>灵岩洞——大型溶洞群，洞内空间最高处约50米，灯光映照下钟乳石造型各异！</p>
                    <p>⛰️ 灵岩洞：约2亿年前形成的喀斯特溶洞，洞内游览路线约2公里，灯光秀美</p>
                    <p>📊 今日行程：篁岭→思溪延村→彩虹桥→灵岩洞，车程约80公里</p>
                    <p>🎫 门票提醒：婺源通票180元/人/5天，含北线多个景点（思溪延村、彩虹桥、灵岩洞、石城等），单点60~80元/景点，建议买通票更划算</p>
                    <p>🌧️ 天气提醒：4月婺源多雨，备好雨具，早晚温差大注意保暖</p>
                    <p>📍 明日计划：婺源东线：江岭（梯田）→庆源古村，或出发前往武夷山（江西→福建，约200km）</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏘️</div>
                    <div class="photo-placeholder">🌉</div>
                    <div class="photo-placeholder">⛰️</div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day57_entry + '\n' + footer_marker)
print('Added Day 57 entry for 婺源北线')

# 6. Update travel tips
old_footer_pattern = r'<div class="footer">.*?<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月13日</p>.*?</div>'

new_footer = '''<div class="footer">
            <p>🚗 环游中国 · 房车日记</p>
            <p>记录每一天的所见所闻</p>
            <div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年4月中旬婺源北线旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🎫 婺源通票：180元/人/5天，含江岭、晓起、江湾、思溪延村、彩虹桥、灵岩洞、石城等12个景点</li>
                    <li>🏘️ 思溪延村：通票景点，单独60元/人，始建于南宋800年古村，《聊斋》取景地，徽商文化浓厚</li>
                    <li>🌉 清华彩虹桥：通票景点，南宋1137年建造，八墩九孔廊桥，"中国最美的廊桥"，约890年历史</li>
                    <li>🕳️ 灵岩洞：通票景点，溶洞群，约2亿年前形成，洞内游览约2公里，灯光秀美，建议提前买通票</li>
                    <li>🌧️ 4月婺源多雨：提前备好雨具，早晚温差大（约15-25°C），建议带外套</li>
                    <li>🚗 北线路况：柏油路+水泥路，路况良好，各村间1小时内可达，家用轿车无压力</li>
                    <li>📅 婺源东线备选：江岭梯田（适合摄影）、庆源古村（宁静古村）；或继续前往武夷山（福建）</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月14日</p>
            </div>
        </div>'''

new_content = re.sub(old_footer_pattern, new_footer, content, flags=re.DOTALL)
if new_content != content:
    print('Updated travel tips')
else:
    print('WARNING: Could not find old footer to replace')

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('\n=== Update Complete ===')
print('Day: 57')
print('Location: 婺源 · 北线')
print('Date: 2026-04-14')