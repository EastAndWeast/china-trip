# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 35 content for March 23, 2026
day_35 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第35天</span>
                    <span class="day-date">2026-03-23 · 三月初四</span>
                </div>
                <div class="day-title">🚗 黄山到杭州 · 西湖春天模式</div>
                <div class="day-content">
                    <p>告别黄山，驱车前往"上有天堂，下有苏杭"的杭州！</p>
                    <p>🏔️ 黄山总结：世界文化与自然双重遗产，奇松、怪石、云海、温泉名不虚传</p>
                    <p>🚗 今日车程约280公里，从黄山到杭州，全程高速约3.5小时</p>
                    <p>下午抵达杭州后，入住西湖附近的酒店，推窗就能看到西湖美景！</p>
                    <p>🌸 西湖春天：苏堤春晓、柳浪闻莺，三月的西湖宛如一幅水彩画卷</p>
                    <p>趁着傍晚时分，沿着西湖散步，杨柳依依，春风拂面，非常惬意！</p>
                    <p>🍜 晚上在河坊街品尝了杭州特色美食：东坡肉、片儿川、叫化鸡</p>
                    <p>🚶 河坊街：杭州最具烟火气的历史街区，夜景别有一番风味</p>
                    <p>📅 特别提示：西湖景区3月7日已开启春季旅游旺季模式！</p>
                    <p>🎯 明天计划：灵隐寺、西湖游船、龙井村问茶</p>
                    <p>📊 今日行程：黄山到杭州，约280公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🚗</div>
                    <div class="photo-placeholder">🌸</div>
                    <div class="photo-placeholder">🍜</div>
                </div>
            </div>
'''

# Find Day 34 position and insert Day 35 after it
pattern = r'(<span class="day-number">第34天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_35 + content[insert_pos:]
    
    # Update day count 34 -> 35
    new_content = re.sub(
        r'<div class="stat-value" id="dayCount">(\d+)</div>', 
        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>', 
        new_content
    )
    
    # Update km count +280km (Huangshan to Hangzhou)
    new_content = re.sub(
        r'<div class="stat-value" id="kmCount">(\d+)</div>', 
        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 280}</div>', 
        new_content
    )
    
    # Update location count 23 -> 24
    new_content = re.sub(
        r'<div class="stat-value" id="locationCount">(\d+)</div>', 
        lambda m: f'<div class="stat-value" id="locationCount">{int(m.group(1)) + 1}</div>', 
        new_content
    )
    
    # Update current location
    new_content = re.sub(
        r'<span>当前所在：<strong id="currentLocation">[^<]+</strong></span>',
        '<span>当前所在：<strong id="currentLocation">杭州 · 西湖景区</strong></span>',
        new_content
    )
    
    # Update travel tips to March 23, 2026 - now covering Hangzhou/Suzhou area
    tips_content = '''<div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年3月杭州苏州旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏙️ 杭州："上有天堂，下有苏杭"，西湖是中国最著名的湖泊之一</li>
                    <li>📍 位置：浙江省杭州市，西湖位于市区中心，免费开放</li>
                    <li>🌸 春季（3-5月）是杭州最美季节，西湖苏堤春晓、柳浪闻莺等景色绝美</li>
                    <li>🎫 西湖：免费5A级景区，游船另收费；灵隐寺门票45元</li>
                    <li>🚇 交通：3月7日-5月31日西湖景区实行春季旅游旺季模式，推荐地铁+公交出行</li>
                    <li>🍜 美食：东坡肉、片儿川、叫化鸡、龙井虾仁、西湖醋鱼</li>
                    <li>🏯 河坊街：杭州最有烟火气的历史街区，夜晚景色别具风味</li>
                    <li>🌿 龙井村：杭州龙井茶产地，可品茶赏景体验茶文化</li>
                    <li>📸 最佳拍摄点：断桥残雪、雷峰塔、三潭印月、苏堤</li>
                    <li>🏔️ 苏州："君到姑苏见，人家尽枕河"，世界园林之城</li>
                    <li>🌸 苏州国际旅游年·春天旅游季进行中（3月21日启幕），碧螺春茶文化体验</li>
                    <li>🏯 苏州园林：拙政园（淡季70元）、留园、网师园等世界文化遗产</li>
                    <li>🌧️ 春季天气：10-22°C，早晚温差大，偶尔春雨，建议"洋葱式"穿衣</li>
                    <li>🛶 水乡古镇：周庄、同里、木渎、甪直，江南水乡韵味十足</li>
                    <li>⚠️ 注意：春季旅游旺季，周末游客较多，建议早出晚归错峰出行</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年3月23日</p>
            </div>'''
    
    # Replace old tips
    old_tips_pattern = r'<div style="margin-top: 20px; padding: 15px; background: rgba\(255,255,255,0\.1\); border-radius: 10px; text-align: left;">.*?</div>\s*</div>\s*</div>\s*</div>\s*</body>'
    new_content = re.sub(old_tips_pattern, tips_content + '\n        </div>\n    </div>\n</body>', new_content, re.DOTALL)
    
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully updated index.html with Day 35!')
    print('Updated stats: dayCount 34->35, locationCount 23->24, kmCount +280')
    print('Current location: 杭州 · 西湖景区')
    print('Travel tips updated to March 23, 2026: Hangzhou + Suzhou area')
else:
    print('Could not find Day 34 position!')
