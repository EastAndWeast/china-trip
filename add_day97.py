# -*- coding: utf-8 -*-
"""环游中国 - Day 97 更新脚本
添加Day 97（杭州 → 南昌，滕王阁之夜）"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount=96, add 1 day and ~500km/2 locations
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 500) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 2) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>南昌 · 滕王阁\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

day97_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">97</span>
                    <span class="day-date">2026-05-25 · 四月廿八 · 周一</span>
                </div>
                <div class="day-title">🚗 杭州 → 南昌 · 滕王阁夜景</div>
                <div class="day-content">
                    <p>🚗 今日行程：杭州 → 南昌（自驾约500km，5.5小时）</p>
                    <p>🛣️ 路线：杭长高速 → 沪昆高速 → 南昌绕城高速</p>
                    <p>🏛️ 下午：八一起义纪念馆（南昌起义纪念馆，免费预约）</p>
                    <p>🌆 傍晚：滕王阁（"江南三大名楼"之一，王勃《滕王阁序》出处）</p>
                    <p>🌃 晚上：滕王阁灯光秀 + 赣江风光带散步</p>
                    <p>🎆 秋水广场音乐喷泉（亚洲最大喷泉群之一，每晚8点）</p>
                    <p>🍜 晚餐：南昌瓦罐汤 + 拌粉（标配"南昌味道"）</p>
                    <p>🏨 住宿推荐：八一广场/滕王阁附近（交通便利）</p>
                    <p>📅 明日预告：南昌深度游——滕王阁登楼 · 万寿宫 · 江西省博物馆</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">🌃</div>
                    <div class="photo-placeholder">🎆</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🏯</span>
                        <span class="tip-text">滕王阁门票50元（夜间贵一些），建议傍晚去拍灯光秀，22:00关灯</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🎆</span>
                        <span class="tip-text">秋水广场音乐喷泉每晚8:00-8:30，免费观看，建议提前10分钟到</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🍜</span>
                        <span class="tip-text">南昌拌粉3-5元/碗，瓦罐汤4-6元/盅，性价比超高</span>
                    </div>
                </div>
            </div>

'''

content = content[:footer_pos] + day97_entry + content[footer_pos:]
print('Added Day 97 entry')

# Update footer travel tips
content = content.replace('📰 2026年5月杭州西湖旅游贴士', '📰 2026年5月南昌旅游贴士')
content = content.replace(
    '''<li>🏯 灵隐寺门票75元（含灵隐+飞来峰），早上6:30开门就去，人少清净</li>
                    <li>🍵 龙井村品茶选择正规茶楼，明前龙井300-800元/斤</li>
                    <li>🚣 西湖游船55元/人（含三潭印月），下午4点左右乘船光线最美</li>
                    <li>🌅 苏堤漫步免费，傍晚看雷峰塔夕阳是精华体验</li>
                    <li>🚗 苏州到杭州约100km，自驾1.5小时；杭州限行需注意</li>
                    <li>🗺️ 地铁1号线直达西湖；建议住断桥/苏堤附近</li>
                    <li>📅 明日预告：杭州——宋城千古情 or 西溪湿地</li>''',
    '''<li>🏯 滕王阁门票50元，傍晚去拍灯光秀最佳，22:00关灯</li>
                    <li>🎆 秋水广场音乐喷泉每晚8:00-8:30，免费，建议提前占位</li>
                    <li>🍜 南昌拌粉3-5元+瓦罐汤4-6元，南昌美食性价比超高</li>
                    <li>🏛️ 八一起义纪念馆免费，需提前在公众号预约</li>
                    <li>🚗 杭州到南昌约500km，自驾5.5小时，走杭长/沪昆高速</li>
                    <li>🗺️ 南昌地铁1号线覆盖主要景区；建议住八一广场附近</li>
                    <li>📅 明日预告：南昌深度游——滕王阁登楼 · 万寿宫 · 绳金塔</li>'''
)
content = content.replace('最后更新：2026年5月24日（周日）', '最后更新：2026年5月25日（周一）')

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