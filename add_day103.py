# -*- coding: utf-8 -*-
"""环游中国 - Day 103/104/105 批量更新脚本
补更 5/31、6/1、6/2 三天：
  Day 103 (5/31 周日): 景德镇 → 婺源（最美乡村，篁岭晒秋、江岭）
  Day 104 (6/1  周一): 婺源 → 三清山（道教名山，巨蟒出山、司春女神）
  Day 105 (6/2  周二): 三清山 → 宏村/徽州古城（皖南徽派古村）
当前 cron 因 web_search 失败、AI 搜索受限，使用 Bing web_fetch 替代 + 行程逻辑更新。
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount 103→106 (+3), kmCount 14160→14495 (+335), locationCount 82→91 (+9)
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 3) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 335) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 9) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>宏村 · 月沼湖畔\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

day103_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">103</span>
                    <span class="day-date">2026-05-31 · 五月初四 · 周日</span>
                </div>
                <div class="day-title">🌸 婺源 · 中国最美乡村 · 篁岭晒秋</div>
                <div class="day-content">
                    <p>🚗 今日行程：景德镇 → 婺源县城 → 篁岭（合计约95km，2小时）</p>
                    <p>🛣️ 路线：景德镇走杭瑞高速向西，转德婺高速到婺源，再上山到篁岭</p>
                    <p>🌼 上午：江岭观景台（中国四大花海之一，5月底油菜花尾季，梯田仍壮观）</p>
                    <p>🏯 中午：篁岭景区（"晒秋"文化发源地，挂在山崖上的古村，门票+索道145元）</p>
                    <p>🌉 下午：篁岭古村漫步，天街商铺、垒心桥、玻璃栈道</p>
                    <p>🌅 傍晚：月亮湾（免费，竹林小岛渔舟，摄影圣地）</p>
                    <p>🍜 晚餐：婺源特色（荷包红鲤、清明粿、汽糕、婺源绿茶）</p>
                    <p>🏨 住宿推荐：婺源县城/江湾镇（便于次日上三清山）</p>
                    <p>📅 明日预告：婺源 → 三清山（约150km，2.5小时），道教名山</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌼</div>
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">🌅</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🌼</span>
                        <span class="tip-text">江岭尾季油菜花已收，仍有绿色梯田；最佳季节3月中-4月初</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🏯</span>
                        <span class="tip-text">篁岭必坐索道！山下停车场到古村垂直高差300米，徒步累</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🎫</span>
                        <span class="tip-text">婺源14景点通票180元（5天有效），单独篁岭145元，按需选择</span>
                    </div>
                </div>
            </div>

'''

day104_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">104</span>
                    <span class="day-date">2026-06-01 · 五月初五 · 周一</span>
                </div>
                <div class="day-title">⛰️ 三清山 · 道教名山 · 奇峰怪石</div>
                <div class="day-content">
                    <p>🚗 今日行程：婺源 → 三清山金沙索道（约150km，2.5小时）</p>
                    <p>🛣️ 路线：婺源走杭瑞高速向西到玉山，再转三清山环山公路</p>
                    <p>⛰️ 上午：乘坐金沙索道上山（门票120元+索道往返125元）</p>
                    <p>🌄 上午/下午：南清园景区（巨蟒出山、司春女神、万笏朝天、东方女神）</p>
                    <p>🌲 下午：西海岸高空栈道（4公里悬空栈道，云海景观）</p>
                    <p>🌅 傍晚：玉京峰观日落（需预约，注意时间，17:00前回到索道）</p>
                    <p>🍜 晚餐：三清山山脚土菜（清炖土鸡、石耳炖鸡、苦槠豆腐）</p>
                    <p>🏨 住宿推荐：三清山山下/玉山县城（次日去宏村方便）</p>
                    <p>📅 明日预告：三清山 → 宏村/徽州古城（约200km，3小时）</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">⛰️</div>
                    <div class="photo-placeholder">🌄</div>
                    <div class="photo-placeholder">🌲</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">⛰️</span>
                        <span class="tip-text">三清山世界自然遗产，与黄山同纬度但更秀美；6月雨水多，看云海几率高</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🚡</span>
                        <span class="tip-text">金沙索道10分钟上山，外双溪索道人少；两日票更划算</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">👟</span>
                        <span class="tip-text">登山穿防滑徒步鞋，西海岸栈道4公里；雨季备一次性雨衣</span>
                    </div>
                </div>
            </div>

'''

day105_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">105</span>
                    <span class="day-date">2026-06-02 · 五月初六 · 周二</span>
                </div>
                <div class="day-title">🏯 宏村 · 西递 · 徽州古韵 · 水墨画里乡村</div>
                <div class="day-content">
                    <p>🚗 今日行程：三清山 → 黟县宏村 → 屯溪老街（约200km，3小时）</p>
                    <p>🛣️ 路线：三清山走杭瑞高速向北到屯溪，转S103省道到黟县宏村</p>
                    <p>🏯 上午：宏村（世界文化遗产，"中国画里乡村"，门票104元）</p>
                    <p>💧 上午：月沼/南湖（电影《卧虎藏龙》取景地，早晨最美）</p>
                    <p>🏘️ 下午：西递（与宏村齐名，徽派建筑博物馆，门票104元）</p>
                    <p>🏛️ 下午/傍晚：徽州古城/歙县（徽商故里，徽州府衙、许国石坊、斗山街）</p>
                    <p>🌃 晚上：屯溪老街（流动的清明上河图，徽墨酥、臭鳜鱼、毛豆腐）</p>
                    <p>🍜 晚餐：徽菜代表（臭鳜鱼108元/条、徽州毛豆腐、问政山笋、黄山烧饼）</p>
                    <p>🏨 住宿推荐：屯溪老街附近（便于次日游黄山）</p>
                    <p>📅 明日预告：黄山风景区（迎客松、光明顶、莲花峰、西海大峡谷）</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">💧</div>
                    <div class="photo-placeholder">🌃</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🏯</span>
                        <span class="tip-text">宏村+西递联票154元，3天有效；早晨7点前进村免门票（部分时段）</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">💧</span>
                        <span class="tip-text">月沼晨雾、南湖倒影是宏村最佳拍摄时机，建议住一晚</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🍜</span>
                        <span class="tip-text">臭鳜鱼是徽菜灵魂，闻臭吃香；屯溪老街"老街第一楼"是老字号</span>
                    </div>
                </div>
            </div>

'''

content = content[:footer_pos] + day103_entry + day104_entry + day105_entry + content[footer_pos:]
print('Added Day 103, 104, 105 entries')

# Update footer travel tips: replace 南昌 tips with 徽州/黄山 tips
old_footer = '''<p style="font-size: 14px; margin-bottom: 10px;">📰 2026年5月南昌旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏯 滕王阁门票50元，傍晚登楼拍赣江日落，22:00关灯</li>
                    <li>🏛️ 江西省博物馆免费，海昏侯文物展必看，需公众号提前预约</li>
                    <li>🍜 万寿宫街区美食：水煮、炒螺蛳、烧烤，南昌口味偏辣</li>
                    <li>🎆 秋水广场音乐喷泉每晚8:00-8:30，免费，建议提前10分钟到</li>
                    <li>🪨 绳金塔千年古塔，免费参观；周边有绳金塔美食街</li>
                    <li>🚗 南昌到庐山约120km，自驾1.5小时，走昌九大道/福银高速</li>
                    <li>📅 明日预告：庐山深度游——庐山云海 · 瀑布泉水 · 牯岭镇</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年5月30日（周六）</p>'''

new_footer = '''<p style="font-size: 14px; margin-bottom: 10px;">📰 2026年6月赣东北·皖南旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🌼 婺源通票180元/5天，篁岭单独145元；6月已过油菜花季，赏绿野+古村</li>
                    <li>⛰️ 三清山门票120元+金沙索道125元；6月雨多云海几率高，备雨衣</li>
                    <li>🏯 宏村104元+西递104元，联票154元；7点前/17点后免票可议价</li>
                    <li>🍜 徽菜必尝：臭鳜鱼（闻臭吃香）、毛豆腐、问政山笋、徽州一品锅</li>
                    <li>🌃 屯溪老街夜景好，徽墨酥/黄山烧饼/黄山毛峰都是伴手礼</li>
                    <li>🚗 婺源→三清山150km / 三清山→宏村200km，高速+省道</li>
                    <li>📅 明日预告：黄山风景区——迎客松 · 光明顶 · 莲花峰 · 西海大峡谷</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年6月3日（周三）</p>'''

if old_footer in content:
    content = content.replace(old_footer, new_footer)
    print('Footer tips updated')
else:
    # Try simpler last-update replacement
    content = content.replace('最后更新：2026年5月30日（周六）', '最后更新：2026年6月3日（周三）')
    print('Footer last-update replaced only')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print('HTML updated successfully')

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    verify = f.read()
day_nums = re.findall(r'class="day-number">(\d+)<', verify)
print('Last 5 day numbers:', day_nums[-5:] if day_nums else 'none')
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
print('Total day cards:', len(day_nums))
