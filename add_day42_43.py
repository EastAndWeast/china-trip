# -*- coding: utf-8 -*-
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 42 content - Suzhou to Nanjing
day_42 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第42天</span>
                    <span class="day-date">2026-03-30 · 三月十三</span>
                </div>
                <div class="day-title">🚄 苏州→南京 · 六朝古都</div>
                <div class="day-content">
                    <p>告别苏州，乘坐高铁前往南京！这座"六朝古都"期待已久！</p>
                    <p>🚄 交通：苏州北→南京南，约1小时10分钟，宁沪高铁极为便捷</p>
                    <p>🏯 下午抵达南京后，首先前往夫子庙-秦淮河风光带！</p>
                    <p>🏮 夫子庙：南京最繁华的商业街区，中国四大文庙之一</p>
                    <p>🌙 夜游秦淮河是重头戏！乘坐画舫游览十里秦淮，两岸灯火辉煌，美不胜收！</p>
                    <p>🚣 秦淮河：南京的母亲河，六朝金粉地，十里秦淮声</p>
                    <p>🍜 晚餐在夫子庙品尝南京特色美食：盐水鸭、鸭血粉丝汤、秦淮八绝</p>
                    <p>🏮 老门东：夫子庙旁的历史街区，保存了明清风格建筑，夜景尤为迷人</p>
                    <p>📊 今日行程：苏州到南京高铁，夫子庙+秦淮河夜游，步行约8公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🚄</div>
                    <div class="photo-placeholder">🏮</div>
                    <div class="photo-placeholder">🌙</div>
                </div>
            </div>
'''

# Day 43 content - Nanjing exploration, cherry blossom season
day_43 = '''
            <div class="day-card">
                <div class="day-header">
                    <span class="day-number">第43天</span>
                    <span class="day-date">2026-03-31 · 三月十四</span>
                </div>
                <div class="day-title">🌸 南京 · 中山陵与梅花山</div>
                <div class="day-content">
                    <p>今天是三月的最后一天，南京春意正浓，梅花山樱花盛放！</p>
                    <p>🌸 特别提示：2026南京春季赏花正当时，梅花、樱花、白玉兰接续绽放</p>
                    <p>🌸 上午前往钟山风景区——中山陵！这里是伟大的革命先行者孙中山先生的陵寝。</p>
                    <p>🏛️ 中山陵：钟山南麓，陵寝面积8万余平方米，被誉为"中国近代建筑史上第一陵"</p>
                    <p>从下往上看，台阶看不到尽头，象征着革命道路的艰辛与漫长。</p>
                    <p>🌸 下午游览明孝陵景区——梅花山正是赏梅最佳时节！</p>
                    <p>🌸 梅花山：被誉为"天下第一梅山"，30000余株梅花竞相绽放</p>
                    <p>2026南京明孝陵梅花山赏梅季活动正在进行中，错过了就要等明年！</p>
                    <p>🍜 午餐品尝南京经典美食：蟹黄汤包、赤豆元宵、糖藕</p>
                    <p>🌆 傍晚在玄武湖散步，这是中国最大的皇家园林湖泊，春色满园！</p>
                    <p>🪷 玄武湖：江南三大名湖之一，环湖一周约10公里，免费开放</p>
                    <p>📊 今日行程：中山陵 + 明孝陵梅花山 + 玄武湖，步行约15公里</p>
                </div>
                <div class="photos">
                    <div class="photo-placeholder">🌸</div>
                    <div class="photo-placeholder">🏛️</div>
                    <div class="photo-placeholder">🌸</div>
                </div>
            </div>
'''

# Find Day 41 position and insert Day 42 after it
pattern = r'(<span class="day-number">第41天</span>.*?</div>\s*</div>\s*</div>\s*)'
match = re.search(pattern, content, re.DOTALL)

if match:
    insert_pos = match.end()
    new_content = content[:insert_pos] + day_42 + day_43 + content[insert_pos:]
    
    # Update statistics
    new_content = re.sub(
        r'<div class="stat-value" id="dayCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="dayCount">{int(m.group(1)) + 2}</div>',
        new_content
    )
    
    # Update km count (Nanjing walking ~15+8=23km)
    new_content = re.sub(
        r'<div class="stat-value" id="kmCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="kmCount">{int(m.group(1)) + 23}</div>',
        new_content
    )
    
    # Update location count (add Nanjing)
    new_content = re.sub(
        r'<div class="stat-value" id="locationCount">(\d+)</div>',
        lambda m: f'<div class="stat-value" id="locationCount">{int(m.group(1)) + 1}</div>',
        new_content
    )
    
    # Update current location
    new_content = new_content.replace(
        'id="currentLocation">苏州 · 拙政园',
        'id="currentLocation">南京 · 玄武湖'
    )
    
    # Update travel dates if needed
    new_content = new_content.replace(
        'id="currentLocation">南京 · 玄武湖',
        'id="currentLocation">南京 · 玄武湖'
    )
    
    # Update last update time
    new_content = re.sub(
        r'最后更新：\d+年\d+月\d+日',
        '最后更新：2026年3月31日',
        new_content
    )
    
    # Write back
    with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully added Day 42 and Day 43!')
    print('Day 42: 苏州→南京 · 六朝古都 (2026-03-30)')
    print('Day 43: 南京 · 中山陵与梅花山 (2026-03-31)')
    print('Stats: dayCount +2, kmCount +23, locationCount +1')
    print('Current location: 南京 · 玄武湖')
else:
    print('Could not find Day 41 position!')
    day_matches = re.findall(r'<span class="day-number">(第\d+天)</span>', content)
    print('Found days: ' + str(day_matches[-5:] if day_matches else 'none'))
