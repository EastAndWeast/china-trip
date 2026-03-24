# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 32 content for March 20, 2026
day_32 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第32天</span>
                    <span class="day-date">2026-03-20 · 三月初二</span>
                </div>
                <div class="day-title">🏯 西递古村 · 桃花源里人家</div>
                <div class="day-content">
                    <p>从宏村出发，仅20公里便来到了另一个世界文化遗产——西递古村！</p>
                    <p>🏯 西递古村：世界文化遗产，始建于北宋年间，被誉为"桃花源里人家"</p>
                    <p>清晨8点抵达西递，趁着游客还未大批涌入，先去拍了拍村口的标志性景观。</p>
                    <p>📸 西递牌楼：西递的标志性地标，青石雕砌，气势恢宏</p>
                    <p>西递古村由三条溪水穿过，整个村落布局如一艘大船，"枕山、环水、面屏"。</p>
                    <p>🚣 西递水系：穿村而过的溪水清澈见底，倒映着白墙黛瓦，如诗如画</p>
                    <p>上午游览了村中的核心景区，西递保存有明清古民居224幢，其中124幢为全国重点文物保护单位。</p>
                    <p>🏠 明清古民居：徽派建筑的精华，木雕、砖雕、石雕精美绝伦</p>
                    <p>村中青石板路蜿蜒曲折，两侧是保存完好的古建筑，漫步其中仿佛穿越回了古代。</p>
                    <p>🛤️ 青石板路：西递的古道，漫步其中感受千年古村的宁静与厚重</p>
                    <p>中午在村中农家乐享用了地道的徽州美食，价格实惠，味道地道！</p>
                    <p>🍜 徽州农家菜：笋干烧肉、清炒时蔬、徽州米酒，品尝地道的乡村味道</p>
                    <p>📅 特别提示：西递春会正在举办中（3月22日-4月29日），各种民俗活动精彩纷呈！</p>
                    <p>🏮 春会活动：传统民俗表演、非遗文化展示、花卉展览等</p>
                    <p>傍晚入住西递村中民宿，期待明天继续探索这座"桃花源里人家"！</p>
                    <p>📊 今日行程：西递深度游，步行约10公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏯</div>
                    <div class="photo-placeholder">🚣</div>
                    <div class="photo-placeholder">🏮</div>
                </div>
            </div>
'''

# Find Day 31 position and insert Day 32 after it
pattern = r'(<span class="day-number">第31天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    # Insert Day 32 after Day 31
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_32 + content[insert_pos:]
    
    # Update stats
    # Update day count 31 -> 32
    new_content = re.sub(
        r'<div class="stat-value" id="dayCount">(\d+)</div>', 
        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>', 
        new_content
    )
    
    # Update km count +12km
    new_content = re.sub(
        r'<div class="stat-value" id="kmCount">(\d+)</div>', 
        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 12}</div>', 
        new_content
    )
    
    # Update location count 20 -> 21
    new_content = re.sub(
        r'<div class="stat-value" id="locationCount">(\d+)</div>', 
        lambda m: f'<div class="stat-value" id="locationCount">{int(m.group(1)) + 1}</div>', 
        new_content
    )
    
    # Update current location
    new_content = re.sub(
        r'<span>当前所在：<strong id="currentLocation">[^<]+</strong></span>',
        '<span>当前所在：<strong id="currentLocation">黄山 · 西递古村</strong></span>',
        new_content
    )
    
    # Update travel tips to March 20, 2026
    tips_content = '''<div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年3月安徽旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏯 西递：世界文化遗产，被誉为"桃花源里人家"，始建于北宋年间</li>
                    <li>🎫 门票：西递门票104元/人，与宏村联票更优惠</li>
                    <li>📅 特别活动：西递春会（3月22日-4月29日）正在进行中！</li>
                    <li>🏮 春会内容：传统民俗表演、非遗文化展示、花卉展览</li>
                    <li>📸 最佳机位：西递牌楼、溪边观景台、古村制高点</li>
                    <li>🚶 建议游览时间：3-4小时，建议清晨或傍晚拍照</li>
                    <li>🏠 住宿：村中民宿众多，200-400元/晚可住到不错的客栈</li>
                    <li>🍜 美食：农家乐人均30-50元，笋干烧肉、毛豆腐、臭鳜鱼</li>
                    <li>🚍 交通：宏村到西递旅游公交2元，约30分钟</li>
                    <li>🏘️ 联游建议：宏村+西递可安排2天深度游，各需4-5小时</li>
                    <li>🚄 高铁：杭州2小时直达黟县东站，出站有公交/打车</li>
                    <li>🌸 春季景色：3-4月油菜花盛开，是最美游览季节</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年3月20日</p>
            </div>'''
    
    # Replace old tips
    old_tips_pattern = r'<div style="margin-top: 20px; padding: 15px; background: rgba\(255,255,255,0\.1\); border-radius: 10px; text-align: left;">.*?</div>\s*</div>\s*</div>\s*</div>\s*</body>'
    new_content = re.sub(old_tips_pattern, tips_content + '\n        </div>\n    </div>\n</body>', new_content, re.DOTALL)
    
    # Write back to file
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully updated index.html with Day 32!')
    print('Updated stats: dayCount 31->32, locationCount 20->21, kmCount +12')
    print('Current location: 黄山·西递古村')
    print('Travel tips updated to March 20, 2026: Xidi travel guide + Spring Festival info')
else:
    print('Could not find Day 31 position!')
