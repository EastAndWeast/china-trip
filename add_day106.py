# -*- coding: utf-8 -*-
"""环游中国 - Day 106/107/108 批量更新脚本
补更 6/3、6/4、6/5 三天：
  Day 106 (6/3 周三): 宏村 → 黄山风景区（迎客松、光明顶、莲花峰）
  Day 107 (6/4 周四): 黄山 → 千岛湖（新安江山水画廊）
  Day 108 (6/5 周五): 千岛湖 → 杭州（西湖、灵隐寺、京杭大运河）
"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Stats: dayCount 106→109 (+3), kmCount 14495→14965 (+470), locationCount 91→97 (+6)
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 3) + m.group(3), content)
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 470) + m.group(3), content)
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 6) + m.group(3), content)
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>杭州 · 西湖断桥边\g<3>', content)

footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

day106_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">106</span>
                    <span class="day-date">2026-06-03 · 五月初七 · 周三</span>
                </div>
                <div class="day-title">🏔️ 黄山 · 五岳归来不看山 · 迎客松</div>
                <div class="day-content">
                    <p>🚗 今日行程：屯溪 → 黄山南大门 → 云谷寺索道（约70km，1.5小时）</p>
                    <p>🛣️ 路线：屯溪老街走G205国道向北到汤口，转黄山风景区南大门</p>
                    <p>🎫 早7点前到售票处：黄山门票旺季190元（3-11月），云谷寺索道80元，太平索道90元，玉屏索道90元</p>
                    <p>⛰️ 上午：云谷寺索道上山 → 始信峰（黑虎松、连理松、龙爪松）→ 北海景区（梦笔生花、清凉台）</p>
                    <p>🌄 中午：西海大峡谷一环/二环（步行约2小时，6月云海高发季）</p>
                    <p>🌅 下午：光明顶（黄山第二高峰1860米，可观云海日出日落）→ 飞来石 → 排云亭</p>
                    <p>🌲 傍晚：经鳌鱼峰、百步云梯到迎客松（玉屏楼景区，黄山标志）</p>
                    <p>🌃 晚：玉屏楼宾馆或山顶住宿（看日出必备，标间800-1500元，提前一周预订）</p>
                    <p>🍜 晚餐：山顶餐厅（贵但省体力）或自带路餐（推荐：自热饭、能量棒、热水）</p>
                    <p>📅 明日预告：黄山日出 → 下山 → 千岛湖（约280km，4小时）</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏔️</div>
                    <div class="photo-placeholder">🌄</div>
                    <div class="photo-placeholder">🌲</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">⛰️</span>
                        <span class="tip-text">黄山"五岳归来不看山，黄山归来不看岳"；6月梅雨季，云海日出几率70%+</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🎫</span>
                        <span class="tip-text">旺季门票190元（3/1-11/30），淡季95元（12/1-2月底）；云谷寺上行最常用</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">👟</span>
                        <span class="tip-text">登山必备：防滑徒步鞋、雨衣、登山杖、头灯；山顶夜间5-10℃，带厚外套</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🏨</span>
                        <span class="tip-text">山顶住宿紧张！6月周末提前2周订；玉屏楼位置最好（迎客松旁）</span>
                    </div>
                </div>
            </div>

'''

day107_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">107</span>
                    <span class="day-date">2026-06-04 · 五月初八 · 周四</span>
                </div>
                <div class="day-title">🌊 千岛湖 · 天下第一秀水 · 1078个岛屿</div>
                <div class="day-content">
                    <p>🌅 凌晨：光明顶/清凉台看日出（5:10左右，看天气，备手电）</p>
                    <p>🚗 上午：玉屏索道下山 → 汤口 → 千岛湖镇（约280km，4小时）</p>
                    <p>🛣️ 路线：汤口走G56杭瑞高速向南到屯溪，转G4012溧黄高速到千岛湖</p>
                    <p>🚢 下午：千岛湖中心湖区游船（门票+船票150元，梅峰岛、渔乐岛、龙山岛、月光岛）</p>
                    <p>🏝️ 重点：梅峰观景台（千岛湖标志性俯瞰点，"千岛"实至名归）→ 渔乐岛观鱼 → 月光岛爱情主题</p>
                    <p>🚴 傍晚：千岛湖绿道骑行（环湖140公里，部分段已建成，免费）</p>
                    <p>🍜 晚餐：千岛湖鱼头宴（千岛湖有机鱼头，68元/斤起，必尝）</p>
                    <p>🏨 住宿推荐：千岛湖镇中心湖区（便于次日游湖），或进贤湾高端酒店群</p>
                    <p>📅 明日预告：千岛湖 → 杭州西湖（约180km，2.5小时）</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌅</div>
                    <div class="photo-placeholder">🚢</div>
                    <div class="photo-placeholder">🏝️</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🌅</span>
                        <span class="tip-text">黄山日出5:10左右，清凉台/光明顶/丹霞峰都OK；先查日出时间再定闹钟</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🚢</span>
                        <span class="tip-text">千岛湖游船分中心/东南/西南湖区，中心湖区最经典；门票+船票联票更划算</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🐟</span>
                        <span class="tip-text">千岛湖鱼头是地理标志产品，认准"淳"牌有机鱼；正宗店：鱼味馆、淳牌有机鱼</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🏨</span>
                        <span class="tip-text">6月非节假日，住宿充足；推荐湖景房，醒来就是湖景</span>
                    </div>
                </div>
            </div>

'''

day108_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">108</span>
                    <span class="day-date">2026-06-05 · 五月初九 · 周五</span>
                </div>
                <div class="day-title">🌸 杭州 · 西子湖畔 · 上有天堂下有苏杭</div>
                <div class="day-content">
                    <p>🚗 今日行程：千岛湖 → 杭州市区 → 西湖（约180km，2.5小时）</p>
                    <p>🛣️ 路线：千岛湖走G2504杭州绕城高速向北，经建德、桐庐、富阳到杭州</p>
                    <p>🌸 上午：西湖断桥/白堤（免费，6月曲院风荷荷花初绽）→ 孤山西泠印社 → 楼外楼午餐</p>
                    <p>⛵ 中午：西湖游船（三潭印月，55元，人民币1元纸币背面取景）</p>
                    <p>🌉 下午：苏堤春晓（苏东坡修，苏堤六桥）→ 花港观鱼（免费）→ 雷峰塔（40元，《白蛇传》发生地）</p>
                    <p>🛕 傍晚：灵隐寺/飞来峰（飞来峰45元+灵隐寺30元，灵隐寺始建东晋326年）</p>
                    <p>🌃 晚上：河坊街/南宋御街（仿古街区，吴山酥油饼、定胜糕、龙井茶）</p>
                    <p>🍜 晚餐：杭帮菜代表（西湖醋鱼、东坡肉、龙井虾仁、叫花鸡、宋嫂鱼羹）</p>
                    <p>🏨 住宿推荐：西湖周边/武林广场（地铁1号线直达）</p>
                    <p>📅 明日预告：杭州深度游——灵隐 · 龙井 · 西溪湿地 · 京杭大运河</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌸</div>
                    <div class="photo-placeholder">⛵</div>
                    <div class="photo-placeholder">🌉</div>
                </div>
                <div class="tips">
                    <div class="tip">
                        <span class="tip-icon">🌸</span>
                        <span class="tip-text">西湖免费！断桥残雪、平湖秋月、苏堤春晓、曲院风荷皆十景；环湖步行2-3小时</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">⛵</span>
                        <span class="tip-text">游船推荐：岳湖码头出发，含三潭印月；55元/人，约1小时</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🍜</span>
                        <span class="tip-text">楼外楼（孤山路30号）老字号，150年历史；外婆家/绿茶是平价杭帮菜</span>
                    </div>
                    <div class="tip">
                        <span class="tip-icon">🛕</span>
                        <span class="tip-text">灵隐寺香花券30元，飞来峰造像45元；早8点前去可避人潮</span>
                    </div>
                </div>
            </div>

'''

content = content[:footer_pos] + day106_entry + day107_entry + day108_entry + content[footer_pos:]
print('Added Day 106, 107, 108 entries')

# Update footer travel tips: replace 赣东北·皖南 tips with 杭州·西湖 tips
old_footer = '''<p style="font-size: 14px; margin-bottom: 10px;">📰 2026年6月赣东北·皖南旅游贴士</p>
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

new_footer = '''<p style="font-size: 14px; margin-bottom: 10px;">📰 2026年6月皖南·浙西旅游贴士</p>
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

if old_footer in content:
    content = content.replace(old_footer, new_footer)
    print('Footer tips updated')
else:
    content = content.replace('最后更新：2026年6月3日（周三）', '最后更新：2026年6月4日（周四）')
    print('Footer last-update replaced only')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print('HTML updated successfully')

# Verify
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
