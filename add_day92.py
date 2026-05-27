# -*- coding: utf-8 -*-
"""环游中国 - Day 92 更新脚本
添加Day 92（杭州 → 黄山/婺源方向 or 武汉）
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats - add 1 day and ~350km/1 location
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 350) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>黄山 · 宏村西递\g<3>', content)

# Find footer and insert before it
footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
else:
    # Day 92 entry (2026-05-20)
    day92_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第92天</span>
                    <span class="day-date">2026-05-20 · 四月二十三 · 周三</span>
                </div>
                <div class="day-title">🌸 杭州 → 黄山 · 徽州古韵</div>
                <div class="day-content">
                    <p>🚗 今日行程：杭州驱车前往黄山（约3.5小时，280km）</p>
                    <p>🛣️ 上午沿杭徽高速离开杭州，前往黄山风景区</p>
                    <p>🌄 下午抵达黄山脚下汤口镇，入住酒店</p>
                    <p>🏔️ 傍晚可游览黄山景区外围或泡温泉休整</p>
                    <p>📅 明日预告：黄山一日深度游——光明顶、迎客松、飞来石</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌄</div>
                    <div class="photo-placeholder">🏔️</div>
                    <div class="photo-placeholder">♨️</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🏔️</span>
                        <span class="tip-text">黄山景区门票190元（旺季），景区大巴19元/单程，索道前山80元/后山65元</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">⛺</span>
                        <span class="tip-text">建议住汤口镇（南门附近），方便次日早起登山；山上住宿需提前预订</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🍜</span>
                        <span class="tip-text">黄山特色美食：毛豆腐、臭鳜鱼、笋干烧肉、一品锅</span>
                    </div>
                </div>
            </div>

'''
    content = content[:footer_pos] + day92_entry + content[footer_pos:]
    print('Added Day 92 entry')

# Update footer travel tips
content = content.replace('📰 2026年5月杭州旅游贴士', '📰 2026年5月黄山旅游贴士')
content = content.replace(
    '''<li>🌸 西湖景区全天免费；断桥、苏堤、曲院风荷为核心景点</li>
                    <li>🚤 西湖游船55元（含三潭印月登岛）；摇橹船可议价约150-200元/小时</li>
                    <li>⛩️ 灵隐寺建议早起（7:00开门）避免人流；永福寺人少景美</li>
                    <li>🏨 湖滨路/南山路住宿位置最佳，方便看夜景和逛河坊街</li>
                    <li>🍜 楼外楼（孤山路店）是百年老店；绿茶/外婆家性价比高</li>
                    <li>🚇 杭州地铁覆盖主要景区；节假日西湖边实行单双号限行</li>
                    <li>📅 明日预告：杭州——灵隐寺、河坊街、宋城或乌镇</li>''',
    '''<li>🏔️ 黄山风景区门票190元（旺季4-11月），建议早起登山避人流</li>
                    <li>🚠 索道建议：后山云谷寺上（65元）、前山慈光阁下（80元），不走回头路</li>
                    <li>⛺ 山顶住宿昂贵（标间1000+），建议住山下汤口镇（100-300元）</li>
                    <li>🌄 黄山日出最佳点：光明顶、清凉台、狮子峰</li>
                    <li>🍜 山下美食：毛豆腐、臭鳜鱼正宗；汤口镇餐厅集中在微笑山庄附近</li>
                    <li>🚗 杭州到黄山约3.5小时（杭徽高速）；黄山北站有高铁直达</li>
                    <li>📅 明日预告：黄山深度一日游 or 宏村西递古村落</li>'''
)
content = content.replace('最后更新：2026年5月19日（周二）', '最后更新：2026年5月20日（周三）')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print('HTML updated successfully')

# Verify
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    verify = f.read()
day92_check = '第92天' in verify
day_nums = re.findall(r'day-number">第(\d+)天', verify)
print('Day 92 added:', day92_check)
print('Last 5 day numbers:', sorted(set(int(d) for d in day_nums))[-5:])