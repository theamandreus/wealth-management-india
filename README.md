# India Wealth Management Plugin for Claude

A comprehensive India-focused wealth management skill set for [Claude Cowork](https://claude.ai). Built for Indian investors, financial advisors, and SEBI-registered RIAs.

## What This Is

7 interconnected skills + 5 reference files that turn Claude into an India-specific financial planning assistant. Covers tax optimization, mutual funds, NPS, home loans, health insurance, financial planning, and investment proposals — all built on Indian tax law, Indian instruments, and Indian market realities.

## Skills

| Skill | What It Does |
|-------|-------------|
| **india-tax-optimizer** | Old vs New regime (FY 2025-26 slabs), 80C deep-dive with remaining room calculator, LTCG/STCG harvesting, HRA optimization |
| **india-financial-plan** | Full financial plan — retirement projections (EPF/PPF/NPS), education funding, estate planning, cash flow analysis |
| **india-mutual-fund-advisor** | Risk profiling, fund selection, SIP/STP/SWP strategy, portfolio audit, behavioural coaching, hidden bond detection |
| **india-nps-planner** | Tier 1 vs 2, Active vs Auto choice, 80CCD tax benefits, annuity modeling, fund manager comparison |
| **india-home-loan-planner** | Section 24/80C/80EEA benefits, joint loan optimization, HRA + home loan dual benefit, prepay vs invest framework |
| **india-health-insurance** | Family floater + super top-up sizing, parents coverage, 80D optimization, claim process |
| **india-investment-proposal** | Advisor-facing — generate client proposals with risk profiling, model portfolios, fee structures |

## Reference Files

Shared knowledge base used across skills:

| File | Contents |
|------|----------|
| `model-portfolios.md` | Risk-profile portfolios, SIP allocation tables, starter portfolios, retirement buckets |
| `goal-templates.md` | Goal targets, SIP calculator, step-up SIP impact, goal-by-goal playbooks |
| `rebalancing-rules.md` | Triggers, methods, safety rules, portfolio health score, hidden bond/debt exposure detection |
| `tax-rates-india.md` | FY 2025-26 slabs (both regimes), deductions, capital gains rates, key updates |
| `user-personas.md` | 8 user types with routing to specific skills and sections |

## Who Is This For

- **Individual investors** — plan taxes, pick mutual funds, build financial plans
- **First-time investors** — guided onboarding with starter portfolios
- **Financial advisors / RIAs** — generate proposals, audit client portfolios
- **Anyone with India-specific financial questions** — NPS, home loans, health insurance, 80C

## How to Use

### With Claude Cowork
Drop the `skills/` folder into your Cowork plugin directory. Skills will auto-trigger on relevant queries.

### As Reference
Read the SKILL.md files directly — each one is a comprehensive, standalone guide even without Claude.

## Key Design Decisions

- **FY 2025-26 tax slabs** — correct New Regime with 8 slabs, ₹4L exemption, ₹12L tax-free via 87A
- **3% withdrawal rate** (not 4%) — accounts for India's higher inflation
- **Hidden bond detection** — identifies when BAFs and equity savings funds secretly make your portfolio conservative
- **No wash sale in India** — tax harvesting strategy leverages this unique advantage
- **Cross-referenced skills** — every skill links to related skills and reference files
- **Persona-aware routing** — detects user type and routes to relevant sections

## Disclaimer

This is an educational framework, not personalized financial advice. Tax laws change frequently — verify with a Chartered Accountant. For investment advice, consult a SEBI-registered Investment Advisor (RIA). Mutual fund investments are subject to market risks.

## Contributing

PRs welcome. Especially for:
- Tax law updates (Union Budget changes)
- New instrument coverage (SGBs, REITs, InvITs, crypto)
- Regional language support
- Correcting any rates or limits

## License

MIT
