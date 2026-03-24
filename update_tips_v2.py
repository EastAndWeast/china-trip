# -*- coding: utf-8 -*-
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Read file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# New travel tips based on latest search results
old_pattern = r'<div style="margin-top: 20px; padding: 15px; background: rgba\(255,255,255,0\.1\); border-radius: 10px; text-align: left;">.*?</div>\s*</div>\s*</div>\s*</div>\s*</body>'

new_tips = '''<div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年3月江浙沪旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🌸 西湖景区：3月21日起已进入春季旅游旺季模式，建议错峰出行</li>
                    <li>🏯 灵隐寺：门票45元，建议早上去避开人流，需提前预约</li>
                    <li>🍵 龙井村：明前龙井正值采摘季，茶农家品茶体验不容错过</li>
                    <li>🛶 西湖游船：建议乘坐手摇船或游船，可游览苏堤、三潭印月</li>
                    <li>🏯 苏州园林：拙政园、留园、虎丘，春季园林赏花最佳时节</li>
                    <li>🌉 乌镇：春季烟雨水乡， 东栅西栅联票更优惠</li>
                    <li>🌆 上海：3月天气宜人，外滩、陆家嘴、田子坊值得一去</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年3月25日</p>
            </div>
        </div>
    </body>
</html>'''

new_content = re.sub(old_pattern, new_tips, content, flags=re.DOTALL)

# Write back
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Successfully updated travel tips!')
