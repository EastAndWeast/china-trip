# -*- coding: utf-8 -*-
import base64, json, re, sys, os
from datetime import datetime
import urllib.request, urllib.parse

sys.stdout.reconfigure(encoding='utf-8')

WP_URL = "https://www.tianao1128.online"
WP_USERNAME = "tianao1128"
WP_APP_PASSWORD = "qEMA oYHb otL5 1SHP IVeJ clIG"
WP_CATEGORY = "环游中国"

def wp_auth():
    credentials = f"{WP_USERNAME}:{WP_APP_PASSWORD}".replace(" ", "")
    token = base64.b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {token}"}

def test_connection():
    import requests
    url = f"{WP_URL}/wp-json/wp/v2/users/me"
    resp = requests.get(url, headers=wp_auth())
    if resp.status_code == 200:
        print(f"WP连接成功: {resp.json().get('name')}")
        return True
    print(f"WP连接失败: {resp.status_code}")
    return False

def get_recent_posts(days=3):
    import requests
    url = f"{WP_URL}/wp-json/wp/v2/posts?per_page=10&status=publish"
    resp = requests.get(url, headers=wp_auth())
    if resp.status_code == 200:
        posts = resp.json()
        print(f"最近 {len(posts)} 篇发布:")
        for p in posts[:5]:
            print(f"  [{p.get('date','')[:10]}] {p.get('title',{}).get('rendered','')[:50]} (ID:{p['id']})")
        return posts
    return []

def get_or_create_category(name):
    import requests
    url = f"{WP_URL}/wp-json/wp/v2/categories?per_page=100"
    resp = requests.get(url, headers=wp_auth())
    if resp.status_code == 200:
        categories = {c["name"]: c["id"] for c in resp.json()}
        if name in categories:
            return categories[name]
    url = f"{WP_URL}/wp-json/wp/v2/categories"
    resp = requests.post(url, headers=wp_auth(), json={"name": name})
    if resp.status_code in (200, 201):
        return resp.json()["id"]
    return 0

def publish_article(title, content, date, category_id):
    import requests
    url = f"{WP_URL}/wp-json/wp/v2/posts"
    payload = {
        "title": title,
        "content": content,
        "status": "publish",
        "date": f"{date}T06:00:00",
        "categories": [category_id] if category_id else [],
    }
    resp = requests.post(url, headers=wp_auth(), json=payload)
    if resp.status_code in (200, 201):
        post = resp.json()
        print(f"发布成功: {title} (ID: {post['id']})")
        return post["id"]
    print(f"发布失败: {resp.status_code} - {resp.text[:200]}")
    return None

HTML_PATH = 'C:/Users/admin/.openclaw/workspace/china-trip/index.html'

print(f"\n{'='*50}")
print(f"环游中国 - WordPress发布")
print(f"{'='*50}")

if not test_connection():
    sys.exit(1)

recent = get_recent_posts()
print()

# Check if Day 81 already published
today_str = "2026-05-09"
for p in recent:
    title = p.get('title',{}).get('rendered','')
    if 'Day81' in title or '第81天' in title or '81' in title:
        print(f"Day 81 already published: {title}")
        already = True
        break
else:
    already = False

# Read HTML content
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Find Day 81 content
day81_pattern = r'<div class="day-card">(.*?)<div class="day-card">'
matches = re.findall(day81_pattern, html_content, re.DOTALL)
print(f"Found {len(matches)} day cards")

# Find latest day
date_pattern = r'<span class="day-number">第(\d+)天</span>.*?<span class="day-date">(\d{4}-\d{2}-\d{2})</span>'
day_matches = re.findall(date_pattern, html_content, re.DOTALL)
if day_matches:
    latest = day_matches[-1]
    print(f"Latest day in HTML: Day {latest[0]} - {latest[1]}")
else:
    print("Could not find day info")
    sys.exit(1)

# Extract Day 81 content specifically
day81_marker = r'<div class="day-header">\s*<span class="day-number">第81天</span>'
start_match = re.search(day81_marker, html_content)
if start_match:
    start = start_match.start()
    # Find next day-header
    next_marker = re.search(r'<div class="day-header">\s*<span class="day-number">第\d+天</span>', html_content[start+10:])
    if next_marker:
        day81_content = html_content[start:start+next_marker.start()]
    else:
        day81_content = html_content[start:start+6000]
    
    # Clean HTML to text
    text = day81_content
    text = re.sub(r'<h3>', '\n## ', text)
    text = re.sub(r'</h3>', '\n', text)
    text = re.sub(r'<p>', '\n', text)
    text = re.sub(r'</p>', '\n', text)
    text = re.sub(r'<br\s*/?>','\n', text)
    text = re.sub(r'<div class="tips">.*?</div>', '', text, flags=re.DOTALL)
    text = re.sub(r'<div class="photos">.*?</div>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = text.strip()
    
    print(f"\nDay 81 content preview:\n{text[:300]}...")
    
    if not already:
        category_id = get_or_create_category(WP_CATEGORY)
        title = f"环游中国 Day81 | 2026-05-09 | 长沙 → 南昌 · 赣江之夜"
        post_id = publish_article(title, text, "2026-05-09", category_id)
        if post_id:
            print(f"\n✅ Published: {WP_URL}/?p={post_id}")
    else:
        print("Skipping publish (already exists)")
else:
    print("Day 81 not found in HTML")