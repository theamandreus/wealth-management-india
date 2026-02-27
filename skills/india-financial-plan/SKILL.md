---
name: india-financial-plan
description: "Build or update a comprehensive financial plan for Indian clients covering retirement projections (EPF/PPF/NPS), education funding, estate/succession planning, and cash flow analysis with Indian tax regime optimization. Use for new client onboarding, annual plan reviews, or scenario modeling. Triggers on 'financial plan', 'retirement plan', 'can I retire', 'education funding', 'estate plan', 'cash flow analysis', 'plan update', 'FIRE India', 'retirement corpus', or any planning question involving Indian tax, EPF, PPF, NPS, or Section 80C."
---

# Financial Plan (India)

Build or update a comprehensive financial plan for Indian residents. All amounts in ₹ (INR). This skill accounts for Indian tax law, retirement vehicles (EPF/PPF/NPS), inflation dynamics, and succession planning.

## Workflow

### Step 1: Client Profile

Gather or confirm:

- **Demographics**: Age, spouse age, dependents (children + dependent parents), city of residence
- **Employment**: CTC, in-hand salary, employment type (salaried/self-employed/business), expected increment %
- **Retirement accounts**: EPF balance + contribution, VPF, PPF balance + contribution, NPS Tier 1 & 2, superannuation, gratuity estimate
- **Investments**: Mutual funds (ELSS, equity, debt, hybrid), direct equity, FDs, RDs, gold (physical/SGB/ETF), real estate, NSC, SCSS, Sukanya Samriddhi
- **Income sources**: Salary (split: basic, HRA, special allowances), rental income, interest income, dividend income, freelance/consulting, capital gains
- **Expenses**: Current annual spending with metro-specific categories (domestic help, school fees, society maintenance)
- **Liabilities**: Home loan, car loan, personal loan, education loan (80E), gold loan, credit card dues, LAP
- **Insurance**: Term life, endowment, ULIP, health (family floater + parents), personal accident, critical illness
- **Estate**: Will status, nominations across all accounts, HUF, trust, POA, digital asset list
- **Parents**: Ages, dependency status, health insurance coverage, ongoing medical costs

### Step 2: Cash Flow Analysis

Build annual cash flow projections:

| Year | Age | CTC (₹) | In-Hand (₹) | Tax Paid | Living Expenses | EMIs | Investments | Net Cash Flow |
|------|-----|---------|-------------|----------|-----------------|------|-------------|--------------|
| | | | | | | | | |

Key inputs:
- **Inflation**: 6% general (India CPI), 10% healthcare, 10% education, 8% lifestyle (metro)
- **Tax regime**: Old vs New — model both and recommend optimal
- **Savings rate**: Where savings go — EPF (mandatory), VPF, PPF, NPS, ELSS, MF SIPs, FD
- **Tax deductions**: 80C (₹1.5L), 80D (₹25K/₹50K/₹75K), 80CCD(1B) (₹50K), 80E, Section 24 (₹2L), 80EEA, HRA exemption

### Step 3: Retirement Projections

**Accumulation Phase:**
- Current corpus: EPF + PPF + NPS + MF + equity + FD + gold + real estate
- Annual contributions by vehicle (mandatory EPF + voluntary investments)
- Expected returns by asset class:
  - Equity (large cap): 12% nominal
  - Equity (mid/small): 14% nominal
  - Debt MF: 7%
  - PPF: 7.1% (govt rate, variable)
  - EPF: 8.25% (current rate)
  - NPS equity: 10%, NPS debt: 8%
  - FD: 7%
  - Gold: 8%
  - Real estate: 5-6%

