# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 读取文件
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 第26天的内容
day_26 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第26天</span>
                    <span class="day-date">2026-03-14 · 二月廿五</span>
                </div>
                <div class="day-title">🦁 武夷山 · 虎啸岩与一线天</div>
                <div class="day-content">
                    <p>今天继续探索武夷山景区！上午前往虎啸岩，这是武夷山最壮观的景点之一。</p>
                    <p>🦁 虎啸岩：因岩上有洞，风吹过时发出虎啸般的声音而得名，海拔500米</p>
                    <p>登上虎啸岩顶，俯瞰整个武夷山景区，云海翻涌，气势磅礴！</p>
                    <p>下午挑战了一线天景区，最窄处仅容一人通过，非常刺激！</p>
                    <p>🪨 一线天：武夷山最奇的景观，两壁高耸，中间仅容一人穿过</p>
                    <p>🍵 晚上在度假区茶馆品尝了武夷山正山小种红茶，回甘绵长</p>
                    <p>武夷山之行即将结束，明天将启程前往下一个目的地——江西婺源！</p>
                    <p>📊 今日行程：在武夷山景区内游览，步行约15公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🦁</div>
                    <div class="photo-placeholder">🪨</div>
                    <div class="photo-placeholder">🍵</div>
                </div>
            </div>
'''

# 找到第25天的位置并在其后插入第26天
# 使用正则表达式找到第25天卡片结束的位置
pattern = r'(<span class="day-number">第25天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    # 在第25天后插入第26天
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_26 + content[insert_pos:]
    
    # 更新统计信息
    # 更新天数
    new_content = re.sub(r'<div class="stat-value" id="dayCount">(\d+)</div>', 
                        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>', 
                        new_content)
    
    # 更新公里数（估计增加15公里）
    new_content = re.sub(r'<div class="stat-value" id="kmCount">(\d+)</div>', 
                        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 15}</div>', 
                        new_content)
    
    # 更新当前地点
    new_content = new_content.replace(
        'id="currentLocation">武夷山 · 度假区',
        'id="currentLocation">武夷山 · 虎啸岩'
    )
    
    # 更新最后更新时间
    new_content = re.sub(
        r'最后更新：\d+年\d+月\d+日',
        '最后更新：2026年3月14日',
        new_content
    )
    
    # 写回文件
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully updated index.html with Day 26!')
    print('Updated stats: dayCount +1, kmCount +15')
    print('Current location changed to: 武夷山 · 虎啸岩')
else:
    print('Could not find Day 25 position!')
