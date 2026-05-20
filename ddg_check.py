# -*- coding: utf-8 -*-
import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

url = 'https://html.duckduckgo.com/html/'
params = {'q': '南昌旅游攻略 2026'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

resp = requests.get(url, params=params, headers=headers)
print('Status:', resp.status_code)
print('Encoding:', resp.encoding)

with open('C:/Users/admin/.openclaw/workspace/china-trip/ddg_out.html', 'w', encoding='utf-8') as f:
    f.write(resp.text)
print('Written', len(resp.text), 'bytes')

# Look for patterns
text = resp.text
import re
patterns = ['result', 'Result', 'RESULT', 'class=']
for p in patterns:
    count = text.count(p)
    print(f'{p}: {count}')