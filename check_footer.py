# -*- coding: utf-8 -*-
import re
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

with open('C:/Users/admin/.openclaw/workspace/china-trip/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find footer
start = content.find('<div class="footer">')
print('Footer starts at:', start)
footer_excerpt = content[start:start+1200]
print(footer_excerpt)
