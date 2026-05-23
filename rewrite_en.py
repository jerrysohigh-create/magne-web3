#!/usr/bin/env python3
"""Rewrite agent-pay.html (EN) with accurate x402 status and roadmap"""

import re

path = "/home/gaojie20/.openclaw/workspace-main/web3-magne-ai/agent-pay.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# ========== 1. FIX og:title ==========
content = content.replace(
    'content="MAGNE Agent Pay V0.1 | x402-Compatible AI Agent Payment Demo"',
    'content="MAGNE Agent Pay | AI Payment Workflow Demo on M Hash L2"'
)

# ========== 2. FIX hero stats: x402 / Compatible -> V0.2 / Testnet ✓ + x402 / Compatibility Under Validation ==========
old_stats = '''<div class="hero-stat">
          <div class="val">V0.1</div>
          <div class="lbl">M Hash L2 Contracts</div>
        </div>
        <div class="hero-stat">
          <div class="val">x402</div>
          <div class="lbl">Compatible</div>
        </div>'''
new_stats = '''<div class="hero-stat">
          <div class="val">V0.2</div>
          <div class="lbl">Contracts & Receipt Demo ✓</div>
        </div>
        <div class="hero-stat">
          <div class="val">x402</div>
          <div class="lbl">Compatibility Under Validation</div>
        </div>'''
content = content.replace(old_stats, new_stats)

# ========== 3. FIX hero subtitle paragraph 2 ==========
old_hero2 = "End-to-end demonstration using smart contracts deployed on M Hash L2 Testnet (chainId: 20250827). All transactions verified on-chain with public explorer links."
new_hero2 = "Currently demonstrating testnet contract deployment and AI Task Receipt recording on M Hash L2 (chainId: 20250827). Full HTTP 402 payment flow, browser wallet authorization, and Facilitator verify/settle are in active development."
content = content.replace(old_hero2, new_hero2)

# ========== 4. FIX workflow section - add note ==========
old_flow_header = '<span class="section-eyebrow">How It Works</span>'
new_flow_header = '''<span class="section-eyebrow">How It Works</span>
      </div>
      <div style="background: rgba(210,153,34,0.08); border: 1px solid rgba(210,153,34,0.2); border-radius: 2px; padding: 1rem 1.25rem; margin-bottom: 1.5rem;">
        <p style="font-size: 0.88rem; color: var(--yellow); line-height: 1.7; margin: 0;">⚠ The workflow below shows MAGNE Agent Pay's target design. Currently verified: M Hash L2 testnet contract deployment and AI Task Receipt recording. HTTP 402 payment challenge, browser wallet authorization, and Facilitator verify/settle are in development.</p>
      </div>
      <div>'''
content = content.replace(old_flow_header, new_flow_header)

# ========== 5. FIX terminal section ==========
old_terminal_note = "All transactions are verified on-chain with public explorer links."
new_terminal_note = "This section shows the verified testnet contract deployment and AI Task Receipt recording. HTTP 402 payment challenge, browser wallet authorization, and Facilitator verify/settle are not in this verification scope."
content = content.replace(old_terminal_note, new_terminal_note)

# Also fix "payment initiated" -> "testnet transaction"
content = content.replace(
    "status: <span class=\"t-ok\">verified</span>",
    "status: <span class=\"t-ok\">testnet</span>"
)

# ========== 6. FIX comparison section - simplify to 4 rows ==========
old_compat = '''<div class="compat-grid">
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">x402 (Coinbase / Linux Foundation)</span>
              <span class="compat-badge p0">P0 — Foundation</span>
            </div>
            <p>The HTTP 402 Payment Required protocol standard for agent payments, initiated by Coinbase and handed to the Linux Foundation in April 2026. Reference implementation available.</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">B402 / Binance x402</span>
              <span class="compat-badge p1">P1</span>
            </div>
            <p>Binance's implementation of the x402-compatible payment verification and submission service on supported chains. Live on select chains.</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">Google AP2</span>
              <span class="compat-badge p1">P1</span>
            </div>
            <p>Google's agent-to-agent payment authorization protocol. Addresses liability, trust chains, and delegation for AI agents. In developer preview.</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">Cloudflare / MCP</span>
              <span class="compat-badge p2">P2</span>
            </div>
            <p>Model Context Protocol for AI agent tool-use and payment integration. Potential x402 integration points.</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">Base / Coinbase Developer Platform</span>
              <span class="compat-badge p1">P1</span>
            </div>
            <p>Coinbase's L2 with smart wallet and session key infrastructure. Native x402 support via Coinbase payments. Actively used by multiple agent frameworks.</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">OKX APP</span>
              <span class="compat-badge p2">P2</span>
            </div>
            <p>OKX exchange with built-in DeFi trading bot and agent payment infrastructure. Agent checkout within the OKX ecosystem.</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">BNB Chain / Binance</span>
              <span class="compat-badge p1">P1</span>
            </div>
            <p>Binance's L1/L2 ecosystem with BNB Greenfield storage andopBNB for agent payment and data requirements. Strong DeFi integration.</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">Solana</span>
              <span class="compat-badge p1">P1</span>
            </div>
            <p>High-performance L1 with ultra-low fees and pump.fun for agent原生 token launch. State compression for receipt onchain storage.</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">OpenZeppelin Relayer</span>
              <span class="compat-badge p2">P2</span>
            </div>
            <p>Account abstraction infrastructure for gasless transactions and automated agent payments. Widely used in production.</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">OpenFacilitator / OpenX402.ai</span>
              <span class="compat-badge p2">P2</span>
            </div>
            <p>Open-source reference implementation of an x402 payment facilitator. Self-hostable and permissionless.</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">Stripe Tempo / MPP</span>
              <span class="compat-badge p2">P2</span>
            </div>
            <p>Stripe's agent payment infrastructure. Market Product Initiative for agent payment standardization. Long-term optionality for MAGNE.</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">OpenAI ACP</span>
              <span class="compat-badge p2">P2</span>
            </div>
            <p>Agent-to-merchant checkout. Future roadmap may explore merchant checkout interoperability.</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">Stellar / Algorand / HyperEVM</span>
              <span class="compat-badge p2">P2</span>
            </div>
            <p>Observe multi-chain facilitator patterns. No immediate integration planned.</p>
          </div>
        </div>

        <div class="compat-summary">
          <h3>MAGNE Positioning</h3>
          <p>x402-compatible payment execution<br>
          + AP2-style authorization awareness<br>
          + M Hash L2 receipt<br>
          + MAGNE Phone secure signing<br>
          + Future stablecoin settlement support</p>
        </div>'''