**Distribution Phase:**
- Required annual spending in retirement (today's ₹ → inflation-adjusted at 6%)
- EPF lump sum at retirement + EPS pension (typically ₹1,000-9,000/month — model realistically)
- NPS: 60% lump sum (tax-free) + 40% annuity (at ~6% annuity rate)
- PPF maturity proceeds
- Rental income (if investment property)
- Systematic Withdrawal Plan (SWP) from mutual funds
- FD ladder for stable income

**Key Output:**
- Projected corpus at retirement age
- Sustainable withdrawal rate: **use 3% for India** (not 4% — higher inflation erodes purchasing power faster)
- Probability of corpus lasting through planning age (target >85%)
- Year-wise corpus depletion chart
- "What if" scenarios: retire early, market crash, higher healthcare costs, parent care event

### Step 4: Goal-Specific Analysis

#### Education Funding
- Children's ages and target education year
- Target: India engineering (₹15-25L), India MBA (₹25-35L), US Masters (₹40-80L), US Undergrad (₹80L-1.5Cr)
- Education inflation: 10% annually
- Current savings: dedicated MF/FD earmarked for education
- Sukanya Samriddhi (if daughters, up to age 10 at account opening)
- Required monthly SIP to reach goal
- Education loan option: interest deductible under 80E for 8 years

#### Children's Wedding
- Common Indian goal — typically ₹15-50L depending on family expectations
- Timeline: usually 20-30 years out for young children
- Dedicated SIP or gold accumulation strategy

#### Estate & Succession Planning
India has NO estate/inheritance tax currently, but succession planning is critical:
- **Will**: Drafted and registered? Covers all asset classes?
- **Nominations**: Updated on every account — bank, demat, MF, insurance, EPF, PPF, NPS?
- **Joint holdings**: First holder vs joint holder implications
- **HUF**: Is a Hindu Undivided Family account being used for tax optimization?
- **Trust**: Discretionary or specific? For minor children or estate planning?
- **Digital assets**: Crypto, digital gold, online accounts — documented?
- **POA**: General or specific, for medical and financial decisions?
- **Succession law**: Hindu Succession Act / Indian Succession Act / Muslim Personal Law — which applies?

#### Risk Management
- **Term insurance**: 10-15x annual income as death benefit (not endowment/ULIP which are investment + insurance hybrids)
- **Health insurance**: Family floater ₹10L-25L + super top-up ₹25-50L + separate policy for parents (80D benefit)
- **Critical illness**: ₹25-50L standalone cover
- **Personal accident**: 10x annual income
- **No LTC concept in India** — model healthcare costs as a separate retirement expense bucket (₹50L-1Cr at 10% inflation)

### Step 5: Tax Optimization

Use india-tax-optimizer for detailed regime analysis and 80C optimization. For quick reference, use references/tax-rates-india.md.

**FY 2025-26 Quick Reference:**

| Regime | Key Thresholds |
|--------|---------------|
| New (Default) | ₹4L exempt, 5%/10%/15%/20%/25%/30% slabs, ₹12L tax-free via 87A, salaried ₹12.75L tax-free |
| Old | ₹2.5L exempt, 5%/20%/30% slabs, all deductions (80C/80D/HRA/Sec24) available |

Model both regimes side-by-side:

| Component | Old Regime | New Regime |
|-----------|-----------|-----------|
| Gross Income | | |
| (-) HRA Exemption | | N/A |
| (-) Standard Deduction | ₹50K | ₹75K |
| (-) Section 80C | ₹1.5L max | N/A |
| (-) Section 80D | ₹25-100K | N/A |
| (-) 80CCD(1B) NPS | ₹50K | N/A |
| (-) Section 24 (home loan) | ₹2L max | N/A |
| Taxable Income | | |
| Tax Payable | | |
| (-) Section 87A Rebate | if ≤₹5L | if ≤₹12L (max ₹60K) |
| (+) 4% Cess | | |
| **Total Tax** | | |
| **Effective Rate** | | |
| **Recommendation** | | |

**Investment tax implications (post Finance Act 2024):**
- LTCG on equity: 12.5% above ₹1.25L/year
- STCG on equity: 20%
- Debt MF: Taxed at slab rate (no indexation post Apr 2023)
- FD interest: Taxed at slab rate (TDS at 10% above ₹40K; ₹1L for senior citizens from FY 2025-26)
- PPF/EPF: EEE (exempt-exempt-exempt) — most tax efficient
- NPS: Partial EEE (60% tax-free at maturity, 40% annuity taxable)
- Gold: LTCG after 2 years, taxed at 12.5%
- Real estate: LTCG after 2 years, taxed at 12.5%
- SGB (held to maturity): Completely tax-free capital gains

### Step 6: Scenario Modeling

Run key scenarios:

| Scenario | Corpus at Retirement (₹Cr) | Lasts Until Age | Notes |
|----------|---------------------------|-----------------|-------|
| Base case | | | |
| Retire 3 years early | | | |
| 30% market crash in Year 1 | | | |
| Higher spending (+25%) | | | |
| One child studies abroad | | | |
| Parent healthcare event (₹30L) | | | |
| One spouse lives to 90 | | | |
| Rental income stops | | | |
| Job loss for 1 year | | | |

### Step 7: Recommendations

Prioritized action items:
1. **Savings rate**: Increase SIP amount, optimize EPF/VPF contribution
2. **Tax regime**: Switch to Old/New based on analysis
3. **80C optimization**: EPF > PPF > ELSS > NPS (prioritize by lock-in and returns)
4. **Insurance gaps**: Term life adequate? Health cover for parents? Super top-up?
5. **Asset allocation**: Equity/debt/gold ratio appropriate for age and goals?
6. **NPS**: Additional 80CCD(1B) ₹50K for extra tax saving
7. **Home loan**: Prepay vs invest? (Compare loan rate vs post-tax investment return)
8. **Estate**: Will, nominations, POA — all in order?
9. **Emergency fund**: 6-12 months expenses in liquid fund/savings

### Step 8: Output

- Financial plan document (Word/PDF, 15-25 pages)
- Cash flow projection spreadsheet (Excel) with year-wise projections
- Retirement corpus growth and depletion charts
- Goal funding analysis with required SIP amounts
- Tax regime comparison (Old vs New)
- Scenario comparison table
- Action item checklist with priority and timeline

## Cross-References

| Topic | Go To |
|-------|-------|
| Tax regime analysis + 80C deep dive | india-tax-optimizer |
| Mutual fund selection + SIP strategy | india-mutual-fund-advisor |
| NPS planning + annuity modeling | india-nps-planner |
| Home loan tax optimization | india-home-loan-planner |
| Health insurance planning + 80D | india-health-insurance |
| Model portfolios by risk profile | references/model-portfolios.md |
| Goal templates + SIP calculator | references/goal-templates.md |
| Rebalancing rules + portfolio health | references/rebalancing-rules.md |
| Tax rates quick reference | references/tax-rates-india.md |
| User persona routing | references/user-personas.md |

## Important Notes

- **Inflation is the silent killer in Indian planning.** At 6% inflation, ₹1L today = ₹55K in 10 years. At 10% healthcare inflation, medical costs double every 7 years. Always stress-test for higher inflation.
- **3% withdrawal rate, not 4%.** The US 4% rule assumes 2-3% inflation. India's 6% inflation means a 4% withdrawal rate has a high failure probability. Use 3% or model a dynamic withdrawal strategy.
- **EPF/PPF are the bedrock.** EEE tax status makes them the most efficient vehicles. Max out before chasing higher returns in taxable instruments.
- **Don't ignore parents.** Elder care costs are a uniquely Indian planning challenge — health insurance for parents, potential long-term care costs, and emotional/financial support obligations.
- **Real estate ≠ investment for most.** Rental yield in Indian metros is 2-3%. Factor in maintenance, vacancy, legal hassles, and illiquidity before counting property as an investment asset.
- **Gold is cultural but also financial.** SGBs give 2.5% interest + gold price appreciation + tax-free LTCG at maturity (8 years). Better than physical gold for investment.
- **Review annually** or after: job change, marriage, child birth, property purchase, parent health event, tax law change.
- **Disclaimer**: This is a planning framework, not personalized financial advice. Consult a SEBI-registered investment advisor (RIA) for specific recommendations.
