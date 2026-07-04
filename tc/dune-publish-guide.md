# Dune Dashboard Publish Guide (5 steps)

**Goal**: Publish MAGNE.AI's 8-metric Session 1 金池 dashboard on
Dune Analytics (visible at the profile under `dune.com/magneai`).

**Time required**: ~15 minutes.

**Prerequisite**: Browser login to Jerry's Dune account. The Dune
profile `magneai` must be created (if not yet, do so at
[dune.com](https://dune.com) → Settings → Profile).

---

## Step 1 — Create Dashboard

1. Open https://dune.com/magneai
2. Click **+ New** → **New Dashboard**
3. Title: `MAGNE.AI · Session 1 金池公開看板`
4. Description: "Public on-chain USDT transfer tracking for the
   MAGNE.AI Session 1 pool on BNB Chain. Read-only; based on
   `bnb.USDT_Transfer` decoded events."
5. Tags: `MAGNE.AI`, `BNB Chain`, `USDT`, `Session 1`

## Step 2 — Add visualizations

For each of the 8 queries in `tc/dune-queries.md`:

1. Click **+ Add Visualization** → **Custom SQL**
2. Paste the SQL
3. Set title to match (`Total USDT Inflow`, etc.)
4. Set chart type:
   - KPI card → Big Number
   - Daily series → Line or Bar chart
   - Distribution → Histogram
   - Top 50 → Sortable table (no chart)

## Step 3 — Arrange

- Use a 4-column grid for the 3 KPI cards (Inflow / Outflow / Net)
- Below: 2-row × 1-col for Daily volume chart
- Below: New Wallets + Cumulative Wallets side by side
- Bottom row: Wallet Distribution + Top 50 table (full width)

## Step 4 — Public visibility

1. Top-right of dashboard → **Permissions** → set to **Public**
2. Verify URL pattern: `https://dune.com/magneai/session-1-pool`
   (Dune auto-generates slug from title)
3. Copy the full dashboard URL and send to the orchestrator —
   they will update `tc/evidence.html`'s View Dune Dashboard button
   to point at the real public dashboard (not just the profile).

## Step 5 — Test

1. Open the dashboard in **incognito** to confirm public visibility
2. Each chart should render within ~30 seconds (Dune caches)
3. Confirm the pool address `0x2598825231...` appears in queries

---

## Maintaining freshness

Dune auto-updates BNB Chain data every few minutes. No manual refresh
required. For a one-off verification, Jerry can compare any Dune KPI
against the live snapshot in `tc/evidence.html` Section 0 (live on-chain
snapshot) — both pull from the same canonical BNB Chain state.

