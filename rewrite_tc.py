#!/usr/bin/env python3
"""Rewrite tc/agent-pay.html with proper Traditional Chinese"""

import re

path = "/home/gaojie20/.openclaw/workspace-main/web3-magne-ai/tc/agent-pay.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# ========== 1. FIX og:title ==========
content = content.replace(
    'content="MAGNE Agent Pay V0.1 | x402 相容 AI 代理支付演示"',
    'content="MAGNE Agent Pay | M Hash L2 上的 AI 支付工作流程演示"'
)

# ========== 2. FIX og:description ==========
content = content.replace(
    'content="A developer demo for AI agent payment on M Hash L2. Designed for low-cost, scalable settlement. Public performance metrics will be published as testnet validation progresses."',
    'content="MAGNE Agent Pay 是 M Hash L2 測試網上的開發階段 AI 支付工作流程演示。結合測試合約部署與 AI 任務收據記錄能力。"'
)

# ========== 3. FIX Hero subtitle ==========
content = content.replace(
    "MAGNE Agent Pay 是面向 AI 代理的開發階段支付工作流程演示，結合 M Hash L2 測試網合約部署與可驗證的 AI 任務收據記錄。<br>",
    "MAGNE Agent Pay 是面向 AI 代理支付場景的開發階段演示，結合 M Hash L2 測試網上的合約部署與 AI 任務收據記錄能力。<br>"
)

# ========== 4. FIX hero-stats: x402 / Compatible -> V0.2 / 相容性驗證中 ==========
# Find and replace the 3rd hero-stat (x402 Compatible)
old_stats = '''<div class="hero-stat">
          <div class="val">x402</div>
          <div class="lbl">Compatible</div>
        </div>'''
new_stats = '''<div class="hero-stat">
          <div class="val">V0.2</div>
          <div class="lbl">合約與收據演示已完成</div>
        </div>
        <div class="hero-stat">
          <div class="val">x402</div>
          <div class="lbl">相容性驗證中</div>
        </div>'''
content = content.replace(old_stats, new_stats)

# Also fix the V0.1 hero-stat label
content = content.replace(
    "<div class=\"val\">V0.1</div>\n          <div class=\"lbl\">M Hash L2 合約</div>",
    "<div class=\"val\">20250827</div>\n          <div class=\"lbl\">M Hash L2 Chain ID</div>"
)

# ========== 5. FIX hero second paragraph ==========
old_hero2 = "目前演示已部署 M Hash L2 測試網上的測試代幣部署與收據記錄能力；正式 x402 相容性、瀏覽器錢包授權及生產級 facilitator 工作流程，仍有待進一步實作與測試。"
new_hero2 = "目前已完成測試網合約部署與收據記錄演示；正式 HTTP 402 支付流程、瀏覽器錢包授權、Facilitator 驗證與結算流程，以及 x402 相容性測試，仍在開發與驗證中。"
content = content.replace(old_hero2, new_hero2)

# ========== 6. FIX "可驗收收據" -> "可驗證收據" ==========
content = content.replace("從任務請求到可驗收收據", "從任務請求到可驗證收據")

# ========== 7. FIX "測試代幣"错译 smart contract ==========
old_sc = "任何一方 — 代理、用戶、審計員或測試代幣 — 都可以獨立在鏈上驗證完整歷史。"
new_sc = "任何一方，包括 AI 代理、使用者、審計方或智能合約，均可透過鏈上資料獨立查驗相關記錄。"
content = content.replace(old_sc, new_sc)

# ========== 8. FIX "一個 Aapp" ==========
old_aapp = "你的代碼 + SKILL.md = 一個 Aapp"
new_aapp = "以 SKILL.md 描述代理可調用的服務"
content = content.replace(old_aapp, new_aapp)

# ========== 9. FIX facilitator terminology ==========
content = content.replace("促進者", "Facilitator")

# ========== 10. FIX broken text ==========
content = content.replace("development.", "評估中。")
content = content.replace("參考架ure.", "參考架構。")
content = content.replace("may explore session-based authorization.", "可能探索基於 Session 的授權模式。")
content = content.replace("代理對商戶結帳roperability.", "代理對商戶結帳場景。")
content = content.replace("暂无即时整合计划。p>", "暫無即時整合計劃。")

