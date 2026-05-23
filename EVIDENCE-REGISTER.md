# EVIDENCE-REGISTER.md

> 一個真實記錄文件，記錄 MAGNE Agent Pay 的所有可驗證公開事實。

---

## Agent Pay Demo Version

- **Demo Version:** Visible in Terminal output as `task_demo_20260522`
- **Demo Date:** 2026-05-22
- **Status:** Testnet developer demonstration

---

## M Hash L2 Network

| Field | Value |
|-------|-------|
| Chain Name | M Hash L2 Testnet |
| Chain ID | 20250827 |
| RPC | `https://l2-rpc.testnet.magicalhash.com` |
| Explorer | `https://l2-explorer.testnet.magicalhash.com` |

---

## Smart Contracts (Current Secure Deployment)

| Contract | Address | Status |
|----------|---------|--------|
| MockMHA (ERC-20 test token) | `0x13fadbC67B25870cF93DBa44f570f355dE456A2E` | Active |
| AITaskReceipt | `0xa0Fe7AD300152eeDC4ca0c17514A1001D6afA408` | Active |

---

## Archived Deployment (DO NOT USE)

| Contract | Address | Security Note |
|----------|---------|---------------|
| MockMHA | `0x5FbDB2315678afecb367f032d93F642f64180aa3` | ⚠ Used publicly-known test key — do not use |
| AITaskReceipt | `0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512` | ⚠ Used publicly-known test key — do not use |

**Archive Reason:** The archived deployment used a publicly-exposed Hardhat test private key. A new secure deployment has been completed at the addresses listed above.

---

## Publicly Verifiable Records

### Receipt Transaction

| Field | Value |
|-------|-------|
| Receipt ID | `0x07bc0ca32a037ab755b4516641fba45fe93ac33ed8864bdd9928d7ac152390fd` |
| Transaction Hash | `0x07bc0ca32a037ab755b4516641fba45fe93ac33ed8864bdd9928d7ac152390fd` |
| Explorer Link | `https://l2-explorer.testnet.magicalhash.com/tx/0x07bc0ca32a037ab755b4516641fba45fe93ac33ed8864bdd9928d7ac152390fd` |
| Network | M Hash L2 (chainId: 20250827) |
| Demo Task | task_demo_20260522 |

---

## Contract Event

### AITaskReceiptCreated

```solidity
event AITaskReceiptCreated(
  bytes32 indexed taskId,
  address indexed agentId,
  address indexed recipient,
  uint256 amount,
  bytes32 paymentTxHash,
  uint256 timestamp
);
```

**Note:** This event is emitted on M Hash L2 when a receipt is finalized.

---

## Deployment Status Summary

| Item | Status | Note |
|------|--------|------|
| M Hash L2 Testnet Contract Deployment | ✅ Verified | Secure deployment at `0x13fadb...` / `0xa0Fe7A...` |
| AI Task Receipt Recording | ✅ Verified | Receipt `0x07bc0c...` on explorer |
| Public Explorer Reference | ✅ Available | `l2-explorer.testnet.magicalhash.com` |
| HTTP 402 Live Challenge | ⏳ In Development | Not yet deployed |
| Browser Wallet Authorization | ⏳ In Development | Not yet deployed |
| Facilitator Verify/Settle | ⏳ In Development | Not yet deployed |
| Formal x402 Compatibility | 🔍 Under Validation | Research ongoing |
| Production Deployment | 📋 Planned | Requires security audit |

---

## Contract Administration

| Role | Status | Note |
|------|--------|------|
| Contract Owner/Admin | Unknown | Not publicly disclosed |
| Mint Authority | Unknown | Not publicly disclosed |
| Upgrade Authority | Unknown | Not publicly disclosed |
| Pause Authority | Unknown | Not publicly disclosed |

**Required Action:** Before any production deployment, all contract administration rights must be identified, disclosed, and assessed.

---

## x402 Compatibility Status

- **Current:** "under-validation"
- **SKILL.md field:** `"x402Compatibility": "under-validation"`
- **Previous (incorrect):** `"x402Compatible": true`

**Note:** MAGNE Agent Pay references emerging x402-compatible patterns. No official x402 integration has been certified by the x402 Foundation or Linux Foundation.

---

## mMHA Token Note

mMHA is a **demo test asset** (ERC-20 test token) on M Hash L2 testnet. It is:
- ❌ NOT a production token
- ❌ NOT equivalent to MHA mainnet token
- ❌ NOT a formally issued security or utility token
- ✅ A test token for demo purposes only

---

## Production Deployment

**Is this a production deployment?** ❌ **NO**

This is a testnet developer demonstration. Production deployment will require:
1. Security audit
2. Controlled signing infrastructure
3. Contract administration procedures
4. Compliance assessment
5. Governance approval

---

## Demo Scope Limitations

The current demo verifies:
1. ✅ Smart contracts compile and deploy to M Hash L2 testnet
2. ✅ ERC-20 token (mMHA) can be transferred on M Hash L2
3. ✅ AITaskReceipt contract can emit events on M Hash L2
4. ✅ Receipt transaction is publicly verifiable on explorer

The current demo does NOT verify:
1. ❌ Real HTTP 402 payment challenge and retry flow
2. ❌ Browser wallet MetaMask authorization in production
3. ❌ Facilitator strictVerify in production conditions
4. ❌ x402 protocol compliance
5. ❌ Real-world payment dispute resolution

---

*Last updated: 2026-05-23*
*Document owner: MAGNE.AI Web3 Team*
