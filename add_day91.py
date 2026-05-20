# -*- coding: utf-8 -*-
"""环游中国 - Day 91 更新脚本
添加Day 91（千岛湖 → 杭州西湖）
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats - add 1 day and ~260km/1 location
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 260) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>杭州 · 西湖\g<3>', content)

# Find footer and insert before it
footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
else:
    # Day 91 entry (2026-05-19)
    day91_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第91天</span>
                    <span class="day-date">2026-05-19 · 四月二十二 · 周二</span>
                </div>
                <div class="day-title">🌸 千岛湖 → 杭州西湖 · 人间天堂</div>
                <div class="day-content">
                    <p>🚗 今日行程：千岛湖驱车前往杭州（约2小时，180km）</p>
                    <p>🌸 上午：抵达杭州，前往西湖景区（免费）</p>
                    <p>🚶 游览路线：断桥残雪 → 白堤 → 苏堤春晓 → 曲院风荷</p>
                    <p>🛶 下午：乘船游西湖（55元船票），登小瀛洲看三潭印月</p>
                    <p>🌅 傍晚：雷峰塔观日落（40元门票），眺望西湖全景</p>
                    <p>🍜 杭州特色美食：东坡肉、西湖醋鱼、龙井虾仁、叫化童鸡</p>
                    <p>🌙 晚上入住西湖边酒店/湖滨路商圈，品杭帮菜</p>
                    <p>📅 明日预告：杭州深度游——灵隐寺、宋城、河坊街</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌸</div>
                    <div class="photo-placeholder">🛶</div>
                    <div class="photo-placeholder">🌅</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🌸</span>
                        <span class="tip-text">西湖景区免费开放；游船55元（普通画坊）/70元（摇橹船）</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">⛩️</span>
                        <span class="tip-text">灵隐寺（飞来峰45元+灵隐寺30元）建议早上前往，避高峰</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🍜</span>
                        <span class="tip-text">杭帮菜推荐：楼外楼（百年老店）、外婆家、知味观</span>
                    </div>
                </div>
            </div>

'''
    content = content[:footer_pos] + day91_entry + content[footer_pos:]
    print('Added Day 91 entry')

# Update footer travel tips
old_footer_tips = '''📰 2026年5月千岛湖旅游贴士'''
new_footer_tips = '''📰 2026年5月杭州旅游贴士'''
if old_footer_tips in content:
    content = content.replace(old_footer_tips, new_footer_tips)
    content = content.replace(
        '''<li>🏝️ 千岛湖中心湖区船票185元（含3岛）；网购175元，建议提前订票</li>
                    <li>🚤 游船分上午班（8:30）和下午班（12:30），游览约5小时</li>
                    <li>⛰️ 梅峰岛是最佳观景岛，徒步15分钟或乘索道（60元）</li>
                    <li>🏨 千岛湖镇住宿集中，湖景房400-800元；中心湖区酒店更贵</li>
                    <li>🐟 千岛湖鱼头是招牌（人均80-150元）；推荐"鱼味馆"等老店</li>
                    <li>🚗 杭州到千岛湖约2小时（杭新景高速）；淳安县可坐船进岛</li>
                    <li>📅 明日预告：千岛湖 → 杭州（西湖）or 继续湖中岛屿游</li>''',
        '''<li>🌸 西湖景区全天免费；断桥、苏堤、曲院风荷为核心景点</li>
                    <li>🚤 西湖游船55元（含三潭印月登岛）；摇橹船可议价约150-200元/小时</li>
                    <li>⛩️ 灵隐寺建议早起（7:00开门）避免人流；永福寺人少景美</li>
                    <li>🏨 湖滨路/南山路住宿位置最佳，方便看夜景和逛河坊街</li>
                    <li>🍜 楼外楼（孤山路店）是百年老店；绿茶/外婆家性价比高</li>
                    <li>🚇 杭州地铁覆盖主要景区；节假日西湖边实行单双号限行</li>
                    <li>📅 明日预告：杭州——灵隐寺、河坊街、宋城或乌镇</li>'''
    )
    content = content.replace('最后更新：2026年5月18日（周一）', '最后更新：2026年5月19日（周二）')
    print('Updated footer travel tips')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print('HTML updated successfully')

# Verify
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    verify = f.read()
day91_check = '第91天' in verify
day92_check = re.findall(r'class="day-number">第(\d+)天', verify)
print('Day 91 added:', day91_check)
print('Last 3 day numbers:', day92_check[-3:] if day92_check else 'none')