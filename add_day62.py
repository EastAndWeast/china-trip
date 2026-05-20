# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update day count 61 -> 62
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 2. Update location count (new city: 福州)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 3. Update km (武夷山到福州高铁约200km)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 200) + '<',
    content)

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">福州 · 三坊七巷<',
    content)

print('Updated stats: Day 62, km +200, location -> 福州 · 三坊七巷')

# 5. Add Day 62 entry before footer
day62_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第62天</span>
                    <span class="day-date">2026-04-19 · 三月廿二</span>
                </div>
                <div class="day-title">🏙️ 武夷山 → 福州 · 三坊七巷穿越之旅</div>
                <div class="day-content">
                    <p>告别武夷山的丹山碧水，乘坐高铁前往福建省会福州，开启福建之旅！</p>
                    <p>🚄 上午：武夷山 → 福州</p>
                    <p>高铁行程约2小时（G/B/C字头），二等座票价约120-150元，推荐乘坐早上8:00-9:30班次，10:30左右抵达福州</p>
                    <p>🏙️ 中午：抵达福州，入住 + 品尝福州美食</p>
                    <p>必吃：佛跳墙（闽菜之王）、肉燕（福州特色小吃）、鱼丸、捞化、芋泥</p>
                    <p>📍 下午：三坊七巷历史文化街区</p>
                    <p>三坊七巷——福州"城市名片"，中国十大历史文化名街之一！保存完好的明清古建筑群，坊巷纵横，白墙黛瓦，尽显闽都文化底蕴！</p>
                    <p>🛤️ 三坊七巷：由三个坊、七条巷组成（衣锦坊、文儒坊、光禄坊；杨桥巷、郎官巷、塔巷、黄巷、安民巷、宫巷、吉庇巷）</p>
                    <p>🏛️ 著名景点：林则徐纪念馆、严复故居、冰心故居、林觉民故居、福建省非遗博物馆</p>
                    <p>📸 三坊七巷最佳拍照点：南后街主街（灯笼+白墙）、花巷教堂、福州茉莉花茶馆天台</p>
                    <p>🌸 傍晚：福州城市漫步</p>
                    <p>可选择：① 西湖公园（福州最美公园，免费）② 上下杭历史文化街区（夜景绝美）③ 烟台山历史风貌区（万国建筑博览）</p>
                    <p>📊 今日行程：武夷山→福州高铁200km，三坊七巷步行约3公里</p>
                    <p>🚗 交通提示：福州地铁1号线直达三坊七巷（南门兜站）；福州共享电动车覆盖全城，出行便捷</p>
                    <p>📅 下一站预告：厦门（高铁1小时或自驾2小时），开始海岛之旅！鼓浪屿、环岛路、南普陀寺在等你！</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏙️</div>
                    <div class="photo-placeholder">🛤️</div>
                    <div class="photo-placeholder">🌆</div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day62_entry + '\n' + footer_marker)
print('Added Day 62 entry for 福州三坊七巷')

# 6. Update travel tips
old_footer_pattern = r'<div class="footer">.*?<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月.*?</p>.*?</div>'

new_footer = '''<div class="footer">
            <p>🚗 环游中国 · 房车日记</p>
            <p>记录每一天的所见所闻</p>
            <div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年4月中旬福州厦门旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🚄 武夷山→福州：高铁约2小时，票价120-150元；推荐早8-9点班次，上午10:30抵达福州</li>
                    <li>🏙️ 三坊七巷：福州城市名片，明清古建筑群，免费开放；地铁1号线南门兜站直达</li>
                    <li>🛤️ 三坊七巷亮点：林则徐纪念馆、严复故居、冰心林觉民故居、福建省非遗博览苑</li>
                    <li>📸 三坊七巷最佳拍照点：南后街灯笼夜景、花巷教堂、茉莉花茶馆天台；建议傍晚4-6点光线最佳</li>
                    <li>🍜 福州必吃：佛跳墙（闽菜之王）、肉燕、鱼丸、捞化、芋泥；推荐老字号：聚春园、安泰楼</li>
                    <li>🌆 福州夜景推荐：上下杭历史文化街区（免费）、烟台山万国建筑群、西湖公园夜景</li>
                    <li>🚄 福州→厦门：高铁1小时或自驾2小时；厦门景点：鼓浪屿、环岛路、南普陀寺、曾厝垵</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月19日</p>
            </div>
        </div>'''

new_content = re.sub(old_footer_pattern, new_footer, content, flags=re.DOTALL)
if new_content != content:
    print('Updated travel tips to 福州厦门')
else:
    print('WARNING: Could not find old footer to replace')

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('\n=== Update Complete ===')
print('Day: 62')
print('Location: 福州 · 三坊七巷')
print('Date: 2026-04-19')
print('Stats: DayCount +1, LocationCount +1, kmCount +200')
