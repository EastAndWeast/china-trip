# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

query = '福州三坊七巷旅游攻略'
encoded = urllib.parse.quote(query)

# Try Bing HTML
url = f'https://www.bing.com/search?q={encoded}'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
})
try:
    resp = urllib.request.urlopen(req, timeout=10)
    html = resp.read().decode('utf-8', errors='replace')
    titles = re.findall(r'<h2[^>]*><a[^>]*href=[^>]*>([^<]+)</a>', html)
    print('Bing titles:', titles[:5])
    snippets = re.findall(r'b_paractl', html)
    print('Has b_paractl:', len(snippets))
    # Try another pattern
    titles2 = re.findall(r'<a[^>]*href=["\']https?://[^"\']*["\'][^>]*>([^<]+)<', html)
    print('Titles2:', titles2[:5])
    print('HTML length:', len(html))
except Exception as e:
    print('Error:', e)

print()

# Try Baidu
url2 = f'https://www.baidu.com/s?wd={urllib.parse.quote("福州三坊七巷旅游攻略")}'
req2 = urllib.request.Request(url2, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
})
try:
    resp2 = urllib.request.urlopen(req2, timeout=10)
    html2 = resp2.read().decode('utf-8', errors='replace')
    print('Baidu HTML length:', len(html2))
    # Try to find result titles
    titles3 = re.findall(r'class="t".*?<a[^>]*>([^<]+)</a>', html2, re.DOTALL)
    print('Baidu titles:', titles3[:5])
except Exception as e:
    print('Baidu Error:', e)
