# SITE-MAP.md

## Site Architecture

**Site:** MAGNE.AI Web3
**EN Root:** `https://jerrysohigh-create.github.io/magne-web3/`
**TC Root:** `https://jerrysohigh-create.github.io/magne-web3/tc/`
**Repo:** `https://github.com/jerrysohigh-create/magne-web3`

---

## Primary Navigation

### EN (`/`)

| Label | File | Description |
|-------|------|-------------|
| HOME | `index.html` | Main landing page |
| AGENT PAY | `agent-pay.html` | Flagship developer demo |
| NETWORK | `network.html` | Technical infrastructure |
| DEVELOPERS | `developers.html` | Developer documentation hub |
| TOKEN | `token.html` | Token disclosure |
| ECOSYSTEM | `ecosystem.html` | Ecosystem and partnerships |
| TRANSPARENCY | `transparency.html` | Transparency and evidence |
| FAQ | `faq.html` | Frequently asked questions |

### TC (`/tc/`)

| Label | File | Description |
|-------|------|-------------|
| 首頁 | `index.html` | 主頁 |
| AGENT PAY | `agent-pay.html` | 旗艦開發者演示 |
| 網絡 | `network.html` | 技術基礎設施 |
| 開發者 | `developers.html` | 開發者文檔中心 |
| 代幣 | `token.html` | 代幣披露 |
| 生態 | `ecosystem.html` | 生態與合作夥伴 |
| 透明中心 | `transparency.html` | 透明與證據 |
| 常見問題 | `faq.html` | 常見問題 |

---

## Secondary Pages (Not in Primary Nav)

### EN

| File | Description | Nav Location |
|------|-------------|-------------|
| `learn.html` | Learn hub | Footer |
| `version-history.html` | Version history | Footer |
| `developers-connect.html` | Connect to testnet | Footer / Developers |
| `developers-contract.html` | Contract reference | Footer / Developers |
| `developers-app.html` | Build DApp guide | Footer / Developers |
| `tokenomics-detail.html` | Tokenomics detail | Footer |
| `session2.html` | Session2 Campaign | Ecosystem footer |
| `coming-soon.html` | Coming soon (deprecated) | None |

### TC

| File | Description | Nav Location |
|------|-------------|-------------|
| `learn.html` | 學習中心 | Footer |
| `version-history.html` | 版本歷史 | Footer |
| `developers-connect.html` | 連接測試網 | Footer / 開發者 |
| `developers-contract.html` | 合約參考 | Footer / 開發者 |
| `developers-app.html` | 建構 DApp 指南 | Footer / 開發者 |
| `tokenomics-detail.html` | 代幣經濟詳情 | Footer |
| `session2.html` | Session2 活動 | Footer / 生態 |
| `coming-soon.html` | 即將上線（停用）| None |

---

## Campaign Pages

| File | Description |
|------|-------------|
| `session2.html` | Session2 AI Agent Campaign — **isolated from technical narrative** |
| `tc/session2.html` | Session2 繁中版 |

**Note:** Session2 is a separate campaign and is NOT part of the MAGNE.AI technical disclosure. It should not appear in primary navigation or be conflated with Agent Pay or network technical documentation.

---

## Page Relationship

```
index.html (HOME)
├── agent-pay.html (Flagship demo — main product page)
├── network.html (Technical infrastructure)
├── developers.html (Dev hub)
│   ├── developers-connect.html
│   ├── developers-contract.html
│   └── developers-app.html
├── token.html (Token disclosure)
│   └── tokenomics-detail.html
├── ecosystem.html (Ecosystem)
│   └── session2.html (ISOLATED CAMPAIGN — not tech narrative)
├── transparency.html (Evidence and verification)
├── learn.html (Educational content)
├── version-history.html (Version history)
└── faq.html (FAQ)
```

---

## Preorder

| Page | EN CTA | TC CTA |
|------|--------|--------|
| index.html | `https://forms.example.com/preorder` | `https://forms.example.com/preorder` |

**Note:** TC preorder link at `forms.example.com` — verify before publishing.

---

## Language Versions

- EN: All primary and secondary pages
- TC (繁中): All primary pages; secondary pages translated

---

## Status

This site map reflects the architecture as of **v1.0.0**. Agent Pay is the flagship developer demo. Network and Developers provide technical support. Token and Transparency provide disclosure support. Session2 is a separate campaign isolated from the technical narrative.
