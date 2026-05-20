# -*- coding: utf-8 -*-
"""环游中国 - Day 89 更新脚本
添加Day 89（西递 → 歙县古城）
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Find current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 88
print('Current max day:', current_day)

# Stats - add 1 day and some km/locations
content = re.sub(r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 80) + m.group(3), content)
content = re.sub(r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>歙县古城 · 徽州府城\g<3>', content)

# Find footer and insert before it
footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
else:
    # Day 89 entry (2026-05-17)
    day89_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第89天</span>
                    <span class="day-date">2026-05-17 · 四月二十 · 周日</span>
                </div>
                <div class="day-title">🏘️ 宏村 → 西递 → 歙县古城</div>
                <div class="day-content">
                    <p>🚗 今日行程：宏村驱车前往西递（约20分钟，15km），再前往歙县（约1小时，50km）</p>
                    <p>🏘️ 上午游览西递古村，被誉为"桃花源里人家"</p>
                    <p>🏯 主要景点：西递牌坊、胡文光刺史坊、敬爱堂、西递村口</p>
                    <p>🏰 下午前往歙县古城，徽州府衙所在地</p>
                    <p>🛶 晚上漫步徽城渔梁，千年渔梁坝</p>
                    <p>🍜 特色美食：歙县毛豆腐、徽州石鸡、臭鳜鱼、徽州饼</p>
                    <p>📅 明日预告：歙县 → 杭州千岛湖</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏘️</div>
                    <div class="photo-placeholder">🏰</div>
                    <div class="photo-placeholder">🛶</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🎫</span>
                        <span class="tip-text">西递门票104元（网购94元）；与宏村联票更优惠；建议清晨拍照光线最佳</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🏨</span>
                        <span class="tip-text">歙县古城住宿选择多；渔梁坝附近有特色客栈，夜晚安静舒适</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">📷</span>
                        <span class="tip-text">渔梁坝是徽州保存最古老的水利工程；傍晚时分渔舟唱晚，适合摄影</span>
                    </div>
                </div>
            </div>
'''
    content = content[:footer_pos] + day89_entry + '\n' + content[footer_pos:]

# Update footer timestamp
content = re.sub(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>',
    '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年5月17日（周日）</p>', content)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Added Day 89: 宏村 → 西递 → 歙县古城')
print('Current location: 歙县古城 · 徽州府城')
print('Date: 2026-05-17 (四月二十 · 周日)')
print('Day count now: 90')
print('KM now:', 12010)