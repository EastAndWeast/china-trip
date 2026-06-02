# -*- coding: utf-8 -*-
"""环游中国 - Day 101 更新脚本
添加Day 101（庐山 → 九江，鄱阳湖 + 长江）"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount=101, add 1 day and ~50km/2 locations
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 50) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 2) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>九江 · 鄱阳湖\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

day101_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">101</span>
                    <span class="day-date">2026-05-29 · 五月初二 · 周五</span>
                </div>
                <div class="day-title">🚗 庐山下山 · 九江 · 鄱阳湖湿地 · 长江</div>
                <div class="day-content">
                   <p>🚗 今日行程：庐山牯岭镇 → 九江市（约50km，1小时下山）</p>
                    <p>🛣️ 上午：庐山下山（乘索道或自驾，经南山园路下山）</p>
                    <p>🏞️ 中午：抵达九江市，午餐（九江特色：茶香饼、萝卜饼）</p>
                    <p>🌊 下午：鄱阳湖湿地（江南最大淡水湖，中国最大淡水湖）</p>
                   <p>🌉 傍晚：长江九江段 + 长江大桥观景</p>
                    <p>🍜 晚餐：九江鱼宴（鄱阳湖鲜鱼，白浇鳜鱼）</p>
                    <p>🏨 住宿推荐：九江城区（滨江路/甘棠湖附近）</p>
                    <p>📅 明日预告：九江 → 景德镇（自驾约150km，2小时），中国瓷都</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌊</div>
                    <div class="photo-placeholder">🌉</div>
                    <div class="photo-placeholder">🏞️</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🌊</span>
                        <span class="tip-text">鄱阳湖湿地公园免费；丰水期（5-9月）湖面扩大，景色壮观</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🍜</span>
                        <span class="tip-text">九江美食：茶香饼、萝卜饼、鄱阳湖醉虾、石鱼炒蛋</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🚗</span>
                        <span class="tip-text">庐山下山索道约10分钟，或自驾下山；山路弯曲需小心驾驶</span>
                    </div>
                </div>
            </div>

'''

content = content[:footer_pos] + day101_entry + content[footer_pos:]
print('Added Day 101 entry')

# Update footer travel tips
old_footer = '''<li>🌅 含鄱口日出需凌晨4:30出发，带手电筒；5月底日出约5:15</li>
                    <li>🕳️ 仙人洞免费；花径公园免费；美庐别墅20元</li>
                    <li>🏛️ 庐山会议旧址免费参观，建议请导游讲解历史</li>
                    <li>🍜 牯岭镇美食：土豆烧肉、笋干烧肉、石耳炖鸡</li>
                    <li>🏨 牯岭镇住宿建议提前预订，节假日价格较高</li>
                    <li>🚗 庐山至九江约50km，下山后走福银高速约1小时</li>
                    <li>📅 明日预告：庐山下山 → 九江（庐山会议旧址/鄱阳湖）</li>'''

new_footer = '''<li>🌊 鄱阳湖湿地免费参观；丰水期景色壮观，建议下午去</li>
                   <li>🍜 九江美食：茶香饼、萝卜饼、鄱阳湖醉虾、鱼宴</li>
                   <li>🚗 庐山至九江约50km，下山1小时，走福银高速</li>
                    <li>🏨 九江住宿推荐滨江路/甘棠湖附近，停车方便</li>
                    <li>📅 明日预告：九江 → 景德镇（自驾约150km，2小时）</li>'''

content = content.replace(old_footer, new_footer)
content = content.replace('最后更新：2026年5月28日（周四）', '最后更新：2026年5月29日（周五）')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print('HTML updated successfully')

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    verify = f.read()
day_nums = re.findall(r'class="day-number">(\d+)<', verify)
print('Last 3 day numbers:', day_nums[-3:] if day_nums else 'none')
day_match = re.search(r'id="dayCount"[^>]*>(\d+)<', verify)
km_match = re.search(r'id="kmCount"[^>]*>(\d+)<', verify)
loc_match = re.search(r'id="locationCount"[^>]*>(\d+)<', verify)
cur_match = re.search(r'id="currentLocation"[^>]*>([^<]+)<', verify)
print('Stats: dayCount=%s, kmCount=%s, locationCount=%s, location=%s' % (
    day_match.group(1) if day_match else '?',
    km_match.group(1) if km_match else '?',
    loc_match.group(1) if loc_match else '?',
    cur_match.group(1) if cur_match else '?'
))