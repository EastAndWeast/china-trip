# -*- coding: utf-8 -*-
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Read file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Old tips block to replace
old_tips_start = '<div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">'
old_tips_end = '</div>\n        </div>\n    </div>\n</body>\n</html>'

# Find the old tips block
start_idx = content.find(old_tips_start)
if start_idx == -1:
    print('Could not find old tips start marker!')
    # Try alternate
    alt_marker = '安徽旅游贴士'
    idx = content.find(alt_marker)
    if idx != -1:
        print(f'Found alt marker at index {idx}')
        # Find the div before it
        start_idx = content.rfind('<div style="margin-top', 0, idx)
        print(f'Found div start at {start_idx}')
    else:
        print('Could not find any tips marker!')
        sys.exit(1)

# Find the end
end_marker = '</body>'
end_idx = content.find(end_marker, start_idx)
if end_idx == -1:
    print('Could not find end marker!')
    sys.exit(1)

# New tips
new_tips = '''<div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年3月江浙沪旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🌸 西湖景区：3月21日起已进入春季旅游旺季模式，建议错峰出行</li>
                    <li>🏯 灵隐寺：门票45元，建议早上去避开人流，需提前预约</li>
                    <li>🍵 龙井村：明前龙井正值采摘季，茶农家品茶体验不容错过</li>
                    <li>🛶 西湖游船：建议乘坐手摇船或游船，可游览苏堤、三潭印月</li>
                    <li>🏯 苏州园林：拙政园、留园、虎丘，春季园林赏花最佳时节</li>
                    <li>🌉 乌镇：春季烟雨水乡，东栅西栅联票更优惠</li>
                    <li>🌆 上海：3月天气宜人，外滩、陆家嘴、田子坊值得一去</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年3月25日</p>
            </div>
        </div>
    </body>
</html>'''

new_content = content[:start_idx] + new_tips

# Write back
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Successfully updated travel tips!')
print('Old block removed, new tips added.')
