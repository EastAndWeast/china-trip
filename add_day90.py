# -*- coding: utf-8 -*-
"""环游中国 - Day 90 更新脚本
添加Day 90（歙县 → 千岛湖）
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats - add 1 day and some km/locations
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 200) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>千岛湖 · 湖光山色\g<3>', content)

# Find footer and insert before it
footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
else:
    # Day 90 entry (2026-05-18)
    day90_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第90天</span>
                    <span class="day-date">2026-05-18 · 四月二十一 · 周一</span>
                </div>
                <div class="day-title">🛶 歙县 → 千岛湖 · 天下第一秀水</div>
                <div class="day-content">
                    <p>🚗 今日行程：歙县驱车前往千岛湖（约2.5小时，180km）</p>
                    <p>🛶 上午离开歙县，沿徽杭高速前往千岛湖</p>
                    <p>🚤 下午乘船游览千岛湖中心湖区</p>
                    <p>🏝️ 主要景点：梅峰岛（登高观千岛湖）、月光岛、渔乐岛、龙山岛</p>
                    <p>🍜 千岛湖特色美食：千岛湖鱼头（必吃！）、银鱼羹、笋干烧肉</p>
                    <p>🌙 晚上入住千岛湖边酒店/民宿，品鱼头赏湖景</p>
                    <p>📅 明日预告：千岛湖深度游 or 前往杭州</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🛶</div>
                    <div class="photo-placeholder">🏝️</div>
                    <div class="photo-placeholder">🌅</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🚤</span>
                        <span class="tip-text">千岛湖中心湖区船票+门票185元（网购175元）；建议早起乘首班船</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🏨</span>
                        <span class="tip-text">千岛湖镇住宿选择多（200-500元/晚）；湖景房推荐</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🐟</span>
                        <span class="tip-text">千岛湖鱼头是招牌，推荐"有机鱼头"；渔乐岛有鱼汤免费品尝</span>
                    </div>
                </div>
            </div>

'''
    content = content[:footer_pos] + day90_entry + content[footer_pos:]
    print('Added Day 90 entry')

# Update footer travel tips
old_footer_tips = '''📰 2026年5月庐山旅游贴士'''
new_footer_tips = '''📰 2026年5月千岛湖旅游贴士'''
if old_footer_tips in content:
    content = content.replace(old_footer_tips, new_footer_tips)
    content = content.replace(
        '''<li>🏔️ 庐山门票160元+景区巴士70元，自驾车不能上山需换乘</li>
                    <li>🌫️ 庐山海拔1474米，山上比山下低10度，带外套防寒</li>
                    <li>🗻 如琴湖+花径+仙人洞：牯岭镇周边经典游览路线</li>
                    <li>🏨 牯岭镇住宿方便，节假日提前订房</li>
                    <li>🌄 含鄱口是看日出和鄱阳湖的最佳地点</li>
                    <li>🍜 庐山三石（石鱼、石鸡、石耳）值得品尝</li>
                    <li>📅 明日预告：庐山深度游——五老峰、三叠泉</li>''',
        '''<li>🏝️ 千岛湖中心湖区船票185元（含3岛）；网购175元，建议提前订票</li>
                    <li>🚤 游船分上午班（8:30）和下午班（12:30），游览约5小时</li>
                    <li>⛰️ 梅峰岛是最佳观景岛，徒步15分钟或乘索道（60元）</li>
                    <li>🏨 千岛湖镇住宿集中，湖景房400-800元；中心湖区酒店更贵</li>
                    <li>🐟 千岛湖鱼头是招牌（人均80-150元）；推荐"鱼味馆"等老店</li>
                    <li>🚗 杭州到千岛湖约2小时（杭新景高速）；淳安县可坐船进岛</li>
                    <li>📅 明日预告：千岛湖 → 杭州（西湖）or 继续湖中岛屿游</li>'''
    )
    content = content.replace('最后更新：2026年5月17日（周日）', '最后更新：2026年5月18日（周一）')
    print('Updated footer travel tips')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print('HTML updated successfully')

# Verify
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    verify = f.read()
day90_check = '第90天' in verify
day91_check = re.findall(r'class="day-number">第(\d+)天', verify)
print('Day 90 added:', day90_check)
print('Last 3 day numbers:', day91_check[-3:] if day91_check else 'none')