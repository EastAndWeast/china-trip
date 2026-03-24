# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

queries = [
    '塔川古村',
    '齐云山风景区',
    '黄山周边景点'
]

all_results = {}

for query in queries:
    encoded_query = urllib.parse.quote(query)
    url = 'https://html.duckduckgo.com/html/?q=' + encoded_query
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    try:
        response = urllib.request.urlopen(req, timeout=10)
        html = response.read().decode('utf-8')
        # Find result titles
        pattern = r'<a class="result__a"[^>]*>([^<]*)</a>'
        results = re.findall(pattern, html)
        print('=== ' + query + ' ===')
        if results:
            for i, r in enumerate(results[:5]):
                print(str(i+1) + '. ' + r)
        else:
            print('No results found')
            # Check if there's any content
            snippet_pattern = r'<a class="result__snippet"[^>]*>([^<]*)</a>'
            snippets = re.findall(snippet_pattern, html)
            for i, s in enumerate(snippets[:3]):
                print('Snippet: ' + s[:80])
        print()
        all_results[query] = results[:5]
    except Exception as e:
        print('Error: ' + str(e))
        all_results[query] = []

# Save
output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print('Results saved')
