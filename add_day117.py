# -*- coding: utf-8 -*-
"""环游中国 - Day117 更新脚本
Day117 (2026-06-14 周日):乌镇→苏州·世界遗产园林·平江路·苏帮菜·寒山寺
 -距离约85km(乌镇→苏州 G50 沪渝高速 1.5h)
 -6 月梅雨季天气:小雨转阴 26/22℃(weather.com.cn 101190401 实测)
 -衔接 Day118:苏州→南京(220km)/ 同里(20km)/ 上海(100km)

AI 搜索数据(2026-06-14 06:01):
- 苏州:2500+ 年历史,514 BC 春秋吴王阖闾命伍子胥建城(古称吴/姑苏/平江);与杭州并称"人间天堂"(唐宋以来)
- 苏州古典园林:1997 UNESCO 第 1 项苏州世界文化遗产(拙政园/留园/网师园/环秀山庄)
- 拙政园:90元/人(旺季 7-8月),东/中/西三部,文徵明参与设计,水面积占 1/3,"中国园林典范"
- 留园:55元/人,以"留"字立意(刘恕/盛康 1593 建),与拙政园并称"苏州园林双壁"
- 狮子林:40元/人,元代 1342 倪瓒参与设计,"假山王国"(500+ 太湖石)
- 网师园:30元/人(夜花园 80元 19:30-22:00),"以小见大"典范,1997 UNESCO
- 寒山寺:20元/人,因张继《枫桥夜泊》"姑苏城外寒山寺"闻名,1512 重修
- 山塘街:免费(山塘阁/古戏台/老茶馆),3600m "七里山塘"白居易 825 修
- 平江路:免费,800+ 年水巷,沿河 1600m,"苏州古城缩影"
- 苏州博物馆:免费(需预约),贝聿铭设计 2006 开放,"现代+传统"建筑典范
- 苏州美食:松鼠桂鱼(松鹤楼 158 元)/ 阳澄湖大闸蟹(秋季)/ 苏式糕点(黄天源 80 年)/ 奥灶面
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = r'C:\Users\admin\.openclaw\workspace\china-trip\index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount117→118 (+1), kmCount15810→15895 (+85), locationCount118→122 (+4)
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 85) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 4) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>苏州 · 拙政园 · 世界文化遗产 · 江南园林甲天下 · 2500年吴文化古城\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

# Day 117 entry - 1 space indentation (verified from actual HTML structure)
day117_entry = '''
 <div class="day-card">
 <div class="day-header">
 <span class="day-number">117</span>
 <span class="day-date">2026-06-14 · 五月十八 · 周日</span>
 </div>
 <div class="day-title">🌧️乌镇→苏州 · 江南园林甲天下 · 拙政园·留园·平江路·苏帮菜</div>
 <div class="day-content">
 <p>🚗今日行程：乌镇→苏州（约 85km，G50 沪渝高速 1.5h；小雨转阴 26/22℃ 梅雨季典型天气，苏州园林烟雨更显韵味）</p>
 <p>🚌上午 8:00：乌镇汽车站乘大巴至苏州南站/苏州北广场汽车站（45 元/人 1.5h，每 30min 一班）或自驾 G50 沪渝高速直达；入住平江路/观前街/园林路附近（400-1200 元/晚 老苏州风情）</p>
 <p>🌳上午 10:00：<b>拙政园</b>（90元/人 7:30-17:30 旺季，中国园林典范，文徵明参与设计）— 兰雪堂（主厅）→ 梧竹幽居（四季景致）→ 远香堂（中部主体）→ 荷风四面亭（夏荷观赏）→ 与谁同坐轩（扇形小亭）→ 小飞虹（廊桥）→ 倒影楼（借景北寺塔）；建议预留 2-3 小时</p>
 <p>🍜中午 12:00：<b>松鹤楼</b>（观前街总店）品尝苏帮菜（人均 100-200 元）— 松鼠桂鱼（招牌/糖醋/形似松鼠）/ 响油鳝糊（鳝鱼+麻油滚油）/ 碧螺虾仁（太湖三白之一）/ 樱桃肉</p>
 <p>🏛️下午 14:00：<b>苏州博物馆</b>（免费 9:00-17:00 周一闭馆，需"苏州博物馆"公众号预约）— 贝聿铭封山之作 2006 开放，"现代+传统"建筑典范（粉墙黛瓦+几何线条+水池倒影）；镇馆之宝：真珠舍利宝幢（北宋）/ 瑞光塔出土文物</p>
 <p>🌉下午 15:30：步行至<b>平江路</b>（免费 全天，800+ 年水巷沿河 1600m，"苏州古城缩影"）— 耦园（东园/西园对偶，世界文化遗产扩展项目 2001）→ 苏州评弹博物馆（吴侬软语评弹表演 30 元/人）→ 翰尔茶馆/猫的天空之城概念书店</p>
 <p>🌃下午 17:00：<b>山塘街</b>（免费 8:00-22:00，"七里山塘" 3600m，唐白居易 825 修筑）— 山塘阁（御碑亭/古戏台/老茶馆）→ 昆曲博物馆（"百戏之祖"昆曲发源地 14 元）→ 苏州商会博物馆；可乘<b>画舫夜游</b>（60 元/人 18:30-21:00）看红灯笼映水巷</p>
 <p>🛕晚上 19:00：打车至<b>寒山寺</b>（20元/人 7:30-17:00，1512 重修）— 因张继《枫桥夜泊》"姑苏城外寒山寺，夜半钟声到客船"千古传诵；聆听新年 108 下钟声（12/31 23:00-00:30 撞钟门票 680 元）；隔<b>枫桥</b>（张继笔下）与<b>铁铃关</b>相望</p>
 <p>🍶晚上 20:30：返回观前街/平江路品尝<b>黄天源</b>（苏式糕点 80 年老字号，糕/团/粽 5-15 元/件）或<b>同得兴</b>（奥灶面 35 元/碗）；推荐<b>哑巴生煎</b>（平江路 12 元/4 个 招牌）</p>
 <p>🌃晚上 21:30：返酒店，枕姑苏城入眠；推荐<b>书香世家·平江府</b>（800-1500 元/晚 五星 园林景观）/ <b>南园宾馆</b>（500-800 元/晚 四星 园外楼）/ <b>桔子精品酒店</b>（300-500 元/晚 精品）</p>
 <p>🍽️晚餐推荐：松鹤楼（观前街 苏帮菜正店/100-200 元/人）/ 松运楼（松鼠桂鱼/80-150 元/人）/ 协和菜馆（凤凰街/人均 80）/ 同得兴（奥灶面/35 元起）</p>
 <p>🏨住宿推荐：平江路/观前街（400-1200 元/晚 老苏州风情）/ 苏州工业园区（300-600 元/晚 现代商务）/ 园林路/十全街（350-700 元/晚 文化氛围）</p>
 <p>📅明日预告：苏州→ 南京（220km G42 沪蓉高速 2.5h，六朝古都/中山陵/秦淮河夫子庙）/ 同里（20km 江南六大水乡之一）/ 上海（100km 高铁 0.5h）</p>
 </div>
 <div class="photos">
 <div class="photo-placeholder">🌳</div>
 <div class="photo-placeholder">🏛️</div>
 <div class="photo-placeholder">🌉</div>
 </div>
 <div class="tips">
 <div class="tip">
 <span class="tip-icon">🌳</span>
 <span class="tip-text">苏州古典园林 1997 UNESCO 第 1 项苏州世界文化遗产！拙政园/留园/网师园/环秀山庄；与北京颐和园/承德避暑山庄并称"中国四大名园"；拙政园 90 元/留园 55 元/狮子林 40 元/网师园 30 元（夜花园 80 元 19:30-22:00）</span>
 </div>
 <div class="tip">
 <span class="tip-icon">🏛️</span>
 <span class="tip-text">苏州博物馆免费（需"苏州博物馆"公众号预约）！贝聿铭封山之作 2006 开放；"现代+传统"粉墙黛瓦+几何线条+水池倒影；镇馆之宝：真珠舍利宝幢（北宋）/ 瑞光塔出土文物；周一闭馆</span>
 </div>
 <div class="tip">
 <span class="tip-icon">🌉</span>
 <span class="tip-text">平江路 800+ 年水巷沿河 1600m 免费！"苏州古城缩影"；苏博→平江路→耦园三步走；翰尔茶馆品碧螺春（明前 1800 元/斤）听评弹（30 元/人）体验最苏州</span>
 </div>
 <div class="tip">
 <span class="tip-icon">🛕</span>
 <span class="tip-text">寒山寺 20 元/人！因张继《枫桥夜泊》"姑苏城外寒山寺"千古传诵；1512 明正德七年重修；新年 12/31 23:00 108 下钟声（680 元撞钟票）；隔壁枫桥+铁铃关同游</span>
 </div>
 <div class="tip">
 <span class="tip-icon">🍜</span>
 <span class="tip-text">苏帮菜八大名菜！松鼠桂鱼（松鹤楼招牌/158 元）/ 响油鳝糊（夏季）/ 碧螺虾仁（太湖三白）/ 樱桃肉 / 蟹粉狮子头 / 酱汁肉 / 母油整鸡 / 鸡汤煮干丝；苏州美食底蕴仅次于粤菜与淮扬菜</span>
 </div>
 </div>
 </div>

'''

content = content[:footer_pos] + day117_entry + content[footer_pos:]
print('Added Day117 entry')

# Update footer tips: 杭州-乌镇·江南水乡双镇 → 苏州·2500年古城·世界文化遗产园林
old_footer_correct = '''                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年6月浙东·杭州-乌镇·江南水乡双镇贴士（世界互联网大会永久会址）</p>
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

new_footer_correct = '''                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年6月苏南·苏州·世界文化遗产园林贴士（拙政园·留园·苏博·寒山寺）</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🌳 苏州古典园林 1997 UNESCO 第 1 项苏州世界文化遗产！拙政园/留园/网师园/环秀山庄；与北京颐和园/承德避暑山庄并称"中国四大名园"</li>
                    <li>🏛️ 苏州博物馆免费（需"苏州博物馆"公众号预约）！贝聿铭封山之作 2006 开放；"现代+传统"粉墙黛瓦+几何线条+水池倒影；周一闭馆</li>
                    <li>🌉 平江路 800+ 年水巷沿河 1600m 免费！"苏州古城缩影"；翰尔茶馆品碧螺春（明前 1800 元/斤）听评弹（30 元/人）体验最苏州</li>
                    <li>🛕 寒山寺 20 元/人！张继《枫桥夜泊》"姑苏城外寒山寺"千古传诵；1512 明正德七年重修；新年 12/31 108 下钟声（680 元撞钟票）</li>
                    <li>🍜 苏帮菜八大名菜：松鼠桂鱼/响油鳝糊/碧螺虾仁/蟹粉狮子头；松鹤楼（观前街/158 元招牌）/ 同得兴（奥灶面 35 元）/ 黄天源（苏式糕点 80 年）</li>
                    <li>🚗 乌镇→苏州 85km G50 沪渝高速 1.5h；苏州地铁 1/2/4 号线串联园林/观前/平江；平江路酒店 400-1200 元/晚 老苏州风情</li>
                    <li>📅 明日预告：苏州→ 南京（220km G42 沪蓉高速 2.5h 六朝古都/中山陵/秦淮河）/ 同里（20km 江南六大水乡）/ 上海（100km 高铁 0.5h）</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年6月14日（周日）</p>'''

if old_footer_correct in content:
    content = content.replace(old_footer_correct, new_footer_correct)
    print('Footer tips fully updated (correct Chinese match)')
else:
    # Fallback: just update last-update line
    print('WARN: exact footer match failed, trying fallback (regex)')
    content = re.sub(
        r'最后更新：2026年6月13日（周六）',
        '最后更新：2026年6月14日（周日）',
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

# Sanity check: Day 117 should exist
if 'day-number">117</span>' in verify:
    print('Day 117 card present: YES')
else:
    print('Day 117 card present: NO -- ERROR!')

# Verify Day 116 still there
day115_count = verify.count('day-number">115</span>')
day116_count = verify.count('day-number">116</span>')
day117_count = verify.count('day-number">117</span>')
print('Day 115 occurrences:', day115_count)
print('Day 116 occurrences:', day116_count)
print('Day 117 occurrences:', day117_count)

# Check file size
import os
print('New file size:', os.path.getsize(HTML_PATH))
