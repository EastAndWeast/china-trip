# -*- coding: utf-8 -*-
"""环游中国 - Day118 更新脚本
Day118 (2026-06-15 周一, 五月十九):苏州→南京·六朝古都·中山陵·秦淮河·夫子庙
 -距离约220km(苏州→南京 G42 沪蓉高速 2.5h)
 -6 月梅雨季天气:小雨转阴 28/22℃ 3-4级转(weather.com.cn 101190101 实测,与苏州模式一致)
 -衔接 Day119:南京→合肥(300km)/ 扬州(100km)/ 镇江(70km)

AI 搜索数据(2026-06-15 06:01,基于 web_fetch weather.com.cn + travelchinaguide.com):
- 南京:2500+ 年建都史,六朝古都(孙吴/东晋/宋/齐/梁/陈);十朝都会(明/南明/太平天国/中华民国);与北京/西安/洛阳并称"中国四大古都"
- 中山陵:5A 免费(需"中山陵预约"公众号),孙中山先生陵寝 1929 建成;392 级台阶/8 个平台;紫金山南麓;蓝白色建筑融合中西
- 明孝陵:5A 70元,世界文化遗产 2003(明清皇家陵寝扩展),朱元璋+马皇后合葬陵;神道"石象生"蜿蜒 2km;紫金山独龙阜玩珠峰
- 夫子庙-秦淮河:5A 江南贡院+大成殿+文德桥;"六朝金粉地,十里秦淮河";夜游 80元/人 18:30-21:30
- 总统府:5A 35元,600+ 年历史;明/清/太平天国/中华民国/共和国五朝遗迹;蒋介石/孙中山办公地
- 南京大屠杀遇难同胞纪念馆:免费(需"南京发布"预约),沉重历史教育,1985 建成
- 玄武湖:江南三大名湖之一 免费;周长 15km,五洲相连(环洲/樱洲/菱洲/梁洲/翠洲)
- 鸡鸣寺:"南朝四百八十寺"之首 10元;始建 300 AD 西晋;"南朝第一寺"
- 老门东:明清古城南保留区 免费;美食:蒋有记锅贴/蓝老大糖芋苗/小郑酥烧饼
- 南京美食:盐水鸭(韩复兴 80年)/ 鸭血粉丝汤(回味 18元)/ 桂花糖芋苗/ 牛肉锅贴/ 金陵小吃
"""
import re, sys, codecs, os
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = r'C:\Users\admin\.openclaw\workspace\china-trip\index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount 118→119 (+1), kmCount 15895→16115 (+220), locationCount 122→126 (+4)
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 220) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 4) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>南京 · 中山陵 · 六朝古都 · 2500年建都史 · 紫金山下扬子江畔\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

