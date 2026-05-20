# -*- coding: utf-8 -*-
"""Search for upcoming destinations"""
import json
import sys
import codecs
import subprocess

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

script = 'C:/Users/admin/.openclaw/workspace/skills/duckduckgo-search/scripts/search.py'

destinations = [
    '杭州西湖旅游攻略 2026年3月 春季',
    '上海旅游攻略 2026年3月',
    '乌镇旅游攻略 2026年春季',
    '黄山宏村西递旅游攻略 2026年3月',
]

all_results = {}

for query in destinations:
    try:
        result = subprocess.run(
            ['python', script, query],
            capture_output=True,
            text=True,
            timeout=30,
            encoding='utf-8'
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            titles = [r['title'] for r in data.get('results', [])]
            print(f'=== {query} ===')
            for i, t in enumerate(titles[:5]):
                print(f'{i+1}. {t}')
            print()
            all_results[query] = titles
        else:
            print(f'Error: {result.stderr}')
            all_results[query] = []
    except Exception as e:
        print(f'Exception for {query}: {e}')
        all_results[query] = []

# Save with updated timestamp
all_results['updated'] = '2026-03-30'

output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_latest.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print(f'\nSaved results to {output_path}')
