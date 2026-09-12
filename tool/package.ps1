# Package the current source and an already-built Windows release.
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$taskRoot = (Get-Location).Path
if (-not (Test-Path -LiteralPath (Join-Path $taskRoot 'pubspec.yaml'))) { throw 'Run from the Learn By Marifat Team project directory.' }
$taskOutput = Join-Path $taskRoot 'outputs'
New-Item -ItemType Directory -Path $taskOutput -Force | Out-Null

function Write-TaskArchive($archivePath, $basePath, $relativeFiles) {
    $taskStream = [System.IO.File]::Open($archivePath, [System.IO.FileMode]::Create)
    $taskArchive = [System.IO.Compression.ZipArchive]::new($taskStream, [System.IO.Compression.ZipArchiveMode]::Create)
    try {
        foreach ($relative in $relativeFiles) {
            $taskFile = [System.IO.Path]::GetFullPath((Join-Path $basePath $relative))
            if (-not $taskFile.StartsWith($basePath + [System.IO.Path]::DirectorySeparatorChar, [System.StringComparison]::OrdinalIgnoreCase)) { throw 'File is outside package root.' }
            [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($taskArchive, $taskFile, $relative.Replace('\', '/')) | Out-Null
        }
    } finally { $taskArchive.Dispose(); $taskStream.Dispose() }
}

$taskSources = @(git ls-files --cached --others --exclude-standard) + @('android/gradlew', 'android/gradlew.bat', 'android/gradle/wrapper/gradle-wrapper.jar')
$taskSources = $taskSources | Sort-Object -Unique | Where-Object { Test-Path -LiteralPath (Join-Path $taskRoot $_) -PathType Leaf }
Write-TaskArchive (Join-Path $taskOutput 'learn-by-marifat-team-source.zip') $taskRoot $taskSources
$taskRelease = Join-Path $taskRoot 'build/windows/x64/runner/Release'
if (Test-Path -LiteralPath (Join-Path $taskRelease 'learn_by_marifat_team.exe')) {
    $taskBinaries = Get-ChildItem -LiteralPath $taskRelease -Recurse -File | Where-Object { $_.Extension -ne '.exe' -or $_.Name -eq 'learn_by_marifat_team.exe' } | ForEach-Object { [System.IO.Path]::GetRelativePath($taskRelease, $_.FullName) }
    Write-TaskArchive (Join-Path $taskOutput 'learn-by-marifat-team-windows.zip') $taskRelease $taskBinaries
}
Get-ChildItem -LiteralPath $taskOutput -Filter '*.zip' | Select-Object Name,Length
