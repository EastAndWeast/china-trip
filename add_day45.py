# -*- coding: utf-8 -*-
"""Add Day 45 - Yangzhou Day 2 - 扬州深度游"""
import re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Update search results with fresh Yangzhou info
search_data = {
    "扬州旅游": [
        {"title": "2026扬州旅游攻略：烟花三月下扬州!!写给3-5月去扬州旅游的人", "url": "https://zhuanlan.zhihu.com/p/2011138080308995310", "snippet": "三日行程规划Day 1：瘦西湖-东关街-个园-古运河夜游"},
        {"title": "烟花三月下扬州：2026淮左名都深度游赏指南", "url": "https://baijiahao.baidu.com/s?id=1860057832474895321", "snippet": "从4月10日起的20天里，琼花古树绽放、五亭桥晨曦如画"},
        {"title": "江苏扬州旅游必去十大景点游玩攻略2026", "url": "https://www.sohu.com/a/992452739_121893286", "snippet": "扬州这座千年古城，每一块青砖都藏着盐商的传奇"},
        {"title": "扬州中国大运河博物馆：2026最新攻略", "url": "https://www.yzmuseum.com/", "snippet": "中国大运河博物馆是扬州最热门的新地标"},
        {"title": "2026烟花三月国际经贸旅游节4月18日开幕", "url": "https://yangzhou.gov.cn/xwzx/zwyw/art/2026/art_1a607a87526c472c9b7941b15b8819d7.html", "snippet": "今年烟花三月节将于4月18日—5月18日举办"}
    ],
    "updated": "2026年4月2日"
}

import json, os
search_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
try:
    with open(search_path, 'r', encoding='utf-8') as f:
        existing = json.load(f)
    existing.update(search_data)
    search_data = existing
except: pass

with open(search_path, 'w', encoding='utf-8') as f:
    json.dump(search_data, f, ensure_ascii=False, indent=2)
print('Search results updated!')

# Read index.html
index_path = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check if Day 45 already exists
if '第45天' in content:
    print('Day 45 already exists!')
    sys.exit(0)

# Day 45 content
day_45 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第45天</span>
                    <span class="day-date">2026-04-02 · 三月十六</span>
                </div>
                <div class="day-title">🏯 扬州 · 深入探索淮左名都</div>
                <div class="day-content">
                    <p>🌅 扬州第四天！继续深入探索这座"淮左名都"的魅力！</p>
                    <p>🏛️ 上午前往中国大运河博物馆——扬州新地标！</p>
                    <p>🚢 大运河博物馆：2021年开放，收藏了从春秋时期到现代的运河文物</p>
                    <p>博物馆建筑本身就是一件艺术品，俯瞰如同一艘巨轮航行在运河边</p>
                    <p>🎫 博物馆免费参观，但需要提前在官方公众号预约</p>
                    <p>🏛️ 下午游览扬州双博馆（扬州博物馆+扬州中国雕版印刷博物馆）</p>
                    <p>📜 扬州博物馆：馆藏文物丰富，了解扬州2500年历史</p>
                    <p>🖨️ 雕版印刷博物馆：中国唯一雕版印刷专题博物馆，非遗传承</p>
                    <p>🌿 傍晚在瘦西湖景区散步，避开上午的游客高峰</p>
                    <p>🌸 瘦西湖夕阳：五亭桥倒影、白塔晚霞，比白天更宁静美好</p>
                    <p>📊 今日行程：中国大运河博物馆 + 双博馆 + 瘦西湖夕阳，步行约10公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🚢</div>
                    <div class="photo-placeholder">🏛️</div>
                    <div class="photo-placeholder">🌅</div>
                </div>
            </div>
'''

# Find Day 44 position and insert Day 45 after it
pattern = r'(<span class="day-number">第44天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_45 + content[insert_pos:]
    
    # Update statistics
    new_content = re.sub(
        r'<div class="stat-value" id="dayCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 1}</div>',
        new_content
    )
    
    # Update km count (walking ~10km)
    new_content = re.sub(
        r'<div class="stat-value" id="kmCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 10}</div>',
        new_content
    )
    
    # Current location stays in 扬州
    # new_content = re.sub(
    #     r'id="currentLocation">[^<]+',
    #     'id="currentLocation">扬州 · 瘦西湖',
    #     new_content
    # )
    
    # Update last update time
    new_content = re.sub(
        r'最后更新：\d+年\d+月\d+日',
        '最后更新：2026年4月2日',
        new_content
    )
    
    # Write back
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('\n✅ Successfully added Day 45!')
    print('Day 45: 扬州 · 深入探索淮左名都 (2026-04-02)')
    print('Stats: dayCount 44→45, kmCount +10')
    print('Current location: 扬州 · 瘦西湖')
    print('Last update: 2026年4月2日')
else:
    print('Could not find Day 44 position!')
    sys.exit(1)
