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
| mMHA ERC-20 deployment | ✓ Verified |
| Local runtime verification | ✓ Verified |
| M Hash L2 testnet deployment | ⏳ In Progress |
| Browser wallet flow | ⏳ Pending |
| Public explorer evidence | ⏳ Pending |
| Formal security audit | ⏳ Pending |

## Agent Pay定位

MAGNE Agent Pay is positioned as the flagship developer demo — demonstrating x402-compatible payment flow, secure mobile authorization (TEE + Secure Element), facilitator verification, and AI Task Receipts on M Hash L2.

It is NOT the entire Web3 portal homepage. The homepage is a portal with Agent Pay as the hero narrative and primary CTA.

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
