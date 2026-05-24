#!/bin/bash

set -e

echo "[+] OSINT Sentinel Bootstrap"

apt update
apt install -y python3 python3-venv python3-pip git

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

echo "[+] Bootstrap complete"
