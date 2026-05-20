# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update day count 60 -> 61
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 2. Update location count (no new city, still in 武夷山)
# No change to locationCount

# 3. Update km (local movement within 武夷山景区，约18km)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 18) + '<',
    content)

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">武夷山 · 虎啸岩<',
    content)

print('Updated stats: Day 61, km +18, location -> 武夷山 · 虎啸岩')

# 5. Add Day 61 entry before footer
day61_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第61天</span>
                    <span class="day-date">2026-04-18 · 三月廿一</span>
                </div>
                <div class="day-title">🏔️ 武夷山深度游 · 虎啸岩·一线天</div>
                <div class="day-content">
                    <p>武夷山深度游第二天！继续探索虎啸岩、一线天、玉女峰等经典景点！</p>
                    <p>🏔️ 上午：虎啸岩登顶</p>
                    <p>虎啸岩——武夷山"三十六峰"之一，海拔510米，以"风起云涌、虎啸龙吟"之势著称！登顶远眺，武夷全景尽收眼底！</p>
                    <p>🦁 虎啸岩：海拔510米，登山约1-1.5小时，台阶较陡，有"宾曦洞""语儿泉"等奇观，风景壮观</p>
                    <p>🚶 从虎啸岩可徒步前往一线天，沿途景色绝美，约40分钟路程！</p>
                    <p>🔍 中午：一线天探险</p>
                    <p>一线天——武夷山最神奇的自然奇观！两座岩石之间最窄处仅容一人侧身通过，最窄处约30cm，极具挑战性！</p>
                    <p>⛰️ 一线天：全长约100米，最窄处约30cm，需侧身通过；一线天左侧还有"水帘洞"可以一并游览</p>
                    <p>📸 一线天摄影：狭窄岩缝透下的光束是绝佳摄影点，建议中午时分光线最佳</p>
                    <p>🌸 下午：玉女峰下休闲漫步</p>
                    <p>玉女峰——武夷山标志性景观，九曲溪畔的"三姐妹"山峰，形态优美，是武夷山的象征性地标！</p>
                    <p>📷 玉女峰：武夷山标志性地标，在九曲溪畔观景最震撼，无需登山，沿溪边步道即可欣赏</p>
                    <p>🛶 傍晚：根据时间和体力，可选择：</p>
                    <p>① 二次体验九曲溪竹筏（下午场次人少景美，约14:00出发）</p>
                    <p>② 水帘洞景区（武夷山最大洞穴，"千山滴翠疑入梦，万壑倾涛欲凌空"）</p>
                    <p>③ 结束武夷山行程，前往下一站：福州或厦门</p>
                    <p>📊 今日行程：武夷山景区深度游，虎啸岩+一线天+玉女峰，步行约10公里</p>
                    <p>🚗 交通提示：武夷山景区环保车联票85元/人，可南北入口通用；虎啸岩到一线天徒步约40分钟</p>
                    <p>📅 下一站预告：武夷山之后前往福州（约2小时高铁），开始福建之旅！</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🦁</div>
                    <div class="photo-placeholder">⛰️</div>
                    <div class="photo-placeholder">🌸</div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day61_entry + '\n' + footer_marker)
print('Added Day 61 entry for 武夷山虎啸岩一线天')

# 6. Update travel tips
old_footer_pattern = r'<div class="footer">.*?<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月17日</p>.*?</div>'

new_footer = '''<div class="footer">
            <p>🚗 环游中国 · 房车日记</p>
            <p>记录每一天的所见所闻</p>
            <div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年4月中旬武夷山旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🦁 虎啸岩：海拔510米，登山约1-1.5小时，台阶较陡，可徒步至一线天（约40分钟），风景壮观</li>
                    <li>⛰️ 一线天：全长约100米，最窄处约30cm需侧身通过；左侧有水帘洞可一并游览；中午光线最佳</li>
                    <li>🌸 玉女峰：武夷山标志性地标，沿九曲溪畔步道即可欣赏，无需登山，傍晚光线最美</li>
                    <li>🛶 九曲溪竹筏：上午6:30出发人少景美；下午14:00场次人少，可根据时间灵活安排</li>
                    <li>🎫 门票：主景区免门票（延续至2026年）；观光车85元/人；竹筏票130元/人</li>
                    <li>🍜 必尝美食：武夷山熏鹅（必尝！）、笋干烧肉、菌菇汤、文公菜、大红袍茶叶蛋</li>
                    <li>🚗 下一站：福州（约2小时高铁），或直接前往厦门（海边城市）</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月18日</p>
            </div>
        </div>'''

new_content = re.sub(old_footer_pattern, new_footer, content, flags=re.DOTALL)
if new_content != content:
    print('Updated travel tips to 武夷山虎啸岩一线天')
else:
    print('WARNING: Could not find old footer to replace')

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('\n=== Update Complete ===')
print('Day: 61')
print('Location: 武夷山 · 虎啸岩')
print('Date: 2026-04-18')
print('Stats: DayCount +1, kmCount +18')
