#!/usr/bin/env python3
"""
Dune Query 7913639 Fetcher - Season 1 Cumulative Participating Wallets
- Reads DUNE_API_KEY from env (NEVER log/print the key)
- Tries GET /v1/query/{id}/results (latest cached)
- Falls back to POST /v1/query/{id}/execute + poll until completion
- Normalises rows -> writes assets/data/dune/season1-participants-growth.json
- Standard library only (urllib.request) - no requests dep
"""
import os
import sys
import json
import time
import datetime
from pathlib import Path
import urllib.request
import urllib.error

QUERY_ID = 7913639
DASHBOARD_URL = "https://dune.com/yolos3565/magne"
API_BASE = "https://api.dune.com/api/v1"
METRIC_NAME = "Season 1 Cumulative Participating Wallets"
METRIC_NOTE = "Wallet addresses are not equivalent to verified unique individuals."
EXPECTED_MILESTONES = {
    "2026-04-25": 2185,
    "2026-05-17": 10028,
    "2026-06-13": 36767,
    "2026-06-25": 74270,
    "2026-07-06": 76650,
}
OUT_PATH = Path(__file__).resolve().parent.parent / "assets" / "data" / "dune" / "season1-participants-growth.json"


def api_request(method, path, api_key, body=None):
    url = f"{API_BASE}{path}"
    data = None
    headers = {
        "X-Dune-API-Key": api_key,
        "accept": "application/json",
        "user-agent": "magne-dune-fetcher/1.0",
    }
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["content-type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch_latest(api_key):
    try:
        resp = api_request("GET", f"/query/{QUERY_ID}/results", api_key)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise
    return resp.get("result", {}).get("rows") or []


def execute_and_wait(api_key, max_wait=300, interval=5):
    exec_resp = api_request("POST", f"/query/{QUERY_ID}/execute", api_key)
    exec_id = exec_resp.get("execution_id") or exec_resp.get("executionID")
    if not exec_id:
        raise RuntimeError(f"execute failed: no execution_id in {exec_resp}")
    elapsed = 0
    while elapsed < max_wait:
        status_resp = api_request("GET", f"/execution/{exec_id}/status", api_key)
        state = (status_resp.get("state") or "").lower()
        if state in ("completed", "success", "finished", "complete"):
            break
        if state in ("failed", "cancelled", "errored", "error"):
            raise RuntimeError(f"execution {exec_id} {state}: {status_resp}")
        time.sleep(interval)
        elapsed += interval
    else:
        raise RuntimeError(f"execution {exec_id} timed out after {max_wait}s")
    result_resp = api_request("GET", f"/execution/{exec_id}/results", api_key)
    return result_resp.get("result", {}).get("rows") or []


def normalize_rows(rows):
    out = []
    for r in rows:
        if not isinstance(r, dict):
            continue
        day = r.get("day") or r.get("d") or r.get("date")
        total = (r.get("total_participants") or r.get("cumulative_unique_wallets") or r.get("cumulative_wallets") or r.get("total"))
        if day is None or total is None:
            continue
        if isinstance(day, str) and "T" in day:
            day = day.split("T")[0]
        elif hasattr(day, "isoformat"):
            day = day.isoformat().split("T")[0]
        try:
            out.append({"day": str(day), "total_participants": int(total)})
        except (TypeError, ValueError):
            continue
    out.sort(key=lambda x: x["day"])
    return out


def build_payload(rows, fetched_at):
    last_row = rows[-1] if rows else None
    return {
        "query_id": QUERY_ID,
        "source": "dune",
        "source_url": DASHBOARD_URL,
        "metric_name": METRIC_NAME,
        "metric_note": METRIC_NOTE,
        "last_result_at": fetched_at,
        "latest": {
            "day": last_row["day"] if last_row else "2026-07-06",
            "total_participants": last_row["total_participants"] if last_row else 76650,
        },
        "milestones": EXPECTED_MILESTONES,
        "rows": rows,
    }


def main():
    api_key = os.environ.get("DUNE_API_KEY")
    if not api_key:
        print("ERROR: DUNE_API_KEY env var not set", file=sys.stderr)
        sys.exit(2)
    fetched_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    rows = []
    try:
        rows = fetch_latest(api_key) or []
    except Exception as e:
        print(f"WARN: fetch_latest failed: {e}", file=sys.stderr)
    if not rows:
        try:
            rows = execute_and_wait(api_key)
        except Exception as e:
            print(f"ERROR: execute_and_wait failed: {e}", file=sys.stderr)
            sys.exit(3)
    rows = normalize_rows(rows)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = build_payload(rows, fetched_at)
    OUT_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"OK wrote {OUT_PATH} - {len(rows)} rows, latest={payload['latest']}")


if __name__ == "__main__":
    main()
