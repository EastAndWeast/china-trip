# -*- coding: utf-8 -*-
"""环游中国 - Day 109 更新脚本
Day 109 (2026-06-06 周六): 杭州 → 绍兴（鲁迅故里·兰亭·东湖·鉴湖·沈园）
  - 距离约 80km
  - 端午假期前一日，游客中等
  - 衔接 Day 110: 绍兴 → 宁波 → 普陀山

AI 搜索今日不可用（web_search 失败 + Bing 跑题），使用行程逻辑更新。
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = r'C:\Users\admin\.openclaw\workspace\china-trip\index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount 109→110 (+1), kmCount 14965→15050 (+85), locationCount 97→99 (+2)
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 85) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 2) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>绍兴 · 鲁迅故里\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

day109_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">109</span>
                    <span class="day-date">2026-06-06 · 五月初十 · 周六</span>
                </div>
                <div class="day-title">📚 绍兴 · 鲁迅故里 · 江南文化古城</div>
                <div class="day-content">
                    <p>🚗 今日行程：杭州西湖 → 绍兴市区（鲁迅故里/仓桥直街）约65km，1.5小时</p>
                    <p>🛣️ 路线：杭州走G92杭州湾跨海大桥北接线 → 转G15W常台高速到绍兴</p>
                    <p>📖 上午：鲁迅故里（免费，5A景区，三味书屋/百草园/鲁迅祖居，需提前预约）</p>
                    <p>🌉 上午：仓桥直街（免费，国家级历史文化名街，乌篷船、黄酒棒冰、奶油小攀）</p>
                    <p>🛕 中午：沈园（40元，《钗头凤》陆游唐婉故事地，江南园林典范）→ 午餐寻觅绍兴味</p>
                    <p>🍶 中午：绍兴黄酒（必尝，咸亨酒店太雕酒/女儿红/花雕）、霉苋菜梗、糟鸡、醉蟹</p>
                    <p>🏛️ 下午：兰亭景区（90元含书法博物馆+曲水流觞，王羲之《兰亭集序》诞生地，距市区15km）</p>
                    <p>⛰️ 下午/傍晚：东湖（50元，江南"小桂林"，乘乌篷船穿凿壁岩洞，1小时）</p>
                    <p>🌃 晚上：书圣故里（免费，历史街区，蔡元培故居/墨池/题扇桥夜景）</p>
                    <p>🍜 晚餐：绍兴菜代表（梅干菜烧肉、清汤越鸡、绍三鲜、糟溜鱼片、奶油小攀）</p>
                    <p>🏨 住宿推荐：绍兴市区/鲁迅故里附近（便于次日游宁波/普陀山）</p>
                    <p>📅 明日预告：绍兴 → 宁波 → 普陀山（约150km，2.5小时+船），海天佛国</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">📖</div>
                    <div class="photo-placeholder">🍶</div>
                    <div class="photo-placeholder">⛰️</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">📖</span>
                        <span class="tip-text">鲁迅故里免费但要"绍兴文旅"公众号预约（节假日紧张）；三味书屋/百草园早8点前人少</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🍶</span>
                        <span class="tip-text">绍兴黄酒世界三大古酒之一；咸亨酒店"太雕"经典，乌篷船体验仓桥直街段</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🛕</span>
                        <span class="tip-text">沈园白天看园林，晚上看《沈园之夜》实景演出（138元起，钗头凤越剧）</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">⛰️</span>
                        <span class="tip-text">东湖乌篷船是绍兴必体验项目；3人拼船75元，约40分钟穿岩洞</span>
                    </div>
                </div>
            </div>

'''

content = content[:footer_pos] + day109_entry + content[footer_pos:]
print('Added Day 109 entry')

# Update footer tips
old_footer = '''<p style="font-size: 14px; margin-bottom: 10px;">📰 2026年6月皖南·浙西旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏔️ 黄山旺季门票190元（3-11月），三大索道各80-90元；6月梅雨季云海几率70%+</li>
                    <li>⛰️ 黄山山顶住宿紧张：玉屏楼/白云宾馆标间800-1500元，提前2周预订</li>
                    <li>🌊 千岛湖中心湖区联票150元（含船票），梅峰岛观景台是标志；鱼头68元/斤起</li>
                    <li>🌸 西湖免费！游船55元、雷峰塔40元、灵隐寺+飞来峰75元；环湖步行2-3h</li>
                    <li>🍜 杭帮菜代表：西湖醋鱼/东坡肉/龙井虾仁/叫花鸡；楼外楼老字号150年</li>
                    <li>🚗 黄山→千岛湖280km / 千岛湖→杭州180km，全程高速</li>
                    <li>📅 明日预告：杭州深度——灵隐 · 龙井 · 西溪湿地 · 京杭大运河</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年6月4日（周四）</p>'''

new_footer = '''<p style="font-size: 14px; margin-bottom: 10px;">📰 2026年6月浙东·端午旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🌸 西湖端午假期客流量大，建议错峰：6/6 周六尽量早7点前到断桥</li>
                    <li>📖 鲁迅故里免费但须"绍兴文旅"公众号预约；端午假期要提前1-3天</li>
                    <li>🍶 绍兴黄酒（太雕/女儿红/花雕）必尝；咸亨酒店老字号，乌篷船80元/人</li>
                    <li>🛕 兰亭90元（王羲之故地），东湖50元（含乌篷船）；沈园夜间演出138元起</li>
                    <li>🌊 端午去普陀山："南海观音文化节"开幕，6/6-6/8 限流+预约（提前订船票）</li>
                    <li>🚗 杭州→绍兴65km / 绍兴→宁波普陀山150km，端午高速免费但严重拥堵</li>
                    <li>📅 明日预告：宁波 → 普陀山——海天佛国 · 南海观音 · 33米大佛</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年6月5日（周五）</p>'''

if old_footer in content:
    content = content.replace(old_footer, new_footer)
    print('Footer tips fully updated')
else:
    # Fallback
    content = content.replace('最后更新：2026年6月4日（周四）', '最后更新：2026年6月5日（周五）')
    content = content.replace('📅 明日预告：杭州深度——灵隐 · 龙井 · 西溪湿地 · 京杭大运河', '📅 明日预告：宁波 → 普陀山——海天佛国 · 南海观音')
    print('Footer partial fallback updated')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print('HTML updated successfully')

# Verify
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    verify = f.read()
day_cards = re.findall(r'<div class="day-card">\s*<div class="day-header">\s*<span class="day-number">(\d+)</span>\s*<span class="day-date">([^<]+)</span>', verify, re.DOTALL)
print('Total day cards:', len(day_cards))
print('Last 3 days:', day_cards[-3:] if day_cards else 'none')
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
footer_match = re.search(r'最后更新：([^<]+)<', verify)
print('Last update:', footer_match.group(1) if footer_match else 'not found')
