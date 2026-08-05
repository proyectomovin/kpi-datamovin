param(
  [string]$RepositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

Add-Type -AssemblyName System.Drawing

function New-RoundedRectanglePath {
  param(
    [System.Drawing.RectangleF]$Bounds,
    [float]$Radius
  )

  $diameter = $Radius * 2
  $path = [System.Drawing.Drawing2D.GraphicsPath]::new()
  $path.AddArc($Bounds.X, $Bounds.Y, $diameter, $diameter, 180, 90)
  $path.AddArc($Bounds.Right - $diameter, $Bounds.Y, $diameter, $diameter, 270, 90)
  $path.AddArc($Bounds.Right - $diameter, $Bounds.Bottom - $diameter, $diameter, $diameter, 0, 90)
  $path.AddArc($Bounds.X, $Bounds.Bottom - $diameter, $diameter, $diameter, 90, 90)
  $path.CloseFigure()
  return $path
}

function New-DataMovinIcon {
  param(
    [string]$Path,
    [int]$Size
  )

  $directory = Split-Path -Parent $Path
  if (-not (Test-Path -LiteralPath $directory)) {
    New-Item -ItemType Directory -Path $directory -Force | Out-Null
  }

  $bitmap = [System.Drawing.Bitmap]::new($Size, $Size)
  $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
  $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
  $graphics.Clear([System.Drawing.Color]::Transparent)

  $padding = [Math]::Max(1, [Math]::Round($Size * 0.04))
  $bounds = [System.Drawing.RectangleF]::new($padding, $padding, $Size - (2 * $padding), $Size - (2 * $padding))
  $radius = [Math]::Max(2, $Size * 0.22)
  $rounded = New-RoundedRectanglePath -Bounds $bounds -Radius $radius
  $orange = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml('#FF6D4D'))
  $graphics.FillPath($orange, $rounded)

  $triangle = [System.Drawing.PointF[]]@(
    [System.Drawing.PointF]::new($Size * 0.50, $Size * 0.22),
    [System.Drawing.PointF]::new($Size * 0.79, $Size * 0.76),
    [System.Drawing.PointF]::new($Size * 0.21, $Size * 0.76)
  )
  $white = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::White)
  $graphics.FillPolygon($white, $triangle)

  $bitmap.Save($Path, [System.Drawing.Imaging.ImageFormat]::Png)
  $white.Dispose()
  $orange.Dispose()
  $rounded.Dispose()
  $graphics.Dispose()
  $bitmap.Dispose()
}

$staticRoot = Join-Path $RepositoryRoot 'static'
$openRosaRoot = Join-Path $RepositoryRoot 'kobo\apps\openrosa\apps\main\static\kobocat\images'

$targets = @{
  (Join-Path $staticRoot 'datamovin-favicon.png') = 64
  (Join-Path $staticRoot 'datamovin-apple-touch-icon.png') = 180
  (Join-Path $staticRoot 'datamovin-android-192x192.png') = 192
  (Join-Path $staticRoot 'datamovin-android-256x256.png') = 256
  (Join-Path $openRosaRoot 'datamovin-favicon-16x16.png') = 16
  (Join-Path $openRosaRoot 'datamovin-favicon-32x32.png') = 32
  (Join-Path $openRosaRoot 'datamovin-favicon-96x96.png') = 96
  (Join-Path $openRosaRoot 'datamovin-android-36x36.png') = 36
  (Join-Path $openRosaRoot 'datamovin-android-48x48.png') = 48
  (Join-Path $openRosaRoot 'datamovin-android-72x72.png') = 72
  (Join-Path $openRosaRoot 'datamovin-android-96x96.png') = 96
  (Join-Path $openRosaRoot 'datamovin-android-144x144.png') = 144
  (Join-Path $openRosaRoot 'datamovin-android-192x192.png') = 192
  (Join-Path $openRosaRoot 'datamovin-apple-57x57.png') = 57
  (Join-Path $openRosaRoot 'datamovin-apple-60x60.png') = 60
  (Join-Path $openRosaRoot 'datamovin-apple-72x72.png') = 72
  (Join-Path $openRosaRoot 'datamovin-apple-76x76.png') = 76
  (Join-Path $openRosaRoot 'datamovin-apple-114x114.png') = 114
  (Join-Path $openRosaRoot 'datamovin-apple-120x120.png') = 120
  (Join-Path $openRosaRoot 'datamovin-apple-144x144.png') = 144
  (Join-Path $openRosaRoot 'datamovin-apple-152x152.png') = 152
  (Join-Path $openRosaRoot 'datamovin-apple-180x180.png') = 180
  (Join-Path $openRosaRoot 'datamovin-ms-70x70.png') = 70
  (Join-Path $openRosaRoot 'datamovin-ms-144x144.png') = 144
  (Join-Path $openRosaRoot 'datamovin-ms-150x150.png') = 150
  (Join-Path $openRosaRoot 'datamovin-ms-310x310.png') = 310
}

foreach ($target in $targets.GetEnumerator()) {
  New-DataMovinIcon -Path $target.Key -Size $target.Value
}

Write-Host "Generated $($targets.Count) DataMovin icons."
