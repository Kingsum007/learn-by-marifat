# Run from the Learn By Marifat Team project directory after flutter pub get if Windows prevents
# symlink creation. Directory junctions are local to this project's build area.
$ErrorActionPreference = 'Stop'
$taskProject = (Get-Location).Path
if (-not (Test-Path -LiteralPath (Join-Path $taskProject 'pubspec.yaml'))) { throw 'Run this from the Learn By Marifat Team project directory.' }
$taskMetadata = Get-Content -LiteralPath (Join-Path $taskProject '.flutter-plugins-dependencies') -Raw | ConvertFrom-Json
$taskLinks = Join-Path $taskProject 'windows/flutter/ephemeral/.plugin_symlinks'
New-Item -ItemType Directory -Path $taskLinks -Force | Out-Null
foreach ($taskPlugin in $taskMetadata.plugins.windows) {
    if ($taskPlugin.name -notmatch '^[a-zA-Z0-9_]+$') { throw 'Invalid plugin name.' }
    $taskLink = Join-Path $taskLinks $taskPlugin.name
    if (-not (Test-Path -LiteralPath $taskLink)) {
        New-Item -ItemType Junction -Path $taskLink -Target $taskPlugin.path | Out-Null
    }
}
Write-Output 'Project-local plugin junctions are ready.'
