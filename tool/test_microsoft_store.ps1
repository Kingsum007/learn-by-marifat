param([Parameter(Mandatory = $true)][string]$PackagePath)

$ErrorActionPreference = 'Stop'
$package = (Resolve-Path -LiteralPath $PackagePath).Path
$kit = 'C:\Program Files (x86)\Windows Kits\10\App Certification Kit\appcert.exe'
if (-not (Test-Path -LiteralPath $kit)) { throw 'Windows App Certification Kit is not installed.' }
$root = Split-Path -Parent $PSScriptRoot
$report = Join-Path $root 'outputs\microsoft-store-wack-report.xml'
& $kit reset
if ($LASTEXITCODE -ne 0) { throw 'WACK reset failed. Run this script from an Administrator PowerShell in an active desktop session.' }
& $kit test -appxpackagepath $package -reportoutputpath $report
if ($LASTEXITCODE -ne 0) { throw "WACK failed. Review $report" }
Get-Item -LiteralPath $report
