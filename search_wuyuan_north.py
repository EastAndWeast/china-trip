# -*- coding: utf-8 -*-
import subprocess
import json
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

queries = [
    "婺源北线 思溪延村 彩虹桥 2026年4月",
    "婺源思溪延村 门票 开放时间",
    "婺源彩虹桥 门票 攻略",
    "婺源灵岩洞 门票 攻略",
    "武夷山旅游 2026年4月 现状"
]

proxy = "http://127.0.0.1:7890"
all_results = {}

for query in queries:
    ps_script = f'''
$proxy = "{proxy}"
$query = "{query}"
$encoded = [uri]::EscapeDataString($query)
$url = "https://html.duckduckgo.com/html/?q=" + $encoded
try {{
    $r = Invoke-WebRequest -Uri $url -Proxy $proxy -TimeoutSec 15 -UseBasicParsing
    $titles = [regex]::Matches($r.Content, '<a class="result__a"[^>]*>([^<]*)</a>') | ForEach-Object {{ $_.Groups[1].Value }} | Select-Object -First 5
    $titles -join "|"
}} catch {{
    "ERROR: " + $_.Exception.Message
}}
'''
    result = subprocess.run(
        ['powershell', '-ExecutionPolicy', 'Bypass', '-Command', ps_script],
        capture_output=True, text=True, encoding='utf-8'
    )
    output = result.stdout.strip()
    name = query.split()[0]
    print(f'=== {name}: {query} ===')
    if '|' in output:
        for item in output.split('|'):
            print(item)
    else:
        print(output)
    print()
    all_results[query] = output.split('|') if '|' in output else []

# Save
output_path = 'C:/Users/admin/.openclaw/workspace/china-trip/search_results_day57.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)
print(f'Saved to {output_path}')
