$proxy = "http://127.0.0.1:7890"
$queries = @(
    "苏州园林 春季旅游 2026年3月 最新攻略",
    "苏州 拙政园 留园 虎丘 2026 门票 开放时间",
    "杭州到苏州 高铁 自驾 2026年3月"
)

foreach ($query in $queries) {
    $encoded = [uri]::EscapeDataString($query)
    $url = "https://lite.duckduckgo.com/lite/?q=" + $encoded
    try {
        $r = Invoke-WebRequest -Uri $url -Proxy $proxy -TimeoutSec 15 -UseBasicParsing
        $r.Content | Out-File -FilePath $env:TEMP\ddg_result.html -Encoding UTF8
        Write-Host "=== $query ==="
        Get-Content $env:TEMP\ddg_result.html | Select-String -Pattern "result__a" | Select-Object -First 5
    } catch {
        Write-Host "Error: $_"
    }
    Write-Host ""
}