# Day 118 entry - 1 space indentation (verified from actual HTML structure of Day 117)
day118_entry = '''
 <div class="day-card">
 <div class="day-header">
 <span class="day-number">118</span>
 <span class="day-date">2026-06-15 · 五月十九 · 周一</span>
 </div>
 <div class="day-title">🏛️苏州→南京 · 六朝古都 · 中山陵·秦淮河·夫子庙·明孝陵·总统府</div>
 <div class="day-content">
 <p>🚗今日行程：苏州→南京（约 220km，G42 沪蓉高速 2.5h；小雨转阴 28/22℃ 3-4 级转，6 月梅雨季典型天气，南京梧桐城在雨季更显历史厚重）</p>
 <p>🚄早 7:30：苏州站乘高铁至南京南站（G 字头 1.5h 145 元/二等座）或自驾 G42 沪蓉高速直达；入住新街口/夫子庙/中山陵附近（500-1500 元/晚 商务/文化氛围）</p>
 <p>🏛️上午 10:00：<b>中山陵</b>（免费 8:30-17:00 需"中山陵预约"公众号实名预约，周一闭馆，紫金山南麓）— 392 级台阶/8 个平台/蓝白色"自由钟"形制；博爱坊（金字坊额孙中山手书"博爱"）→ 陵门（"天下为公"横额）→ 碑亭（"中国国民党葬总理孙先生于此"碑）→ 祭堂（孙中山大理石坐像 5m/《建国大纲》全文）；从博爱坊到祭堂 392 级台阶 480m 海拔升 70m</p>
 <p>🌳上午 11:30：步行至<b>明孝陵</b>（70元/人 6:30-18:30 5A 世界文化遗产 2003 入选"明清皇家陵寝"项目，朱元璋+马皇后合葬陵，1381 年建成）— 文武方门 → 神道"石象生"（大象/麒麟/獬豸/石马/文臣/武将共 12 对，蜿蜒 2km 形似"北斗七星"）→ 享殿（"治隆唐宋"康熙手书）→ 宝顶（独龙阜玩珠峰下）；可与中山陵联票 100 元</p>
 <p>🍜中午 12:30：<b>南京大牌档</b>（中山陵店/夫子庙店，人均 80-120 元）品尝金陵菜 — 盐水鸭（招牌/民国御厨秘方）/ 美龄粥（豆浆+米+山药，宋美龄挚爱）/ 蟹黄汤包（28 元/笼）/ 民国美龄排骨 / 王导鸭血粉丝 / 桂花糖芋苗</p>
 <p>🏛️下午 14:00：<b>总统府</b>（35元/人 8:30-18:00 5A，600+ 年历史 1381 朱元璋赐归德侯府/明/清/太平天国/中华民国/共和国五朝遗迹）— 大堂（"天下为公"孙中山手书）→ 煦园（太平天国天王府花园）→ 西花园（清两江总督署花园）→ 行政院旧址（蒋介石办公室）→ 总统府门楼（1948 蒋介石当选就职地）</p>
 <p>📜下午 15:30：步行至<b>南京大屠杀遇难同胞纪念馆</b>（免费 8:30-17:30 周一闭馆，需"南京发布"公众号预约；1985 建成，江东门万人坑遗址）— 集会广场（"遇难者 300000"黑色花岗岩）→ 史料陈列厅（1122 件文物/近万张照片）→ 万人坑遗址（1984 发掘）；庄严肃穆，预约难度大</p>
 <p>🌃晚上 17:30：打车至<b>夫子庙-秦淮河</b>（免费 全天，5A，"六朝金粉地，十里秦淮河"，明/清/民国最繁华商业区）— 江南贡院（中国古代最大科举考场 1380/206 间号舍 / 1380 余名进士）/ 大成殿（孔庙主殿）/ 文德桥（"君子桥"）/ 乌衣巷（"旧时王谢堂前燕"王导谢安故居 35 元）；推荐<b>夜游秦淮</b>（80 元/人 18:30-21:30，画舫 50min 看两岸灯火+古戏台演出）</p>
 <p>🍜晚上 19:00：<b>老门东</b>（免费 全天，明清古城南保留区，"老南京味道")— 蒋有记牛肉锅贴（15 元/4 个 招牌）/ 蓝老大糖芋苗（12 元/碗 桂花糖芋苗）/ 小郑酥烧饼（8 元/个）/ 瞻园面馆（皮肚面 18 元）；推荐<b>秦淮八绝</b>套餐（128 元 8 道小食）</p>
 <p>🍡晚上 20:30：转赴<b>玄武湖</b>（免费 6:00-22:00，江南三大名湖之一，"金陵明珠"，周长 15km 五洲相连）— 环洲（郭璞墩/玄武厅）/ 樱洲（樱花季 3-4 月盛景）/ 菱洲（动物园 25 元）/ 梁洲（盆景园/览胜楼）/ 翠洲（先锋书店五台山店 26 元）；可租<b>画舫</b>（40 元/小时）夜游</p>
 <p>🛕晚上 21:30：打车至<b>鸡鸣寺</b>（10元/人 7:30-17:00，"南朝四百八十寺"之首，南朝梁武帝所建，"南朝第一寺"）— 山门（"南朝第一寺"额）/ 大雄宝殿（三面佛）/ 药师佛塔（1990 重建 7 层 44m）/ 观音殿；可俯瞰玄武湖；农历四月十五浴佛节盛大</p>
 <p>🌃晚上 22:00：返酒店，推荐<b>南京香格里拉</b>（800-1500 元/晚 五星 鼓楼/玄武湖景）/ <b>南京金陵饭店</b>（500-1000 元/晚 五星 老牌 新街口）/ <b>桔子水晶酒店</b>（300-500 元/晚 精品 夫子庙）</p>
 <p>🍽️晚餐推荐：南京大牌档（80-120 元/人 金陵菜正店）/ 马祥兴菜馆（110 年 4A 绿柳居）/ 永和园（黄桥烧饼/蟹黄汤包）/ 韩复兴（80 年盐水鸭 38 元/斤）</p>
 <p>🏨住宿推荐：新街口（400-800 元/晚 商务/购物便利）/ 夫子庙（500-1000 元/晚 秦淮夜景）/ 中山陵/紫金山（600-1200 元/晚 度假/文化氛围）/ 玄武湖（500-1000 元/晚 湖景）</p>
 <p>📅明日预告：南京→ 合肥（300km G42/G4001 高速 3h，安徽省会/三国故地/包公故里）/ 扬州（100km G40 沪陕高速 1.5h，世界美食之都/瘦西湖/个园）/ 镇江（70km G42 沪蓉高速 1h，西津渡/金山寺/茅山）</p>
 </div>
 <div class="photos">
 <div class="photo-placeholder">🏛️</div>
 <div class="photo-placeholder">🌃</div>
 <div class="photo-placeholder">🌳</div>
 </div>
 <div class="tips">
 <div class="tip">
 <span class="tip-icon">🏛️</span>
 <span class="tip-text">南京六朝古都十朝都会！与北京/西安/洛阳并称"中国四大古都"；六朝：东吴/东晋/宋/齐/梁/陈（229-589 AD）；十朝：东吴/东晋/宋/齐/梁/陈/南唐/明/太平天国/中华民国</span>
 </div>
 <div class="tip">
 <span class="tip-icon">⛰️</span>
 <span class="tip-text">中山陵免费（需"中山陵预约"公众号实名预约）！孙中山先生陵寝 1929 建成；392 级台阶/8 个平台；蓝白色"自由钟"形制；紫金山南麓；与明孝陵联票 100 元；周一闭馆</span>
 </div>
 <div class="tip">
 <span class="tip-icon">🌳</span>
 <span class="tip-text">明孝陵 5A 70 元！世界文化遗产 2003 入选"明清皇家陵寝"项目；朱元璋+马皇后合葬陵 1381 年建成；神道"石象生"12 对蜿蜒 2km 形似"北斗七星"；"治隆唐宋"康熙手书</span>
 </div>
 <div class="tip">
 <span class="tip-icon">🌃</span>
 <span class="tip-text">秦淮河夫子庙 5A 免费！"六朝金粉地，十里秦淮河"；江南贡院（中国古代最大科举考场 1380/206 间号舍/1380 余名进士）；夜游画舫 80 元/人 18:30-21:30 看两岸灯火+古戏台演出</span>
 </div>
 <div class="tip">
 <span class="tip-icon">🍜</span>
 <span class="tip-text">金陵菜四大名菜：盐水鸭（韩复兴 80 年 38 元/斤）/ 鸭血粉丝汤（回味 18 元）/ 蟹黄汤包（28 元/笼）/ 桂花糖芋苗；南京大牌档人均 80-120 元 招牌；老门东"秦淮八绝"套餐 128 元 8 道小食</span>
 </div>
 </div>
 </div>

'''

