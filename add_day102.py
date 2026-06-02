# -*- coding: utf-8 -*-
"""环游中国 - Day 102 更新脚本
添加Day 102（景德镇——中国瓷都，陶瓷艺术之旅）"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount=102, add 1 day and ~150km/3 locations
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 150) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 3) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>景德镇 · 陶瓷博物馆\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

day102_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">102</span>
                    <span class="day-date">2026-05-30 · 五月初三 · 周六</span>
                </div>
                <div class="day-title">🏺 景德镇 · 中国瓷都 · 陶瓷艺术之旅</div>
                <div class="day-content">
                    <p>🚗 今日行程：九江 → 景德镇（约150km，2小时）</p>
                    <p>🛣️ 路线：九江走杭瑞高速向南，经湖口县到景德镇</p>
                    <p>🏺 上午：中国陶瓷博物馆（免费，公认最好的陶瓷博物馆）</p>
                    <p>🏛️ 上午/中午：景德镇古窑民俗博览区（制瓷工艺展示）</p>
                    <p>🎨 中午：陶溪川文创街区（老厂房改造，文艺清新）</p>
                    <p>🛒 下午：国贸陶瓷市场 / 樊家井陶瓷批发市场（淘货）</p>
                    <p>🍜 晚餐：景德镇特色（碱水粑、冷粉、饺子糕）</p>
                    <p>🏨 住宿推荐：人民广场/陶溪川附近（方便夜游）</p>
                    <p>📅 明日预告：景德镇 → 婺源（自驾约85km，1.5小时），最美乡村</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏺</div>
                    <div class="photo-placeholder">🎨</div>
                    <div class="photo-placeholder">🛒</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🏺</span>
                        <span class="tip-text">中国陶瓷博物馆免费，周一闭馆；陶瓷惊艳，必看</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🎨</span>
                        <span class="tip-text">陶溪川夜景很美，周末有创意市集，适合年轻人</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🛒</span>
                        <span class="tip-text">买瓷器去樊家井（便宜）或国贸（品种全），记得讲价</span>
                    </div>
                </div>
            </div>

'''

content = content[:footer_pos] + day102_entry + content[footer_pos:]
print('Added Day 102 entry')

# Update footer travel tips
old_footer = '''<li>🌊 鄱阳湖湿地免费参观；丰水期景色壮观，建议下午去</li>
                    <li>🍜 九江美食：茶香饼、萝卜饼、鄱阳湖醉虾、鱼宴</li>
                    <li>🚗 庐山至九江约50km，下山1小时，走福银高速</li>
                    <li>🏨 九江住宿推荐滨江路/甘棠湖附近，停车方便</li>
                    <li>📅 明日预告：九江 → 景德镇（自驾约150km，2小时）</li>'''

new_footer = '''<li>🏺 中国陶瓷博物馆免费，周一闭馆；镇馆之宝多，必去</li>
                    <li>🎨 陶溪川文创街区夜景美，周末有创意市集</li>
                    <li>🛒 买瓷器去樊家井（便宜）或国贸，记得讲价</li>
                    <li>🍜 景德镇美食：碱水粑、冷粉、饺子糕</li>
                    <li>🚗 景德镇到婺源约85km，自驾1.5小时</li>
                    <li>📅 明日预告：景德镇 → 婺源（最美乡村，晒秋）</li>'''

content = content.replace(old_footer, new_footer)
content = content.replace('最后更新：2026年5月29日（周五）', '最后更新：2026年5月30日（周六）')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print('HTML updated successfully')

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    verify = f.read()
day_nums = re.findall(r'class="day-number">(\d+)<', verify)
print('Last 3 day numbers:', day_nums[-3:] if day_nums else 'none')
day_match = re.search(r'id="dayCount"[^>]*>(\d+)<', verify)
km_match = re.search(r'id="kmCount"[^>]*>(\d+)<', verify)
loc_match = re.search(r'id="locationCount"[^>]*>(\d+)<', verify)
cur_match = re.search(r'id="currentLocation"[^>]*>([^<]+)<', verify)
print('Stats: dayCount=%s, kmCount=%s, locationCount=%s, location=%s' % (
    day_match.group(1) if day_match else '?',
    km_match.group(1) if km_match else '?',
    loc_match.group(1) if loc_match else '?',
    cur_match.group(1) if cur_match else '?'
))