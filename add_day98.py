# -*- coding: utf-8 -*-
"""环游中国 - Day 98 更新脚本
添加Day 98（南昌深度游——滕王阁登楼 · 万寿宫 · 江西省博物馆）
同时修复footer中的杭州旧内容"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount=97, add 1 day and ~50km/3 locations
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 50) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 3) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>南昌 · 万寿宫历史文化街区\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

day98_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">98</span>
                    <span class="day-date">2026-05-26 · 四月廿九 · 周二</span>
                </div>
                <div class="day-title">🏯 南昌深度游 · 滕王阁登楼 · 万寿宫 · 江西省博物馆</div>
                <div class="day-content">
                    <p>🏛️ 上午：江西省博物馆（"赣鄱风华"常设展，海昏侯国出土文物）</p>
                    <p>🏯 上午/中午：滕王阁登楼（"江南三大名楼"之一，王勃《滕王阁序》出处）</p>
                    <p>🍜 中午：万寿宫历史文化街区（南昌老城区美食，蛤蟆街/船山路）</p>
                    <p>🛍️ 下午：万寿宫商帮文化展示 + 周边老南昌巷弄CityWalk</p>
                    <p>🪨 傍晚：绳金塔（南昌"镇城之宝"，千年古塔）</p>
                    <p>🌆 晚上：秋水广场音乐喷泉（亚洲最大喷泉群之一，每晚8点）</p>
                    <p>🍜 晚餐：南昌水煮 + 麻辣小吃（当地特色街头美食）</p>
                    <p>🏨 住宿推荐：八一广场/滕王阁附近（交通便利，方便看喷泉）</p>
                    <p>📅 明日预告：南昌 → 庐山（自驾约120km，1.5小时），庐山云海+瀑布</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏛️</div>
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">🌆</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🏯</span>
                        <span class="tip-text">滕王阁门票50元，建议傍晚登楼拍赣江日落，22:00关灯</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🏛️</span>
                        <span class="tip-text">江西省博物馆免费，海昏侯国文物展必看，需提前公众号预约</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🍜</span>
                        <span class="tip-text">万寿宫街区美食：蛤蟆街炒螺蛳、船山路烧烤、南昌水煮（辣）</span>
                    </div>
                </div>
            </div>

'''

content = content[:footer_pos] + day98_entry + content[footer_pos:]
print('Added Day 98 entry')

# Fix footer travel tips - replace old 杭州 content with proper 南昌 content
old_footer = '''<li>🌸 西湖景区全天免费；断桥、苏堤、曲院风荷为核心景点</li>
                    <li>🚤 西湖游船55元（含三潭印月登岛）；摇橹船可议价约150-200元/小时</li>
                    <li>⛩️ 灵隐寺建议早起（7:00开门）避免人流；永福寺人少景美</li>
                    <li>🏨 湖滨路/南山路住宿位置最佳，方便看夜景和逛河坊街</li>
                    <li>🍜 楼外楼（孤山路店）是百年老店；绿茶/外婆家性价比高</li>
                    <li>🚇 杭州地铁覆盖主要景区；节假日西湖边实行单双号限行</li>
                    <li>📅 明日预告：杭州——灵隐寺、河坊街、宋城或乌镇</li>'''

new_footer = '''<li>🏯 滕王阁门票50元，傍晚登楼拍赣江日落，22:00关灯</li>
                    <li>🏛️ 江西省博物馆免费，海昏侯文物展必看，需公众号提前预约</li>
                    <li>🍜 万寿宫街区美食：水煮、炒螺蛳、烧烤，南昌口味偏辣</li>
                    <li>🎆 秋水广场音乐喷泉每晚8:00-8:30，免费，建议提前10分钟到</li>
                    <li>🪨 绳金塔千年古塔，免费参观；周边有绳金塔美食街</li>
                    <li>🚗 南昌到庐山约120km，自驾1.5小时，走昌九大道/福银高速</li>
                    <li>📅 明日预告：庐山深度游——庐山云海 · 瀑布泉水 · 牯岭镇</li>'''

content = content.replace(old_footer, new_footer)
content = content.replace('最后更新：2026年5月25日（周一）', '最后更新：2026年5月26日（周二）')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print('HTML updated successfully')

# Verify
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