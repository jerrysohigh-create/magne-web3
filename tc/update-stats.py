#!/usr/bin/env python3
"""
Live on-chain snapshot fetcher for MAGNE.AI Session 1 金池 (Track B).

Jerry can rerun this script weekly/monthly to refresh the static
"Live On-chain Snapshot" section in tc/evidence.html with current
numbers (Pool's USDT balance, BNB balance, tx count, etc).

Usage:
    python3 tc/update-stats.py [--rpc https://bsc-dataseed.binance.org/]

Output:
    Prints a ready-to-paste JSON snippet for tc/evidence.html.
    Jerry can then copy the snippet and replace the existing
    snapshot block.

Optional: pipe to file and `git commit` to publish.
"""
import json
import urllib.request
import sys
from datetime import datetime, timezone

POOL = "0x2598825231f9aff0018c407b46e8e50facf082d7"
USDT_CONTRACT = "0x55d398326f99059ff775485246999027b3197955"
RPC = "https://bsc-dataseed.binance.org/"

def rpc(method, params):
    """Minimal JSON-RPC POST helper."""
    body = json.dumps({"jsonrpc":"2.0", "method":method, "params":params, "id":1}).encode()
    req = urllib.request.Request(RPC, data=body, headers={"Content-Type":"application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=20) as r:
        d = json.loads(r.read())
    if "error" in d:
        raise RuntimeError(f"RPC error {method}: {d['error']}")
    return d["result"]

def hexpad(addr: str) -> str:
    """Pad address to 32-byte word, ERC-20 calldata convention."""
    a = addr.lower().replace("0x", "")
    return "0x" + "0"*24 + a

def wei_to_units(wei_hex: str, decimals: int = 18) -> float:
    return int(wei_hex, 16) / (10 ** decimals)

def main():
    rpc_url = RPC
    if len(sys.argv) > 2 and sys.argv[1] == "--rpc":
        rpc_url = sys.argv[2]

    # 1. Latest block height
    latest_block_hex = rpc("eth_blockNumber", [])
    latest_block = int(latest_block_hex, 16)

    # 2. Pool address stats
    bnb_wei = rpc("eth_getBalance", [POOL, "latest"])
    bnb_bal = wei_to_units(bnb_wei, 18)
    tx_count = int(rpc("eth_getTransactionCount", [POOL, "latest"]), 16)
    code_hex = rpc("eth_getCode", [POOL, "latest"])

    # 3. USDT balanceOf(Pool) via calldata
    calldata = "0x70a08231" + hexpad(POOL).replace("0x", "")
    usdt_wei = rpc("eth_call", [{"to": USDT_CONTRACT, "data": calldata}, "latest"])
    usdt_bal = wei_to_units(usdt_wei, 18)

    # 4. USDT total supply
    total_supply_hex = rpc("eth_call", [{"to": USDT_CONTRACT, "data": "0x18160ddd"}, "latest"])
    total_supply = wei_to_units(total_supply_hex, 18)

    # 5. Pool "type": empty code → EOA
    pool_type = "EOA (個人錢包)" if code_hex in ("0x", "0x0") else f"Contract ({len(code_hex)//2} bytes)"

    snapshot = {
        "snapshot_at_block": latest_block,
        "snapshot_at_iso": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "snapshot_block_tip": f"~{(latest_block - latest_block)+0} blocks behind tip",
        "pool_address": POOL,
        "pool_type": pool_type,
        "pool_usdt_balance": round(usdt_bal, 4),
        "pool_usdt_balance_str": f"{usdt_bal:,.4f}",
        "pool_bnb_balance": round(bnb_bal, 6),
        "pool_bnb_balance_str": f"{bnb_bal:.6f}",
        "pool_tx_count": tx_count,
        "usdt_total_supply": round(total_supply, 4),
        "usdt_total_supply_str": f"{total_supply:,.4f}",
    }

    print(json.dumps(snapshot, indent=2, ensure_ascii=False))

    print("\n# HTML snippet for tc/evidence.html Section 0 (paste into data-stat attrs):")
    print(f'<section class="section" id="live-snapshot">')
    print(f'  <div class="container">')
    print(f'    <h2>Live On-chain Snapshot</h2>')
    print(f'    <p class="section-sub">Static snapshot from BNB Chain RPC at snapshot_at_iso (block {snapshot["snapshot_at_block"]}). For live numbers, re-run <code>tc/update-stats.py</code> and commit.</p>')
    print(f'    <div class="evidence-card">')
    print(f'      <h3>📊 Session 1 Pool — Real-time State</h3>')
    print(f'      <div class="tx-row"><span class="tx-label">USDT Balance</span><span class="tx-value" data-stat="usdt_balance">{snapshot["pool_usdt_balance_str"]} USDT</span></div>')
    print(f'      <div class="tx-row"><span class="tx-label">BNB Balance</span><span class="tx-value" data-stat="bnb_balance">{snapshot["pool_bnb_balance_str"]} BNB</span></div>')
    print(f'      <div class="tx-row"><span class="tx-label">Tx Count</span><span class="tx-value" data-stat="tx_count">{snapshot["pool_tx_count"]}</span></div>')
    print(f'      <div class="tx-row"><span class="tx-label">Pool Type</span><span class="tx-value" data-stat="pool_type">{snapshot["pool_type"]}</span></div>')
    print(f'      <div class="tx-row"><span class="tx-label">Snapshot Block</span><span class="tx-value" data-stat="block">{snapshot["snapshot_at_block"]}</span></div>')
    print(f'    </div>')
    print(f'  </div>')
    print(f'</section>')

if __name__ == "__main__":
    main()
