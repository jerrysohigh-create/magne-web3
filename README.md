# MAGNE.AI Web3 Infrastructure Portal

**Site:** https://jerrysohigh-create.github.io/magne-web3/
**Main Domain:** https://web3.magne.ai (redirects to GitHub Pages)

This repository contains the public Web3 infrastructure portal for MAGNE.AI.

## Product Structure

### Flagship Product
- **Agent Pay** (`agent-pay.html`) — x402-compatible AI agent payment demo. Core narrative on homepage hero.

### Network
- **M Hash L2** — Layer 2 settlement network for agent payments, token transfers, and receipt anchoring.
- Chain ID: 20250827 (testnet active)
- Explorer: https://l2-explorer.testnet.magicalhash.com

### Developer Platform
- Developer Hub (`developers.html`)
- Connect to Testnets (`developers-connect.html`)
- Deploy Smart Contracts (`developers-contract.html`)
- Build a DApp (`developers-app.html`)

### Campaign Pages
- **Session2** (`session2.html`) — Separate community campaign page. Not in main nav. Accessible via Ecosystem page. Separate campaign terms apply.

## Page Tree

### English (`/`)
| Page | Title |
|------|-------|
| index.html | Web3 Portal / Agent Pay hero |
| agent-pay.html | Agent Pay — x402 AI Payment Demo |
| network.html | M Hash L2 Network |
| developers.html | Developer Hub |
| developers-contract.html | Deploy Smart Contracts |
| developers-connect.html | Connect to Testnets |
| developers-app.html | Build a DApp |
| token.html | Token |
| ecosystem.html | Ecosystem (includes Session2 campaign card) |
| transparency.html | Transparency Center |
| version-history.html | Version History |
| faq.html | FAQ |
| session2.html | **Session2 Campaign** |

### Traditional Chinese (`/tc/`)
| Page | Title |
|------|-------|
| tc/index.html | Web3 入口 / Agent Pay 主叙事 |
| tc/session2.html | Session2 活动页面 |

> Additional TC pages (token, transparency, faq, version-history) remain as prior versions pending update.

## Technical Status

| Component | Status |
|-----------|--------|
| Smart contracts — compile | ✓ Verified |
| Smart contracts — local deploy | ✓ Verified |
| mMHA ERC-20 deployment (testnet) | ✓ Verified |
| AI Task Receipt recording (testnet) | ✓ Verified |
| Public explorer evidence | ✓ Available |
| M Hash L2 testnet contract deployment | ✓ Verified |
| HTTP 402 payment flow | ⏳ In Development |
| Browser wallet authorization | ⏳ In Development |
| Facilitator verify / settle workflow | ⏳ In Development |
| Formal x402 compatibility | 🔍 Under Validation |
| Production deployment | 📋 Planned |

## Agent Pay 定位

MAGNE Agent Pay 是面向 AI 代理支付場景的開發階段演示，結合 M Hash L2 測試網上的合約部署與 AI 任務收據記錄能力。

正式 HTTP 402 支付流程、瀏覽器錢包授權、Facilitator 驗證與結算流程，以及 x402 相容性測試仍在開發與驗證中。

Agent Pay 是旗艦開發者演示頁，不是整個 Web3 入口的首頁。首頁是以 Agent Pay 為核心敘事的主頁門戶。

## Important Notice

**This website is for technical, ecosystem, and informational purposes only.**

Nothing on this website constitutes investment advice, financial advice, public offering, solicitation, or a guarantee of rewards, income, profit, liquidity, exchange listing, or token value.

Campaign participation information (including Session2) is governed by separate campaign terms. Session2 does not form part of the technical network disclosure.

## Deployment

- **GitHub Pages:** https://jerrysohigh-create.github.io/magne-web3/
- **Main domain:** https://web3.magne.ai (CNAME configured)
- **Repository:** https://github.com/jerrysohigh-create/magne-web3

## Trademark

MAGNE.AI™ is a trademark of Magical Hash Global Tech Limited, currently in registration process (USPTO Serial: 99311528).

---

© 2026 MAGNE.AI. All rights reserved.
