#!/usr/bin/env bash
# viewport-check.sh — MAGNE.AI Web3 Portal responsive screenshot tool
#
# Usage:
#   ./viewport-check.sh <url> <slug>
#   Example: ./viewport-check.sh http://127.0.0.1:4174/token.html token
#
# Viewports: 1440 1320 1280 1024 900 768 430 375 360
# Output:    /tmp/magne-responsive-screenshots/<slug>-<width>px.png

set -euo pipefail

# ── CLI args ────────────────────────────────────────────────────────────────
if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <url> <slug>" >&2
  echo "  <url>  — full URL or path, e.g. http://127.0.0.1:4174/token.html" >&2
  echo "  <slug> — output name prefix, e.g. token" >&2
  exit 1
fi

URL="$1"
SLUG="$2"
VIEWPORTS=(1440 1320 1280 1024 900 768 430 375 360)
OUTPUT_DIR="/tmp/magne-responsive-screenshots/${SLUG}"
TIMEOUT_MS=30000

# ── Resolve Chrome binary ────────────────────────────────────────────────────
find_chrome() {
  for bin in google-chrome chromium-browser chromium chrome; do
    if command -v "$bin" &>/dev/null; then
      echo "$bin"
      return 0
    fi
  done
  return 1
}

CHROME=$(find_chrome) || {
  echo "ERROR: Neither google-chrome nor chromium found in PATH." >&2
  echo "Please install Google Chrome or Chromium and ensure it is in your PATH." >&2
  exit 1
}

echo "Using Chrome binary: $CHROME"

# ── Prepare output dir ───────────────────────────────────────────────────────
mkdir -p "$OUTPUT_DIR"
echo "Output directory: $OUTPUT_DIR"

# ── Capture screenshots ──────────────────────────────────────────────────────
for W in "${VIEWPORTS[@]}"; do
  OUT="$OUTPUT_DIR/${SLUG}-${W}px.png"
  echo -n "Capturing ${W}px... "

  "$CHROME" \
    --headless \
    --no-sandbox \
    --disable-setuid-sandbox \
    --disable-dev-shm-usage \
    --window-size="$W,3000" \
    --screenshot="$OUT" \
    --timeout="$TIMEOUT_MS" \
    --wait-for-navigation load \
    "$URL" \
    &>/dev/null

  if [[ -f "$OUT" ]]; then
    SIZE=$(identify -format "%wx%h" "$OUT" 2>/dev/null || echo "unknown")
    echo "✅ → ${OUT} (${SIZE})"
  else
    echo "❌ FAILED (no output file)"
  fi
done

# ── Summary ──────────────────────────────────────────────────────────────────
COUNT=$(find "$OUTPUT_DIR" -name "*.png" | wc -l)
echo ""
echo "Done. $COUNT / ${#VIEWPORTS[@]} screenshots captured."
echo "Output dir: $OUTPUT_DIR"
echo ""
echo "Paths:"
find "$OUTPUT_DIR" -name "*.png" -printf "  %f\n"
