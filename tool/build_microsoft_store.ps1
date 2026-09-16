param(
    [Parameter(Mandatory = $false)][string]$PackageName,
    [Parameter(Mandatory = $false)][string]$Publisher,
    [string]$PublisherDisplayName = 'Marifat Software Team',
    [string]$Version = '3.1.0.0',
    [switch]$AllowPlaceholderIdentity,
    [string]$Flutter = 'D:\flutter\bin\flutter.bat'
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
if ($AllowPlaceholderIdentity) {
    if (-not $PackageName) { $PackageName = 'MarifatTeam.LearnByMarifat' }
    if (-not $Publisher) { $Publisher = 'CN=MarifatSoftwareTeam' }
} elseif (-not $PackageName -or -not $Publisher) {
    throw 'Provide the exact Package identity Name and Publisher from Partner Center. Use -AllowPlaceholderIdentity only for local validation.'
}
if ($Version -notmatch '^\d+\.\d+\.\d+\.\d+$') { throw 'MSIX version must contain four numeric parts, for example 3.1.0.0.' }

$makeAppx = Get-ChildItem 'C:\Program Files (x86)\Windows Kits\10\bin' -Recurse -Filter MakeAppx.exe |
    Where-Object { $_.FullName -match '\\x64\\MakeAppx\.exe$' } |
    Sort-Object FullName -Descending | Select-Object -First 1 -ExpandProperty FullName
if (-not $makeAppx) { throw 'MakeAppx.exe was not found. Install the Windows 10/11 SDK.' }

Push-Location $root
try {
    & $Flutter --no-version-check build windows --release --no-tree-shake-icons
    if ($LASTEXITCODE -ne 0) { throw 'Flutter Windows release build failed.' }
    $release = Join-Path $root 'build\windows\x64\runner\Release'
    $layout = Join-Path $root 'work\microsoft-store\layout'
    if (Test-Path -LiteralPath $layout) { Remove-Item -LiteralPath $layout -Recurse -Force }
    New-Item -ItemType Directory -Force -Path $layout | Out-Null
    Get-ChildItem -LiteralPath $release -Force | Where-Object { $_.Extension -ne '.pdb' } |
        Copy-Item -Destination $layout -Recurse -Force
    Copy-Item -LiteralPath (Join-Path $root 'distribution\microsoft-store\assets\package') -Destination (Join-Path $layout 'Assets') -Recurse -Force

    $manifest = Get-Content -LiteralPath (Join-Path $root 'distribution\microsoft-store\AppxManifest.template.xml') -Raw
    $manifest = $manifest.Replace('{{PACKAGE_NAME}}', [Security.SecurityElement]::Escape($PackageName))
    $manifest = $manifest.Replace('{{PUBLISHER}}', [Security.SecurityElement]::Escape($Publisher))
    $manifest = $manifest.Replace('{{PUBLISHER_DISPLAY_NAME}}', [Security.SecurityElement]::Escape($PublisherDisplayName))
    $manifest = $manifest.Replace('{{VERSION}}', $Version)
    Set-Content -LiteralPath (Join-Path $layout 'AppxManifest.xml') -Value $manifest -Encoding utf8NoBOM

    $outputDir = Join-Path $root 'outputs'
    New-Item -ItemType Directory -Force -Path $outputDir | Out-Null
    $suffix = if ($AllowPlaceholderIdentity) { '-placeholder-unsigned' } else { '-store' }
    $output = Join-Path $outputDir "learn-by-marifat-team-$Version-x64$suffix.msix"
    & $makeAppx pack /d $layout /p $output /o
    if ($LASTEXITCODE -ne 0) { throw 'MakeAppx packaging failed.' }
    Get-Item -LiteralPath $output
} finally {
    Pop-Location
}
