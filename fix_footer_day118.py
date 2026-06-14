"""Fix footer for Day 118 - use regex group replacement (LRN-20260612-001 lesson)"""
import re, sys, codecs, os
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = r'C:\Users\admin\.openclaw\workspace\china-trip\index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# The current footer (after Day 117) should be the 苏州 footer. Let's read it fresh.
# Find the footer block
m = re.search(r'(<div class="footer">.*?最后更新：2026年6月15日（周一）</p>)', content, re.DOTALL)
if not m:
    print('ERROR: Footer block not found')
    sys.exit(1)

old_footer = m.group(1)
print('=== OLD FOOTER (read fresh) ===')
print(old_footer)
print()
print('Length:', len(old_footer))

# Build the new footer (Day 118 version, 南京)
new_footer_inner = '''<div class="footer">
            <p>🚗 环游中国 · 汽车日记</p>
            <p>记录每一天的所见所闻</p>
            <div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; text-align: left;">
                <p style="font-size: 14px; margin-bottom: 10px;">🏛️ 2026年6月苏南（1）· 南京·六朝古都·中山陵·明孝陵·总统府</p>
                <ul style="font-size: 12px; opacity: 0.8; padding-left: 20px;">
                    <li>🏙️ 南京六朝古都十朝都会！与北京/西安/洛阳并称"中国四大古都"；六朝（229-589 AD 东吴/东晋/宋/齐/梁/陈）；十朝（东吴/东晋/宋/齐/梁/陈/南唐/明/太平天国/中华民国）</li>
                    <li>⛰️ 中山陵免费（需"中山陵预约"公众号实名预约）！孙中山先生陵寝 1929 建成；392 级台阶/8 个平台；蓝白色"自由钟"形制；紫金山南麓；与明孝陵联票 100 元；周一闭馆</li>
                    <li>🌲 明孝陵 5A 70 元！世界文化遗产 2003 入选"明清皇家陵寝"项目；朱元璋+马皇后合葬陵 1381 年建成；神道"石象生"12 对蜿蜒 2km 形似"北斗七星"；"治隆唐宋"康熙手书</li>
                    <li>🏛️ 秦淮河夫子庙 5A 免费！"六朝金粉地，十里秦淮河"；江南贡院（中国古代最大科举考场 1380/206 间号舍/1380 余名进士）；夜游画舫 80 元/人 18:30-21:30 看两岸灯火+古戏台演出</li>
                    <li>🍜 金陵菜四大名菜：盐水鸭（韩复兴 80 年 38 元/斤）/ 鸭血粉丝汤（回味 18 元）/ 蟹黄汤包（28 元/笼）/ 桂花糖芋苗；南京大牌档人均 80-120 元 招牌；老门东"秦淮八绝"套餐 128 元 8 道小食</li>
                    <li>🚗 苏州→南京 220km G42 沪蓉高速 2.5h；南京南站乘高铁（G 字头 145 元/1.5h/周一闭馆 G42 直达）/ 自驾 G42 直达；新街口/夫子庙酒店 400-1500 元/晚 商务/秦淮</li>
                    <li>📅 明日预告：南京→ 合肥（300km G42/G4001 高速 3h 安徽省会/三国故地/包公故里）/ 扬州（100km G40 沪陕高速 1.5h 世界美食之都/瘦西湖/个园）/ 镇江（70km G42 沪蓉高速 1h 西津渡/金山寺/茅山）</li>
                </ul>
                <p style="margin-top: 15px; font-size: 11px; opacity: 0.6;">最后更新：2026年6月15日（周一）</p>
            </div>
        </div>'''

# Use regex group replacement (LRN-20260612-001 lesson): replace the entire footer block
# Pattern: capture the footer start, find the closing </div> of the footer
# We need to find the FULL footer including its closing tags

# Locate the footer end - find the </div> closing the footer
# Look for the outer footer block
footer_pattern = re.compile(
    r'(<div class="footer">.*?最后更新：2026年6月15日（周一）</p>\s*</div>\s*</div>)',
    re.DOTALL
)
m_full = footer_pattern.search(content)
if not m_full:
    print('ERROR: Full footer pattern not found')
    # Try a broader pattern
    footer_pattern2 = re.compile(
        r'(<div class="footer">.*?最后更新：2026年6月15日（周一）</p>.*?</div>)',
        re.DOTALL
    )
    m_full = footer_pattern2.search(content)
    if not m_full:
        print('ERROR: Even broader footer pattern not found')
        sys.exit(1)
    print('Used broader pattern')

old_full = m_full.group(1)
print('Old full footer length:', len(old_full))

# Replace using regex count=1
new_content = footer_pattern.sub(new_footer_inner, content, count=1)
if new_content == content:
    print('WARN: regex sub did not modify content')
    # Try the broader pattern
    new_content = footer_pattern2.sub(new_footer_inner, content, count=1)

if new_content != content:
    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Footer updated successfully')
else:
    print('ERROR: Footer update failed')
    sys.exit(1)

# Verify
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    verify = f.read()

# Check key new content
checks = [
    ('南京六朝古都十朝都会', '六朝古都 tip'),
    ('中山陵免费', '中山陵 tip'),
    ('明孝陵 5A 70 元', '明孝陵 tip'),
    ('秦淮河夫子庙 5A', '秦淮河 tip'),
    ('金陵菜四大名菜', '金陵菜 tip'),
    ('苏州→南京 220km', '220km tip'),
    ('2026年6月15日（周一）', 'last update line'),
]

for keyword, desc in checks:
    found = keyword in verify
    print(f'  {desc}: {"YES" if found else "NO"}')

# Verify old content removed
old_keywords = ['苏州古典园林 1997', '拙政园·留园', '中山陵→明孝陵→秦淮']
for keyword in old_keywords:
    if keyword in verify:
        print(f'  WARN: Old content "{keyword}" still present!')
    else:
        print(f'  Old content "{keyword}" removed: YES')

print()
print('New file size:', os.path.getsize(HTML_PATH))
