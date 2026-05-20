# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

url = "https://html.duckduckgo.com/html/"
params = {'q': '苏州旅游攻略 2026'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'https://duckduckgo.com/',
}

session = requests.Session()
response = session.get(url, params=params, headers=headers, allow_redirects=True)
print(f"Status: {response.status_code}")
print(f"Final URL: {response.url}")
print(f"Content length: {len(response.text)}")

soup = BeautifulSoup(response.text, 'html.parser')

# Check for different result classes
result_classes = ['.result', '.result__a', '.results__result']
for cls in result_classes:
    found = soup.select(cls)
    print(f"Selector '{cls}': {len(found)} found")

# Try to find all links
links = soup.find_all('a')
print(f"\nTotal links: {len(links)}")

# Print first few links
for i, link in enumerate(links[:10]):
    href = link.get('href', '')
    text = link.get_text(strip=True)[:50]
    if href:
        print(f"Link {i+1}: {text} -> {href}")
