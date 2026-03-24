# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update travel tips
old_tips = '''<div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年3月福建旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🎫 武夷山九曲溪竹筏：约225元/人，建议提前预约早班6:40</li>
                    <li>🏔️ 天游峰：武夷山最险峻峰顶，雨后云海翻涌似仙境</li>
                    <li>🛶 竹筏漂流全程约9.5km，1.5小时，穿越丹霞地貌</li>
                    <li>🍵 武夷山岩茶：大红袍母树不容错过</li>
                    <li>📅 景区联票：3日通票385元，含门票+观光车+竹筏</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年3月15日</p>
            </div>'''

new_tips = '''<div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">📰 2026年3月江西安徽旅游贴士</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🌼 婺源油菜花：3月中下旬仍是最佳观赏期，江岭、篁岭为主要观赏点</li>
                    <li>🏘️ 婺源古村落：李坑、晓起、思溪延村保存完好，建议包车游览</li>
                    <li>🏔️ 黄山：春季云海较多，建议提前关注天气预报</li>
                    <li>🛶 黄山宏村：徽派建筑典范，春季油菜花与古村相映成趣</li>
                    <li>🍜 婺源美食：荷包红鲤鱼、糊豆腐、粉蒸菜、清明果</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年3月16日</p>
            </div>'''

new_content = content.replace(old_tips, new_tips)

# Write back to file
with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Successfully updated travel tips!')
