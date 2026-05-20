# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Try the lite version with POST
url = "https://lite.duckduckgo.com/lite/"
data = {'q': '苏州旅游攻略 2026'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
}

response = requests.post(url, data=data, headers=headers, allow_redirects=True)
print(f"Status: {response.status_code}")
print(f"Content length: {len(response.text)}")

soup = BeautifulSoup(response.text, 'html.parser')

# Check for different result classes
result_classes = ['.result', '.result-link', '.links']
for cls in result_classes:
    found = soup.select(cls)
    print(f"Selector '{cls}': {len(found)} found")

# Print some of the HTML
print("\nFirst 1000 chars of HTML:")
print(response.text[:1000])
