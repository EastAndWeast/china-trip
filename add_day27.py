# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read the HTML file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 27 content - travel to Wuyuan (婺源)
day_27 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第27天</span>
                    <span class="day-date">2026-03-15 · 二月廿六</span>
                </div>
                <div class="day-title">🌼 婺源 · 中国最美乡村</div>
                <div class="day-content">
                    <p>今天从武夷山出发，前往被誉为"中国最美乡村"的婺源！</p>
                    <p>🌼 婺源：江西省东北部，以油菜花海、徽派建筑、古村落著称</p>
                    <p>上午驱车约300公里，从福建武夷山到江西婺源，沿途风景如画。</p>
                    <p>🏘️ 下午抵达婺源后，首先游览了江岭景区——这里是婺源油菜花的最佳观赏点！</p>
                    <p>🌼 江岭：万亩梯田油菜花海，金黄色的花海与白墙黛瓦的徽派建筑交相辉映</p>
                    <p>虽然已是3月中旬，但江岭的油菜花依然盛放，吸引众多摄影爱好者前来。</p>
                    <p>随后前往篁岭古村，这座挂在山崖上的古村晾晒着红红的辣椒、黄黄的玉米，充满了浓郁的乡土气息！</p>
                    <p>🏮 篁岭："晒秋"文化的发源地，古村落保存完好，梯田花海与徽派建筑完美融合</p>
                    <p>🍜 晚上在婺源县城品尝了当地特色美食：荷包红鲤鱼、糊豆腐、粉蒸菜</p>
                    <p>今晚入住婺源特色民宿，明天将继续探索李坑、晓起等古村落！</p>
                    <p>📊 今日行程：从武夷山到婺源，约300公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌼</div>
                    <div class="photo-placeholder">🏘️</div>
                    <div class="photo-placeholder">🏮</div>
                </div>
            </div>
'''

# Find Day 26 position and insert Day 27 after it
pattern = r'(<span class="day-number">第26天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    # Insert Day 27 after Day 26
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_27 + content[insert_pos:]
    
    # Update statistics
    # Update day count
    new_content = re.sub(r'<div class="stat-value" id="dayCount">(\d+)</div>', 
                        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>', 
                        new_content)
    
    # Update km count (approx 300km + local travel)
    new_content = re.sub(r'<div class="stat-value" id="kmCount">(\d+)</div>', 
                        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 320}</div>', 
                        new_content)
    
    # Update location count
    new_content = re.sub(r'<div class="stat-value" id="locationCount">(\d+)</div>', 
                        lambda m: f'<div class="stat-value" id="locationCount">{int(m.group(1)) + 1}</div>', 
                        new_content)
    
    # Update current location
    new_content = new_content.replace(
        'id="currentLocation">武夷山 · 虎啸岩',
        'id="currentLocation">婺源 · 江岭'
    )
    
    # Update last update time
    new_content = re.sub(
        r'最后更新：\d+年\d+月\d+日',
        '最后更新：2026年3月15日',
        new_content
    )
    
    # Write back
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully updated index.html with Day 27!')
    print('Updated stats: dayCount +1 (27), kmCount +320 (3235), locationCount +1 (19)')
    print('Current location changed to: 婺源 · 江岭')
else:
    print('Could not find Day 26 position!')
