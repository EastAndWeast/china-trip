$proxy = "http://127.0.0.1:7890"
$queries = @(
    "杭州西湖旅游攻略 2026年3月",
    "苏州园林旅游攻略 2026年春季",
    "上海旅游攻略 2026年3月"
)

foreach ($query in $queries) {
    $encoded = [uri]::EscapeDataString($query)
    $url = "https://lite.duckduckgo.com/lite/?q=" + $encoded
    try {
        $r = Invoke-WebRequest -Uri $url -Proxy $proxy -TimeoutSec 15 -UseBasicParsing
        Write-Host "=== $query ==="
        # Extract result titles
        $r.Content -split "`n" | Where-Object { $_ -match "result__a" } | Select-Object -First 5 | ForEach-Object {
            if ($_ -match '>([^<]+)<') {
                Write-Host $Matches[1]
            }
        }
        Write-Host ""
    } catch {
        Write-Host "Error for $query : $_"
    }
}