# ========== 11. FIX comparison section: simplify to 4 rows ==========
# Find and replace the compat-grid
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
            <p>代理對商戶結帳。未來路線可能探索商戶結帳roperability.</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">Stellar / Algorand / HyperEVM</span>
              <span class="compat-badge p2">P2</span>
            </div>
            <p>觀察多鏈促進者模式。暂无即时整合计划。p>
          </div>
        </div>'''

new_compat = '''<div class="compat-grid" style="grid-template-columns: repeat(2, 1fr);">
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">x402</span>
              <span class="compat-badge p0">P0 — 開放協議</span>
            </div>
            <p>以 HTTP 402 為基礎的開放支付協議方向，由 Coinbase 首創並於 2026 年 4 月移交 Linux Foundation 管理。</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">B402 / Binance x402</span>
              <span class="compat-badge p1">P1 — 產業參考</span>
            </div>
            <p>Binance 基於 x402 的交易驗證與提交服務。作為公開產業案例參考；不表示 MAGNE 已接入 Binance 服務。</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">Google AP2</span>
              <span class="compat-badge p1">P1 — 概念參考</span>
            </div>
            <p>面向 AI agent 支付授權、信任與責任鏈的協議方向。作為行動端安全授權及可驗證支付意圖的概念參考。</p>
          </div>
          <div class="compat-item">
            <div class="compat-header">
              <span class="compat-name">MAGNE Agent Pay</span>
              <span class="compat-badge p0">自研</span>
            </div>
            <p>M Hash L2 測試網上的合約與 AI 任務收據演示。聚焦行動端安全授權方向與鏈上收據記錄。</p>
          </div>
        </div>
        <div class="compat-summary">
          <h3>生態定位說明</h3>
          <p>本表僅用於說明公開可查的技術方向與 MAGNE Agent Pay 的研究定位，不表示 MAGNE.AI 與 Coinbase、Linux Foundation、Binance、Google 或任何第三方存在合作、背書、官方整合，亦不表示已完成相關協議或服務的相容性驗證。</p>
        </div>'''

content = content.replace(old_compat, new_compat)

# ========== 12. FIX compat-summary ==========
old_summary = '''<div class="compat-summary">
      <h3>MAGNE Positioning</h3>
      <p>x402 相容支付執行<br>
      + AP2 風格授權意識<br>
      + M Hash L2 receipt<br>
      + MAGNE Phone 安全簽名<br>
      + 未來穩定幣結算支援</p>
    </div>'''
# Remove this (replaced by the new compat grid section above)
content = content.replace(old_summary, "")

# ========== 13. FIX roadmap: rename + V0.3 + simplify ==========
old_roadmap = '''<div class="roadmap-grid">
        <div class="roadmap-item">
          <span class="roadmap-phase done">✓ V0.1 — Done</span>
          <h3>M Hash L2 合約演示</h3>
          <p>完整支付流程在本地 Hardhat 上驗證。ERC20 支付、促進者驗證、鏈上收據。</p>
          <ul>
            <li>Smart contracts compile and deploy</li>
            <li>Backend API with x402 response</li>
            <li>促進者嚴格驗證模式</li>
            <li>AI 任務收據事件</li>
          </ul>
        </div>
        <div class="roadmap-item">
          <span class="roadmap-phase active">⟡ V0.2 — M Hash L2 測試網合約與收據演示</span>
          <h3>M Hash L2 測試網</h3>
          <p>將合約部署到活的 M Hash L2 測試網。真實水龍頭注資、真實區塊瀏覽器。</p>
          <ul>
            <li>M Hash L2 測試網部署</li>
            <li>真實錢包 MetaMask 流程</li>
            <li>瀏覽器實時交易驗證</li>
            <li>測試網上的促進者</li>
          </ul>
        </div>
        <div class="roadmap-item">
          <span class="roadmap-phase next">○ V1.0 — 生產就緒</span>
          <h3>主網就緒</h3>
          <p>取決於安全審計、合規評估和治理批准。計劃中。</p>
          <ul>
            <li>安全審計</li>
            <li>MHA 作為結算資產</li>
            <li>Production facilitator SLA</li>
            <li>x402 spec compliance review</li>
          </ul>
        </div>
      </div>'''

new_roadmap = '''<div class="roadmap-grid">
        <div class="roadmap-item">
          <span class="roadmap-phase done">✓ V0.1 — 已完成</span>
          <h3>本地合約與 AI 任務收據流程演示</h3>
          <p>完整支付流程在本地 Hardhat 上驗證。ERC20 支付、Facilitator 驗證、鏈上收據。</p>
          <ul>
            <li>合約編譯與本地部署</li>
            <li>後端 API 模擬 x402 回應</li>
            <li>Facilitator 驗證模式</li>
            <li>AI 任務收據事件</li>
          </ul>
        </div>
        <div class="roadmap-item">
          <span class="roadmap-phase active">⟡ V0.2 — 已完成</span>
          <h3>M Hash L2 測試網合約部署與公開收據記錄</h3>
          <p>將合約部署到活的 M Hash L2 測試網。真實水龍頭注資、真實區塊瀏覽器。已完成，需保留公開驗證資料。</p>
          <ul>
            <li>M Hash L2 測試網部署</li>
            <li>真實錢包 MetaMask 流程</li>
            <li>瀏覽器實時交易驗證</li>
            <li>測試網上的 Facilitator</li>
          </ul>
        </div>
        <div class="roadmap-item">
          <span class="roadmap-phase next">○ V0.3 — 開發中</span>
          <h3>真實 HTTP 402、瀏覽器錢包授權、Facilitator 驗證與結算</h3>
          <p>真實 HTTP 402 挑戰與重試流程、瀏覽器錢包授權，以及 Facilitator 鏈上結算驗證。積極開發中。</p>
          <ul>
            <li>MetaMask / 瀏覽器錢包連接</li>
            <li>HTTP 402 挑戰與重試流程</li>
            <li>Facilitator verify / settle 工作流程</li>
            <li>端到端用戶授權流程</li>
          </ul>
        </div>
        <div class="roadmap-item">
          <span class="roadmap-phase next">○ V0.4 — 研究中</span>
          <h3>x402 相容性測試與 B402 / Binance x402 服務模式研究</h3>
          <p>研究與驗證中。</p>
          <ul>
            <li>x402 相容性測試</li>
            <li>B402 服務模式研究</li>
          </ul>
        </div>
        <div class="roadmap-item">
          <span class="roadmap-phase next">○ V0.5 — 規劃中</span>
          <h3>穩定幣結算、MAGNE Phone 安全授權及安全審查</h3>
          <p>規劃中。</p>
          <ul>
            <li>穩定幣結算支援</li>
            <li>MAGNE Phone 安全授權</li>
            <li>安全審查準備</li>
          </ul>
        </div>
        <div class="roadmap-item">
          <span class="roadmap-phase next">○ V1.0 — 規劃中</span>
          <h3>經安全與合規評估後的生產部署</h3>
          <p>取決於安全審計、合規評估和治理批准。規劃中。</p>
          <ul>
            <li>安全審計</li>
            <li>MHA 作為結算資產</li>
            <li>Production Facilitator SLA</li>
            <li>x402 spec 合規審查</li>
          </ul>
        </div>
      </div>
      <p style="margin-top: 1.5rem; font-size: 0.85rem; color: var(--text-secondary);">以上內容屬產品與技術驗證方向，可能依據安全審查、技術結果、協議演進、監管因素及治理決策調整，不構成對功能上線時間、合作關係、交易支援或商業成果的承諾。</p>'''

content = content.replace(old_roadmap, new_roadmap)

# ========== 14. FIX roadmap section eyebrow ==========
content = content.replace(
    '<span class="section-eyebrow">Development 路線圖</span>',
    '<span class="section-eyebrow">技術驗證路線</span>'
)

# ========== 15. FIX footer disclaimer ==========
old_footer = "MAGNE Agent Pay V0.1 是一個測試網階段的開發者演示。它不是生產支付系統、不是財務建議、也不是未來功能的保證。所有交易都在 M Hash L2 測試網上 — 沒有主網活動。MHA 和 mMHA 是沒有主網價值的測試代幣。取決於適用的合規要求。"
new_footer = "MAGNE Agent Pay 是測試網階段的開發者演示，不是生產支付系統。頁面所示內容不構成對正式 x402 相容性、未來功能、合作關係、支付可用性、代幣價值或商業成果的保證。測試網資產僅供技術演示用途，不具主網或法幣價值。"
content = content.replace(old_footer, new_footer)

# ========== 16. FIX "Payment" in terminal - remove misleading "支付已部署" ==========
content = content.replace(
    "支付已部署",
    "測試網部署完成"
)

# ========== 17. FIX workflow section note ==========
# Add note after "預期支付工作流程" section header
content = content.replace(
    '<span class="section-eyebrow">預期支付工作流程</span>',
    '<span class="section-eyebrow">預期支付工作流程</span>\n      </div>\n      <div style="background: rgba(210,153,34,0.08); border: 1px solid rgba(210,153,34,0.2); border-radius: 2px; padding: 1rem 1.25rem; margin-bottom: 1.5rem;">\n        <p style="font-size: 0.88rem; color: var(--yellow); line-height: 1.7; margin: 0;">⚠ 以下工作流程展示 MAGNE Agent Pay 的目標設計。當前已驗證部分為 M Hash L2 測試網上的合約部署與 AI 任務收據記錄；HTTP 402 支付挑戰、瀏覽器錢包授權及 Facilitator 驗證／結算流程仍在開發中。</p>\n      </div>\n      <div>'
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("TC rewrite complete")
