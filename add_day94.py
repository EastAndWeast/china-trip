# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount=93, add 1 day and ~100km
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 100) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>苏州 · 拙政园\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

day94_entry = (
    '\n            <div class="day-card">\n'
    '                <div class="day-header">\n'
    '                    <span class="day-number">94</span>\n'
    '                    <span class="day-date">2026-05-22 · 四月廿五 · 周五</span>\n'
    '                </div>\n'
    '                <div class="day-title">🏛️ 乌镇 → 苏州 · 江南园林之冠</div>\n'
    '                <div class="day-content">\n'
    '                    <p>🚗 今日行程：乌镇 → 苏州（自驾约100km，1.5小时）</p>\n'
    '                    <p>🏛️ 上午：抵达苏州，前往拙政园（门票70元，建议7:30开门就到）</p>\n'
    '                    <p>🚶 游览路线：拙政园 → 苏州博物馆（贝聿铭设计，免费）→ 狮子林</p>\n'
    '                    <p>🍜 中午：平江路历史街区（苏州小吃：苏帮菜、松鼠桂鱼、蟹壳黄）</p>\n'
    '                    <p>🛶 下午：山塘街（千年古街，夜景绝美）→ 虎丘（云岩寺塔）</p>\n'
    '                    <p>🌙 晚上：山塘街夜景，乘手摇船（50元/人）穿行水巷</p>\n'
    '                    <p>🏨 住宿推荐：苏州老城区（平江路/山塘街附近），体验苏式慢生活</p>\n'
    '                    <p>📅 明日预告：苏州——寒山寺 or 周庄水乡（自驾1小时）</p>\n'
    '                </div>\n'
    '                <div class="photos">\n'
    '                    <div class="photo-placeholder">🏛️</div>\n'
    '                    <div class="photo-placeholder">🛶</div>\n'
    '                    <div class="photo-placeholder">🌙</div>\n'
    '                </div>\n'
    '                <div class="tips">\n'
    '                    <div class="tip">\n'
    '                        <span class="tip-icon">🏛️</span>\n'
    '                        <span class="tip-text">拙政园门票70元，旺季建议提前网上购票；7:30开门尽量早到</span>\n'
    '                    </div>\n'
    '                    <div class="tip">\n'
    '                        <span class="tip-icon">🏛️</span>\n'
    '                        <span class="tip-text">苏州博物馆免费（周一闭馆），贝聿铭设计，需提前预约</span>\n'
    '                    </div>\n'
    '                    <div class="tip">\n'
    '                        <span class="tip-icon">🌙</span>\n'
    '                        <span class="tip-text">山塘街夜景是精华；推荐傍晚去，先逛古街再等天黑看灯景</span>\n'
    '                    </div>\n'
    '                </div>\n'
    '            </div>\n'
    '\n'
)

content = content[:footer_pos] + day94_entry + content[footer_pos:]
print('Added Day 94 entry')

old_footer_tips = '📰 2026年5月乌镇水乡旅游贴士'
new_footer_tips = '📰 2026年5月苏州园林旅游贴士'
if old_footer_tips in content:
    content = content.replace(old_footer_tips, new_footer_tips)
    content = content.replace(
        '<li>🌉 乌镇西栅建议8:30开门就到；联票200元，东西栅联游更划算</li>\n                    <li>🚢 摇橹船水巷游览（约60元/人），清晨或傍晚光线最美</li>\n                    <li>🍜 西栅美食：书生羊肉面、定胜糕、乌镇粽子、姑嫂饼</li>\n                    <li>🏨 西栅临水民宿需提前预约；五一/十一等节假日很抢手</li>\n                    <li>🌙 西栅夜景是精华，红灯笼+倒影绝美，建议住景区内</li>\n                    <li>🚗 杭州到乌镇约75km，自驾1小时；也可在杭州九堡客运站坐大巴</li>\n                    <li>📅 明日预告：乌镇 → 苏州（自驾1.5小时），或继续杭州深度游</li>',
        '<li>🏛️ 拙政园门票70元（旺季建议提前订票），7:30开门，建议一早就去</li>\n                    <li>🏛️ 苏州博物馆免费，周一闭馆，贝聿铭设计，需提前在公众号预约</li>\n                    <li>🛶 山塘街手摇船约50元/人；傍晚去光线最美，夜景绝伦</li>\n                    <li>🍜 平江路美食：松鹤楼（苏帮菜老字号）、蟹壳黄、绿豆糕</li>\n                    <li>🚗 乌镇到苏州约100km，自驾1.5小时；苏州老城区停车较贵</li>\n                    <li>🗺️ 苏州地铁1号线覆盖主要景区；建议住平江路/山塘街附近</li>\n                    <li>📅 明日预告：苏州——寒山寺 or 周庄/同里水乡（自驾1小时）</li>'
    )
    content = content.replace('最后更新：2026年5月21日（周四）', '最后更新：2026年5月22日（周五）')
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