param(
    [string]$Flutter = "D:\flutter\bin\flutter.bat",
    [switch]$AllowUnsigned
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$keyProperties = Join-Path $root "android\key.properties"
if (-not $AllowUnsigned -and -not (Test-Path -LiteralPath $keyProperties)) {
    throw "Missing android/key.properties. Copy android/key.properties.example, add the owner-controlled upload key details, and rerun. Use -AllowUnsigned only for local validation."
}

Push-Location $root
try {
    & $Flutter --no-version-check build appbundle --release --dart-define=STORE_BUILD=true --no-tree-shake-icons
    if ($LASTEXITCODE -ne 0) { throw "Flutter Android App Bundle build failed." }
    $bundle = Join-Path $root "build\app\outputs\bundle\release\app-release.aab"
    if (-not (Test-Path -LiteralPath $bundle)) { throw "Expected App Bundle was not created." }
    New-Item -ItemType Directory -Force (Join-Path $root "outputs") | Out-Null
    $outputName = if ($AllowUnsigned) {
        "learn-by-marifat-team-google-play-unsigned.aab"
    } else {
        "learn-by-marifat-team-google-play.aab"
    }
    $outputPath = Join-Path $root "outputs\$outputName"
    Copy-Item -LiteralPath $bundle -Destination $outputPath -Force
    Get-Item $outputPath
} finally {
    Pop-Location
}