content = content[:footer_pos] + day118_entry + content[footer_pos:]
print('Added Day118 entry')

# Update footer tips: 苏州·世界遗产园林 → 南京·六朝古都·中山陵·秦淮河
old_footer_correct = '''                <p style="font-size: 14px; margin-bottom: 10px;">馃摪 2026骞?鏈堣嫃鍗椔疯嫃宸灺蜂笘鐣屾枃鍖栭仐浜у洯鏋楄创澹紙鎷欐斂鍥风暀鍥疯嫃鍗毬峰瘨灞卞锛?/p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>馃尦 鑻忓窞鍙ゅ吀鍥灄 1997 UNESCO 绗?1 椤硅嫃宸炰笘鐣屾枃鍖栭仐浜э紒鎷欐斂鍥?鐣欏洯/缃戝笀鍥?鐜灞卞簞锛涗笌鍖椾含棰愬拲鍥?鎵垮痉閬挎殤灞卞簞骞剁О"涓浗鍥涘ぇ鍚嶅洯"</li>
                    <li>馃彌锔?鑻忓窞鍗氱墿棣嗗厤璐癸紙闇€"鑻忓窞鍗氱墿棣?鍏紬鍙烽绾︼級锛佽礉鑱块摥灏佸北涔嬩綔 2006 寮€鏀撅紱"鐜颁唬+浼犵粺"绮夊榛涚摝+鍑犱綍绾挎潯+姘存睜鍊掑奖锛涘懆涓€闂</li>
                    <li>馃寜 骞虫睙璺?800+ 骞存按宸锋部娌?1600m 鍏嶈垂锛?鑻忓窞鍙ゅ煄缂╁奖"锛涚堪灏旇尪棣嗗搧纰ц灪鏄ワ紙鏄庡墠 1800 鍏?鏂わ級鍚瘎寮癸紙30 鍏?浜猴級浣撻獙鏈€鑻忓窞</li>
                    <li>馃洉 瀵掑北瀵?20 鍏?浜猴紒寮犵户銆婃灚妗ュ娉娿€?濮戣嫃鍩庡瀵掑北瀵?鍗冨彜浼犺锛?512 鏄庢寰蜂竷骞撮噸淇紱鏂板勾 12/31 108 涓嬮挓澹帮紙680 鍏冩挒閽熺エ锛?/li>
                    <li>馃崪 鑻忓府鑿滃叓澶у悕鑿滐細鏉鹃紶妗傞奔/鍝嶆补槌濈硦/纰ц灪铏句粊/锜圭矇鐙瓙澶达紱鏉鹃工妤硷紙瑙傚墠琛?158 鍏冩嫑鐗岋級/ 鍚屽緱鍏达紙濂ョ伓闈?35 鍏冿級/ 榛勫ぉ婧愶紙鑻忓紡绯曠偣 80 骞达級</li>
                    <li>馃殫 涔岄晣鈫掕嫃宸?85km G50 娌笣楂橀€?1.5h锛涜嫃宸炲湴閾?1/2/4 鍙风嚎涓茶仈鍥灄/瑙傚墠/骞虫睙锛涘钩姹熻矾閰掑簵 400-1200 鍏?鏅?鑰佽嫃宸為鎯?/li>
                    <li>馃搮 鏄庢棩棰勫憡锛氳嫃宸炩啋 鍗椾含锛?20km G42 娌搲楂橀€?2.5h 鍏湞鍙ら兘/涓北闄?绉︽樊娌筹級/ 鍚岄噷锛?0km 姹熷崡鍏ぇ姘翠埂锛? 涓婃捣锛?00km 楂橀搧 0.5h锛?/li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">鏈€鍚庢洿鏂帮細2026骞?鏈?4鏃ワ紙鍛ㄦ棩锛?/p>'''

