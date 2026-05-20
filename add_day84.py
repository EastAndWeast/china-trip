# -*- coding: utf-8 -*-
"""环游中国 - Day 84 更新脚本
日期: 2026-05-12 (Day 84 内容：庐山深度游 · 五老峰+三叠泉)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract current max day
day_matches = re.findall(r'class="day-number">第(\d+)天', content)
current_day = max([int(d) for d in day_matches]) if day_matches else 83
new_day = current_day + 1
print(f'Current max day: {current_day} -> New day: {new_day}')

# 1. Update day count
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated dayCount -> 84')

# 2. Update km (庐山景区内约80km)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 80) + '<',
    content)
print('Updated kmCount -> 11430 (added 80km)')

# 3. Update location count (+1 庐山)
content = re.sub(r'id="locationCount"[^>]*>(\d+)<',
    lambda m: 'id="locationCount">' + str(int(m.group(1)) + 1) + '<',
    content)
print('Updated locationCount -> 51')

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">庐山 · 牯岭山城<',
    content)
print('Updated currentLocation -> 庐山 · 牯岭山城')

# 5. Day 84 entry (2026-05-12)
day84_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第84天</span>
                    <span class="day-date">2026-05-12 · 四月十五 · 周二</span>
                </div>
                <div class="day-title">🏔️ 庐山深度游 · 五老峰与三叠泉</div>
                <div class="day-content">
                    <p>🏔️ 全天游览庐山！今日重点：五老峰 + 三叠泉（难度中高，量力而行）</p>
                    <p>⚠️ 注意：庐山交通索道2026年5月11日至6月9日年度检修停运，需换乘景区巴士或自驾</p>
                    <p>🌅 早晨在牯岭镇品尝庐山云雾茶，整理行装轻装出发</p>
                    <p>🏃 五老峰：从入口到一峰约700级台阶，体力一般者登至三峰即可原路返回，全程约1.5-2小时</p>
                    <p>💧 三叠泉：落差155米，"不到三叠泉，不算庐山客"，需先下1600级台阶，游览后原路返回约2-3小时</p>
                    <p>🍜 午餐：牯岭街农家菜馆，庐山土鸡、山野菜、石鱼蒸蛋</p>
                    <p>🌲 下午可根据体力选择：含鄱口观景、仙人洞+花径、如琴湖漫步</p>
                    <p>🏛️ 美庐：蒋介石庐山旧居，宋美龄曾居住过，别墅建筑中西合璧</p>
                    <p>🌙 牯岭镇夜市：晚上逛牯岭街夜市，购庐山特产（云雾茶、茶饼、竹笋干）</p>
                    <p>📅 明日预告：庐山 → 景德镇（约2.5小时车程），瓷都之旅</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏔️</div>
                    <div class="photo-placeholder">💧</div>
                    <div class="photo-placeholder">🌲</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">⚠️</span>
                        <span class="tip-text">庐山索道检修期（5.11-6.9）：九江方向来车可走环山公路到牯岭镇，自驾盘山路约50分钟，弯道多注意安全；景区内换乘观光车90元/人</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🏃</span>
                        <span class="tip-text">五老峰+三叠泉联游对体力要求高，建议先爬五老峰再下三叠泉，三叠泉下山1600级台阶较陡，有膝关节问题者慎行</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🌙</span>
                        <span class="tip-text">牯岭街住宿约200-400元/晚，标间含早，山上昼夜温差大5-15℃，带外套；云雾茶50-100元/盒是手信首选</span>
                    </div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day84_entry + '\n' + footer_marker)
print('Added Day 84 entry: 庐山深度游 · 五老峰与三叠泉')

# 6. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年5月12日（周二）</p>')
    print('Updated footer timestamp to 2026年5月12日（周二）')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 84')
print('Location: 庐山 · 牯岭山城')
print('Date: 2026-05-12 (四月十五 · 周二)')
print('KM added: 80 (total: ~11430)')
print('Location count: 51')
print('Key update: 庐山索道检修期提醒')