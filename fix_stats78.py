# -*- coding: utf-8 -*-
import re, codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    c = f.read()

# Fix dayCount: was incremented twice, should be 78
m = re.search(r'id="dayCount"[^>]*>(\d+)<', c)
if m:
    print('dayCount currently:', m.group(1))
    if m.group(1) == '79':
        c = c.replace('id="dayCount">79<', 'id="dayCount">78<')
        print('Fixed dayCount to 78')

# Fix kmCount: was incremented twice, should be 9203
m = re.search(r'id="kmCount"[^>]*>(\d+)<', c)
if m:
    print('kmCount currently:', m.group(1))
    if m.group(1) == '9533':
        c = c.replace('id="kmCount">9533<', 'id="kmCount">9203<')
        print('Fixed kmCount to 9203')

# Fix locationCount: was incremented twice, should be 48
m = re.search(r'id="locationCount"[^>]*>(\d+)<', c)
if m:
    print('locationCount currently:', m.group(1))
    if m.group(1) == '49':
        c = c.replace('id="locationCount">49<', 'id="locationCount">48<')
        print('Fixed locationCount to 48')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(c)

print('Done - stats corrected')