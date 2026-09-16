$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$root = Split-Path -Parent $PSScriptRoot
$output = Join-Path $root 'outputs\learn-by-marifat-team-microsoft-store-publication-kit.zip'
$files = @(
    'outputs/learn-by-marifat-team-3.1.0.0-x64-placeholder-unsigned.msix',
    'distribution/privacy-policy.html',
    'distribution/microsoft-store/AppxManifest.template.xml',
    'distribution/microsoft-store/STORE_LISTING.md',
    'distribution/microsoft-store/RELEASE_CHECKLIST.md',
    'tool/build_microsoft_store.ps1',
    'tool/test_microsoft_store.ps1'
)
$files += Get-ChildItem -LiteralPath (Join-Path $root 'distribution\microsoft-store\assets\package') -File |
    ForEach-Object { [IO.Path]::GetRelativePath($root, $_.FullName) }
$files += Get-ChildItem -LiteralPath (Join-Path $root 'distribution\microsoft-store\assets\screenshots') -File |
    Where-Object { $_.Name -match '^(home|courses)-(en|fa|ps)\.png$' } |
    ForEach-Object { [IO.Path]::GetRelativePath($root, $_.FullName) }
$stream = [IO.File]::Open($output, [IO.FileMode]::Create)
$archive = [IO.Compression.ZipArchive]::new($stream, [IO.Compression.ZipArchiveMode]::Create)
try {
    foreach ($relative in $files | Sort-Object -Unique) {
        $source = Join-Path $root $relative
        if (-not (Test-Path -LiteralPath $source -PathType Leaf)) { throw "Missing Microsoft Store file: $relative" }
        $entry = if ($relative.StartsWith('outputs/')) { Split-Path $relative -Leaf } else { $relative }
        [IO.Compression.ZipFileExtensions]::CreateEntryFromFile($archive, $source, $entry.Replace('\', '/')) | Out-Null
    }
} finally {
    $archive.Dispose()
    $stream.Dispose()
}
Get-Item -LiteralPath $output
