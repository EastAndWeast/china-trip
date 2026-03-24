# -*- coding: utf-8 -*-
import subprocess
import sys

queries = [
    "杭州西湖旅游攻略 2026年3月",
    "苏州园林旅游攻略 2026年春季",
    "上海旅游攻略 2026年3月",
    "乌镇旅游攻略 2026年春季",
]

proxy = "http://127.0.0.1:7890"

for query in queries:
    ps_script = f'''
$proxy = "{proxy}"
$query = "{query}"
$encoded = [uri]::EscapeDataString($query)
$url = "https://html.duckduckgo.com/html/?q=" + $encoded
try {{
    $r = Invoke-WebRequest -Uri $url -Proxy $proxy -TimeoutSec 15 -UseBasicParsing
    $r.Content | Out-File -FilePath $env:TEMP\\ddg_result.html -Encoding UTF8
    Write-Host "=== {query} ==="
    Get-Content $env:TEMP\\ddg_result.html | Select-String -Pattern "result__a|result__snippet" | Select-Object -First 10
}} catch {{
    Write-Host "Error: $_"
}}
'''
    result = subprocess.run(['powershell', '-Command', ps_script], capture_output=True, text=True, encoding='utf-8')
    print(result.stdout)
    print(result.stderr)
