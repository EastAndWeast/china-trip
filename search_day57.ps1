$proxy = "http://127.0.0.1:7890"
$queries = @(
    "婺源北线 思溪延村 彩虹桥 2026年4月",
    "婺源思溪延村 门票 开放时间",
    "婺源彩虹桥 门票 攻略",
    "婺源灵岩洞 门票 攻略",
    "武夷山旅游 2026年4月 现状"
)

$allResults = @{}

foreach ($query in $queries) {
    $encoded = [uri]::EscapeDataString($query)
    $url = "https://html.duckduckgo.com/html/?q=" + $encoded
    try {
        $r = Invoke-WebRequest -Uri $url -Proxy $proxy -TimeoutSec 15 -UseBasicParsing
        # Extract titles
        $titles = [regex]::Matches($r.Content, '<a class="result__a"[^>]*>([^<]*)</a>') | ForEach-Object { $_.Groups[1].Value } | Select-Object -First 5
        $name = ($query -split ' ')[0]
        Write-Host "=== $name ==="
        $titles | ForEach-Object { Write-Host $_ }
        Write-Host ""
        $allResults[$query] = $titles
    } catch {
        Write-Host "Error for $query : $_"
        $allResults[$query] = @()
    }
}

# Save to JSON
$json = $allResults | ConvertTo-Json -Depth 10
$json | Out-File -FilePath "C:\Users\admin\.openclaw\workspace\china-trip\search_results_day57.json" -Encoding UTF8
Write-Host "Saved to search_results_day57.json"
