# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 28 content for March 16, 2026
day_28 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第28天</span>
                    <span class="day-date">2026-03-16 · 二月廿七</span>
                </div>
                <div class="day-title">🏘️ 婺源李坑 · 小桥流水人家</div>
                <div class="day-content">
                    <p>今天继续探索婺源的古村落！上午前往李坑，这是一座有着千年历史的水乡村落。</p>
                    <p>🏘️ 李坑：四面环山，一条小溪穿村而过，是典型的徽派水乡</p>
                    <p>漫步在青石板路上，两侧是保存完好的明清古建筑，白墙黛瓦，马头墙高耸。</p>
                    <p>小桥流水人家，夕阳西下时，整个村落笼罩在金色的余晖中，如诗如画！</p>
                    <p>下午前往晓起村，这里以"晓起三宝"著称：砖雕、木雕、石雕，雕刻精美绝伦。</p>
                    <p>🪵 晓起：始建于唐代，是中国历史文化名村，徽派建筑艺术的代表</p>
                    <p>傍晚在晓起的观景台欣赏了日落，远眺层层梯田和古村落，美不胜收！</p>
                    <p>🍜 晚上品尝了婺源特色美食：蒸汽糕、清明果、婺源绿茶</p>
                    <p>婺源的古村落让人流连忘返，明天将启程前往下一个目的地——安徽黄山！</p>
                    <p>📊 今日行程：在婺源各古村落间游览，约50公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏘️</div>
                    <div class="photo-placeholder">🌉</div>
                    <div class="photo-placeholder">🍜</div>
                </div>
            </div>
'''

# Find Day 27 position and insert Day 28 after it
pattern = r'(<span class="day-number">第27天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    # Insert Day 28 after Day 27
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_28 + content[insert_pos:]
    
    # Update stats
    # Update day count
    new_content = re.sub(r'<div class="stat-value" id="dayCount">(\d+)</div>', 
                        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>', 
                        new_content)
    
    # Update km count (add ~50km for today)
    new_content = re.sub(r'<div class="stat-value" id="kmCount">(\d+)</div>', 
                        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 50}</div>', 
                        new_content)
    
    # Update current location
    new_content = new_content.replace(
        'id="currentLocation">婺源 · 中国最美乡村',
        'id="currentLocation">婺源 · 李坑'
    )
    
    # Update travel tips
    tips_content = '''<div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年3月江西安徽旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🌼 婺源油菜花：3月中下旬仍是最佳观赏期，江岭、篁岭为主要观赏点</li>
                    <li>🏘️ 婺源古村落：李坑、晓起、思溪延村保存完好，建议包车游览</li>
                    <li>🏔️ 黄山：春季云海较多，建议提前关注天气预报</li>
                    <li>🛶 黄山宏村：徽派建筑典范，春季油菜花与古村相映成趣</li>
                    <li>🍜 婺源美食：荷包红鲤鱼、糊豆腐、粉蒸菜、清明果</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年3月16日</p>
            </div>'''
    
    # Replace old tips
    old_tips_pattern = r'<div style="margin-top: 20px; padding: 15px; background: rgba\(255,255,255,0\.1\); border-radius: 10px; text-align: left;">.*?</div>\s*</div>\s*</div>\s*</div>\s*</body>'
    new_content = re.sub(old_tips_pattern, tips_content + '\n        </div>\n    </div>\n</body>', new_content, re.DOTALL)
    
    # Write back to file
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully updated index.html with Day 28!')
    print('Updated stats: dayCount +1 (27->28), kmCount +50 (3235->3285)')
    print('Current location changed to: 婺源 · 李坑')
    print('Travel tips updated to March 16, 2026')
else:
    print('Could not find Day 27 position!')
