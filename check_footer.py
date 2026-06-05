# -*- coding: utf-8 -*-
import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
# Find footer div
m = re.search(r'<div class="footer">(.*?)$', c, re.DOTALL)
if m:
    text = m.group(1)
    print(text[:3000])
