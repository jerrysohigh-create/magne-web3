# RELEASE-RECORD.md — MAGNE.AI Web3 Site Release History

---

## Current Status — 2026-05-22

### Architecture Update

- **Homepage rebuilt** in nara.build terminal aesthetic style
- **Agent Pay** positioned as flagship developer demo (not full homepage)
- **Session2** demoted from main nav — campaign page only
- **TRANSPARENCY** and **DEVELOPERS** restored as primary nav items
- Nav restructured: HOME / AGENT PAY / NETWORK / DEVELOPERS / TOKEN / ECOSYSTEM / TRANSPARENCY / FAQ
- Session2 accessible only via Ecosystem page
- GitHub Pages: https://jerrysohigh-create.github.io/magne-web3/

---

## Version Reference

### Current Site Structure

**English (`/`)**
| Page | Description |
|------|-------------|
| index.html | Web3 Portal + Agent Pay hero narrative |
| agent-pay.html | **Flagship** — x402 AI agent payment demo |
| network.html | M Hash L2 network |
| developers.html | Developer Hub |
| developers-contract.html | Deploy Smart Contracts |
| developers-connect.html | Connect to Testnets |
| developers-app.html | Build a DApp |
| token.html | Token disclosure |
| ecosystem.html | Ecosystem + Session2 campaign card |
| transparency.html | Transparency Center |
| version-history.html | Version History |
| faq.html | FAQ |
| session2.html | **Campaign** — separate terms, not in main nav |

**Traditional Chinese (`/tc/`)**
| Page | Description |
|------|-------------|
| tc/index.html | Web3 入口 + Agent Pay 主叙事 |
| tc/session2.html | Session2 繁體中文活動頁面 |

---

## Agent Pay Messaging — Revision Log

Corrected 7 messaging items on agent-pay.html:

1. Problem card: "No Agent Payment Rail" → "Agent payment rails are emerging..."
2. Flow: "on-chain receipt — in milliseconds" → "verifiable receipt — a programmable workflow"
3. Hero sub: Added testnet disclaimer — "local runtime demonstration... M Hash L2 testnet deployment in progress"
4. Terminal demo header: Removed "real transaction hashes" claim
5. Runtime status: Split into clear categories (local verified vs. testnet pending vs. browser pending vs. explorer pending)
6. TEE Runtime: English-only (removed mixed EN/TC text)
7. x402 compatibility: Added "subject to implementation and compatibility testing"

---

## Session2 Campaign Page — Isolation

- Removed from main navigation (all pages)
- Added to ecosystem.html Community Campaigns section with card + disclaimer
- Added campaign-specific disclaimer: "Separate campaign terms apply... This page does not form part of the technical network disclosure."
- Nav updated to "← Back to Portal" CTA

---

## GitHub Pages Deployment

- **URL:** https://jerrysohigh-create.github.io/magne-web3/
- **Main domain:** https://web3.magne.ai (CNAME target)
- **Last rebuild:** 2026-05-22

---

## Technical Verification Status

| Component | Status |
|-----------|--------|
| Smart contracts compile | ✓ Verified |
| Smart contracts deploy (local) | ✓ Verified |
| mMHA ERC-20 (testnet) | ✓ Verified |
| AI Task Receipt recording (testnet) | ✓ Verified |
| Public explorer evidence | ✓ Available |
| M Hash L2 testnet contract deployment | ✓ Verified |
| HTTP 402 payment flow | ⏳ In Development |
| Browser wallet authorization | ⏳ In Development |
| Facilitator verify / settle workflow | ⏳ In Development |
| Formal x402 compatibility | 🔍 Under Validation |
| Production deployment | 📋 Planned |

---

## Previous Release History

| Version | Date | Description |
|---------|------|-------------|
| v1.2.0 | 2026-05-01 | Complete Traditional Chinese translation (all pages) |
| v1.1.1 | 2026-05-01 | TC expansion: Learn, Network, Ecosystem |
| v1.1.0 | 2026-05-01 | TC core pages: index, token, transparency, faq, version-history |
| v1.0.1 | 2026-05-01 | English + multilingual architecture prepared |
| v1.0.0 | 2026-05-01 | Initial English public release |

> Versions prior to 2026-05-22 are archived. Current active development is unversioned (rolling releases).
>
> **2026-05-23 — Architecture + Status Revision**
> - Site-wide status口径统一 (STATUS-CONSTANTS.md)
> - EVIDENCE-REGISTER.md 建立
> - Agent Pay EN/TC 首页与演示页状态口径修正
> - Session2 隔离声明强化
> - coming-soon.html 转为语言说明页

---

## Important Notice

**This website is for technical, ecosystem, and informational purposes only.**

Nothing on this website constitutes investment advice, financial advice, public offering, solicitation, or a guarantee of rewards, income, profit, liquidity, exchange listing, or token value.

Campaign participation (Session2) is governed by separate campaign terms and does not form part of the technical network disclosure.

---

## Network Information

| Network | Chain ID | Status |
|---------|----------|--------|
| MAGNE L1 Testnet | 20250810 | Testing |
| M Hash L2 Testnet | 20250827 | Testing — deployment in progress |

**Token:** MHA / mMHA (test tokens, no mainnet value)

---

## Trademark

MAGNE.AI™ is a trademark of Magical Hash Global Tech Limited, currently in registration process (USPTO Serial: 99311528).

---

## Contact

- Website: https://magne.ai
- Telegram: https://t.me/MagneAI
- X (Twitter): https://x.com/Magne_Ai
- Discord: https://discord.gg/tX2xRAkd

---

© 2026 MAGNE.AI. All rights reserved.