new_compat = '''<div class="compat-grid" style="grid-template-columns: repeat(2, 1fr);">
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">x402</span>
              <span class="compat-badge p0">P0 — Open Protocol</span>
            </div>
            <p>HTTP 402-based open payment protocol for agent payments, initiated by Coinbase and transferred to the Linux Foundation in April 2026.</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">B402 / Binance x402</span>
              <span class="compat-badge p1">P1 — Industry Reference</span>
            </div>
            <p>Binance's x402-compatible payment verification and submission service on supported chains. Included as a public industry reference case; does not indicate MAGNE is integrated with Binance services.</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">Google AP2</span>
              <span class="compat-badge p1">P1 — Concept Reference</span>
            </div>
            <p>Google's agent-to-agent payment authorization protocol addressing liability, trust chains, and delegation for AI agents. Included as a concept reference for mobile secure authorization.</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">MAGNE Agent Pay</span>
              <span class="compat-badge p0">Self-developed</span>
            </div>
            <p>Contracts and AI Task Receipt demonstration on M Hash L2 testnet. Focus on mobile secure authorization and on-chain receipt recording.</p>
          </div>
        </div>
        <div class="compat-summary">
          <h3>Positioning Note</h3>
          <p>This table is for reference only, describing publicly available technical directions and MAGNE Agent Pay's research positioning. It does not indicate that MAGNE.AI has any partnership, endorsement, or official integration with Coinbase, Linux Foundation, Binance, Google, or any third party, nor does it indicate completion of compatibility certification for any protocol or service.</p>
        </div>'''

content = content.replace(old_compat, new_compat)

# ========== 7. FIX roadmap: add V0.3 + rename section ==========
old_roadmap = '''<div class="roadmap-grid">
        <div class="roadmap-item">
          <span class="roadmap-phase done">✓ V0.1 — Done</span>
          <h3>M Hash L2 Contracts Demo</h3>
          <p>Full payment flow verified on local Hardhat. ERC20 payments, facilitator verification, on-chain receipts.</p>
          <ul>
            <li>Smart contracts compile and deploy</li>
            <li>Backend API with x402 response</li>
            <li>Facilitator strict verify mode</li>
            <li>AI Task Receipt events</li>
          </ul>
        </div>
        <div class="roadmap-item">
          <span class="roadmap-phase active">⟡ V0.2 — M Hash L2 Testnet Contract & Receipt Demonstration</span>
          <h3>M Hash L2 Testnet</h3>
          <p>M Hash L2 Testnet contract deployment, AI Task Receipt recording, and public explorer verification. Completed.</p>
          <ul>
            <li>M Hash L2 testnet deployment</li>
            <li>Real wallet MetaMask flow</li>
            <li>Live explorer tx verification</li>
            <li>Facilitator on testnet</li>
          </ul>
        </div>
        <div class="roadmap-item">
          <span class="roadmap-phase next">○ V1.0 — Production Readiness</span>
          <h3>Mainnet Readiness</h3>
          <p>Subject to security audit, compliance assessment, and governance approval. Planned.</p>
          <ul>
            <li>Security audit</li>
            <li>MHA as settlement asset</li>
            <li>Production facilitator SLA</li>
            <li>x402 spec compliance review</li>
          </ul>
        </div>
      </div>'''

