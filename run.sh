#!/bin/bash

set -e

source venv/bin/activate 2>/dev/null || true

python3 core/engine.py "$1"
