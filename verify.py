# -*- coding: utf-8 -*-
import re

f = open(r'C:\Users\admin\.openclaw\workspace\china-trip\index.html', 'r', encoding='utf-8')
content = f.read()
f.close()

# 提取关键数据
day = re.search(r'id="dayCount">(\d+)', content)
loc = re.search(r'id="locationCount">(\d+)', content)
km = re.search(r'id="kmCount">(\d+)', content)
current = re.search(r'id="currentLocation">([^<]+)', content)

print('更新后的数据:')
print(f'天数: {day.group(1)}')
print(f'地点: {loc.group(1)}')
print(f'公里: {km.group(1)}')
print(f'当前位置: {current.group(1)}')

# 检查第13天是否存在
if '第13天' in content:
    print('\n✓ 第13天行程已添加')
else:
    print('\n✗ 第13天行程未找到')
