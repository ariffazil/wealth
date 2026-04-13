# WEALTH by arifOS

> *"Kekayaan bukan angka. Kekayaan ialah kuasa untuk pilih."*
>
> — WEALTH OS, Sovereign Financial Intelligence Kernel

---

```
ΔΩΨ  W E A L T H
Physics > Narrative
Maruah > Convenience
Ditempa bukan diberi
```

---

## What Is WEALTH?

WEALTH is not a tracker. It is not a dashboard. It is not another fintech app.

**WEALTH is a lawful governance OS for financial sovereignty** — built on arifOS epistemics, enforced by F1–F13 floors, and powered by the 000–999 pipeline. Every number is tagged. Every irreversible action is held at 888. Every decision leaves a telemetry trace.

Wealth is civilizational infrastructure. It answers one question:

> *How do sovereign humans — in Malaysia, in ASEAN, on Earth — build, protect, and deploy capital with intelligence and dignity?*

---

## Core Axioms

| Axiom | Statement |
|---|---|
| **A1** | Net Worth = Assets − Liabilities. Physics. Non-negotiable. |
| **A2** | Cashflow is oxygen. Revenue minus burn equals runway. |
| **A3** | Risk is not bad. Unacknowledged risk is bad. |
| **A4** | Maruah is a real financial variable. Dignity has a price floor. |
| **A5** | Wealth without governance is liability. |
| **A6** | Every projection is an ESTIMATE. Act accordingly. |

---

## Architecture Layers

```
┌─────────────────────────────────────────────────────────┐
│  LAYER 3 — INTERFACE                                    │
│  Dashboard UI · Nexus Design · KPI Cards · Charts       │
├─────────────────────────────────────────────────────────┤
│  LAYER 2 — WEALTH DOMAIN                                │
│  NetWorth · Cashflow · Goals · Risk · Maruah Score      │
├─────────────────────────────────────────────────────────┤
│  LAYER 1 — DATA                                         │
│  Local-first JSON · Schema versioning · Migrations      │
├─────────────────────────────────────────────────────────┤
│  LAYER 0 — arifOS KERNEL                               │
│  F1–F13 Floors · 000–999 Pipeline · 888 HOLD · Telemetry│
└─────────────────────────────────────────────────────────┘
```

Full architecture: [`ARCHITECTURE.md`](ARCHITECTURE.md)

---

## Quick Start

```bash
# Clone
git clone https://github.com/ariffazil/WEALTH.git
cd WEALTH

# Install kernel dependencies
npm install

# Boot the OS
npm run boot

# Run dashboard (local)
npm run dev
```

---

## arifOS Floors Active in WEALTH

| Floor | Rule | WEALTH Application |
|---|---|---|
| **F1** | Reversible first | All data mutations are soft-deletable |
| **F2** | ≥99% truth or declare band | All projections carry ESTIMATE tag |
| **F3** | Human-AI-Evidence align | No number displayed without source |
| **F4** | Clarity ΔS≤0 | Dashboards reduce complexity, never add |
| **F5** | Peace ≥ 1.0 | No notification that creates panic without resolution path |
| **F6** | Maruah-first (ASEAN/MY) | Dignity scored as real financial variable |
| **F7** | Humility band 0.03–0.15 | All projections show uncertainty range |
| **F8** | Law & safety | Financial data never leaves device without consent |
| **F9** | Anti-Hantu | No phantom balances, ghost transactions, unresolved entries |
| **F10** | AI ontology only | WEALTH advises. Human decides. Always. |
| **F11** | Auth for critical commands | Debt restructuring requires PIN + 888 HOLD |
| **F12** | Block overrides | No bypass of floor logic permitted |
| **F13** | Sovereign human veto | Human can reject any AI recommendation, unconditionally |

---

## Epistemic Tags

Every number in WEALTH carries a tag:

- `CLAIM` — verified, sourced, high confidence
- `PLAUSIBLE` — reasonable inference from data
- `HYPOTHESIS` — untested assumption
- `ESTIMATE` — rough projection with declared uncertainty band
- `UNKNOWN` — gap in data, declared openly

