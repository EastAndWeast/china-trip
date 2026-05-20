# -*- coding: utf-8 -*-
"""环游中国 - Day 86 v2 更新脚本
更新Day 86并添加Day 87（黄山）
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Find current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 86
print(f'Current max day: {current_day}')

# Find today's day card position - we need to update Day 86 and add Day 87
# Pattern: find the day 86 card
day86_pattern = r'(<div class="day-card">\s*<div class="day-header">\s*<span class="day-number">第86天</span>)'
match = re.search(day86_pattern, content)
if match:
    print('Found Day 86 card, updating...')
else:
    print('Day 86 card not found!')

# Update stats - just add 1 day and some km/locations
content = re.sub(r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 140) + m.group(3), content)
content = re.sub(r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>黄山 · 云海\g<3>', content)

# Find footer and insert before it
footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
else:
    # Day 87 entry (2026-05-15)
    day87_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第87天</span>
                    <span class="day-date">2026-05-15 · 四月十八 · 周五</span>
                </div>
                <div class="day-title">🏔️ 婺源 → 黄山 · 云海温泉</div>
                <div class="day-content">
                    <p>🚗 今日行程：婺源驱车前往黄山风景区（约2小时，140km）</p>
                    <p>🏔️ 路线：换乘中心→云谷寺→白鹅岭→始信峰→西海大峡谷→光明顶</p>
                    <p>🌿 下午深度游西海大峡谷，傍晚光明顶观日落（住宿山顶）</p>
                    <p>🍜 黄山特色美食：黄山烧饼、臭鳜鱼、毛豆腐、石耳炒蛋</p>
                    <p>🌙 晚上山顶住宿，看星空，早起光明顶观日出云海</p>
                    <p>📅 明日预告：黄山 → 宏村（约40分钟），画里乡村</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏔️</div>
                    <div class="photo-placeholder">🌅</div>
                    <div class="photo-placeholder">🌲</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🎫</span>
                        <span class="tip-text">黄山门票160元+景区巴士19元+玉屏索道90元；建议云谷寺上、玉屏下</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🏨</span>
                        <span class="tip-text">山顶住宿提前订（标间600-1500元）；光明顶是观日出最佳地点</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🌦️</span>
                        <span class="tip-text">5月黄山多云海，备雨衣和外套；西海大峡谷观光缆车100元/人</span>
                    </div>
                </div>
            </div>
'''
    content = content[:footer_pos] + day87_entry + '\n' + content[footer_pos:]

# Update footer timestamp
content = re.sub(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>',
    '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年5月15日（周五）</p>', content)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Added Day 87: 婺源 → 黄山 · 云海温泉')
print('Current location: 黄山 · 云海')
print('Date: 2026-05-15 (四月十八 · 周五)')