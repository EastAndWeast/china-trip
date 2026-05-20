# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update day count 62 -> 63
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 2. Update km (福州到厦门约400km高速)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 400) + '<',
    content)

# 3. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">厦门 · 鼓浪屿<',
    content)

print('Updated stats: Day 63, km +400, location -> 厦门 · 鼓浪屿')

# 4. Add Day 63 entry before footer
day63_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第63天</span>
                    <span class="day-date">2026-04-20 · 三月廿三</span>
                </div>
                <div class="day-title">🚄🏖️ 福州 → 厦门 · 海上花园初见</div>
                <div class="day-content">
                    <p>告别"有福之州"福州，乘坐高铁前往"海上花园"厦门，开启海岛之旅！</p>
                    <p>🚄 上午：福州 → 厦门</p>
                    <p>高铁行程约1小时（G/D字头），二等座票价约85-120元，推荐乘坐早上8:00-9:30班次，10:00左右抵达厦门</p>
                    <p>🚗 也可选择自驾：福州→厦门约280公里，全程高速约3小时，沿途风景优美</p>
                    <p>🏖️ 中午：抵达厦门，入住环岛路海景酒店</p>
                    <p>厦门——中国最早的经济特区之一，被誉为"鹭岛"、"海上花园"，气候宜人，四季如春</p>
                    <p>🌊 推荐入住：环岛路沿线海景酒店（曾厝垵/珍珠湾附近），推窗见海，出门即沙滩</p>
                    <p>🛤️ 下午：鼓浪屿——世界文化遗产，"钢琴之岛"</p>
                    <p>⛴️ 交通：厦门邮轮中心（东渡）乘船至鼓浪屿三丘田码头，船票35元/人，需提前在"厦门轮渡有限公司"公众号预约</p>
                    <p>🏛️ 鼓浪屿看点：世界文化遗产岛屿，汇集各国建筑风格，有"万国建筑博览会"之称</p>
                    <p>🎹 必游景点：日光岩（登顶俯瞰厦门全景）、菽庄花园（百年园林+钢琴博物馆）、皓月园、郑成功纪念馆</p>
                    <p>🍵 鼓浪屿美食：叶氏麻糍（15元/份）、黄金香肉松、馅饼、花生汤</p>
                    <p>🛍️ 龙头路：鼓浪屿最热闹的商业街，汇聚各种特色小店、咖啡馆和文艺店铺</p>
                    <p>🌅 傍晚：返回厦门，在环岛路散步欣赏海上日落，金色余晖洒在海面上</p>
                    <p>🚴 环岛路：厦门最美的海滨公路，全长约31公里，可租电动车骑行，吹着海风看日落</p>
                    <p>🦐 晚餐：环岛路海鲜大排档，新鲜便宜！必点：厦门沙茶面、酱油水海鲜、白灼虾</p>
                    <p>📊 今日行程：福州→厦门（高铁1小时/自驾3小时），鼓浪屿半日游 + 环岛路日落</p>
                    <p>🚗 交通提示：厦门地铁1号线穿越老城区；共享电动车环岛路全覆盖；鼓浪屿船票需提前预约</p>
                    <p>📅 明日预告：厦门深度游——南普陀寺登高、厦门大学怀旧、曾厝垵寻味、沙坡尾文艺</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏖️</div>
                    <div class="photo-placeholder">⛴️</div>
                    <div class="photo-placeholder">🌅</div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day63_entry + '\n' + footer_marker)
print('Added Day 63 entry for 福州→厦门 鼓浪屿')

# 5. Update travel tips
old_footer_pattern = r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月.*?</p>'

new_footer = '''<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月20日</p>'''

content = re.sub(old_footer_pattern, new_footer, content)
print('Updated travel tips timestamp')

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 63')
print('Location: 厦门 · 鼓浪屿')
print('Date: 2026-04-20')
print('Stats: DayCount 63, kmCount +400, Location unchanged')
