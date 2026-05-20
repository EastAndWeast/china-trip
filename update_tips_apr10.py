# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\admin\.openclaw\workspace\china-trip\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if already updated
if '最后更新：2026年4月10日' in content and '2026年4月中旬' in content:
    print('Already updated to April 10 tips, skipping.')
else:
    # Replace the old tips div
    old_tips = '''            <div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年4月上旬江浙沪旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏯 苏州园林：拙政园、留园、狮子林春季赏花正当时，4月游客增多建议早出发</li>
                    <li>🏛️ 苏州博物馆：贝聿铭设计，免费需预约，建筑本身就是一件艺术品</li>
                    <li>🌉 平江路：800米古街保存完整，小桥流水，免费漫步，两旁评弹茶馆韵味十足</li>
                    <li>🌙 金鸡湖夜景：摩天轮灯光秀每晚亮起，诚品书店、月光码头值得一看</li>
                    <li>🍜 苏州美食：松鼠桂鱼、碧螺虾仁、苏式汤面、糕团点心，观前街选择丰富</li>
                    <li>🌸 扬州烟花节：2026年4月18日开幕，持续一个月，瘦西湖琼花正盛</li>
                    <li>🏯 无锡灵山：灵山大佛、拈花湾禅意小镇，春日祈福好去处</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月8日</p>
            </div>'''

    new_tips = '''            <div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年4月中旬旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏔️ 黄山登山：4月中旬云海概率高，建议早起观日出，备好防风外套和登山杖</li>
                    <li>🌸 宏村西递：4月油菜花虽过但桃花、紫藤盛开，清明后人流减少正是好时机</li>
                    <li>🌉 扬州烟花节：2026年4月18日开幕，瘦西湖琼花正盛，需提前订房</li>
                    <li>🏯 苏州园林：拙政园、留园、狮子林春季赏花正当时，建议早7点前入园避人流</li>
                    <li>🍜 徽州美食：黄山毛豆腐、臭鳜鱼、石耳炖鸡，宏村村内农家乐价格实惠</li>
                    <li>🚗 交通提示：黄山景区换乘中心至云谷寺/慈光阁需乘景区大巴，平日人少畅通</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年4月10日</p>
            </div>'''

    if old_tips in content:
        new_content = content.replace(old_tips, new_tips)
        with open(r'C:\Users\admin\.openclaw\workspace\china-trip\index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('SUCCESS: Travel tips updated!')
    else:
        print('WARNING: Old tips not found exactly, trying pattern match...')
        # Try pattern-based replacement
        pattern = r'(<p style="font-size: 14px; margin-bottom: 10px;">📰 )2026年4月上旬江浙沪旅游贴士(</p>.*?最后更新：)2026年4月8日(</p>)'
        replacement = r'\g<1>2026年4月中旬旅游贴士\2 2026年4月10日\3'
        new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
        if count > 0:
            with open(r'C:\Users\admin\.openclaw\workspace\china-trip\index.html', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'SUCCESS: Travel tips updated via pattern ({count} replacements)')
        else:
            print('ERROR: Could not find tips to replace')
