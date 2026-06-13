# -*- coding: utf-8 -*-
"""环游中国 - Day116 更新脚本
Day116 (2026-06-13 周六):杭州→乌镇·西栅·江南水乡·茅盾故里·木心美术馆
 -距离约80km(杭州→乌镇 G2504 + S12 高速 1.5h)
 -6 月梅雨季天气:小雨 25/20℃(weather.com.cn 实测)
 -衔接 Day117:乌镇→苏州(85km)/ 西塘(40km)/ 上海(120km)

AI 搜索数据(2026-06-13 06:01):
- 乌镇:江南六大水乡之首(与周庄/同里/西塘/南浔/甪直),1300+ 年历史(春秋吴越边陲)
- 西栅景区:150元/人,12.5km²,河道 1.8 万米,72 座古桥,2021 改造后度假+古镇合一
- 东栅景区:110元/人,原汁原味水乡生活,茅盾故居/修真观/老邮局
- 联票(西+东):190元/人(2 日有效)
- 木心美术馆:20元/人,贝聿铭弟子冈本博设计,2015 开放,木心故里
- 老邮局:建于 1900 年(光绪二十六年),仍可寄明信片
- 茅盾故居:1983 列为省级文保单位,《子夜》《林家铺子》创作地
- 宏源泰染坊:蓝印花布非遗体验(20元)
- 乌镇互联网国际会展中心:世界互联网大会永久会址(2014 起)
- 天气:6/13 杭州小雨 25/20℃(梅雨季初阵雨,江南水乡意境更浓)
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = r'C:\Users\admin\.openclaw\workspace\china-trip\index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount116→117 (+1), kmCount15730→15810 (+80), locationCount114→118 (+4)
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 80) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 4) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>乌镇 · 西栅 · 江南水乡之首 · 茅盾故里与木心美术馆\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

# Day 116 entry - 1 space indentation (verified from actual HTML structure)
day116_entry = '''
 <div class="day-card">
 <div class="day-header">
 <span class="day-number">116</span>
 <span class="day-date">2026-06-13 · 五月十七 · 周六</span>
 </div>
 <div class="day-title">🏞️杭州→乌镇 · 江南水乡之首 · 茅盾故里·木心美术馆·西栅夜游</div>
 <div class="day-content">
 <p>🚗今日行程：杭州→乌镇（约 80km，G2504 杭长高速+S12 申嘉湖高速 1.5h；小雨 25/20℃ 梅雨季阵雨，正合江南水乡意境）</p>
 <p>🚌上午 8:00：杭州东站/汽车西站乘大巴至乌镇汽车站（35 元/人 1.5h，每 30min 一班）或自驾 G2504 高速直达；入住西栅景区内民宿（400-1200 元/晚，推窗见水）</p>
 <p>📮上午 10:30：<b>东栅景区</b>（110 元/人 开放 7:30-17:30，原汁原味水乡生活）— 茅盾故居（1983 省级文保，《子夜》《林家铺子》《春蚕》创作地）→ 修真观（始建于北宋 998 年，道教圣地）→ 翰墨轩（林家铺子原型）→ 老邮局（1900 年光绪二十六年建，仍寄明信片）</p>
 <p>🍜中午 12:00：东栅内<b>翰墨轩酒楼</b>品尝乌镇三珍（姑嫂饼/三珍斋酱鸡/定胜糕）或<b>张恒兴面馆</b>（35-50 元/人招牌羊肉面/红烧羊肉）</p>
 <p>🎨下午 14:00：<b>木心美术馆</b>（20 元/人 9:00-17:30，贝聿铭弟子冈本博设计 2015 年开馆）— 木心（1927-2011）从乌镇走向世界，木心文学+绘画双遗产，《文学回忆录》《木心谈木心》</p>
 <p>🌉下午 15:30：步行/摆渡至<b>西栅景区</b>（150 元/人 9:00-22:00，12.5km² 大型度假古镇，72 座古桥+河道 1.8 万米）— 草本染色作坊（蓝印花布非遗 20 元/人体验）→ 乌镇互联网国际会展中心（2014 世界互联网大会永久会址）→ 昭明书院（南朝梁昭明太子萧统读书地，《昭明文选》）</p>
 <p>⛵下午 17:00：<b>摇橹船夜游</b>（60 元/人 18:30-21:00 单程 25min）— 灯笼亮起，乘船穿过 12 座古桥，看两岸白墙黛瓦倒映水面</p>
 <p>🍶晚上 19:00：<b>西栅夜景</b>（免费，景区内）— 乌镇大戏院（评弹/锡剧/越剧 30 元/人）、乌将军庙、灵水居；可尝<b>外婆桥船菜</b>（80-150 元/人 临河）或<b>民国时代咖啡馆</b>（手冲咖啡 38 元）</p>
 <p>🌃晚上 21:30：返回民宿，枕水而眠；推荐<b>枕水度假酒店</b>（800-1500 元/晚 五星）/ <b>乌镇行馆</b>（500-800 元/晚 四星）/ <b>民宿</b>（400-600 元/晚 推窗见水）</p>
 <p>🍽️晚餐推荐：翰墨轩酒楼（东栅）/ 外婆桥船菜（西栅 临河）/ 张恒兴面馆（招牌羊肉）/ 乌镇小火锅（60-80 元/人）</p>
 <p>🏨住宿推荐：西栅景区内民宿（400-1200 元/晚 推窗见水）/ 西栅外酒店（200-400 元/晚 经济）/ 乌镇镇区（150-300 元/晚 平价）</p>
 <p>📅明日预告：乌镇→ 苏州（85km，G50 沪渝高速 1.5h，园林/评弹/苏帮菜）/ 乌镇→ 西塘（40km，江南六大水乡之一）/ 乌镇→ 上海（120km，高铁/自驾 1.5h）</p>
 </div>
 <div class="photos">
 <div class="photo-placeholder">🏞️</div>
 <div class="photo-placeholder">🎨</div>
 <div class="photo-placeholder">⛵</div>
 </div>
 <div class="tips">
 <div class="tip">
 <span class="tip-icon">🏞️</span>
 <span class="tip-text">乌镇江南六大水乡之首（与周庄/同里/西塘/南浔/甪直）！1300+ 年历史；西栅 150 元 / 东栅 110 元 / 联票 190 元（2 日有效）；西栅夜景 21:00 前最盛</span>
 </div>
 <div class="tip">
 <span class="tip-icon">🎨</span>
 <span class="tip-text">木心美术馆 20 元/人，贝聿铭弟子冈本博设计 2015 开放；木心（1927-2011）从乌镇走向世界，《文学回忆录》《木心谈木心》；建议先读《木心遗稿》再参观</span>
 </div>
 <div class="tip">
 <span class="tip-icon">📮</span>
 <span class="tip-text">乌镇老邮局建于 1900 年（光绪二十六年），中国早期邮局之一，至今仍可寄明信片；从这里寄一张盖乌镇邮戳的明信片回家，留念感拉满</span>
 </div>
 <div class="tip">
 <span class="tip-icon">🏛️</span>
 <span class="tip-text">茅盾故居 1983 列为省级文保；《子夜》《林家铺子》《春蚕》创作地；修真观始建于北宋 998 年（宋真宗年间），道教圣地；江南水乡文学+宗教双遗产</span>
 </div>
 <div class="tip">
 <span class="tip-icon">⛵</span>
 <span class="tip-text">摇橹船夜游 60 元/人 18:30-21:00 单程 25min；穿过 12 座古桥看两岸白墙黛瓦；2021 西栅改造后成"度假+古镇"；梅雨季雨中水乡意境最浓</span>
 </div>
 </div>
 </div>

'''

content = content[:footer_pos] + day116_entry + content[footer_pos:]
print('Added Day116 entry')

# Update footer tips: 杭州深度游 → 杭州-乌镇·江南水乡双镇(西栅·东栅·木心美术馆·茅盾)
old_footer = '''                <p style="font-size: 14px; margin-bottom: 10px;">馃摪 2026骞?鏈堟禉涓溌锋澀宸炴繁搴︽父+4 澶т笘鐣岄仐浜т竾绾胯创澹?/p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>鉀帮笍 椋炴潵宄?5A + UNESCO锛堣タ婀栨枃鍖栨櫙瑙?2011锛夛紒浜斾唬鍗佸浗鑷冲厓浠?380+ 鎽╁礀鐭冲埢閫犲儚锛涢潚鏋楁礊鍗㈣垗閭ｄ經浼氭诞闆曚负鍖楀畫宸呭嘲</li>
                    <li>馃檹 鐏甸殣瀵洪棬绁?30鍏?7:00-18:15锛涘寤?328 AD锛堜笢鏅嬶級鍗板害鍍т汉鎱х悊锛?9m 閲婅喀鐗熷凹鍧愬儚 / 500 缃楁眽 / 澶ч泟瀹濇</li>
                    <li>馃嵉 榫欎簳鏉?鐙?瀛楀彿锛堢嫯宄伴緳浜曪級鏄タ婀栭緳浜曢《绾э紒鏄庡墠 5800/鏂?/ 闆ㄥ墠 2800/鏂わ紱鑰侀緳浜?鍗佸叓妫靛尽鑼?鑳″叕搴欏繀鐪?/li>
                    <li>馃寜 浜澀澶ц繍娌?2014 UNESCO 涓栫晫鏂囧寲閬椾骇锛佸寤烘槬绉嬶紙鍓?486 閭楁矡锛夐殝鐐€甯?610 璐€氾紱鎷卞妗ユ槑宕囩ク鍥涘勾锛?631锛夐噸寤?/li>
                    <li>馃殺 杩愭渤澶滄父"閽辫繍鍙?180鍏?浜?19:00 寮€鑸?90min锛?19 搴у彜妗ヤ寒鐏紱姝︽灄骞垮満闊充箰鍠锋硥鍏嶈垂 19:30/20:30</li>
                    <li>馃殗 鏉窞甯傚唴 1/5 鍙风嚎涓茶仈鐏甸殣-杩愭渤锛涘ぉ绔轰笁瀵鸿仈绁?10鍏冿紱6/12 澶氫簯 34/24鈩?姊呴洦瀛ｅ垵鏈熸渶浣冲嚭娓告棩</li>
                    <li>馃搮 鏄庢棩棰勫憡锛氭澀宸炩啋 鑻忓窞锛?70km 鍥灄/璇勫脊/鑻忓府鑿滐級/ 涓婃捣锛?80km 楂橀搧 1h锛? 鍗冨矝婀栵紙150km G2504 楂橀€?2h锛?/li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">鏈€鍚庢洿鏂帮細2026骞?鏈?2鏃ワ紙鍛ㄤ簲锛?/p>'''

# Note: we have to use the actual UTF-8 text in the comparison, not the mojibake
# Let me use the correct Chinese text directly

# Update footer with proper Chinese text
old_footer_correct = '''                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年6月浙东·杭州深度游+4 大世界遗产一线贴士</p>
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

new_footer_correct = '''                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年6月浙东·杭州-乌镇·江南水乡双镇贴士（世界互联网大会永久会址）</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏞️ 乌镇江南六大水乡之首（周庄/同里/西塘/南浔/甪直）！1300+ 年历史；西栅 150 元 / 东栅 110 元 / 联票 190 元（2 日有效）</li>
                    <li>🎨 木心美术馆 20 元/人！贝聿铭弟子冈本博设计 2015 开放；木心（1927-2011）《文学回忆录》《木心谈木心》；先读《木心遗稿》再参观</li>
                    <li>📮 乌镇老邮局 1900 年光绪二十六年建！中国早期邮局之一，至今可寄明信片；从这里寄一张盖乌镇邮戳的明信片回家</li>
                    <li>🏛️ 茅盾故居 1983 省级文保！《子夜》《林家铺子》《春蚕》创作地；修真观始建北宋 998 年（宋真宗），道教圣地</li>
                    <li>⛵ 摇橹船夜游 60 元/人 18:30-21:00！穿过 12 座古桥；西栅夜景 21:00 前最盛；6/13 小雨 25/20℃ 梅雨季水乡意境最浓</li>
                    <li>🚗 杭州→乌镇 80km G2504 + S12 高速 1.5h；西栅内民宿 400-1200 元/晚推窗见水；乌镇互联网国际会展中心 2014 起永久会址</li>
                    <li>📅 明日预告：乌镇→ 苏州（85km G50 沪渝高速 1.5h 园林/评弹/苏帮菜）/ 西塘（40km 江南六大水乡）/ 上海（120km 高铁 1.5h）</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年6月13日（周六）</p>'''

if old_footer_correct in content:
    content = content.replace(old_footer_correct, new_footer_correct)
    print('Footer tips fully updated (correct Chinese match)')
else:
    # Fallback: just update last-update + tomorrow preview
    print('WARN: exact footer match failed, trying fallback (regex)')
    # Update last update line using regex (16-space indent)
    content = re.sub(
        r'最后更新：2026年6月12日（周五）',
        '最后更新：2026年6月13日（周六）',
        content)

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

# Sanity check: Day 116 should exist
if 'day-number">116</span>' in verify:
    print('Day 116 card present: YES')
else:
    print('Day 116 card present: NO -- ERROR!')

# Verify Day 115 still there (should be after Day 116)
day115_count = verify.count('day-number">115</span>')
day116_count = verify.count('day-number">116</span>')
print('Day 115 occurrences:', day115_count)
print('Day 116 occurrences:', day116_count)

# Check file size
import os
print('New file size:', os.path.getsize(HTML_PATH))