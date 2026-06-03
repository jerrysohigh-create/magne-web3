#!/usr/bin/env bash
# copy-to-workspace.sh — Copy screenshots to workspace for image tool analysis
#
# Usage:
#   ./copy-to-workspace.sh /path/to/magne-web3
#   ./copy-to-workspace.sh /path/to/magne-web3 ecosystem token
#
# If no slugs given, copies all subdirectories under /tmp/magne-responsive-screenshots/
# Destination: <repo>/.tmp-screens/<slug>/<file>

set -euo pipefail

REPO="${1:-}"
DEST_BASE=".tmp-screens"

if [[ -z "$REPO" ]]; then
  echo "Usage: $0 <repo-path> [slug [slug ...]]" >&2
  echo "  e.g.: $0 /home/user/magne-web3 token ecosystem" >&2
  exit 1
fi

if [[ ! -d "$REPO" ]]; then
  echo "ERROR: $REPO is not a directory" >&2
  exit 1
fi

SRC_BASE="/tmp/magne-responsive-screenshots"

if [[ ! -d "$SRC_BASE" ]]; then
  echo "ERROR: $SRC_BASE does not exist (run viewport-check.sh first)" >&2
  exit 1
fi

SLUGS=("${@:2}")
if [[ ${#SLUGS[@]} -eq 0 ]]; then
  # No slugs given — copy all
  mapfile -t SLUGS < <(ls "$SRC_BASE" 2>/dev/null)
fi

DEST_DIR="$REPO/$DEST_BASE"
mkdir -p "$DEST_DIR"

COPIED=0
for slug in "${SLUGS[@]}"; do
  SRC_SLUG="$SRC_BASE/$slug"
  if [[ ! -d "$SRC_SLUG" ]]; then
    echo "WARNING: $SRC_SLUG does not exist, skipping" >&2
    continue
  fi
  DST_SLUG="$DEST_DIR/$slug"
  mkdir -p "$DST_SLUG"
  cp -f "$SRC_SLUG"/*.png "$DST_SLUG/" 2>/dev/null || true
  COUNT=$(find "$DST_SLUG" -name "*.png" | wc -l)
  echo "Copied $COUNT screenshots: $slug → $DST_SLUG/"
  COPIED=$((COPIED + COUNT))
done

echo ""
echo "Done. $COPIED screenshot(s) copied to $DEST_DIR/"
echo "Load them with the image tool for visual validation."
