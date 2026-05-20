# -*- coding: utf-8 -*-
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Read file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update day count from 54 to 55
content = re.sub(r'id="dayCount"[^>]*>(\d+)<', 
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<' if int(m.group(1)) == 54 else m.group(0),
    content)

# 2. Update location count (宏村西递塔川卢村 = still 黟县 area, stays 31)
# No change needed for location count

# 3. Update km (add ~40km 宏村到西递到塔川)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 40) + '<' if int(m.group(1)) == 5810 else m.group(0),
    content)

# 4. Update current location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">西递 · 敬爱堂<',
    content)

print('Updated stats: Day 54 -> 55, km +40, location -> 西递')

# 5. Add Day 55 entry before the closing </div> of timeline
day55_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第55天</span>
                    <span class="day-date">2026-04-12 · 三月十五</span>
                </div>
                <div class="day-title">🏯 西递古村 · 桃花源里人家</div>
                <div class="day-content">
                    <p>西递——被联合国教科文组织列入世界文化遗产的古村落，被誉为"桃花源里人家"！</p>
                    <p>🏯 西递古村：始建于北宋年间（公元1047年），现有明清古建筑224幢保存完好</p>
                    <p>上午首先来到敬爱堂，这是西递最大的一座宗祠，气势恢宏，木雕精美绝伦！</p>
                    <p>🏛️ 敬爱堂：西递胡氏宗祠，面积达1800平方米，展现徽州宗族文化的辉煌</p>
                    <p>接着游览了西递的标志性建筑——青石牌坊群，其中"胶州刺史坊"最为著名！</p>
                    <p>🪨 西递牌坊：明代石坊的代表作，雕刻精细，记录着胡氏家族的荣耀</p>
                    <p>中午在西递村中的农家乐享用了地道的徽州午餐，笋干烧肉和徽州米酒味道极佳！</p>
                    <p>🍜 徽州美食：笋干烧肉32元/份，徽州米酒8元/碗，村中农家乐价格实惠</p>
                    <p>下午驱车前往距西递仅8公里的塔川村，这里以秋色闻名，但春天的竹林和油菜花田同样美不胜收！</p>
                    <p>🎋 塔川：被誉为"中国三大秋色之一"，春天竹海翠绿，油菜花点缀其间</p>
                    <p>随后顺道探访了卢村，这里有徽州最精美的木雕楼——志诚堂！</p>
                    <p>🏠 卢村木雕楼：清代徽派木雕的巅峰之作，"天下第一木雕楼"实至名归</p>
                    <p>📊 今日行程：西递深度游 + 塔川 + 卢村，西递/牌坊群/塔川竹林/卢村木雕楼，车程约25公里</p>
                    <p>📍 明日计划：离开黟县前往江西婺源，徽州到婺源约120公里，3小时车程</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">🪨</div>
                    <div class="photo-placeholder">🏠</div>
                </div>
            </div>
'''

# Insert Day 55 before footer
footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day55_entry + '\n' + footer_marker)
print('Added Day 55 entry for 西递古村')

# 6. Update travel tips with latest search info
old_footer = '''<div class="footer">
            <p>🚗 环游中国 · 房车日记</p>
            <p>记录每一天的所见所闻</p>
            <div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年4月中旬皖南旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏘️ 宏村西递：4月中旬桃花、紫藤盛开，清晨6-7点入园可拍晨雾倒影，游人最少</li>
                    <li>🏯 西递古村：距宏村仅20公里，世界文化遗产，"桃花源里人家"实至名归</li>
                    <li>🌸 扬州烟花节：2026年4月18日开幕，瘦西湖琼花盛放，需提前1周订房</li>
                    <li>🏔️ 黄山：4月云海概率仍较高，光明顶日出是必打卡项目，备好防风外套</li>
                    <li>🍜 徽州美食：宏村农家乐毛豆腐15元/份、臭鳜鱼68元，村中用餐实惠</li>
                    <li>🚗 交通：黟县各古村间建议打车或拼车，宏村到西递约30元/车</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月11日</p>
            </div>
        </div>'''

new_footer = '''<div class="footer">
            <p>🚗 环游中国 · 房车日记</p>
            <p>记录每一天的所见所闻</p>
            <div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年4月中旬皖南旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏯 西递古村：4月中旬游客较少，清晨入村可拍到"桃花源里人家"的宁静之美</li>
                    <li>🏠 卢村木雕楼：距塔川仅3公里，"天下第一木雕楼"需购票进入，门票40元</li>
                    <li>🎋 塔川：春天的塔川竹海翠绿、油菜花点缀，适合徒步摄影，建议游玩2-3小时</li>
                    <li>🌸 扬州烟花节：2026年4月18日开幕，瘦西湖琼花盛放，需提前1周订房</li>
                    <li>🚗 交通：黟县各古村间打车或拼车便捷，宏村-西递-塔川-卢村一圈约60公里</li>
                    <li>🍜 徽州美食：黟县农家乐笋干烧肉32元/份，宏村毛豆腐15元/份，建议村中用餐</li>
                    <li>📅 下站预告：婺源（江湾/篁岭/思溪延村），距黟县约120公里，车程3小时</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月12日</p>
            </div>
        </div>'''

if old_footer in content:
    content = content.replace(old_footer, new_footer)
    print('Updated travel tips')
else:
    print('WARNING: Could not find old footer to replace')

# Write back
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 55')
print('Location: 西递 · 敬爱堂')
print('Date: 2026-04-12')
