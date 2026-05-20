# -*- coding: utf-8 -*-
import json, codecs, sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

data['updated'] = '2026-04-24'

# Add Fuzhou search results
data['福州三坊七巷'] = [
    {'title': '三坊七巷免费开放 中国十大历史文化名街之一'},
    {'title': '福州鱼丸肉燕 最地道的福州美食推荐'},
    {'title': '西湖公园免费 福州最古老园林始建于晋代'},
    {'title': '闽江夜游 福州经典项目两岸灯光璀璨'},
    {'title': '林则徐纪念馆 三坊七巷重要历史景点'},
]
data['福州景点'] = [
    {'title': '鼓山登山道 福州著名风景名胜'},
    {'title': '马尾船政文化 中国近代海军发源地'},
    {'title': '烟台山历史文化街区 福州最美老街'},
    {'title': '福建省博物馆 免费参观周二零闭馆'},
]
data['福州交通'] = [
    {'title': '漳州到福州约220公里 自驾2.5小时'},
    {'title': 'G15沈海高速直达 沿途风景优美'},
]

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated search_results_latest.json with Fuzhou data')
print('Updated timestamp to 2026-04-24')
print(f'Queries now: {[k for k in data.keys() if k != "updated"]}')