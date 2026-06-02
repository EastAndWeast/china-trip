# -*- coding: utf-8 -*-
"""环游中国 - Day 100 更新脚本
添加Day 100（庐山日出 + 仙人洞 + 含鄱口）"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount=100, add 1 day and ~50km/3 locations
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 50) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 3) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>庐山 · 含鄱口\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

day100_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">100</span>
                    <span class="day-date">2026-05-28 · 五月初一 · 周四</span>
                </div>
                <div class="day-title">🌅 庐山日出 · 仙人洞 · 含鄱口 · 美庐别墅</div>
                <div class="day-content">
                    <p>🌄 凌晨4:30出发，前往含鄱口观日出（需提前查天气预报）</p>
                    <p>🏔️ 早晨：含鄱口（庐山最佳日出观赏点，俯瞰鄱阳湖）</p>
                    <p>🕳️ 上午：仙人洞（"天生一个仙人洞"，吕洞宾在此修炼）</p>
                    <p>🌿 上午/中午：花径公园 + 白居易草堂（"人间四月芳菲尽，山寺桃花始盛开"）</p>
                    <p>🏛️ 中午：美庐别墅（蒋介石庐山官邸，宋美龄曾居住）</p>
                    <p>🍜 午餐：牯岭镇（庐山土豆烧肉、笋干烧肉）</p>
                   <p>🌳 下午：庐山会议旧址 + 芦林湖（毛泽东旧居）</p>
                    <p>🌆 傍晚：街心公园远眺庐山云海</p>
                    <p>🏨住宿：牯岭镇（第二晚）</p>
                    <p>📅 明日预告：庐山 → 九江（下山游湖）or 返程休整</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌅</div>
                    <div class="photo-placeholder">🏔️</div>
                    <div class="photo-placeholder">🏛️</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🌅</span>
                        <span class="tip-text">含鄱口日出需凌晨出发，山路较黑建议带手电；5月底日出约5:15</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🏛️</span>
                        <span class="tip-text">美庐别墅20元，庐山会议旧址免费；建议请导游讲解历史</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🕳️</span>
                        <span class="tip-text">仙人洞免费游览；附近有朱元璋题刻和御碑亭</span>
                    </div>
                </div>
            </div>

'''

content = content[:footer_pos] + day100_entry + content[footer_pos:]
print('Added Day 100 entry')

# Update footer travel tips
old_footer = '''<li>🏔️ 庐山门票160元（旺季）+ 大巴70元，索道80元/单程</li>
                    <li>💧 三叠泉徒步来回3小时，需爬1600级台阶；建议穿防滑鞋</li>
                    <li>🌅 看日出推荐含鄱口/五老峰，凌晨4:30出发，带外套</li>
                    <li>🏨 牯岭镇住宿提前预订，山顶物价较贵</li>
                    <li>🍜 牯岭镇美食：石耳炖鸡、庐山石鸡、庐山茶饼</li>
                    <li>🚗 庐山上山有两条索道：东门（庐山站）或南门（九江站）</li>
                   <li>📅 明日预告：庐山日出 + 仙人洞 + 美庐别墅 + 含鄱口</li>'''

new_footer = '''<li>🌅 含鄱口日出需凌晨4:30出发，带手电筒；5月底日出约5:15</li>
                   <li>🕳️ 仙人洞免费；花径公园免费；美庐别墅20元</li>
                   <li>🏛️ 庐山会议旧址免费参观，建议请导游讲解历史</li>
                    <li>🍜 牯岭镇美食：土豆烧肉、笋干烧肉、石耳炖鸡</li>
                    <li>🏨 牯岭镇住宿建议提前预订，节假日价格较高</li>
                   <li>🚗 庐山至九江约50km，下山后走福银高速约1小时</li>
                    <li>📅 明日预告：庐山下山 → 九江（庐山会议旧址/鄱阳湖）</li>'''

content = content.replace(old_footer, new_footer)
content = content.replace('最后更新：2026年5月27日（周三）', '最后更新：2026年5月28日（周四）')

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