new_roadmap = '''<div class="roadmap-grid">
        <div class="roadmap-item">
          <span class="roadmap-phase done">✓ V0.1 — Done</span>
          <h3>Local Contract & AI Task Receipt Demo</h3>
          <p>Full payment flow verified on local Hardhat. ERC20 payments, Facilitator verification, on-chain receipts.</p>
          <ul>
            <li>Smart contracts compile and deploy</li>
            <li>Backend API with x402 response</li>
            <li>Facilitator strict verify mode</li>
            <li>AI Task Receipt events</li>
          </ul>
        </div>
        <div class="roadmap-item">
          <span class="roadmap-phase active">⟡ V0.2 — Done</span>
          <h3>M Hash L2 Testnet Contract Deployment & Public Receipt Recording</h3>
          <p>M Hash L2 Testnet contract deployment, AI Task Receipt recording, and public explorer verification. Completed.</p>
          <ul>
            <li>M Hash L2 testnet deployment</li>
            <li>Real wallet MetaMask flow</li>
            <li>Live explorer tx verification</li>
            <li>Facilitator on testnet</li>
          </ul>
        </div>
        <div class="roadmap-item">
          <span class="roadmap-phase next">○ V0.3 — In Development</span>
          <h3>Real HTTP 402, Browser Wallet Authorization & Facilitator Verification</h3>
          <p>Browser wallet authorization, HTTP 402 challenge/response flow, and Facilitator on-chain settlement verification. In active development.</p>
          <ul>
            <li>MetaMask / browser wallet connection</li>
            <li>HTTP 402 challenge and retry flow</li>
            <li>Facilitator verify / settle workflow</li>
            <li>End-to-end user authorization flow</li>
          </ul>
        </div>
        <div class="roadmap-item">
          <span class="roadmap-phase next">○ V0.4 — Research</span>
          <h3>x402 Compatibility Testing & B402 / Binance x402 Service Model Research</h3>
          <p>Research and validation in progress.</p>
          <ul>
            <li>x402 compatibility testing</li>
            <li>B402 service model research</li>
          </ul>
        </div>
        <div class="roadmap-item">
          <span class="roadmap-phase next">○ V0.5 — Planned</span>
          <h3>Stablecoin Settlement, MAGNE Phone Secure Authorization & Security Audit</h3>
          <p>Planned.</p>
          <ul>
            <li>Stablecoin settlement support</li>
            <li>MAGNE Phone secure authorization</li>
            <li>Security audit preparation</li>
          </ul>
        </div>
        <div class="roadmap-item">
          <span class="roadmap-phase next">○ V1.0 — Planned</span>
          <h3>Production Deployment After Security & Compliance Assessment</h3>
          <p>Subject to security audit, compliance assessment, and governance approval. Planned.</p>
          <ul>
            <li>Security audit</li>
            <li>MHA as settlement asset</li>
            <li>Production Facilitator SLA</li>
            <li>x402 spec compliance review</li>
          </ul>
        </div>
      </div>
      <p style="margin-top: 1.5rem; font-size: 0.85rem; color: var(--text-secondary);">This roadmap describes product and technical validation directions and may be adjusted based on security review, technical results, protocol evolution, regulatory factors, and governance decisions. It does not constitute a commitment to feature launch timelines, partnerships, transaction support, or commercial outcomes.</p>'''

content = content.replace(old_roadmap, new_roadmap)

# ========== 8. FIX roadmap section eyebrow ==========
content = content.replace(
    '<span class="section-eyebrow">Development Roadmap</span>',
    '<span class="section-eyebrow">Technical Validation Roadmap</span>'
)

# ========== 9. FIX "facilitator" casing ==========
# Keep "Facilitator" capitalized throughout
content = content.replace(
    "Facilitator on testnet",
    "Facilitator on testnet"
)

# ========== 10. FIX footer disclaimer ==========
old_footer = "MAGNE Agent Pay V0.1 is a testnet-stage developer demo. It is not a production payment system, not financial advice, and not a guarantee of future functionality. All transactions are on M Hash L2 testnet — no mainnet activity. MHA and mMHA are test tokens with no mainnet value. Subject to applicable compliance requirements."
new_footer = "MAGNE Agent Pay is a testnet-stage developer demo, not a production payment system. Content shown here does not constitute a guarantee of x402 compatibility, future functionality, partnerships, payment availability, token value, or commercial outcomes. Testnet assets are for technical demonstration only and have no mainnet or fiat value."
content = content.replace(old_footer, new_footer)

# ========== 11. FIX receipt verifiable ==========
content = content.replace(
    "From task request to <strong>verifiable receipt</strong>",
    "From task request to <strong>verifiable receipt</strong>"
)

# ========== 12. FIX SDK section note ==========
old_sdk_note = "The code below is for reference only. A production implementation would require key management infrastructure, security audit, and compliance assessment."
new_sdk_note = "The code below is for developer demonstration purposes only. Production implementation requires controlled signing infrastructure, security review, and compliance assessment."
content = content.replace(old_sdk_note, new_sdk_note)

# ========== 13. FIX status section ==========
content = content.replace(
    "正式 x402 相容性審查 — 開發中",
    "x402 compatibility review — In Development"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("EN rewrite complete")
