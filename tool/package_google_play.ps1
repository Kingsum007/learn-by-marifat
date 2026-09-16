$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$root = Split-Path -Parent $PSScriptRoot
$output = Join-Path $root 'outputs\learn-by-marifat-team-google-play-publication-kit.zip'
$files = @(
    'outputs/learn-by-marifat-team-google-play-unsigned.aab',
    'distribution/privacy-policy.html',
    'distribution/google-play/DATA_SAFETY.md',
    'distribution/google-play/RELEASE_CHECKLIST.md',
    'distribution/google-play/STORE_LISTING.md',
    'distribution/google-play/assets/app-icon-512.png',
    'distribution/google-play/assets/feature-graphic-1024x500.png',
    'distribution/google-play/assets/phone-home-en.png',
    'distribution/google-play/assets/phone-courses-en.png',
    'distribution/google-play/assets/phone-courses-fa.png',
    'distribution/google-play/assets/phone-courses-ps.png',
    'docs/PRIVACY_POLICY.md',
    'android/key.properties.example',
    'tool/build_google_play.ps1'
)
$stream = [System.IO.File]::Open($output, [System.IO.FileMode]::Create)
$archive = [System.IO.Compression.ZipArchive]::new($stream, [System.IO.Compression.ZipArchiveMode]::Create)
try {
    foreach ($relative in $files) {
        $source = Join-Path $root $relative
        if (-not (Test-Path -LiteralPath $source -PathType Leaf)) { throw "Missing publication file: $relative" }
        $entry = if ($relative.StartsWith('outputs/')) { Split-Path $relative -Leaf } else { $relative }
        [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($archive, $source, $entry.Replace('\', '/')) | Out-Null
    }
} finally {
    $archive.Dispose()
    $stream.Dispose()
}
Get-Item -LiteralPath $output
