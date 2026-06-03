# responsive-master

**Project-level QA tool for MAGNE.AI Web3 Portal page migrations.**

---

## What is this?

This directory contains reproducible validation scripts and a skill definition for verifying that new page migrations meet the established MAGNE.AI Web3 Portal baseline:

- Portal shell structure (header / nav / mobile menu / footer)
- Responsive behavior across 9 standard viewports
- Compliance wording checks
- Footer legal links and social icons

---

## Not Part of the Runtime Site

- **Do not reference** any file in `tools/responsive-master/` from production pages
- This toolset is **excluded from the deployed site** (not served via GitHub Pages)
- It exists only in the repository for agent/bot reuse during migration QA

---

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Skill definition for agents (GPT-5.5 / MINIMAX) |
| `README.md` | This file |
| `scripts/viewport-check.sh` | Headless Chrome screenshot automation |
| `scripts/check-page.js` | Playwright structural validation |
| `scripts/copy-to-workspace.sh` | Copy screenshots to workspace for image tool |

---

## Quick Start

### 1. Start local server

```bash
cd /path/to/magne-web3
python3 -m http.server 4174
```

### 2. Run screenshots

```bash
./tools/responsive-master/scripts/viewport-check.sh \
  http://127.0.0.1:4174/ecosystem.html ecosystem
```

### 3. Copy to workspace

```bash
./tools/responsive-master/scripts/copy-to-workspace.sh /path/to/magne-web3 ecosystem
```

### 4. Validate

Read `SKILL.md` and cross-reference with workspace screenshots using the image tool.

---

## Agent Role Separation

| Agent | Role |
|-------|------|
| GPT-5.5 BOT | Migrate pages, run self-checks, generate screenshots |
| MINIMAX BOT | Read-only validation, compliance checks, responsive复核 |

**Do not run both agents on the same branch simultaneously.**
