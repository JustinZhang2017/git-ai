#!/usr/bin/env bash
# Helper to install the pre-push hook into the repo's .git/hooks directory.
set -e
ROOT_DIR=$(dirname "$0")/..
ROOT_DIR=$(cd "$ROOT_DIR" && pwd)
HOOK_DEST="$ROOT_DIR/.git/hooks/pre-push"
cp "$ROOT_DIR/website/hooks/pre-push" "$HOOK_DEST"
chmod +x "$HOOK_DEST"
echo "Installed pre-push hook to $HOOK_DEST"
