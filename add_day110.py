# -*- coding: utf-8 -*-
"""环游中国 - Day 110 更新脚本
Day 110 (2026-06-07 周日): 绍兴 → 宁波 → 普陀山（海天佛国·南海观音）
  - 距离约 150km（绍兴→宁波 100km + 宁波→朱家尖码头 80km 含摆渡）
  - 端午假期第一天，宁波/普陀山客流高峰
  - 衔接 Day 111: 普陀山深度 → 返宁波

AI 搜索今日不可用（web_search/web_fetch 全部失败），使用行程逻辑更新。
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = r'C:\Users\admin\.openclaw\workspace\china-trip\index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount 110→111 (+1), kmCount 15050→15200 (+150), locationCount 99→101 (+2)
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 150) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 2) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>普陀山 · 南海观音\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

day110_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">110</span>
                    <span class="day-date">2026-06-07 · 五月十一 · 周日 · 端午</span>
                </div>
                <div class="day-title">🌊 普陀山 · 海天佛国 · 南海观音道场</div>
                <div class="day-content">
                    <p>🚗 今日行程：绍兴 → 宁波 → 朱家尖蜈蚣峙码头 → 普陀山（约 150km，2.5h+船 15-30min）</p>
                    <p>🛣️ 路线：绍兴上G1522常台高速向东到宁波，转G9211甬舟高速到舟山，朱家尖码头停车坐快艇</p>
                    <p>🎫 提前订！普陀山大门票+往返船票 220元/人（半山/全山），端午高峰须"普陀山"公众号提前1-3天预约</p>
                    <p>⛴️ 上午：朱家尖蜈蚣峙码头 7:00-17:00 班船密集（15分钟一班，单程15分钟）</p>
                    <p>🛕 上午：登岛后坐景区巴士到 慧济寺（普陀山最高处，普陀山三大寺之一）→ 缆车单程 40元</p>
                    <p>🌅 中午：法雨寺（三大寺之二，清康熙赐匾"天花法雨"）→ 午餐素斋 20元起</p>
                    <p>🗿 下午：南海观音立像（33米高，1997年建成，普陀山标志，乘景区巴士到）</p>
                    <p>🛕 下午：普济寺（三大寺之首，前身为"不肯去观音院"，建于后梁 916年）</p>
                    <p>🌊 傍晚：千步沙（百步沙之姐妹，沙滩 1.5公里，免费，6月可踩水不可游）</p>
                    <p>🌃 晚上：返回宁波住宿（普陀山民宿 600-1500元/晚，端午暴涨）或 住岛上（次日免二次船票）</p>
                    <p>🍜 晚餐：宁波菜代表（红膏炝蟹、雪菜黄鱼、宁波汤圆、年糕、虾籽面），或岛上素斋</p>
                    <p>🏨 住宿推荐：宁波市区（次日高铁/自驾方便）/ 普陀山民宿（深度体验）</p>
                    <p>📅 明日预告：普陀山深度（洛迦山/梵音洞/西天景区）→ 返宁波 → 奉化溪口</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🛕</div>
                    <div class="photo-placeholder">⛴️</div>
                    <div class="photo-placeholder">🗿</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🌊</span>
                        <span class="tip-text">普陀山是"中国佛教四大名山"之一（文殊·五台·普贤·峨眉·地藏·九华·观音·普陀），观音菩萨道场</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">⛴️</span>
                        <span class="tip-text">端午假期客流量大！船票+门票实名制提前预约（公众号"普陀山"），朱家尖码头停车 30元/天</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🗿</span>
                        <span class="tip-text">33米南海观音是必打卡，1997年建成；顺路看"不肯去观音院"传说（普济寺前身，日本僧人慧锷）</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">💰</span>
                        <span class="tip-text">岛上香花券 + 寺院小门票另收（普济寺 5元、法雨寺 5元、慧济寺 5元、观音立像 6元），准备好零钱</span>
                    </div>
                </div>
            </div>

'''

content = content[:footer_pos] + day110_entry + content[footer_pos:]
print('Added Day 110 entry')

# Update footer tips: 浙东端午 → 海岛佛国普陀山端午
old_footer = '''<p style="font-size: 14px; margin-bottom: 10px;">📰 2026年6月浙东·端午旅游贴士</p>
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

new_footer = '''<p style="font-size: 14px; margin-bottom: 10px;">📰 2026年6月浙东·普陀山端午旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🌊 端午普陀山"南海观音文化节"开幕（6/6-6/8），客流量是平日3-5倍，限流+实名预约</li>
                    <li>⛴️ 普陀山船票+门票 220元/人，朱家尖蜈蚍峙码头出发，15-30min一班，停车30元/天</li>
                    <li>🛕 三大寺：普济寺（首）/ 法雨寺 / 慧济寺（顶），香花券各5元；南海观音立像33米（必看）</li>
                    <li>🦀 宁波必尝：红膏炝蟹、雪菜黄鱼、宁波汤圆、虾籽面、奉化芋头；缸鸭狗老字号</li>
                    <li>🏨 端午住宿暴涨：普陀山民宿 600-1500元/晚，宁波市区 400-800元；建议住宁波 性价比更高</li>
                    <li>🚗 绍兴→宁波100km / 宁波→朱家尖码头80km，端午高速免费但严重拥堵，备3-4小时</li>
                    <li>📅 明日预告：普陀山深度（洛迦山·梵音洞·西天景区）→ 返宁波 → 奉化溪口</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年6月6日（周六）</p>'''

if old_footer in content:
    content = content.replace(old_footer, new_footer)
    print('Footer tips fully updated')
else:
    # Fallback: just update last-update + tomorrow preview
    content = content.replace('最后更新：2026年6月5日（周五）', '最后更新：2026年6月6日（周六）')
    content = content.replace(
        '📅 明日预告：宁波 → 普陀山——海天佛国 · 南海观音 · 33米大佛',
        '📅 明日预告：普陀山深度（洛迦山·梵音洞·西天景区）→ 返宁波 → 奉化溪口')
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
