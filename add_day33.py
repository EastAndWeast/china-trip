# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 33 content for March 21, 2026
day_33 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第33天</span>
                    <span class="day-date">2026-03-21 · 三月初三</span>
                </div>
                <div class="day-title">🏔️ 齐云山 · 道教名山云中游</div>
                <div class="day-content">
                    <p>告别西递古村，驱车前往中国四大道教名山之一——齐云山！</p>
                    <p>🏔️ 齐云山：古称白岳，因"遥观山顶与云平齐"而得名，道教名山</p>
                    <p>早上从西递出发，车程约1小时便抵达齐云山脚下。</p>
                    <p>☁️ 山中云雾缭绕，仿佛置身仙境，果然名不虚传！</p>
                    <p>齐云山位于安徽省黄山市休宁县境内，景区面积110平方公里，由九座山峰组成。</p>
                    <p>🛤️ 登山步道：沿途风景秀丽，雨后云海翻涌蔚为壮观</p>
                    <p>齐云山不仅自然风光秀美，更有深厚的道教文化底蕴，是修身养性的好去处。</p>
                    <p>🏯 道教文化：中国四大道教名山之一，古迹众多</p>
                    <p>下午下山后在山脚下的农家乐享用了地道的徽州美食，疲劳感一扫而空！</p>
                    <p>🍜 农家菜：新鲜的山野菜、笋干烧肉、清炒时蔬</p>
                    <p>傍晚入住齐云山脚的民宿，为明天的旅程养精蓄锐。</p>
                    <p>📊 今日行程：齐云山深度游览，步行约8公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🏔️</div>
                    <div class="photo-placeholder">☁️</div>
                    <div class="photo-placeholder">🏯</div>
                </div>
            </div>
'''

# Find Day 32 position and insert Day 33 after it
pattern = r'(<span class="day-number">第32天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    # Insert Day 33 after Day 32
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_33 + content[insert_pos:]
    
    # Update stats
    # Update day count 32 -> 33
    new_content = re.sub(
        r'<div class="stat-value" id="dayCount">(\d+)</div>', 
        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>', 
        new_content
    )
    
    # Update km count +45km (Xidi to Qiyunshan ~45km)
    new_content = re.sub(
        r'<div class="stat-value" id="kmCount">(\d+)</div>', 
        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 45}</div>', 
        new_content
    )
    
    # Update location count 21 -> 22
    new_content = re.sub(
        r'<div class="stat-value" id="locationCount">(\d+)</div>', 
        lambda m: f'<div class="stat-value" id="locationCount">{int(m.group(1)) + 1}</div>', 
        new_content
    )
    
    # Update current location
    new_content = re.sub(
        r'<span>当前所在：<strong id="currentLocation">[^<]+</strong></span>',
        '<span>当前所在：<strong id="currentLocation">黄山 · 齐云山</strong></span>',
        new_content
    )
    
    # Update travel tips to March 21, 2026
    tips_content = '''<div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年3月安徽旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏔️ 齐云山：中国四大道教名山之一，古称白岳，"遥观山顶与云平齐"得名</li>
                    <li>📍 位置：安徽省黄山市休宁县城西约15公里</li>
                    <li>🏯 道教文化：齐云山是修身养性的道教圣地，古迹众多</li>
                    <li>☁️ 云海：雨后云海翻涌最为壮观，建议关注天气</li>
                    <li>🏔️ 山峰：由齐云、白岳、歧山等9座山峰组成，景区面积110平方公里</li>
                    <li>🚶 登山建议：穿舒适登山鞋，步道较为平缓适合大众</li>
                    <li>🏠 住宿：山脚民宿众多，150-300元/晚</li>
                    <li>🍜 美食：山野菜、笋干系列、土鸡煲</li>
                    <li>📸 最佳拍摄点：山顶观景台，雨后云海日出</li>
                    <li>🚗 交通：距黄山市区约33公里，自驾或乘公交可达</li>
                    <li>🏘️ 联游建议：可与宏村、西递组合游玩，建议安排2-3天</li>
                    <li>🌸 春季景色：3-4月山花烂漫，云海频繁</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年3月21日</p>
            </div>'''
    
    # Replace old tips
    old_tips_pattern = r'<div style="margin-top: 20px; padding: 15px; background: rgba\(255,255,255,0\.1\); border-radius: 10px; text-align: left;">.*?</div>\s*</div>\s*</div>\s*</div>\s*</body>'
    new_content = re.sub(old_tips_pattern, tips_content + '\n        </div>\n    </div>\n</body>', new_content, re.DOTALL)
    
    # Write back to file
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully updated index.html with Day 33!')
    print('Updated stats: dayCount 32->33, locationCount 21->22, kmCount +45')
    print('Current location: 黄山·齐云山')
    print('Travel tips updated to March 21, 2026: Qiyunshan Taoist mountain guide')
else:
    print('Could not find Day 32 position!')
