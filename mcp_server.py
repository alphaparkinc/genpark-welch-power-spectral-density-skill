import sys
import json
from client import WelchPSDEngine

def main():
    welch = WelchPSDEngine()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "estimate_psd":
            p = welch.estimate_psd(params.get("signal", []), params.get("segment_len", 16), params.get("overlap", 8))
            res = {"psd": p}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
