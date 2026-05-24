# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount=95, add 1 day and ~100km
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 100) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 2) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>杭州 · 西湖湖畔\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

day96_entry = (
    '\n            <div class="day-card">\n'
    '                <div class="day-header">\n'
    '                    <span class="day-number">96</span>\n'
    '                    <span class="day-date">2026-05-24 · 四月廿七 · 周日</span>\n'
    '                </div>\n'
    '                <div class="day-title">🌸 杭州西湖 · 灵隐寺 · 龙井问茶</div>\n'
    '                <div class="day-content">\n'
    '                    <p>🚗 今日行程：苏州 → 杭州（自驾约100km，1.5小时）</p>\n'
    '                    <p>🏯 上午：灵隐寺（"飞来峰"北高峰，门票75元含灵隐+飞来峰）</p>\n'
    '                    <p>🚶 游览路线：灵隐寺 → 飞来峰 → 永福寺 → 韬光寺</p>\n'
    '                    <p>🍵 中午：龙井村（"茶乡第一村"，品明前龙井）</p>\n'
    '                    <p>🚣 下午：西湖游船（断桥残雪 → 白堤 → 苏堤 → 雷峰塔）</p>\n'
    '                    <p>🌅 傍晚：苏堤漫步，看夕阳下的雷峰塔</p>\n'
    '                    <p>🌙 晚上：河坊街步行街（杭州历史街区美食品）</p>\n'
    '                    <p>🏨 住宿推荐：西湖边特色酒店（断桥/苏堤附近）</p>\n'
    '                    <p>📅 明日预告：杭州深度游——宋城千古情 or 西溪湿地</p>\n'
    '                </div>\n'
    '                <div class="photos">\n'
    '                    <div class="photo-placeholder">🏯</div>\n'
    '                    <div class="photo-placeholder">🌸</div>\n'
    '                    <div class="photo-placeholder">🌅</div>\n'
    '                </div>\n'
    '                <div class="tips">\n'
    '                    <div class="tip">\n'
    '                        <span class="tip-icon">🏯</span>\n'
    '                        <span class="tip-text">灵隐寺门票75元（含灵隐+飞来峰），建议早上6:30开门就去</span>\n'
    '                    </div>\n'
    '                    <div class="tip">\n'
    '                        <span class="tip-icon">🍵</span>\n'
    '                        <span class="tip-text">龙井村品茶要选择正规茶楼，明前龙井价格较高（300-800元/斤）</span>\n'
    '                    </div>\n'
    '                    <div class="tip">\n'
    '                        <span class="tip-icon">🚣</span>\n'
    '                        <span class="tip-text">西湖游船55元/人（往返湖滨-三潭印月），建议下午4点左右乘船</span>\n'
    '                    </div>\n'
    '                </div>\n'
    '            </div>\n'
    '\n'
)

content = content[:footer_pos] + day96_entry + content[footer_pos:]
print('Added Day 96 entry')

# Update footer tips
old_footer_tips = '📰 2026年5月苏州深度游贴士'
new_footer_tips = '📰 2026年5月杭州西湖旅游贴士'
if old_footer_tips in content:
    content = content.replace(old_footer_tips, new_footer_tips)
    content = content.replace(
        '<li>🏛️ 寒山寺+枫桥：清晨去人少，"月落乌啼霜满天"意境十足</li>\n                    <li>🌉 周庄门票100元含游船；建议网上提前购票，避免排队</li>\n                    <li>🛶 周庄摇橹船约50元/人，水巷穿行是精华体验</li>\n                    <li>🍜 周庄美食：万三蹄（浓油赤酱）、阿婆茶、清明青团</li>\n                    <li>🚗 苏州到周庄约40km，自驾1小时；周庄停车较贵（50元/次）</li>\n                    <li>🗺️ 苏州地铁1号线覆盖主要景区；建议住平江路/山塘街附近</li>\n                    <li>📅 明日预告：苏州 → 杭州（自驾1.5小时）or 无锡太湖</li>',
        '<li>🏯 灵隐寺门票75元（含灵隐+飞来峰），早上6:30开门就去，人少清净</li>\n                    <li>🍵 龙井村品茶选择正规茶楼，明前龙井300-800元/斤</li>\n                    <li>🚣 西湖游船55元/人（含三潭印月），下午4点左右乘船光线最美</li>\n                    <li>🌅 苏堤漫步免费，傍晚看雷峰塔夕阳是精华体验</li>\n                    <li>🚗 苏州到杭州约100km，自驾1.5小时；杭州限行需注意</li>\n                    <li>🗺️ 地铁1号线直达西湖；建议住断桥/苏堤附近</li>\n                    <li>📅 明日预告：杭州——宋城千古情 or 西溪湿地</li>'
    )
    content = content.replace('最后更新：2026年5月23日（周六）', '最后更新：2026年5月24日（周日）')
    print('Updated footer travel tips')
else:
    print('Footer tips not found, skipping')

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