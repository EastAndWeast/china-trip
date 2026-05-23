# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount=94, add 1 day and ~100km
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 80) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 2) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>苏州 · 山塘街\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

day95_entry = (
    '\n            <div class="day-card">\n'
    '                <div class="day-header">\n'
    '                    <span class="day-number">95</span>\n'
    '                    <span class="day-date">2026-05-23 · 四月廿六 · 周六</span>\n'
    '                </div>\n'
    '                <div class="day-title">🌸 苏州深度游 · 寒山寺 · 周庄水乡</div>\n'
    '                <div class="day-content">\n'
    '                    <p>🚗 今日行程：苏州深度游——寒山寺 + 周庄（自驾约80km，1小时）</p>\n'
    '                    <p>🏛️ 上午：寒山寺（"月落乌啼霜满天"——门票20元，千年古刹）</p>\n'
    '                    <p>🚶 游览路线：寒山寺 → 枫桥 → 山塘街（上午游客少）</p>\n'
    '                    <p>🛶 中午：前往周庄（"中国第一水乡"，自驾约40分钟）</p>\n'
    '                    <p>🍜 中午：周庄特色美食（万三蹄、阿婆茶、清明青团）</p>\n'
    '                    <p>🌉 下午：周庄水乡游览（摇橹船、沈厅、张厅、双桥）</p>\n'
    '                    <p>🌙 晚上：返回苏州，住宿老城区（山塘街/平江路附近）</p>\n'
    '                    <p>🏨 住宿推荐：苏州老城区特色民宿，体验苏式慢生活</p>\n'
    '                    <p>📅 明日预告：苏州 → 杭州（自驾约1.5小时）or 无锡太湖</p>\n'
    '                </div>\n'
    '                <div class="photos">\n'
    '                    <div class="photo-placeholder">🏛️</div>\n'
    '                    <div class="photo-placeholder">🌉</div>\n'
    '                    <div class="photo-placeholder">🌸</div>\n'
    '                </div>\n'
    '                <div class="tips">\n'
    '                    <div class="tip">\n'
    '                        <span class="tip-icon">🏛️</span>\n'
    '                        <span class="tip-text">寒山寺门票20元，枫桥免费；建议清晨去，人少安静</span>\n'
    '                    </div>\n'
    '                    <div class="tip">\n'
    '                        <span class="tip-icon">🌉</span>\n'
    '                        <span class="tip-text">周庄门票100元（包含游船），建议网上提前购票</span>\n'
    '                    </div>\n'
    '                    <div class="tip">\n'
    '                        <span class="tip-icon">🛶</span>\n'
    '                        <span class="tip-text">周庄摇橹船约50元/人，穿行水巷是精华体验</span>\n'
    '                    </div>\n'
    '                </div>\n'
    '            </div>\n'
    '\n'
)

content = content[:footer_pos] + day95_entry + content[footer_pos:]
print('Added Day 95 entry')

old_footer_tips = '📰 2026年5月苏州园林旅游贴士'
new_footer_tips = '📰 2026年5月苏州深度游贴士'
if old_footer_tips in content:
    content = content.replace(old_footer_tips, new_footer_tips)
    content = content.replace(
        '<li>🏛️ 拙政园门票70元（旺季建议提前订票），7:30开门，建议一早就去</li>\n                    <li>🏛️ 苏州博物馆免费，周一闭馆，贝聿铭设计，需提前在公众号预约</li>\n                    <li>🛶 山塘街手摇船约50元/人；傍晚去光线最美，夜景绝伦</li>\n                    <li>🍜 平江路美食：松鹤楼（苏帮菜老字号）、蟹壳黄、绿豆糕</li>\n                    <li>🚗 乌镇到苏州约100km，自驾1.5小时；苏州老城区停车较贵</li>\n                    <li>🗺️ 苏州地铁1号线覆盖主要景区；建议住平江路/山塘街附近</li>\n                    <li>📅 明日预告：苏州——寒山寺 or 周庄/同里水乡（自驾1小时）</li>',
        '<li>🏛️ 寒山寺+枫桥：清晨去人少，"月落乌啼霜满天"意境十足</li>\n                    <li>🌉 周庄门票100元含游船；建议网上提前购票，避免排队</li>\n                    <li>🛶 周庄摇橹船约50元/人，水巷穿行是精华体验</li>\n                    <li>🍜 周庄美食：万三蹄（浓油赤酱）、阿婆茶、清明青团</li>\n                    <li>🚗 苏州到周庄约40km，自驾1小时；周庄停车较贵（50元/次）</li>\n                    <li>🗺️ 苏州地铁1号线覆盖主要景区；建议住平江路/山塘街附近</li>\n                    <li>📅 明日预告：苏州 → 杭州（自驾1.5小时）or 无锡太湖</li>'
    )
    content = content.replace('最后更新：2026年5月22日（周五）', '最后更新：2026年5月23日（周六）')
    print('Updated footer travel tips')
else:
    print('Footer tips not found, skipping')

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