# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 34 content for March 22, 2026
day_34 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第34天</span>
                    <span class="day-date">2026-03-22 · 二月廿三</span>
                </div>
                <div class="day-title">🏔️ 黄山风景区 · 云海日出</div>
                <div class="day-content">
                    <p>清晨从齐云山出发，车程约1小时抵达黄山风景区！</p>
                    <p>🏔️ 黄山：世界文化与自然遗产，"五岳归来不看山，黄山归来不看岳"</p>
                    <p>今天天气晴朗，正是观赏云海日出的最佳时机！</p>
                    <p>🚠 乘坐云谷索道上山，沿途欣赏壮丽的山景</p>
                    <p>☁️ 黄山云海：云雾缭绕在山峰之间，宛如仙境</p>
                    <p>🏔️ 主要景点：光明顶、迎客松、飞来石、猴子观海...</p>
                    <p>📸 在光明顶拍摄了绝美的云海日出照片</p>
                    <p>🌅 站在山顶俯瞰群山，云海翻涌气势磅礴</p>
                    <p>下午游览西海大峡谷，感叹大自然的鬼斧神工！</p>
                    <p>🚶 全天步行约12公里，虽然疲惫但收获满满</p>
                    <p>傍晚入住黄山山顶酒店，期待明天清晨的日出！</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏔️</div>
                    <div class="photo-placeholder">☁️</div>
                    <div class="photo-placeholder">🌅</div>
                </div>
            </div>
'''

# Find Day 33 position and insert Day 34 after it
pattern = r'(<span class="day-number">第33天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    # Insert Day 34 after Day 33
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_34 + content[insert_pos:]
    
    # Update stats
    # Update day count 33 -> 34
    new_content = re.sub(
        r'<div class="stat-value" id="dayCount">(\d+)</div>', 
        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>', 
        new_content
    )
    
    # Update km count +65km (Qiyunshan to Huangshan ~65km)
    new_content = re.sub(
        r'<div class="stat-value" id="kmCount">(\d+)</div>', 
        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 65}</div>', 
        new_content
    )
    
    # Update location count 22 -> 23
    new_content = re.sub(
        r'<div class="stat-value" id="locationCount">(\d+)</div>', 
        lambda m: f'<div class="stat-value" id="locationCount">{int(m.group(1)) + 1}</div>', 
        new_content
    )
    
    # Update current location
    new_content = re.sub(
        r'<span>当前所在：<strong id="currentLocation">[^<]+</strong></span>',
        '<span>当前所在：<strong id="currentLocation">黄山 · 黄山风景区</strong></span>',
        new_content
    )
    
    # Update travel tips to March 22, 2026
    tips_content = '''<div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年3月黄山旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏔️ 黄山：中国著名山岳景区，世界文化与自然遗产</li>
                    <li>📍 位置：安徽省黄山市黄山区汤口镇</li>
                    <li>🌅 日出：光明顶、始信峰是最佳观赏点，建议凌晨4-5点起床</li>
                    <li>☁️ 云海：雨后初晴最容易出现云海壮观景象</li>
                    <li>🚠 索道：云谷寺索道、太平索道、玉屏楼索道可选</li>
                    <li>🏨 住宿：山顶有多家酒店，北海、光明顶、西海等</li>
                    <li>🥾 登山建议：穿防滑登山鞋，拐杖很有用</li>
                    <li>🍜 美食：黄山烧饼、臭鳜鱼、毛豆腐</li>
                    <li>📸 最佳拍摄点：光明顶、始信峰、猴子观海、飞来石</li>
                    <li>🌸 春季景色：3-4月山花盛开，气候宜人</li>
                    <li>⚠️ 注意：山顶早晚温差大，需带保暖衣物</li>
                    <li>🎫 门票：旺季230元/人，索道另付</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年3月22日</p>
            </div>'''
    
    # Replace old tips
    old_tips_pattern = r'<div style="margin-top: 20px; padding: 15px; background: rgba\(255,255,255,0\.1\); border-radius: 10px; text-align: left;">.*?</div>\s*</div>\s*</div>\s*</div>\s*</body>'
    new_content = re.sub(old_tips_pattern, tips_content + '\n        </div>\n    </div>\n</body>', new_content, re.DOTALL)
    
    # Write back to file
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully updated index.html with Day 34!')
    print('Updated stats: dayCount 33->34, locationCount 22->23, kmCount +65')
    print('Current location: 黄山 · 黄山风景区')
    print('Travel tips updated to March 22, 2026: Huangshan travel guide')
else:
    print('Could not find Day 33 position!')
