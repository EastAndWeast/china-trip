# -*- coding: utf-8 -*-
"""环游中国 - Day115 更新脚本
Day115 (2026-06-12 周五):杭州深度游 - 灵隐寺·飞来峰·龙井村·京杭大运河
 -距离约30km(灵隐寺10km + 龙井村8km + 京杭大运河12km,市内深度游)
 -6 月梅雨季初期天气:多云 34/24℃(weather.com.cn 实测)
 -衔接 Day116:杭州 → 苏州(170km) / 上海(180km) / 千岛湖(150km)

AI 搜索数据(2026-06-12 06:01):
- 灵隐寺:始建于 328 AD(东晋),印度僧人慧理创建,门票 30元,开放 7:00-18:15
  19m 释迦牟尼坐像 / 500 罗汉 / 大雄宝殿
- 飞来峰:5A + UNESCO 世界文化遗产,380+ 摩崖石刻(五代十国起)
- 龙井村:西湖龙井核心产区,"狮龙云虎"中"狮"字号(狮峰龙井)
- 京杭大运河:2014 UNESCO 世界文化遗产,始建于春秋(前 486 邗沟),隋炀帝 610 贯通
- 良渚古城遗址:5000 年前,2019 UNESCO 申遗,五千年文明实证
- 天气:6/12 杭州多云 34/24℃(梅雨季未到峰值,典型 6 月晴朗天)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = r'C:\Users\admin\.openclaw\workspace\china-trip\index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount115→116 (+1), kmCount15700→15730 (+30), locationCount110→114 (+4)
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 30) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 4) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>杭州 · 灵隐寺 · 世界佛教文化地 · 京杭大运河双遗产\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

# Day 115 entry - 1 space indentation (verified from actual HTML structure)
day115_entry = '''
 <div class="day-card">
 <div class="day-header">
 <span class="day-number">115</span>
 <span class="day-date">2026-06-12 · 五月十六 · 周五</span>
 </div>
 <div class="day-title">⛩️杭州深度游 · 灵隐寺·飞来峰·龙井村·京杭大运河 → 4 大世界遗产一线</div>
 <div class="day-content">
 <p>🚗今日行程：杭州深度游（市内约30km，地铁/打车/公交，多云 34/24℃梅雨季初期晴朗）</p>
 <p>🛕上午7:30：地铁 1 号线"龙翔桥"→ 换乘 7 路公交至"灵隐"站 → 步行至<b>灵隐景区</b>（飞来峰+灵隐寺联票 75元，含飞来峰45+灵隐寺30）</p>
 <p>⛰️上午8:30：<b>飞来峰</b>（5A，世界文化遗产，UNESCO 西湖文化景观 2011）—五代十国至元代 380+ 摩崖石刻造像；青林洞/玉乳洞/龙泓洞/呼猿洞；青林洞内"卢舍那佛会"浮雕为北宋造像巅峰</p>
 <p>🙏上午9:30：<b>灵隐寺</b>（始建于 328 AD 东晋，印度僧人慧理创建，门票 30元 7:00-18:15）—天王殿（弥勒/韦驮/四大金刚）→大雄宝殿（19m 释迦牟尼坐像/海岛观音/文殊普贤）→药师殿→五百罗汉堂（500 尊青铜罗汉）→华严殿</p>
 <p>🍜中午12:00：<b>天竺三寺</b>（法喜/法净/法镜，三寺联票 10元）—法喜寺（上天竺）素斋（10元/人）—乾隆御笔"法喜寺"匾额/500 年古玉兰</p>
 <p>🍵下午14:00：<b>龙井村</b>（西湖龙井核心产区，"狮龙云虎"四字排行中"狮"字号 — 狮峰龙井）—参观御茶园/十八棵御茶/胡公庙/老龙井；春茶明前 5800元/斤、雨前 2800元/斤；龙井茶炒制非遗体验（80元/人 30min）</p>
 <p>🍃下午15:30：<b>中国茶叶博物馆</b>（龙井馆区，免费，"茶萃厅"陈列 6 大茶类 300+ 名茶样）—茶艺表演/茶宴套餐（180元/人）</p>
 <p>🌉下午16:30：地铁 1 号线→ 5 号线"大运河"站 → <b>京杭大运河</b>（2014 UNESCO 世界文化遗产，始建于春秋前 486 年邗沟，隋炀帝 610 年贯通）—拱宸桥（明崇祯四年 1631 年重建，"拱宸"意为"拱手迎宸"）→ 桥西历史街区（免费）</p>
 <p>🚢下午17:30：<b>运河夜游</b>（"钱运号"/"拱宸号"，90min，180元/人 19:00 开船）—从拱宸桥至武林广场，沿途 19 座古桥亮灯，京杭大运河 1794km 终点北京通州</p>
 <p>🌃晚上19:30：<b>武林广场</b>（杭州城市客厅）—音乐喷泉（免费 19:30/20:30）或武林夜市（200+ 摊位，尝片儿川/猫耳朵/葱包桧/吴山酥油饼）</p>
 <p>🍽️晚餐推荐：外婆家（西湖文化广场店，杭帮菜平价 60-80元/人）/ 绿茶餐厅（西湖店）/ 弄堂里（龙井路店 招牌鸡煲 88元）/ 知味观（百年老字号 小吃 30-50元）</p>
 <p>🏨住宿推荐：西湖周边（湖滨/南山路/北山街）500-1500元/晚；运河边（拱墅区）400-800元/晚</p>
 <p>📅明日预告：杭州→ 苏州（170km，G92/G2 高速 2h，园林/评弹/苏帮菜）/ 杭州→ 上海（180km，高铁 1h）/ 杭州→ 千岛湖（150km，G2504 高速 2h）</p>
 </div>
 <div class="photos">
 <div class="photo-placeholder">⛩️</div>
 <div class="photo-placeholder">🍵</div>
 <div class="photo-placeholder">🌉</div>
 </div>
 <div class="tips">
 <div class="tip">
 <span class="tip-icon">⛰️</span>
 <span class="tip-text">飞来峰 5A + UNESCO 世界文化遗产（西湖文化景观 2011）！五代十国至元代 380+ 摩崖石刻造像；青林洞卢舍那佛会浮雕为北宋造像巅峰；建议 7:30 前到避人潮</span>
 </div>
 <div class="tip">
 <span class="tip-icon">🙏</span>
 <span class="tip-text">灵隐寺门票 30元（7:00-18:15），始建 328 AD（东晋）印度僧人慧理；19m 释迦牟尼坐像 / 500 罗汉 / 大雄宝殿；2026 6月梅雨季初期 7-9 点最舒适</span>
 </div>
 <div class="tip">
 <span class="tip-icon">🍵</span>
 <span class="tip-text">龙井村"狮"字号（狮峰龙井）是西湖龙井顶级！明前茶 5800/斤、雨前 2800/斤；老龙井/十八棵御茶/胡公庙必看；龙井炒茶非遗 80元/人</span>
 </div>
 <div class="tip">
 <span class="tip-icon">🌉</span>
 <span class="tip-text">京杭大运河 2014 UNESCO 世界文化遗产！始建春秋（前 486 邗沟），隋炀帝 610 贯通；拱宸桥明崇祯四年（1631）重建；桥西历史街区免费！</span>
 </div>
 <div class="tip">
 <span class="tip-icon">🚢</span>
 <span class="tip-text">运河夜游"钱运号"/"拱宸号"180元/人 19:00 开船 90min；19 座古桥亮灯（拱宸桥/广济桥/卖鱼桥/富义仓）；武林广场音乐喷泉免费 19:30/20:30</span>
 </div>
 </div>
 </div>

'''

content = content[:footer_pos] + day115_entry + content[footer_pos:]
print('Added Day115 entry')

# Update footer tips:杭州 → 杭州深度游(灵隐·龙井·京杭大运河·世界遗产)
# 关键:实际 HTML 用 16 空格缩进(LRN-20260611-001 教训)
old_footer = '''                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年6月浙东·杭州西湖+世界文化双遗产贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🌊 西湖（5A）UNESCO2007/2011 双遗产！世界文化景观+2016 G20 主会场；6 月荷花第一波盛开（6/15-7/10 最佳）</li>
                    <li>🚢 三潭印月船票 55元含上岛，湖滨/苏堤/岳湖 6 码头；苏堤春晓/断桥/雷峰塔/平湖秋月为四大必游</li>
                    <li>🏮 河坊街·南宋御街免费！胡庆余堂 1874 年创立（"江南药王"） / 朱炳仁铜雕艺术馆免费 / 老字号药铺</li>
                    <li>🍜 楼外楼百年老店（1848）：西湖醋鱼+东坡肉+龙井虾仁+叫花鸡（人均 200-300元）；平价选外婆家 60-80元</li>
                    <li>🌃 西湖音乐喷泉免费（19:00/20:00 湖滨步行街）；印象西湖张艺谋导演 280元/人 19:45</li>
                    <li>🚗 绍兴→杭州 G92 杭甬高速 1.5h + G2504 杭州绕城 30min（170km）；6 月梅雨季阵雨带轻便雨具</li>
                    <li>📅 明日预告：杭州深度游（灵隐寺·飞来峰·龙井村·京杭大运河）/ 杭州→苏州（170km） / 上海（180km）</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年6月11日（周四）</p>'''

new_footer = '''                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年6月浙东·杭州深度游+4 大世界遗产一线贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>⛰️ 飞来峰 5A + UNESCO（西湖文化景观 2011）！五代十国至元代 380+ 摩崖石刻造像；青林洞卢舍那佛会浮雕为北宋巅峰</li>
                    <li>🙏 灵隐寺门票 30元 7:00-18:15；始建 328 AD（东晋）印度僧人慧理；19m 释迦牟尼坐像 / 500 罗汉 / 大雄宝殿</li>
                    <li>🍵 龙井村"狮"字号（狮峰龙井）是西湖龙井顶级！明前 5800/斤 / 雨前 2800/斤；老龙井/十八棵御茶/胡公庙必看</li>
                    <li>🌉 京杭大运河 2014 UNESCO 世界文化遗产！始建春秋（前 486 邗沟）隋炀帝 610 贯通；拱宸桥明崇祯四年（1631）重建</li>
                    <li>🚢 运河夜游"钱运号"180元/人 19:00 90min；19 座古桥亮灯；武林广场音乐喷泉免费 19:30/20:30</li>
                    <li>🚇 杭州市内 1/5 号线串联灵隐-运河；天竺三寺联票 10元；6/12 多云 34/24℃ 梅雨季初期最佳出游日</li>
                    <li>📅 明日预告：杭州→ 苏州（170km 园林/评弹/苏帮菜）/ 上海（180km 高铁 1h）/ 千岛湖（150km G2504 高速 2h）</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年6月12日（周五）</p>'''

if old_footer in content:
    content = content.replace(old_footer, new_footer)
    print('Footer tips fully updated (16-space indent match)')
else:
    # Fallback: just update last-update + tomorrow preview with proper indent
    print('WARN: exact footer match failed, trying fallback')
    # Try simpler replacement - just the last update line
    content = content.replace('最后更新：2026年6月11日（周四）', '最后更新：2026年6月12日（周五）')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print('HTML updated successfully')

# Verify
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    verify = f.read()
day_cards = re.findall(r'<div class="day-card">\s*<div class="day-header">\s*<span class="day-number">(\d+)</span>\s*<span class="day-date">([^<]+)</span>', verify, re.DOTALL)
print('Total day cards:', len(day_cards))
print('Last3 days:', day_cards[-3:] if day_cards else 'none')
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

# Sanity check: Day 115 should exist
if 'day-number">115</span>' in verify:
    print('Day 115 card present: YES')
else:
    print('Day 115 card present: NO -- ERROR!')