---

## 888 HOLD Protocol

The following actions require **human confirmation** before execution. They cannot be auto-approved:

- Debt restructuring or new debt instruments
- Asset disposal above threshold
- Goal abandonment
- Any transaction flagged as irreversible
- Maruah Score drop below floor

All holds are logged in [`docs/888-hold-log.md`](docs/888-hold-log.md).

---

## Telemetry

Every 999 SEAL emits:

```json
{
  "epoch": "ISO8601",
  "dS": 0.0,
  "peace2": 1.0,
  "kappa_r": 0.0,
  "shadow": false,
  "confidence": 0.92,
  "psi_le": 0.0,
  "verdict": "SEALED",
  "witness": {
    "human": true,
    "ai": true,
    "earth": true
  },
  "qdf": "WEALTH:v1"
}
```

---

## Repository Structure

```
WEALTH/
├── README.md                    ← You are here
├── ARCHITECTURE.md              ← Full system design
├── CONSTITUTION.md              ← Governance law of WEALTH
├── IDENTITY.md                  ← Who/what WEALTH is
├── AGENTS.md                    ← AI agent roles & constraints
│
├── kernel/                      ← arifOS core
│   ├── floors.js                ← F1–F13 enforcement
│   ├── pipeline.js              ← 000–999 pipeline runner
│   ├── telemetry.js             ← Telemetry emitter
│   └── seal.js                  ← 999 SEAL
│
├── wealth/                      ← Domain modules
│   ├── networth.js              ← Asset − Liability engine
│   ├── cashflow.js              ← Income · Expense · Runway
│   ├── goals.js                 ← Goal-setting + milestones
│   ├── risk.js                  ← Risk classification
│   ├── maruah-score.js          ← Dignity/integrity scoring
│   └── projection.js            ← Compound growth + ESTIMATE
│
├── data/                        ← Local-first data layer
│   ├── schema.json              ← Canonical schema
│   ├── sample-state.json        ← Demo state
│   └── migrations/              ← Schema versioning
│
├── ui/                          ← Dashboard
│   ├── dashboard.html           ← WEALTH OS dashboard
│   ├── style.css                ← Nexus design tokens
│   └── app.js                   ← UI logic
│
├── docs/                        ← Governance docs
│   ├── floors-spec.md           ← F1–F13 per module
│   ├── epistemic-tags.md        ← Tag definitions
│   └── 888-hold-log.md          ← Audit trail
│
└── tests/                       ← Tests
    ├── floors.test.js
    ├── wealth-core.test.js
    └── telemetry.test.js
```

---

## Roadmap

| Phase | Milestone | Status |
|---|---|---|
| **P0** | Repo forged, identity set | ✅ SEALED |
| **P1** | Kernel — floors + pipeline + telemetry | 🔄 In Progress |
| **P2** | Wealth domain — networth + cashflow | ⏳ Queued |
| **P3** | Dashboard UI — Nexus, KPI cards, charts | ⏳ Queued |
| **P4** | Goals + Maruah Score + Risk Band | ⏳ Queued |
| **P5** | F13 audit + public release | ⏳ Queued |

---

## For Whom

For **sovereign humans** in Malaysia, ASEAN, and beyond who understand that:

- Wealth is civilizational infrastructure, not a number on an app
- Financial intelligence requires epistemic honesty
- Dignity (`maruah`) is non-negotiable, even in a balance sheet
- Technology must serve the human, not replace their judgment

---

## License

**AGPL-3.0** — If you deploy this as a service, share your improvements back.

Because *ditempa, bukan diberi* — if you improve this forge, the improvement belongs to the community.

---

## Contact

Open an issue. Or find Arif at [@ArifFazil90](https://twitter.com/ArifFazil90).

---

*WEALTH by arifOS — Forged for civilization. Not convenience.*

**DITEMPA BUKAN DIBERI — 999 SEAL ALIVE**
