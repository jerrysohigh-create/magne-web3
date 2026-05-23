# STATUS-CONSTANTS.md

> 全站狀態口徑統一標準。所有 EN / TC 頁面必須使用以下狀態辭令。

## Status Constants

| Key | EN | TC |
|-----|-----|-----|
| `M_HASH_L2_TESTNET` | M Hash L2 testnet contract deployment | M Hash L2 測試網合約部署 |
| `M_HASH_L2_TESTNET_STATUS` | **Verified demo** | **已完成演示** |
| `AI_TASK_RECEIPT` | AI Task Receipt recording | AI 任務收據記錄 |
| `AI_TASK_RECEIPT_STATUS` | **Verified demo** | **已完成演示** |
| `PUBLIC_EXPLORER` | Public explorer reference | 公開瀏覽器參考 |
| `PUBLIC_EXPLORER_STATUS` | **Available** | **已提供** |
| `HTTP_402` | HTTP 402 live challenge and retry | HTTP 402 即時挑戰與重試 |
| `HTTP_402_STATUS` | **In development** | **開發中** |
| `BROWSER_WALLET` | Browser wallet authorization | 瀏覽器錢包授權 |
| `BROWSER_WALLET_STATUS` | **In development** | **開發中** |
| `FACILITATOR` | Facilitator verify / settle workflow | Facilitator 驗證/結算流程 |
| `FACILITATOR_STATUS` | **In development** | **開發中** |
| `X402_COMPAT` | Formal x402 compatibility | 正式 x402 相容性 |
| `X402_COMPAT_STATUS` | **Under validation** | **相容性驗證中** |
| `PRODUCTION` | Production deployment | 生產環境部署 |
| `PRODUCTION_STATUS` | **Planned** | **規劃中** |

## Usage in Pages

### Verified items (can be stated as completed):
- M Hash L2 testnet contract deployment: 已完成演示
- AI Task Receipt recording: 已完成演示
- Public explorer reference: 已提供

### In-development items (must not be stated as completed):
- HTTP 402 challenge and retry flow: 開發中
- Browser wallet authorization: 開發中
- Facilitator verify/settle workflow: 開發中

### Under research/validation:
- Formal x402 compatibility: 相容性驗證中
- Production deployment: 規劃中

## Prohibited Claims

以下表述嚴禁使用：
- ❌ "HTTP 402 payment flow completed"
- ❌ "Facilitator verification completed"
- ❌ "x402 compatible"
- ❌ "Atomic payment settlement"
- ❌ "Every settled task generates a receipt" (implies 100% completion)
- ❌ "End-to-end AI task payment flow completed"
- ❌ "Production deployment"

## Required Disclaimers

Agent Pay 頁面必須包含：
> 目前已完成測試網合約部署與收據記錄演示；正式 HTTP 402 支付流程、瀏覽器錢包授權、Facilitator 驗證與結算流程，以及 x402 相容性測試仍在開發與驗證中。

Terminal Demo 必須標記為：
> 以下流程包含目標工作流程示意。其中，M Hash L2 測試網合約部署與 AI 任務收據記錄已完成驗證；HTTP 402 支付挑戰、瀏覽器錢包授權及 Facilitator 驗證/結算流程仍在開發中。
