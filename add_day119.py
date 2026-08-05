# -*- coding: utf-8 -*-
"""环游中国 - Day 119 更新脚本
添加 Day 119（南京→镇江 · 大江风貌·白蛇传·西津渡古街）
从南京出发，约 70km，1 小时到镇江
2026-08-05 恢复项目续写
"""
import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# --- 1. 更新统计数字 ---
# dayCount 119 -> 120
content = re.sub(
    r'(id="dayCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), content)
# kmCount +70 = 16185
content = re.sub(
    r'(id="kmCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 70) + m.group(3), content)
# locationCount +4 = 130
content = re.sub(
    r'(id="locationCount"[^>]*>)(\d+)(<)',
    lambda m: m.group(1) + str(int(m.group(2)) + 4) + m.group(3), content)
# currentLocation
content = re.sub(
    r'(id="currentLocation"[^>]*>)([^<]+)(<)',
    r'\g<1>镇江 · 西津渡 · 金山寺 · 大江风貌\g<3>', content)

# --- 2. 找到 footer 位置（插入 Day119 卡片在最后一个 day-card 之后、footer 之前）---
# 在 Day118 卡片结束后插入。用 </div>\n    </div>\n    <div class="footer"> 定位
footer_pos = content.find('<div class="footer">')
if footer_pos == -1:
    print('Footer not found!')
    sys.exit(1)

# 找 footer 之前最后一个 card 结尾 </div>，定位到紧跟卡片结束的位置
# 简单方案：直接插在 footer 前（Day118 已是最后一个卡片）
day119_entry = '''            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">119</span>
 <span class="day-date">2026-06-16 · 五月廿一 · 周二</span>
 </div>
 <div class="day-title">🏞️ 南京→镇江 · 大江风貌 · 西津渡古街 · 金山寺·白蛇传 · 中泠泉水</div>
 <div class="day-content">
 <p>🧳 今日行程：南京→镇江（约 70km，G42 沪蓉高速 1h；6/16 阵雨转多云 27/21℃ 东南风 3-4 级，梅雨季镇江"江山烟雨"别有一番意境）</p>
 <p>🚗 早 8:00：南京新街口出发，自驾 G42 沪蓉高速向西约 1 小时（或高铁南京南→镇江南 20min 34 元）抵达镇江；入住西津渡/大市口附近（300-800 元/晚）</p>
 <p>🏯 上午 9:30：<b>金山寺</b>（65元/人 8:00-17:00 5A，"江天禅寺"，中国佛教禅宗四大名刹之一，始建于东晋）— 白蛇传"水漫金山"故事发生地！山门（康熙御笔"江天禅寺"）/ 大雄宝殿 / 妙高台（苏轼在此赏月）/ 留云亭（纪念李白"金陵津渡小山楼"旧址）；金山高 44m，寺庙依山而建，殿宇栉比层层叠叠，"金山寺裹山"奇观</p>
 <p>🏮 上午 11:00：步行至<b>西津渡古街</b>（免费 全天，"千年古渡，唐宋元明清五朝渡口"，镇江"文脉"所在）— 昭关石塔（元代过街石塔，全国仅存）/ 英国领事馆旧址（西式建筑群）/ 云台阁（登高俯瞰长江渡口）/ 西津渡历史文化街区（青石板路+明清建筑，李白/孟浩然/苏轼/王安石曾在此渡江）；"京口瓜洲一水间，钟山只隔数重山"（王安石泊船处在此）</p>
 <p>🍜 中午 12:30：西津渡街区品尝<b>镇江锅盖面</b>（15-25 元/碗）— 中国十大面条之一！"面锅里面煮锅盖，先烫浇头再烫筷"独特做法；推荐：红星锅盖面（招牌）/ 大华面馆（长鱼面）/ 老镇江（肴肉面）；配<b>镇江香醋</b>（恒顺醋业，中国四大名醋之一）</p>
 <p>🏯 下午 14:00：<b>北固山</b>（免费 8:00-17:00，"天下第一江山"，辛弃疾"何处望神州，满眼风光北固楼"）— 北固楼（北固山峰顶，镇江最高点）/ 甘露寺（三国"甘露寺招亲"刘备孙尚香故事地）/ 多景楼（"天下江山第一楼"）/ 祭江亭；登楼远眺长江，江天一色尽收眼底</p>
 <p>🏞️ 下午 15:30：<b>焦山</b>（65元/人 8:00-17:00 5A，长江中唯一四面环水的岛屿，须乘渡轮）— 定慧寺（江南第一大古刹）/ 焦山碑林（全国重点文保，大书法家瘗鹤铭"/个/大字之祖"）/ 摩崖石刻（米芾/乾隆题刻）；长江"浮玉"孤岛，山水相映</p>
 <p>🏔️ 傍晚 17:30：若时间充裕可往<b>茅山</b>（90元/人 8:00-17:30，道教上清派发源地，"第一福地，第八洞天"，5A）— 老子神像（高达 99 米全球最大道祖像）/ 九霄万福宫 / 元符万宁宫；离市区约 40km，可次日再往</p>
 <p>🌃 晚上 19:00：返回<b>大市口-西津渡夜景</b>，逛古街感受"京口夜色"；推荐<b>镇江三怪</b>：香醋摆不坏（恒顺香醋）、肴肉不当菜（水晶肴肉）、面锅里面煮锅盖（锅盖面）</p>
 <p>🥢 晚餐推荐：西津渡老街（锅盖面/肴肉/河豚 镇江扬中河豚 3-5 月当季）/ 老赵家面馆（镇江老字号）/ 宴春酒楼（镇江三怪套餐 88 元）；长江三鲜（刀鱼/鲥鱼/河豚）季节性强</p>
 <p>🏨 住宿推荐：西津渡景区内民宿（400-800 元/晚 古街氛围）/ 大市口商圈（300-600 元/晚 便利）/ 镇江富力万达嘉华（500-900 元/晚 五星）/ 金山湖畔酒店（400-700 元/晚 湖景）</p>
 <p>🗓️ 明日预告：镇江→ 扬州（35km 润扬大桥 40min，世界美食之都/瘦西湖/个园/东关街）/ 常州（60km G42 高速 1h，中华恐龙园/天宁寺）/ 无锡（90km G42 高速 1.5h，太湖鼋头渚/灵山大佛）</p>
 </div>
 <div class="photos">
 <div class="photo-placeholder">🏯</div>
 <div class="photo-placeholder">🏮</div>
 <div class="photo-placeholder">⛰️</div>
 </div>
 <div class="tips">
 <div class="tip">
 <span class="tip-icon">🏯</span>
 <span class="tip-text">镇江"三山一渡"名扬天下：金山（白蛇传"水漫金山"发源地，金山寺裹山奇观）、北固山（"天下第一江山"辛弃疾词）、焦山（长江唯一四面环水岛，碑林闻名）+ 西津渡千年古渡！镇江是"江河交汇处"，长江+京杭大运河在此交汇</span>
 </div>
 <div class="tip">
 <span class="tip-icon">🏮</span>
 <span class="tip-text">西津渡免费！"千年古渡"唐宋元明清五朝渡口，王安石"京口瓜洲一水间"泊船处；全国唯一元代过街石塔"昭关石塔"在此；英国领事馆旧址+青石板古街，夜景尤美</span>
 </div>
 <div class="tip">
 <span class="tip-icon">🍜</span>
 <span class="tip-text">镇江"三怪"：香醋摆不坏（恒顺香醋中国四大名醋）、肴肉不当菜（水晶肴肉）、面锅里面煮锅盖（锅盖面中国十大面条）！西津渡红星锅盖面 15-25 元必尝</span>
 </div>
 <div class="tip">
 <span class="tip-icon">🏞️</span>
 <span class="tip-text">金山寺 65 元 5A！白蛇传说发生地，东晋始建禅宗四大名刹之一；康熙御笔"江天禅寺"；妙高台苏轼赏月；"金山寺裹山"层层叠叠依山而建，中国佛教名山典范</span>
 </div>
 <div class="tip">
 <span class="tip-icon">⛰️</span>
 <span class="tip-text">茅山 90 元 5A！道教上清派发源地"第一福地第八洞天"；99 米全球最大老子神像；焦山碑林藏书法“大字之祖”《瘗鹤铭》；北固山免费看长江天下第一江山</span>
 </div>
 </div>
 </div>

'''

content = content[:footer_pos] + day119_entry + content[footer_pos:]

# --- 3. 更新 footer 行程提示 ---
# 更新 footer 里的"今日/最新"提示，将南京相关改为镇江（用正则替换部分地址关键词）
# footer 里的相关条目通常以 <li> 形式存在，这里做关键词增强替换
old_tip = '南京六朝古都十朝都会'
if old_tip in content:
    content = content.replace(old_tip, '镇江"三山一渡"，江水浩荡，东晋建寺两千年的江南名城')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('Added Day 119 entry (南京→镇江)')
print('dayCount -> 120, kmCount -> 16185, locationCount -> 130')
