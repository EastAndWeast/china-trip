# -*- coding: utf-8 -*-
"""环游中国 - Day 99 更新脚本
添加Day 99（庐山深度游——云海 · 瀑布 · 牯岭镇）
从南昌出发，约120km，1.5小时到庐山"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount=99, add 1 day and ~120km/3 locations
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 120) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 3) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>庐山 · 牯岭镇\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

day99_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">99</span>
                    <span class="day-date">2026-05-27 · 五月三十 · 周三</span>
                </div>
                <div class="day-title">🏔️ 庐山深度游 · 云海 · 瀑布 · 牯岭镇</div>
                <div class="day-content">
                    <p>🚗 今日行程：南昌 → 庐山（约120km，1.5小时）</p>
                   <p>🛣️ 路线：南昌沿福银高速/昌九大道向北，经九江到庐山南门</p>
                   <p>🏔️ 上午：抵达庐山牯岭镇（山顶小镇，海拔1100m），办理入住</p>
                   <p>🌅 下午：庐山三叠泉（"飞流直下三千尺"原型，徒步约3小时）</p>
                    <p>🌄 傍晚：如琴湖畔散步 + 花径公园（白居易草堂）</p>
                    <p>🍜 晚餐：牯岭镇（庐山特色菜：石耳炖鸡、庐山石鸡）</p>
                   <p>🏨 住宿推荐：牯岭镇（山顶住宿，需提前预订，节假日较贵）</p>
                    <p>📅 明日预告：庐山日出 + 仙人洞 + 美庐别墅 + 含鄱口</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏔️</div>
                    <div class="photo-placeholder">💧</div>
                    <div class="photo-placeholder">🌅</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🏔️</span>
                        <span class="tip-text">庐山门票160元（旺季）+景区大巴70元，索道80元/单程</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">💧</span>
                        <span class="tip-text">三叠泉徒步来回约3小时，需爬1600级台阶，建议穿防滑鞋</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🌅</span>
                        <span class="tip-text">看日出推荐含鄱口或五老峰，需凌晨4:30出发；带上外套</span>
                    </div>
                </div>
            </div>

'''

content = content[:footer_pos] + day99_entry + content[footer_pos:]
print('Added Day 99 entry')

# Update footer travel tips - replace 南昌 with 庐山
old_footer = '''<li>🏯 滕王阁门票50元，傍晚登楼拍赣江日落，22:00关灯</li>
                    <li>🏛️ 江西省博物馆免费，海昏侯文物展必看，需公众号提前预约</li>
                    <li>🍜 万寿宫街区美食：水煮、炒螺蛳、烧烤，南昌口味偏辣</li>
                    <li>🎆 秋水广场音乐喷泉每晚8:00-8:30，免费，建议提前10分钟到</li>
                    <li>🪨 绳金塔千年古塔，免费参观；周边有绳金塔美食街</li>
                   <li>🚗 南昌到庐山约120km，自驾1.5小时，走昌九大道/福银高速</li>
                    <li>📅 明日预告：庐山深度游——庐山云海 · 瀑布泉水 · 牯岭镇</li>'''

new_footer = '''<li>🏔️ 庐山门票160元（旺季）+ 大巴70元，索道80元/单程</li>
                    <li>💧 三叠泉徒步来回3小时，需爬1600级台阶；建议穿防滑鞋</li>
                    <li>🌅 看日出推荐含鄱口/五老峰，凌晨4:30出发，带外套</li>
                    <li>🏨 牯岭镇住宿提前预订，山顶物价较贵</li>
                    <li>🍜 牯岭镇美食：石耳炖鸡、庐山石鸡、庐山茶饼</li>
                   <li>🚗 庐山上山有两条索道：东门（庐山站）或南门（九江站）</li>
                    <li>📅 明日预告：庐山日出 + 仙人洞 + 美庐别墅 + 含鄱口</li>'''

content = content.replace(old_footer, new_footer)
content = content.replace('最后更新：2026年5月26日（周二）', '最后更新：2026年5月27日（周三）')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print('HTML updated successfully')

# Verify
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