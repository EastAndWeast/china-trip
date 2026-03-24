# -*- coding: utf-8 -*-
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Add Xidi search results
data['西递古村旅游攻略 2026年3月'] = [
    '西递古村：世界文化遗产，被誉为"桃花源里人家"，始建于北宋',
    '保存明清古民居224幢，124幢为全国重点文物保护单位',
    '春会时间：2026年3月22日—4月29日',
    '杭州高铁2小时直达黟县东站',
    '西递门票104元/人，与宏村联票更优惠',
    '建议游览时间3-4小时，清晨或傍晚拍照最佳'
]

with open('C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated search_results_latest.json with Xidi info')
