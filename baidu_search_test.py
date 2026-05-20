# -*- coding: utf-8 -*-
import sys
import json
import os
sys.stdout.reconfigure(encoding='utf-8')

api_key = os.getenv("BAIDU_API_KEY")
if not api_key:
    print("Error: BAIDU_API_KEY must be set in environment.")
    sys.exit(1)

request_body = {
    "messages": [{"content": "南昌旅游攻略 2026年5月 滕王阁 八一广场", "role": "user"}],
    "edition": "standard",
    "search_source": "baidu_search_v2",
    "resource_type_filter": [{"type": "web", "top_k": 5}],
    "search_recency_filter": "year",
}

import requests
url = "https://qianfan.baidubce.com/v2/ai_search/web_search"
headers = {
    "Authorization": "Bearer %s" % api_key,
    "X-Appbuilder-From": "openclaw",
    "Content-Type": "application/json"
}
try:
    resp = requests.post(url, json=request_body, headers=headers)
    resp.raise_for_status()
    results = resp.json()
    if "code" in results:
        print("Error:", results["message"])
    else:
        for item in results.get("references", []):
            title = item.get("title", "")
            url_link = item.get("url", "")
            print(f"- {title}: {url_link}")
except Exception as e:
    print("Error:", e)