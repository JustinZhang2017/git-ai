from flask import Flask, request, jsonify
import os
import json
import time
from pathlib import Path

app = Flask(__name__)

RECEIVED_DIR = Path(__file__).resolve().parent / "received"
RECEIVED_DIR.mkdir(exist_ok=True)

@app.route("/api/push", methods=["POST"])
def receive_push():
    data = request.get_json(force=True, silent=True)
    if data is None:
        return jsonify({"error": "missing json body"}), 400

    ts = int(time.time() * 1000)
    fname = RECEIVED_DIR / f"push_{ts}.json"
    try:
        with open(fname, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        return jsonify({"error": "failed to save", "details": str(e)}), 500

    return jsonify({"status": "ok", "saved": str(fname)}), 200

if __name__ == "__main__":
    # Default port 8000
    port = int(os.environ.get("AI_WEB_PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
