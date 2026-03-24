# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 31 content for March 19, 2026
day_31 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第31天</span>
                    <span class="day-date">2026-03-19 · 三月初一</span>
                </div>
                <div class="day-title">🏘️ 宏村水墨 · 画里乡村</div>
                <div class="day-content">
                    <p>告别黄山，今天来到了期待已久的宏村！</p>
                    <p>🏘️ 宏村：世界文化遗产，被誉为"画里乡村"，是徽派古村落的杰出代表</p>
                    <p>清晨6点半抵达宏村，正是拍摄南湖的最佳时间！</p>
                    <p>🖼️ 南湖：宏村的标志性景观，湖面如镜，白墙黛瓦倒映水中，宛如水墨画卷</p>
                    <p>南湖书院的晨雾还未散去，荷塘边的古树静静伫立，仿佛穿越回了明清时代。</p>
                    <p>📚 南湖书院：宏村最重要的古建筑之一，清末时期宏村子弟的学堂</p>
                    <p>上午游览了月沼（奇墅湖），这里是宏村的心脏地带。</p>
                    <p>🌙 月沼：半月形的池塘，周围是古老的徽派建筑，是宏村风水的精华</p>
                    <p>中午在村中品尝了地道的徽州美食：毛豆腐、臭鳜鱼、笋干烧肉。</p>
                    <p>🍜 徽州美食：宏村特色美食价格实惠，村中有许多农家乐提供特色餐饮</p>
                    <p>下午漫步在青石板路上，感受着古村的宁静与厚重。</p>
                    <p>🏮 徽派建筑：马头墙、天井、四合院，浓缩了徽州文化的精华</p>
                    <p>傍晚入住村中精品民宿，泡上一杯黄山毛峰，回味这一天的美好。</p>
                    <p>🍵 黄山毛峰：中国十大名茶之一，产自黄山周边，滋味醇厚回甘</p>
                    <p>明天计划前往西递古村，感受另一个世界文化遗产的魅力！</p>
                    <p>📊 今日行程：宏村深度游，步行约12公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🖼️</div>
                    <div class="photo-placeholder">🌙</div>
                    <div class="photo-placeholder">🏮</div>
                </div>
            </div>
'''

# Find Day 30 position and insert Day 31 after it
pattern = r'(<span class="day-number">第30天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    # Insert Day 31 after Day 30
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_31 + content[insert_pos:]
    
    # Update stats
    # Update day count
    new_content = re.sub(r'<div class="stat-value" id="dayCount">(\d+)</div>', 
                        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>', 
                        new_content)
    
    # Update km count (add ~12km for walking in Hongcun)
    new_content = re.sub(r'<div class="stat-value" id="kmCount">(\d+)</div>', 
                        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 12}</div>', 
                        new_content)
    
    # Update travel tips
    tips_content = '''<div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年3月安徽旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏘️ 宏村：世界文化遗产，建议清晨6-7点去南湖拍照，游客最少</li>
                    <li>🎫 门票：宏村门票104元/人，凭票可多次入园（48小时有效）</li>
                    <li>📸 最佳机位：南湖北岸、月沼观景台、宏村中学后山</li>
                    <li>🏠 住宿：村中民宿众多，300-500元/晚可住到不错的精品客栈</li>
                    <li>🍜 美食：毛豆腐10元/份，臭鳜鱼68-88元/份，笋干烧肉38元/份</li>
                    <li>🚍 交通：黄山北站有旅游大巴直达宏村，30元/人，约70分钟</li>
                    <li>🏘️ 西递：距离宏村约20公里，乘旅游公交2元/人，车程约30分钟</li>
                    <li>📅 建议游览时间：宏村4-5小时，西递2-3小时，可安排两天深度游</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年3月19日</p>
            </div>'''
    
    # Replace old tips
    old_tips_pattern = r'<div style="margin-top: 20px; padding: 15px; background: rgba\(255,255,255,0\.1\); border-radius: 10px; text-align: left;">.*?</div>\s*</div>\s*</div>\s*</div>\s*</body>'
    new_content = re.sub(old_tips_pattern, tips_content + '\n        </div>\n    </div>\n</body>', new_content, re.DOTALL)
    
    # Write back to file
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully updated index.html with Day 31!')
    print('Updated stats: dayCount +1 (30->31), kmCount +12 (3455->3467)')
    print('Travel tips updated to March 19, 2026: Hongcun travel guide')
    print('Next destination: Xidi (西递) on Day 32')
else:
    print('Could not find Day 30 position!')
