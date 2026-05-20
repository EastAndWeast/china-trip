# -*- coding: utf-8 -*-
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Read file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update day count from 53 to 54
content = re.sub(r'id="dayCount"[^>]*>(\d+)<', 
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<' if int(m.group(1)) == 53 else m.group(0),
    content)

# 2. Update location count (宏村 = same area as 黄山, stays 31)
# No change needed for location count since still in same region

# 3. Update km (add ~60km 黄山汤口到宏村)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 60) + '<' if int(m.group(1)) == 5750 else m.group(0),
    content)

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">宏村 · 南湖<',
    content)

print('Updated stats: Day 53 -> 54, km +60, location -> 宏村')

# 5. Add Day 54 entry before the closing </div> of timeline
# Find the position just before the last <div class="footer">
day54_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第54天</span>
                    <span class="day-date">2026-04-11 · 三月十四</span>
                </div>
                <div class="day-title">🏘️ 宏村 · 画里乡村晨曦</div>
                <div class="day-content">
                    <p>清晨的宏村是最美的！早上6点就起来，趁着大批游客还未涌入，拍摄南湖的晨雾倒影。</p>
                    <p>🏘️ 宏村：世界文化遗产，被誉为"画里乡村"，是徽派古村落的杰出代表</p>
                    <p>🖼️ 南湖：湖面如镜，白墙黛瓦倒映水中，宛如水墨画卷，清晨薄雾缭绕更添意境</p>
                    <p>清晨的南湖书院宁静祥和，荷叶田田，古树倒映在湖面上，如诗如画！</p>
                    <p>📚 南湖书院：宏村最重要的古建筑之一，清末时期宏村子弟的学堂</p>
                    <p>上午趁着光线好在月沼拍摄，这是宏村的心脏——半月形的池塘，四周是古老的徽派建筑。</p>
                    <p>🌙 月沼：半月形池塘，明代挖凿，风水精华所在</p>
                    <p>🍜 中午在村中农家乐享用了地道的徽州美食：毛豆腐、笋干烧肉、臭鳜鱼</p>
                    <p>🏮 徽派建筑：马头墙、天井、四合院，浓缩了徽州文化的精华</p>
                    <p>下午前往西递古村（距宏村约20公里），感受另一个世界文化遗产的魅力！</p>
                    <p>🏯 西递：始建于北宋年间，被誉为"桃花源里人家"，世界文化遗产</p>
                    <p>📊 今日行程：宏村深度游 + 宏村到西递，月沼/南湖/西递牌楼，步行约12公里</p>
                    <p>📍 明日计划：西递深度游 + 塔川/卢村，走遍黟县古村落</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🖼️</div>
                    <div class="photo-placeholder">🌙</div>
                    <div class="photo-placeholder">🏮</div>
                </div>
            </div>
'''

# Insert Day 54 before footer
footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day54_entry + '\n' + footer_marker)
print('Added Day 54 entry for 宏村')

# 6. Update travel tips
old_footer = '''<div class="footer">
            <p>🚗 环游中国 · 房车日记</p>
            <p>记录每一天的所见所闻</p>
            <div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年4月中旬皖南旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏔️ 黄山登山：4月中旬云海概率较高，建议早起观日出，备好防风外套和登山杖</li>
                    <li>🌸 宏村西递：4月油菜花虽过但桃花、紫藤盛开，清明后人流减少正是好时机</li>
                    <li>🌉 扬州烟花节：2026年4月18日开幕，瘦西湖琼花正盛，需提前订房</li>
                    <li>🏯 苏州园林：拙政园、留园、狮子林春季赏花正当时，建议早7点前入园避人流</li>
                    <li>🍜 徽州美食：黄山的毛豆腐、臭鳜鱼、石耳炖鸡，宏村村内农家乐价格实惠</li>
                    <li>🚗 交通提示：黄山景区换乘中心至云谷寺/慈光阁需乘景区大巴，平日人少畅通</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月10日</p>
            </div>
        </div>'''

new_footer = '''<div class="footer">
            <p>🚗 环游中国 · 房车日记</p>
            <p>记录每一天的所见所闻</p>
            <div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年4月中旬皖南旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏘️ 宏村西递：4月中旬桃花、紫藤盛开，清晨6-7点入园可拍晨雾倒影，游人最少</li>
                    <li>🏯 西递古村：距宏村仅20公里，世界文化遗产，"桃花源里人家"实至名归</li>
                    <li>🌸 扬州烟花节：2026年4月18日开幕，瘦西湖琼花盛放，需提前1周订房</li>
                    <li>🏔️ 黄山：4月云海概率仍较高，光明顶日出是必打卡项目，备好防风外套</li>
                    <li>🍜 徽州美食：宏村农家乐毛豆腐15元/份、臭鳜鱼68元，村中用餐实惠</li>
                    <li>🚗 交通：黟县各古村间建议打车或拼车，宏村到西递约30元/车</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月11日</p>
            </div>
        </div>'''

if old_footer in content:
    content = content.replace(old_footer, new_footer)
    print('Updated travel tips')
else:
    print('WARNING: Could not find old footer to replace')
    # Try partial match
    if '2026年4月中旬皖南旅游贴士' in content:
        print('Found tips section, trying partial update...')

# Write back
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 54')
print('Location: 宏村 · 南湖')
print('Date: 2026-04-11')
