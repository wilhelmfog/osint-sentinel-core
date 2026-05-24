#!/bin/bash

set -e

if [ ! -d "venv" ]; then
    echo "[!] venv not found. Run ./bootstrap.sh first"
    exit 1
fi

source venv/bin/activate

TARGET=$1

if [ -z "$TARGET" ]; then
    echo "Usage: ./run.sh example.com"
    exit 1
fi

echo "[ENGINE] Starting: $TARGET"

python3 core/engine.py "$TARGET"
