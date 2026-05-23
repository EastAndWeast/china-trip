# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 80) + m.group(3), content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

day93_entry = (
    '\n            <div class="day-card">\n'
    '                <div class="day-header">\n'
    '                    <span class="day-number">93</span>\n'
    '                    <span class="day-date">2026-05-21 · 四月廿四 · 周四</span>\n'
    '                </div>\n'
    '                <div class="day-title">🌉 乌镇西栅 · 江南水乡最后的枕水人家</div>\n'
    '                <div class="day-content">\n'
    '                    <p>🚗 今日行程：杭州 → 乌镇西栅（自驾约75km，1小时）</p>\n'
    '                    <p>🌉 上午：抵达乌镇西栅景区（门票200元，建议8:30开门就到）</p>\n'
    '                    <p>🚶 游览路线：木心美术馆 → 灵水居 → 司马第 → 露天戏台</p>\n'
    '                    <p>🚢 特色体验：乘坐摇橹船（60元/人）穿行水巷，限高1.2m需低头</p>\n'
    '                    <p>🏠 中午：西栅老街传统小吃（书生羊肉面、定胜糕、乌镇粽子）</p>\n'
    '                    <p>🌿 下午：乌镇互联网国际会展中心（建筑师王澍作品）</p>\n'
    '                    <p>🌙 晚上：西栅夜色——红灯笼倒映水面，体验水乡夜景</p>\n'
    '                    <p>🏨 住宿推荐：乌镇西栅景区内临水民宿（需提前预约，节假日较贵）</p>\n'
    '                    <p>📅 明日预告：乌镇 → 苏州（自驾约1.5小时），或返回杭州</p>\n'
    '                </div>\n'
    '                <div class="photos">\n'
    '                    <div class="photo-placeholder">🌉</div>\n'
    '                    <div class="photo-placeholder">🚢</div>\n'
    '                    <div class="photo-placeholder">🌙</div>\n'
    '                </div>\n'
    '                <div class="tips">\n'
    '                    <div class="tip">\n'
    '                        <span class="tip-icon">🌉</span>\n'
    '                        <span class="tip-text">乌镇西栅门票200元，东西栅联票200元；建议网上提前购票</span>\n'
    '                    </div>\n'
    '                    <div class="tip">\n'
    '                        <span class="tip-icon">🚢</span>\n'
    '                        <span class="tip-text">摇橹船水巷游览（约60元/人），清晨或傍晚光线最美</span>\n'
    '                    </div>\n'
    '                    <div class="tip">\n'
    '                        <span class="tip-icon">🏨</span>\n'
    '                        <span class="tip-text">西栅临水民宿需提前预约；临水标间约400-800元，含景区门票</span>\n'
    '                    </div>\n'
    '                </div>\n'
    '            </div>\n'
    '\n'
)

content = content[:footer_pos] + day93_entry + content[footer_pos:]
print('Added Day 93 entry')

old_footer_tips = '📰 2026年5月杭州深度游贴士'
new_footer_tips = '📰 2026年5月乌镇水乡旅游贴士'
if old_footer_tips in content:
    content = content.replace(old_footer_tips, new_footer_tips)
    content = content.replace(
        '<li>⛩️ 灵隐寺7:00开门，建议早去；永福寺免费，紧邻灵隐更清静</li>\n                    <li>🏯 胡庆余堂（河坊街）"江南药王"，清代徽派商业建筑，门票免费</li>\n                    <li>🚢 京杭大运河夜游（拱宸桥-武林门，约60元，45分钟）</li>\n                    <li>🍜 河坊街美食：知味观（片儿川）、菊英面馆、定胜糕、葱包烩</li>\n                    <li>🚇 杭州地铁3号线后通段已开通，武林广场可换乘</li>\n                    <li>🚗 宋城（1小时）或乌镇（1.5小时）可当日往返</li>\n                    <li>📅 明日预告：杭州——宋城千古情 or 乌镇西栅夜景</li>',
        '<li>🌉 乌镇西栅建议8:30开门就到；联票200元，东西栅联游更划算</li>\n                    <li>🚢 摇橹船水巷游览（约60元/人），清晨或傍晚光线最美</li>\n                    <li>🍜 西栅美食：书生羊肉面、定胜糕、乌镇粽子、姑嫂饼</li>\n                    <li>🏨 西栅临水民宿需提前预约；五一/十一等节假日很抢手</li>\n                    <li>🌙 西栅夜景是精华，红灯笼+倒影绝美，建议住景区内</li>\n                    <li>🚗 杭州到乌镇约75km，自驾1小时；也可在杭州九堡客运站坐大巴</li>\n                    <li>📅 明日预告：乌镇 → 苏州（自驾1.5小时），或继续杭州深度游</li>'
    )
    content = content.replace('最后更新：2026年5月20日（周三）', '最后更新：2026年5月21日（周四）')
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
print('Stats: dayCount=%s, kmCount=%s' % (
    day_match.group(1) if day_match else '?',
    km_match.group(1) if km_match else '?'
))