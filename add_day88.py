# -*- coding: utf-8 -*-
"""环游中国 - Day 88 更新脚本
更新Day 87并添加Day 88（宏村）
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Find current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 87
print(f'Current max day: {current_day}')

# Update stats - add 1 day and some km/locations
content = re.sub(r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 45) + m.group(3), content)
content = re.sub(r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>宏村 · 画里乡村\g<3>', content)

# Find footer and insert before it
footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
else:
    # Day 88 entry (2026-05-16)
    day88_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第88天</span>
                    <span class="day-date">2026-05-16 · 四月十九 · 周六</span>
                </div>
                <div class="day-title">🏡 黄山 → 宏村 · 画里乡村</div>
                <div class="day-content">
                    <p>🚗 今日行程：黄山风景区驱车前往宏村（约40分钟，30km）</p>
                    <p>🏡 上午游览宏村景区，中国画里乡村</p>
                    <p>🏯 主要景点：南湖书院、月沼、乐叙堂、敬德堂、敬修堂</p>
                    <p>🌸 下午漫步村中，感受徽派建筑与水系完美融合</p>
                    <p>🍜 宏村特色美食：宏村毛豆腐、乌米饭、腊八豆腐、蟹壳黄烧饼</p>
                    <p>🌙 晚上入住宏村内特色民宿，体验徽派庭院</p>
                    <p>📅 明日预告：宏村 → 西递 → 歙县古城</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏡</div>
                    <div class="photo-placeholder">🌸</div>
                    <div class="photo-placeholder">🏯</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🎫</span>
                        <span class="tip-text">宏村门票104元（网购94元）；建议请导游讲解100元/次</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🏨</span>
                        <span class="tip-text">村内民宿体验徽派生活；月沼附近景观最佳，建议日出时段拍照</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">📷</span>
                        <span class="tip-text">南湖和月沼是最佳拍摄点；清晨6点前游客少，光线美</span>
                    </div>
                </div>
            </div>
'''
    content = content[:footer_pos] + day88_entry + '\n' + content[footer_pos:]

# Update footer timestamp
content = re.sub(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>',
    '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年5月16日（周六）</p>', content)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Added Day 88: 黄山 → 宏村 · 画里乡村')
print('Current location: 宏村 · 画里乡村')
print('Date: 2026-05-16 (四月十九 · 周六)')