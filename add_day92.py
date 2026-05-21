# -*- coding: utf-8 -*-
"""环游中国 - Day 92 更新脚本
添加Day 92（杭州深度游——灵隐寺、河坊街）"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats - add 1 day and ~60km/1 location
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 60) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>杭州 · 河坊街\g<3>', content)

# Find footer and insert before it
footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
else:
    # Day 92 entry (2026-05-20)
    day92_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">92</span>
                    <span class="day-date">2026-05-20 · 四月廿三 · 周三</span>
                </div>
                <div class="day-title">⛩️ 灵隐寺 · 河坊街 · 杭州深度游</div>
                <div class="day-content">
                    <p>🚗 今日行程：杭州深度一日游</p>
                    <p>⛩️ 上午：灵隐寺（飞来峰+永福寺），7:00开门早去避高峰</p>
                    <p>🌿 永福寺（紧邻灵隐）：人少景美，乾隆题名"康熙六次南巡驻跸地"</p>
                    <p>🚶 中午：岳王庙（栖霞岭）& 孤山公园</p>
                    <p>🏯 下午：河坊街步行 + 胡庆余堂（"江南药王"，清代徽派建筑）</p>
                    <p>🚢 傍晚：京杭大运河游船（拱宸桥至武林门，夜景绝美）</p>
                    <p>🍜 晚餐：河坊街知味观 or 菊英面馆（片儿川）</p>
                    <p>🌙 晚上入住湖滨/南山路区域</p>
                    <p>📅 明日预告：杭州——宋城 or 乌镇（自驾1.5小时）</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">⛩️</div>
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">🚢</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">⛩️</span>
                        <span class="tip-text">灵隐寺门票75元（含飞来峰）；永福寺免费；建议7:00早到</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🏯</span>
                        <span class="tip-text">河坊街，胡庆余堂"北有同仁堂，南有庆余堂"，国药老字号</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🚢</span>
                        <span class="tip-text">京杭大运河夜游（拱宸桥-武林门，约60元，45分钟）</span>
                    </div>
                </div>
            </div>

'''
    content = content[:footer_pos] + day92_entry + content[footer_pos:]
    print('Added Day 92 entry')

# Update footer travel tips
content = content.replace('📰 2026年5月杭州旅游贴士', '📰 2026年5月杭州深度游贴士')
content = content.replace(
    '''<li>🌸 西湖景区全天免费；断桥、苏堤、曲院风荷为核心景点</li>
                    <li>🚤 西湖游船55元（含三潭印月登岛）；摇橹船可议价约150-200元/小时</li>
                    <li>⛩️ 灵隐寺建议早起（7:00开门）避免人流；永福寺人少景美</li>
                    <li>🏨 湖滨或南山路住宿位置最佳，方便看夜景和逛河坊街</li>
                    <li>🍜 楼外楼（孤山路店）是百年老店；绿茶、外婆家性价比高</li>
                    <li>🚇 杭州地铁覆盖主要景区；节假日西湖边实行单双号限行</li>
                    <li>📅 明日预告：杭州——灵隐寺、河坊街、宋城或乌镇</li>''',
    '''<li>⛩️ 灵隐寺7:00开门，建议早去；永福寺免费，紧邻灵隐更清静</li>
                    <li>🏯 胡庆余堂（河坊街）"江南药王"，清代徽派商业建筑，门票免费</li>
                    <li>🚢 京杭大运河夜游（拱宸桥-武林门，约60元，45分钟）</li>
                    <li>🍜 河坊街美食：知味观（片儿川）、菊英面馆、定胜糕、葱包烩</li>
                    <li>🚇 杭州地铁3号线后通段已开通，武林广场可换乘</li>
                    <li>🚗 宋城（1小时）或乌镇（1.5小时）可当日往返</li>
                    <li>📅 明日预告：杭州——宋城千古情 or 乌镇西栅夜景</li>'''
)
content = content.replace('最后更新：2026年5月19日（周二）', '最后更新：2026年5月20日（周三）')
print('Updated footer travel tips')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print('HTML updated successfully')

# Verify
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    verify = f.read()
day92_check = '92' in verify
day_nums = re.findall(r'class="day-number">(\d+)<', verify)
print('Day 92 added:', day92_check)
print('Last 3 day numbers:', day_nums[-3:] if day_nums else 'none')