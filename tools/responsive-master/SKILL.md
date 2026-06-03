# responsive-master — MAGNE.AI Web3 Portal Migration Validation Skill

## Purpose

- Validate MAGNE.AI Web3 Portal page migrations to the multilingual portal shell
- Verify portal-shell header / mobile menu / footer / responsive behavior / content integrity / compliance
-供 GPT-5.5 BOT and MINIMAX BOT reuse
- Deterministic pass/fail criteria; reproducible across agents

---

## Baseline Pages (Shell-Compliant, Locked)

| EN | TC |
|----|----|
| index.html | tc/index.html |
| agent-pay.html | tc/agent-pay.html |
| network.html | tc/network.html |
| developers.html | tc/developers.html |
| token.html | tc/token.html |
| ecosystem.html | tc/ecosystem.html |

All future migrations must match or exceed this baseline.

---

## Standard Viewports

| Width | Type |
|-------|------|
| 1440 | Desktop large |
| 1320 | Desktop |
| 1280 | Desktop |
| 1024 | Tablet |
| 900 | Tablet |
| 768 | Mobile breakpoint |
| 430 | Mobile |
| 375 | Mobile small |
| 360 | Mobile small |

---

## Header Validation Checklist

For each viewport, check:

| # | Item | Pass Criteria |
|---|------|--------------|
| H1 | `.portal-shell-header` exists | Boolean |
| H2 | Logo renders | `<img>` or SVG visible |
| H3 | Desktop nav not overlapping | Links do not stack/overflow |
| H4 | Active nav link is cyan | `color: var(--ps-accent)` or equivalent |
| H5 | Preorder / 預購 button is cyan | Background or border is accent color |
| H6 | Desktop hamburger hidden | `display: none` or `visibility: hidden` above 768px |
| H7 | Mobile hamburger visible | `☰` icon visible at ≤768px |
| H8 | Mobile hamburger inside viewport | No overflow past right edge |

---

## Mobile Menu Validation Checklist

Open menu (tap hamburger), then check:

| # | Item | Pass Criteria |
|---|------|--------------|
| M1 | Menu opens | Overlay visible |
| M2 | Phone Portal visible | Link present in menu |
| M3 | Preorder / 預購 visible | CTA present in menu |
| M4 | 8 language options visible | EN / 繁中 / 日本語 / 한국어 / Français / Español / Tiếng Việt / Bahasa Indonesia |
| M5 | Menu covers header to viewport bottom | Full-height overlay |
| M6 | Body content not visible behind menu | Scrim covers content |
| M7 | No white background | Menu background is dark/portal-shell |
| M8 | No horizontal overflow | `body.scrollWidth <= body.clientWidth` |

---

## Footer Validation Checklist

| # | Item | Pass Criteria |
|---|------|--------------|
| F1 | GitHub icon | Link present |
| F2 | X (Twitter) icon | Link present |
| F3 | Telegram icon | Link present |
| F4 | YouTube icon | Link present |
| F5 | Icon size 34×34 / 16px content | CSS matches baseline |
| F6 | Trademark line (EN) | `MAGNE.AI™ is a trademark of Magical Hash Global Tech Limited...USPTO Serial No. 99311528` |
| F7 | Copyright line (EN) | `© 2026 MAGNE.AI. All rights reserved.` |
| F8 | Legal links (EN) | `Privacy Policy · Contact · Media Kit` |
| F9 | Trademark line (TC) | `MAGNE.AI™ 為 Magical Hash Global Tech Limited 的商業標誌...USPTO 序號：99311528` |
| F10 | Copyright line (TC) | `© 2026 MAGNE.AI. 版權所有。` |
| F11 | Legal links (TC) | `隱私政策 · 聯繫我們 · 媒體資料` |
| F12 | No horizontal overflow | `body.scrollWidth <= body.clientWidth` |

---

## Responsive Validation Checklist

For every viewport:

| # | Item | Pass Criteria |
|---|------|--------------|
| R1 | `document.documentElement.scrollWidth <= document.documentElement.clientWidth` | true |
| R2 | `document.body.scrollWidth <= document.body.clientWidth` | true |
| R3 | No white background | Page background is dark |
| R4 | No bare/unstyled text | All text inside proper containers |
| R5 | Cards / grids do not overflow | `scrollWidth <= clientWidth` for each card grid |
| R6 | Tables do not overflow | Horizontal scroll not triggered |
| R7 | Code blocks / terminal do not overflow | `scrollWidth <= clientWidth` |
| R8 | Mobile content readable | Text size ≥12px, no cutoff |

---

## Compliance / Forbidden Wording Baseline

### EN — Never permit in migrated content:

| Forbidden Phrase | Severity |
|-----------------|----------|
| guaranteed rewards | Critical |
| guaranteed airdrop | Critical |
| guaranteed listing | Critical |
| risk-free | Critical |
| fixed APY | Critical |
| fixed yield | Critical |
| passive income | Major |
| mining income | Major |
| buy phone and earn | Critical |
| earn by holding | Critical |

**Permitted negative context:** `No guaranteed rewards`, `No guaranteed listing`

### TC — Never permit in migrated content:

| 禁用詞 | 嚴重程度 |
|--------|---------|
| 保證收益 | Critical |
| 保證空投 | Critical |
| 保證上市 | Critical |
| 無風險 | Critical |
| 固定收益 | Critical |
| 被動收入 | Major |
| 挖礦收入 | Major |
| 買手機賺錢 | Critical |
| 持有即賺 | Critical |
| 穩賺 | Critical |

**允許否定語境：** `無保證獎勵`、`無保證上市`

---

## Standard Report Template

### Per Page — Per Viewport

```
### {PAGE} — {WIDTH}px

| Check | Result |
|-------|--------|
| Header | PASS / FAIL |
| Hamburger / Menu | PASS / FAIL |
| Body content | PASS / FAIL |
| Card / Table / Code | PASS / FAIL |
| Footer | PASS / FAIL |
| bodyScrollW <= clientW | PASS / FAIL |

**Overall: PASS / FAIL**
```

### Issue Summary

```
Critical: 0
Major: 0
Minor: 0
Non-blocking Known Issue: 0
```

---

## GPT-5.5 / MINIMAX Role Separation

| Agent | Responsibility |
|-------|---------------|
| **GPT-5.5 BOT** | Generate migration branch, edit pages, take screenshots, run self-checks |
| **MINIMAX BOT** | Read-only validation, compliance checks, responsive复核 |

**Rule: Do not let both agents modify the same branch simultaneously.**

---

## Usage

### 1. Start local HTTP server

```bash
cd /path/to/magne-web3
python3 -m http.server 4174
```

### 2. Run viewport-check.sh

```bash
./tools/responsive-master/scripts/viewport-check.sh http://127.0.0.1:4174/ecosystem.html ecosystem
```

Output: `/tmp/magne-responsive-screenshots/ecosystem-{width}.png`

### 3. Load screenshots in workspace for image analysis

```bash
./tools/responsive-master/scripts/copy-to-workspace.sh /path/to/magne-web3
```

### 4. MINIMAX reads this SKILL.md and validates

```
Read tools/responsive-master/SKILL.md
```

Then cross-reference against screenshots in workspace.

---

## File Structure

```
tools/responsive-master/
├── SKILL.md                              ← This file
├── README.md                             ← Project-level QA tool notice
└── scripts/
    ├── viewport-check.sh                 ← Screenshot automation
    ├── check-page.js                     ← Playwright structural checks
    └── copy-to-workspace.sh              ← Copy screenshots to workspace
```
