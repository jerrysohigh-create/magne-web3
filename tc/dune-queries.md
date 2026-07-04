# Dune Analytics SQL Queries — MAGNE.AI Session 1 金池

**Pool**: `0x2598825231f9aff0018c407b46e8e50facf082d7`  
**USDT contract**: `0x55d398326f99059ff775485246999027b3197955`  
**Network**: BNB Chain (chain id 56)  
**Decoded table**: `bnb.USDT_Transfer` (BEP-20 Transfer events table)

These 8 queries correspond to the planned Dune Dashboard Scope in
`tc/evidence.html`. Jerry pastes each query into Dune (Custom SQL
visualization) — they run on Dune's indexed BNB Chain data and reflect
canonical, public on-chain transfers.

> Constraints: All queries are read-only. No external API calls.
> Network: All queries default to BNB Chain (Dune tracks it as `bnb.*`).

---

## Query 1 — Total USDT Inflow to Pool

```sql
SELECT SUM(amount / 1e18) AS total_usdt_inflow
FROM bnb.USDT_Transfer
WHERE "to" = 0x2598825231f9aff0018c407b46e8e50facf082d7;
```

Visualize as: Big number / KPI card

---

## Query 2 — Total USDT Outflow from Pool

```sql
SELECT SUM(amount / 1e18) AS total_usdt_outflow
FROM bnb.USDT_Transfer
WHERE "from" = 0x2598825231f9aff0018c407b46e8e50facf082d7;
```

Visualize as: Big number / KPI card

---

## Query 3 — Net USDT Inflow

```sql
SELECT
  (SUM(CASE WHEN "to"   = 0x2598825231f9aff0018c407b46e8e50facf082d7 THEN amount ELSE 0 END) -
   SUM(CASE WHEN "from" = 0x2598825231f9aff0018c407b46e8e50facf082d7 THEN amount ELSE 0 END)) / 1e18
    AS net_usdt_inflow
FROM bnb.USDT_Transfer
WHERE "to"   = 0x2598825231f9aff0018c407b46e8e50facf082d7
   OR "from" = 0x2598825231f9aff0018c407b46e8e50facf082d7;
```

Visualize as: Big number / KPI card

---

## Query 4 — Daily USDT Inflow / Outflow

```sql
SELECT
  DATE_TRUNC('day', evt_block_time) AS day,
  SUM(CASE WHEN "to"   = 0x2598825231f9aff0018c407b46e8e50facf082d7 THEN amount ELSE 0 END) / 1e18 AS daily_inflow,
  SUM(CASE WHEN "from" = 0x2598825231f9aff0018c407b46e8e50facf082d7 THEN amount ELSE 0 END) / 1e18 AS daily_outflow
FROM bnb.USDT_Transfer
WHERE "to"   = 0x2598825231f9aff0018c407b46e8e50facf082d7
   OR "from" = 0x2598825231f9aff0018c407b46e8e50facf082d7
GROUP BY 1
ORDER BY 1 DESC;
```

Visualize as: Time series line / bar chart (x-axis = day, y = USDT)

---

## Query 5 — Daily New Wallets

```sql
WITH pool_addresses AS (
  SELECT "to" AS address, evt_block_time FROM bnb.USDT_Transfer
    WHERE "to" = 0x2598825231f9aff0018c407b46e8e50facf082d7
  UNION ALL
  SELECT "from" AS address, evt_block_time FROM bnb.USDT_Transfer
    WHERE "from" = 0x2598825231f9aff0018c407b46e8e50facf082d7
),
first_seen AS (
  SELECT
    address,
    MIN(DATE_TRUNC('day', evt_block_time)) AS first_day
  FROM pool_addresses
  GROUP BY 1
)
SELECT
  first_day AS day,
  COUNT(*) AS new_wallets
FROM first_seen
GROUP BY 1
ORDER BY 1 DESC;
```

Visualize as: Bar chart (x = day, y = new wallet count)

---

## Query 6 — Cumulative Unique Wallets

```sql
WITH pool_addresses AS (
  SELECT "to" AS address, evt_block_time FROM bnb.USDT_Transfer
    WHERE "to" = 0x2598825231f9aff0018c407b46e8e50facf082d7
  UNION ALL
  SELECT "from" AS address, evt_block_time FROM bnb.USDT_Transfer
    WHERE "from" = 0x2598825231f9aff0018c407b46e8e50facf082d7
),
first_seen AS (
  SELECT
    address,
    MIN(DATE_TRUNC('day', evt_block_time)) AS first_day
  FROM pool_addresses
  GROUP BY 1
),
daily_new AS (
  SELECT first_day AS day, COUNT(*) AS new_count
  FROM first_seen
  GROUP BY 1
)
SELECT
  day,
  SUM(new_count) OVER (ORDER BY day) AS cumulative_unique_wallets
FROM daily_new
ORDER BY 1 DESC;
```

Visualize as: Area chart (x = day, y = cumulative wallet count)

---

## Query 7 — Wallet Participation Distribution

```sql
WITH interactions AS (
  SELECT "to" AS wallet, amount FROM bnb.USDT_Transfer
    WHERE "from" = 0x2598825231f9aff0018c407b46e8e50facf082d7
  UNION ALL
  SELECT "from" AS wallet, amount FROM bnb.USDT_Transfer
    WHERE "to" = 0x2598825231f9aff0018c407b46e8e50facf082d7
),
per_wallet AS (
  SELECT wallet, SUM(amount) / 1e18 AS participation_usdt
  FROM interactions
  WHERE wallet != 0x2598825231f9aff0018c407b46e8e50facf082d7  -- exclude self
  GROUP BY 1
)
SELECT
  wallet,
  participation_usdt
FROM per_wallet
ORDER BY participation_usdt DESC;
```

Visualize as: Histogram (bin wallets by participation tier) or table

---

## Query 8 — Top 50 Wallets by USDT Contribution

```sql
SELECT
  "from" AS wallet,
  SUM(amount) / 1e18 AS total_usdt_sent_to_pool,
  COUNT(*) AS transfer_count
FROM bnb.USDT_Transfer
WHERE "to" = 0x2598825231f9aff0018c407b46e8e50facf082d7
GROUP BY 1
ORDER BY total_usdt_sent_to_pool DESC
LIMIT 50;
```

Visualize as: Sorted table (top 50)

---

## Notes for Jerry

1. The `bnb.USDT_Transfer` table is Dune's auto-decoded ERC-20-style
   Transfer event index for the BNB-Chain USDT BEP-20 contract.
2. Quotes around `"to"` / `"from"` are required because those columns
   conflict with SQL reserved keywords.
3. Address values use `0x`-prefixed lowercase hex.
4. Dune picks up BNB-Chain data with ~few-minutes lag.
5. All amounts are stored in raw (wei-scale 1e18). Divide by 1e18 for
   human-readable USDT values.

