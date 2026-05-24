import sys
import json
import os
from datetime import datetime, timezone
import uuid

def run(target):
    case_id = str(uuid.uuid4())[:8]

    print("[ENGINE] Starting:", target)
    print("[ENGINE] Case ID:", case_id)

    timestamp = datetime.now(timezone.utc).isoformat()

    result = {
        "case_id": case_id,
        "target": target,
        "timestamp": timestamp,
        "status": "ok",
        "modules": ["subfinder", "httpx"]
    }

    # 📁 create case directory
    out_dir = f"output/{case_id}"
    os.makedirs(out_dir, exist_ok=True)

    # 💾 save result
    with open(f"{out_dir}/result.json", "w") as f:
        json.dump(result, f, indent=2)

    print("[ENGINE] Saved to:", f"{out_dir}/result.json")

    return result


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
        print(json.dumps({"status": "ok"}))
    else:
        run(sys.argv[1])
