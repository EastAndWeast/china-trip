# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update day count 59 -> 60
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 2. Update location count (no new city, still in 武夷山)
# No change to locationCount

# 3. Update km (local movement within 武夷山景区，约15km)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 15) + '<',
    content)

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">武夷山 · 天游峰<',
    content)

print('Updated stats: Day 60, km +15, location -> 武夷山 · 天游峰')

# 5. Add Day 60 entry before footer
day60_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第60天</span>
                    <span class="day-date">2026-04-17 · 三月二十</span>
                </div>
                <div class="day-title">🏔️ 武夷山深度游 · 九曲溪竹筏·天游峰登顶</div>
                <div class="day-content">
                    <p>武夷山深度游第一天！经过昨天一路奔波，今天终于可以好好感受这座世界自然与文化双重遗产的魅力！</p>
                    <p>🛶 清晨体验：九曲溪竹筏漂流（重头戏！）</p>
                    <p>早上6:30景区开门就出发！九曲溪是武夷山的精华所在，"溪曲三三水，山环六六峰"，乘竹筏漂流而下，抬头可观山景，俯首能赏水色！</p>
                    <p>🌊 九曲溪竹筏：武夷山最经典体验！约130元/人，全程约2小时，建议清晨6:30出发人少景美，需提前在"福建武夷山"公众号预订</p>
                    <p>竹筏上可听船工讲解两岸典故（一般每位船工需给20-30元小费），经过"架壑船棺"等奇观，非常震撼！</p>
                    <p>🏔️ 上午：天游峰登山</p>
                    <p>天游峰——武夷山第一胜地，海拔408.8米，有"不到天游，等于白游"之说！登顶俯瞰九曲溪全景，云海翻涌，宛如仙境！</p>
                    <p>天游峰登山路线：景区南入口→乘坐观光车→天游峰入口→登顶约1-1.5小时，台阶较陡，建议穿防滑鞋，体力消耗中等</p>
                    <p>☁️ 天游峰云海：雨后乍晴或清晨最容易看到云海，今天运气不错，看到了云雾缭绕的壮观景象！</p>
                    <p>🍵 下午：岩茶体验——朝圣大红袍</p>
                    <p>武夷山是岩茶（武夷岩茶）发源地，大红袍母树就生长在九龙窠景区！4月正值采茶季，云雾缭绕的茶园飘散着岩骨花香！</p>
                    <p>🍃 特别提醒：武夷山连续两年位居全国县域自驾游榜首；"武夷山采茶制茶体验之旅"成功入选2026全国100条"茶乡四时好风光"旅游精品线路！</p>
                    <p>🌱 采茶体验：可在茶庄园预约采茶制茶体验（费用约58元/人），亲手采摘、摇青、炒茶，感受非遗文化</p>
                    <p>🏨 下午入住武夷山景区内酒店，继续探索明天的一线天、虎啸岩！</p>
                    <p>📊 今日行程：武夷山景区深度游，竹筏2小时+天游峰登山2小时+大红袍景区1小时，步行约8公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🛶</div>
                    <div class="photo-placeholder">🏔️</div>
                    <div class="photo-placeholder">🍵</div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day60_entry + '\n' + footer_marker)
print('Added Day 60 entry for 武夷山深度游')

# 6. Update travel tips
old_footer_pattern = r'<div class="footer">.*?<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月16日</p>.*?</div>'

new_footer = '''<div class="footer">
            <p>🚗 环游中国 · 房车日记</p>
            <p>记录每一天的所见所闻</p>
            <div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年4月中旬武夷山旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🛶 九曲溪竹筏：武夷山最经典体验！约130元/人，约2小时，建议清晨6:30出发人少景美，需提前7天在"福建武夷山"公众号预订</li>
                    <li>🏔️ 天游峰："不到天游，等于白游"，海拔408.8米，登山约1-1.5小时，雨后乍晴清晨最容易看到云海</li>
                    <li>🍵 武夷山采茶季：4月正值！岩骨花香，采茶制茶体验入选2026全国100条茶旅精品线路，建议提前预约茶庄园体验</li>
                    <li>🎫 门票信息：主景区免门票（延续至2026年）；观光车85元/人；竹筏票130元/人；1日联票约340元/人</li>
                    <li>🍜 必尝美食：武夷山熏鹅（必尝！）、笋干烧肉、菌菇汤、文公菜，大红袍茶叶蛋也很有名</li>
                    <li>🏨 住宿：推荐住三姑度假区或景区南入口附近，离竹筏码头近，出行方便</li>
                    <li>🚗 交通：武夷山机场有直飞航班，高铁也很便捷；景区内环保车很方便，可南北入口通用</li>
                    <li>📅 特别活动：游侠风第二届武夷山徒步大会进行中！感兴趣可咨询当地旅行社</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月17日</p>
            </div>
        </div>'''

new_content = re.sub(old_footer_pattern, new_footer, content, flags=re.DOTALL)
if new_content != content:
    print('Updated travel tips to 武夷山')
else:
    print('WARNING: Could not find old footer to replace')

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('\n=== Update Complete ===')
print('Day: 60')
print('Location: 武夷山 · 天游峰')
print('Date: 2026-04-17')
print('Stats: DayCount +1, kmCount +15')
