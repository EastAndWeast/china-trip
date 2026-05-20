# -*- coding: utf-8 -*-
"""Add Day 47 - Suzhou Day 2 and update travel tips - April 4, 2026"""
import re, sys, codecs, json, os
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

index_path = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check if Day 47 already exists
if '第47天' in content:
    print('Day 47 already exists!')
else:
    # Day 47 content - Suzhou Day 2
    day_47 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第47天</span>
                    <span class="day-date">2026-04-04 · 三月十八</span>
                </div>
                <div class="day-title">🏯 苏州 · 拙政园与狮子林</div>
                <div class="day-content">
                    <p>🌸 苏州第二天！今天游览苏州最具代表性的园林！</p>
                    <p>🏯 上午前往拙政园——中国四大名园之首！</p>
                    <p>🌺 拙政园：始建于明正德年间，占地约78亩，以水为中心，山水萦绕</p>
                    <p>4月的拙政园春花烂漫，玉兰、海棠、琼花次第开放，美不胜收！</p>
                    <p>🦁 下午游览狮子林——以假山著称的禅意园林</p>
                    <p>⛰️ 狮子林：假山群峰起伏，最高峰约12米，有"假山王国"之誉</p>
                    <p>穿行于假山迷宫中，仿佛进入了一座石头动物园，十分有趣！</p>
                    <p>🏛️ 傍晚参观苏州博物馆——贝聿铭设计！</p>
                    <p>🏛️ 苏州博物馆：建筑大师贝聿铭封山之作，粉墙黛瓦，山水园林融入现代设计</p>
                    <p>免费开放，需提前预约，建筑本身就是一件艺术品！</p>
                    <p>📊 今日行程：拙政园 + 狮子林 + 苏博，步行约12公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">🌺</div>
                    <div class="photo-placeholder">🏛️</div>
                </div>
            </div>
'''
    
    # Find Day 46 position and insert Day 47 after it
    pattern = r'(<span class="day-number">第46天</span>.*?</div>\s*</div>\s*</div>)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        insert_pos = match.end()
        content = content[:insert_pos] + day_47 + content[insert_pos:]
        print('✅ Added Day 47: 苏州 · 拙政园与狮子林')
    else:
        print('⚠️ Could not find Day 46 position, appending to timeline end')
        # Find timeline end
        timeline_match = re.search(r'(<div class="timeline">.*?)</div>\s*<div class="footer">', content, re.DOTALL)
        if timeline_match:
            end_pos = timeline_match.end()
            content = content[:end_pos] + day_47 + content[end_pos:]

# Update statistics
content = re.sub(
    r'<div class="stat-value" id="dayCount">(\d+)</div>',
    lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>',
    content
)
print('✅ Updated dayCount')

# Update last update time
content = re.sub(
    r'最后更新：\d+年\d+月\d+日',
    '最后更新：2026年4月4日',
    content
)
print('✅ Updated last update date')

# Update travel tips section for April
old_tips_pattern = r'<div style="margin-top: 20px; padding: 15px; background: rgba\(255,255,255,0\.1\); border-radius: 10px; text-align: left;">.*?</div>\s*</div>\s*</div>\s*</div>\s*</body>'

new_tips = '''<div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年4月江浙沪旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🌸 苏州园林：拙政园、留园、狮子林春季赏花正当时，4月游客增多建议早出发</li>
                    <li>🏯 苏州博物馆：贝聿铭设计，免费需预约，建筑本身就是艺术品</li>
                    <li>🌉 平江路：800米古街保存完整，小桥流水，免费漫步，两旁评弹茶馆韵味十足</li>
                    <li>🌙 金鸡湖夜景：摩天轮灯光秀每晚亮起，诚品书店、月光码头值得一看</li>
                    <li>🍜 苏州美食：松鼠桂鱼、碧螺虾仁、苏式汤面、糕团点心，观前街选择丰富</li>
                    <li>🌸 扬州烟花节：2026年4月18日开幕，持续一个月，瘦西湖夜游别错过</li>
                    <li>🏯 无锡灵山：灵山大佛、拈花湾禅意小镇，春日祈福好去处</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月4日</p>
            </div>
        </div>
    </body>
</html>'''

new_content = re.sub(old_tips_pattern, new_tips, content, flags=re.DOTALL)
if new_content != content:
    print('✅ Updated travel tips for April 2026')
else:
    print('⚠️ Travel tips pattern did not match, trying alternate pattern')
    # Try simpler pattern
    simple_pattern = r'(最后更新：\d+年\d+月\d+日)(?=\s*</p>\s*</div>\s*</div>\s*</body>)'
    simple_replacement = '最后更新：2026年4月4日'
    new_content = re.sub(simple_pattern, simple_replacement, content)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('\n✅ Website updated successfully!')
print('Day 47: 苏州 · 拙政园与狮子林 (2026-04-04)')
print('Updated: 2026年4月4日')