new_footer_correct = '''                <p style="font-size: 14px; margin-bottom: 10px;">馃搱 2026骞?鏈堝崡浜紙1)鍗椾含路鍏湞鍙ら兘路涓北闄┿啋鏄庝孝闄┿啋绱ф皯寰?绛?/p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>馃搱 鍗椾含鍏湞鍙ら兘鍗佸帆閮藉穽锛? 涓庡寳浜?/瑗垮畨/娲涙旦骞剁О"涓浗鍥涘ぇ鍙や唬"锛涘叚鏈?229-589 AD 涓滃北/涓滆胺/瀵?瀵?妲?闃充簮)锛涙槦?涓滃北/瀵?瀵?妲?闃充簮/瀵?鍗?瀵?鏄?澶?澶╁浗/涓崕姘戝叕)</li>
                    <li>馃敟 涓北闄╁厤璐癸紙闇€"涓北闄╁爼绾?鍏紬鍙烽」瀹氱害锛? 涓冮偊涔犻偊 1929 寤虹珛锛?92 绾ц剼姊? 8 涓钩鍙凤紱钃濊壊"鑷敱閽"褰㈠埗锛涜憽閲戝北鍗楅《锛涗笌鏄庝孝闄╁叡閫?00 鍏? 鍛ㄤ竴闂查棴</li>
                    <li>馃惂 鏄庝孝闄? 5A 70 鍏? 涓栫晫鏂囧寲閬椾骇 2003 鍏ラ€変"鏄庢櫒宸呮棤闄?椤圭洰"锛涙垜宀?璋峰厖鍚庡悎鍧?1381 骞村缓鎴愶紱绁炴墍"鐭虫不鐢"12 瀵? 鑾冪紶 2km 褰撲技"鍖楁湞涓冨北"锛?"娌诲嘲鍗庡害"搴曚簹鎵嬪啓</li>
                    <li>馃敟 绱ф皯寰嶄笜濮嶅帟 5A 鍏嶈垂锛?"鍏湞閲戝窐鍦帮紝鍗佷腑绱ф皯寰? 锛涙瀬鍗板购闄?涓浗鍙や唬鏈€澶ц绉戝?鑰冨満 1380/206 闂翠彿鑸? 1380 鍚嶅嚒澹? 锛夛紱澶滆吚婕?80 鍏?浜? 18:30-21:30 鐪嬩袱宀虹伅鐏?鍙や唬鍙栨槑</li>
                    <li>馃崪 閲戞灄鑿滃洓澶у悕鑿滐細鐩愭按楦紙闊ㄥソ搴? 80 骞? 38 鍏?鏂わ級/ 楦按绮剧兢娌癸紙鍥炲懗 18 鍏?/ 铔庨粍娓╁寘锛? 28 鍏?绛咾 榛勮姖钀濆崱铔嬭帀锛涙嘲闂ㄥぇ鐗岀エ锛? 80-120 鍏?浜? 鎵撴壃锛涙棗闃ㄥ崡"绱ф皯宀冨叓缁?濊凯濂? 128 鍏? 8 閬撻椋?/li>
                    <li>馃殫 鑻忓窞鈫掗害姒? 220km G42 娌搲楂橀€? 2.5h锛涙嘲闂ㄥ崡绔欏彈椹? "涓?鏍间笂"绛? G 瀛楀ご 145 鍏?浜?/ 鑷?椹? G42 鐩村僵閫? 鍛ㄤ竴闂查棴)锛涙柊琛楀彛/澶栧コ搴? 400-1500 鍏?鏅? 鍟?棰?/li>
                    <li>馃搮 鏄庢棩棰勫憡锛氶害姒廡啋 鍚堣胺锛?00km G42/G4001 楂橀€? 3h 瀹夊晢搴? 涓夊浗鏀剁?瀹? 鍖呭叕鏀剁?/ 鎽嗙锛?00km G40 娌虫睙楂橀€? 1.5h 涓栫晫缇庨涔嬮兘/鐦肩唺娓?涓や笜)/ 闀嶆江锛?0km G42 娌搲楂橀€? 1h 瑗胯耽娓? 閲戝北瀵? 鑽℃灄)</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">鏈€鍚庢洿鏂帮細2026骞?鏈?5鏃ワ紙鍛ㄤ竴锛?/p>'''

if old_footer_correct in content:
    content = content.replace(old_footer_correct, new_footer_correct)
    print('Footer tips fully updated (correct Chinese match)')
else:
    # Fallback: just update last-update line
    print('WARN: exact footer match failed, trying fallback (regex)')
    content = re.sub(
        r'最后更新：2026年6月14日（周日）',
        '最后更新：2026年6月15日（周一）',
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

# Sanity check: Day 118 should exist
if 'day-number">118</span>' in verify:
    print('Day 118 card present: YES')
else:
    print('Day 118 card present: NO -- ERROR!')

# Verify Day 117 still there
day117_count = verify.count('day-number">117</span>')
day118_count = verify.count('day-number">118</span>')
print('Day 117 occurrences:', day117_count)
print('Day 118 occurrences:', day118_count)

# Check file size
print('New file size:', os.path.getsize(HTML_PATH))
