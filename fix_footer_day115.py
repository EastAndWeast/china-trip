# -*- coding: utf-8 -*-
"""Fix Day 115 footer - replace tips section with new 杭州深度游 content
The previous add_day115.py only updated the last-update line via fallback.
Now do the full footer replacement with verified actual content.
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = r'C:\Users\admin\.openclaw\workspace\china-trip\index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Use regex to find the inner <p style="font-size: 14px;..."> and <ul>...</ul> and <p>最后更新</p>
# This is more robust than exact string match

old_pattern = re.compile(
    r'(<p style="font-size: 14px; margin-bottom: 10px;">)([^<]+)(</p>\s*<ul style="font-size: 12px; opacity: 0\.8; padding-left: 20px;">)(.*?)(</ul>\s*<p style="margin-top: 15px; font-size: 11px; opacity: 0\.6;">最后更新：)([^<]+)(</p>)',
    re.DOTALL
)

m = old_pattern.search(content)
if not m:
    print('ERROR: footer pattern not found')
    sys.exit(1)

print('Found footer block')
print('Old title:', repr(m.group(2)[:80]))
print('Old last update:', repr(m.group(6)))

new_title = '📰 2026年6月浙东·杭州深度游+4 大世界遗产一线贴士'
new_li_items = '''                    <li>⛰️ 飞来峰 5A + UNESCO（西湖文化景观 2011）！五代十国至元代 380+ 摩崖石刻造像；青林洞卢舍那佛会浮雕为北宋巅峰</li>
                    <li>🙏 灵隐寺门票 30元 7:00-18:15；始建 328 AD（东晋）印度僧人慧理；19m 释迦牟尼坐像 / 500 罗汉 / 大雄宝殿</li>
                    <li>🍵 龙井村"狮"字号（狮峰龙井）是西湖龙井顶级！明前 5800/斤 / 雨前 2800/斤；老龙井/十八棵御茶/胡公庙必看</li>
                    <li>🌉 京杭大运河 2014 UNESCO 世界文化遗产！始建春秋（前 486 邗沟）隋炀帝 610 贯通；拱宸桥明崇祯四年（1631）重建</li>
                    <li>🚢 运河夜游"钱运号"180元/人 19:00 90min；19 座古桥亮灯；武林广场音乐喷泉免费 19:30/20:30</li>
                    <li>🚇 杭州市内 1/5 号线串联灵隐-运河；天竺三寺联票 10元；6/12 多云 34/24℃ 梅雨季初期最佳出游日</li>
                    <li>📅 明日预告：杭州→ 苏州（170km 园林/评弹/苏帮菜）/ 上海（180km 高铁 1h）/ 千岛湖（150km G2504 高速 2h）</li>'''
new_last_update = '2026年6月12日（周五）'

replacement = m.group(1) + new_title + m.group(3) + '\n' + new_li_items + '\n                ' + m.group(5) + new_last_update + m.group(7)

new_content = old_pattern.sub(lambda mm: replacement, content, count=1)
if new_content == content:
    print('ERROR: replacement did not change content')
    sys.exit(1)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Footer replaced successfully')

# Verify
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    verify = f.read()

# Find the new footer block
m = re.search(r'<div class="footer">.*?</div>\s*</div>\s*</body>', verify, re.DOTALL)
if m:
    raw = m.group(0)
    for i, line in enumerate(raw.split('\n')):
        print(f'{i:3d}: {line[:200]}')

# Sanity checks
if '杭州深度游+4 大世界遗产' in verify:
    print('\n✅ New footer title present')
if '最后更新：2026年6月12日（周五）' in verify:
    print('✅ Last update is 2026-06-12 周五')
