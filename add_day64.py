# -*- coding: utf-8 -*-
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update day count 63 -> 64
content = re.sub(r'id="dayCount"[^>]*>(\d+)<',
    lambda m: 'id="dayCount">' + str(int(m.group(1)) + 1) + '<',
    content)

# 2. Update km (厦门市区游约80km)
content = re.sub(r'id="kmCount"[^>]*>(\d+)<',
    lambda m: 'id="kmCount">' + str(int(m.group(1)) + 80) + '<',
    content)

# 3. Update location
content = re.sub(r'id="currentLocation"[^>]*>([^<]+)<',
    'id="currentLocation">厦门 · 思明区<',
    content)

print('Updated stats: Day 64, km +80, location -> 厦门 · 思明区')

# 4. Add Day 64 entry
day64_entry = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第64天</span>
                    <span class="day-date">2026-04-21 · 三月廿四</span>
                </div>
                <div class="day-title">🏯 厦门深度游 · 南普陀寺与沙坡尾</div>
                <div class="day-content">
                    <p>在"海上花园"厦门的第二天深度探索！</p>
                    <p>🛕 上午：南普陀寺——千年古刹，闽南佛教胜地</p>
                    <p>南普陀寺：始建于唐朝末年，居于五老峰下，紧邻厦门大学</p>
                    <p>🙏 寺庙免费参观，但需提前预约；登五老峰俯瞰厦门全景，约40分钟登顶</p>
                    <p>🏛️ 厦门大学：中国最美大学之一，校园内嘉庚建筑风格独特</p>
                    <p>🎓 参观方式：通过"厦门大学访客预约系统"预约，周末开放参观</p>
                    <p>🛍️ 中午：曾厝垵——"中国最文艺村落"，各种特色小吃汇聚</p>
                    <p>🍜 必吃：阿杰五香卷（8元）、黄则和花生汤、沙茶里脊肉串、烧仙草</p>
                    <p>曾厝垵由原来渔村改造而成，汇集了闽南、台湾、东南亚等多元美食文化</p>
                    <p>🕍 下午：沙坡尾——老厦门发源地，艺术西区焕发新生</p>
                    <p>🚢 沙坡尾曾是厦门最古老的港口，避风坞渔船穿梭，闽南渔村风情浓郁</p>
                    <p>🎨 艺术西区：旧工厂改造的文艺区，汇聚独立设计店、咖啡馆、画廊</p>
                    <p>☕ 推荐：大学路"Barista Honor"咖啡，老剧场咖啡馆</p>
                    <p>🌆 傍晚：演武大桥观景台，欣赏厦门海岸线日落</p>
                    <p>🌉 演武大桥：世界上离海平面最近的桥，观景台视野绝佳</p>
                    <p>🦐 晚餐：中山路步行街，厦门老城区核心商业街</p>
                    <p>中山路保留了南洋骑楼建筑风貌，美食与购物两相宜</p>
                    <p>📊 今日行程：南普陀寺 + 厦门大学 + 曾厝垵 + 沙坡尾 + 中山路，全程约60公里</p>
                    <p>🚗 交通提示：厦门地铁1号线可达镇海路站（南普陀）、曾厝垵站；共享电动车出行方便</p>
                    <p>📅 明日预告：厦门最后一站——集美学村、陈嘉庚纪念馆，告别厦门前往下一站</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🛕</div>
                    <div class="photo-placeholder">🎓</div>
                    <div class="photo-placeholder">🌆</div>
                </div>
            </div>
'''

footer_marker = '<div class="footer">'
content = content.replace(footer_marker, day64_entry + '\n' + footer_marker)
print('Added Day 64 entry for 厦门深度游')

# 5. Update footer timestamp
old_footer = re.search(r'<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：[^<]+</p>', content)
if old_footer:
    content = content.replace(old_footer.group(0), '<p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月21日</p>')
    print('Updated footer timestamp to 2026年4月21日')

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\n=== Update Complete ===')
print('Day: 64')
print('Location: 厦门 · 思明区')
print('Date: 2026-04-21')
print('KM added: 80 (total: 7023)')