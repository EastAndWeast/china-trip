# -*- coding: utf-8 -*-
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
    # 查找第23天的内容
    if '第23天' in content:
        print('✅ 第23天行程已添加')
    if '福州' in content:
        print('✅ 当前位置已更新为福州')
    if 'dayCount">23' in content:
        print('✅ 天数已更新为23天')
    if 'kmCount">2350' in content:
        print('✅ 公里数已更新为2350')
    if '三坊七巷' in content:
        print('✅ 位置显示三坊七巷')
    print('\n更新完成！')
