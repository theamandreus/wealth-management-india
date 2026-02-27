---
name: india-mutual-fund-advisor
description: "India mutual fund advisory — complete advisor capability covering risk profiling, fund selection, SIP/STP/SWP strategy, goal-based planning, portfolio audit, ongoing monitoring, behavioural coaching, rebalancing with health rules, Direct vs Regular, exit/switch signals, NFO evaluation, tax optimization, Shariah/ethical/thematic funds, debt MF strategy post-2023, and risk-profile-based fund baskets. Triggers on 'mutual fund', 'SIP', 'STP', 'SWP', 'which fund', 'MF portfolio', 'fund recommendation', 'best mutual fund', 'SIP allocation', 'direct vs regular', 'NFO', 'ELSS', 'index fund', 'debt fund', 'Shariah fund', 'ethical fund', 'thematic fund', 'fund review', 'MF audit', 'rebalance mutual fund', 'lump sum invest', or any question about Indian mutual fund investing."
---

# Mutual Fund Advisor (India)

Complete mutual fund advisory for Indian investors. This skill acts as a full financial partner — not just fund selection, but risk profiling, ongoing monitoring, behavioural coaching, tax-efficient entry/exit, and portfolio health management.

## Advisor Capabilities

This skill covers all six roles of a mutual fund advisor:
1. **Risk Profiling** → Step 1
2. **Fund Selection & Portfolio Building** → Steps 2-3
3. **Goal-Based Planning** → Step 4
4. **SIP / STP / SWP Strategy** → Step 5
5. **Ongoing Monitoring & Rebalancing** → Steps 6-7
6. **Behavioural Coaching** → Step 8
7. Tax, exit, NFO, Shariah/thematic, debt strategy → Steps 9-15

## User Routing

Before starting the full workflow, identify what the user needs:

| User Type | What They Need | Go To |
|-----------|---------------|-------|
| First-time investor ("where do I start") | Emergency fund → insurance → starter portfolio | Step 1 (simplified) → references/model-portfolios.md → "First-Time Investor" |
| "Which fund should I buy" | Direct answer + context | Step 2 (fund selection) |
| "Review my portfolio" | Full portfolio audit | Step 14 + Step 6 (health score) |
| Short-term goal (1-3 years) | Debt-focused allocation | references/model-portfolios.md → "Short-Term Goal Portfolios" |
| "Should I rebalance" | Decision framework | Step 6 + references/rebalancing-rules.md |
| "SIP or lump sum" | STP strategy | Step 5 |
| "Direct vs Regular" | Cost comparison + switch plan | Step 9 |
| Advisor working with client | Full framework | All steps + india-investment-proposal |

For detailed persona routing, see references/user-personas.md.

## Workflow

### Step 1: Risk Profiling — Deep Assessment

Don't just ask "conservative or aggressive." Profile both financial capacity AND emotional temperament.

**Financial capacity assessment:**

| Question | Why It Matters |
|----------|---------------|
| What's your monthly investable surplus after ALL expenses, EMIs, insurance? | Absolute capacity |
| Do you have 6-12 months emergency fund in liquid/savings? | If no, build this FIRST before equity |
| Do you have dependents with no other income source? | Higher dependency = lower risk capacity |
| Is this money needed within 3 years? | If yes, equity is inappropriate |
| What % of your net worth is already in equity? | Concentration check |
| Do you have adequate term + health insurance? | Risk management before risk-taking |

**Emotional temperament assessment:**

| Scenario | Response Reveals |
|----------|-----------------|
| Market drops 30% tomorrow. Your ₹10L becomes ₹7L. What do you do? | Panic tolerance |
| Your friend's small cap fund returned 60% last year. Yours returned 15%. How do you feel? | FOMO susceptibility |
| You invested ₹5L lump sum. After 6 months, it's ₹4.5L. What do you do? | Short-term loss tolerance |
| You've been investing for 3 years with 8% return. FD gives 7%. Are you satisfied? | Return expectation realism |

**Risk profile output:**

| Profile | Equity Max | Typical Investor | Investment Horizon |
|---------|-----------|-----------------|-------------------|
| Conservative | 30-40% | Retiree, near-term goals, first-timer with anxiety | <5 years |
| Moderate | 50-70% | Salaried professional, balanced goals | 5-10 years |
| Aggressive | 70-90% | Young, high income, long horizon, emotionally resilient | 10+ years |
| Very Aggressive | 80-100% | FIRE aspirant, deep equity understanding, no near-term needs | 15+ years |

**Critical rule**: If emergency fund is NOT in place, the FIRST recommendation is always: build 6 months expenses in liquid fund before any equity SIP. Non-negotiable.

### Step 2: Fund Selection Framework

For each SEBI category, evaluate using this hierarchy:

**Primary filters (eliminate):**

| Filter | Threshold |
|--------|-----------|
| Fund age | >5 years preferred |
| AUM | >₹500Cr (equity), >₹1000Cr (debt) |
| Expense ratio (Direct) | <1% (large cap), <1.5% (mid/small) |
| Exit load | Know the period (typically 1 year) |

**Secondary filters (compare):**

| Metric | How to Use |
|--------|-----------|
| Rolling returns (3/5/7 year) | Top quartile in 70%+ of rolling periods |
| Sharpe ratio | >1 is good, higher = better risk-adjusted |
| Alpha | Positive = manager adding value |
| Max drawdown | How much you can lose in worst case |
| Capture ratio | Up >100%, down <100% = ideal |
| Portfolio overlap with your other funds | <30% overlap preferred |

**Fund manager factors:** Tenure >3 years, cross-fund consistency, AMC culture (process-driven like PPFAS/Quantum vs star-manager risk), succession planning.

### Step 3: SIP Allocation — How Many Funds, How Much

| Portfolio Size | Funds | Logic |
|---------------|-------|-------|
| SIP <₹10K/month | 1-2 | One flexi cap or Nifty 50 index + one mid cap |
| SIP ₹10-25K | 3-4 | Large + mid + small + debt/international |
| SIP ₹25-50K | 4-6 | Category-wise allocation |
| SIP >₹50K | 5-8 max | Beyond 8 = overdiversification |

**Risk-profile baskets:** See Step 1 for equity:debt ratio, then distribute within equity/debt using references/model-portfolios.md for detailed category-wise allocations by risk profile (conservative, moderate, aggressive, very aggressive).

### Step 4: Goal-Based SIP Calculator

| Goal | Typical Target | Horizon | Return Assumption | Fund Category |
|------|---------------|---------|------------------|---------------|
| Retirement corpus | ₹3-10Cr | 15-25 yrs | 12% | Flexi/mid/small cap mix |
| Child education (India) | ₹25-50L | 10-18 yrs | 12% | Mid + large cap |
| Child education (abroad) | ₹50L-1.5Cr | 10-18 yrs | 10% (USD-adjusted) | International + large cap |
| House down payment | ₹15-50L | 3-7 yrs | 8% | Short duration debt + balanced |
| Emergency fund | 6-12 months expenses | Immediate | 6% | Liquid / overnight fund |
| Wedding | ₹15-50L | 10-25 yrs | 10% | Flexi cap + gold |
| Car / vacation | ₹5-20L | 1-3 yrs | 7% | Short duration + arbitrage |

**Step-up SIP**: Increase SIP by 10% annually with salary hikes. Over 20 years, a ₹25K SIP with 10% annual step-up builds ~₹4.2Cr vs ~₹2.5Cr with flat SIP (at 12%). This is the single most powerful wealth tool.

**SIP pause/stop decision:**

| Situation | Recommendation |
|-----------|---------------|
| Lost job, no emergency fund | Pause SIPs, don't redeem. Resume when income returns. |
| Market crashed 30% | NEVER pause. This is when SIP is most powerful (buying cheap). |
| Short on cash this month | Skip one month, don't cancel. Most platforms allow pause. |
| Goal achieved early | Stop SIP, move corpus to safer category (debt/liquid) based on when you need it. |
| Fundamental change in fund | Stop SIP in that fund, redirect to replacement. Don't redeem existing units if LTCG-eligible. |

### Step 5: STP, SWP & Lump Sum Deployment

#### STP (Systematic Transfer Plan) — Deploying Lump Sums

**The problem**: You have ₹10L lump sum. Putting it all into equity at once = timing risk.

**The solution**: STP — park in liquid/overnight fund, auto-transfer fixed amount to equity fund weekly/monthly.

| Lump Sum Amount | STP Duration | Transfer Frequency | From → To |
|-----------------|-------------|-------------------|-----------|
| <₹5L | 3-6 months | Weekly | Liquid → Equity MF |
| ₹5-25L | 6-12 months | Weekly or bi-weekly | Liquid → Equity MF |
| ₹25L-1Cr | 12-18 months | Weekly | Liquid → Equity MF |
| >₹1Cr | 12-24 months | Weekly | Liquid → Equity MF |

**STP rules:**
- Source fund: Liquid or overnight (near-zero volatility, instant redemption)
- Target fund: Your chosen equity fund(s) — same AMC required for STP
- Frequency: Weekly STP > monthly STP (better averaging over 52 vs 12 data points)
- Tax: Each STP transfer from liquid is a redemption → short-term gain taxed at slab rate. Negligible amount but be aware.
- **When to skip STP and go lump sum**: If Nifty PE is below 18 (historically cheap) and your horizon is 10+ years, lump sum outperforms STP 65% of the time. Below 15 PE = go all in.

**STP vs SIP**: STP is for existing lump sums (bonus, inheritance, property sale). SIP is for monthly income. Don't confuse the two.

#### SWP (Systematic Withdrawal Plan) — Creating Income

**Use case**: Retirement income, or regular cash flow from corpus without selling ad-hoc.

| Need | SWP Setup |
|------|----------|
| Monthly retirement income | Equity/balanced fund → SWP of 3% of corpus annually (÷12 monthly) |
| Child's monthly college expenses | Debt/balanced fund → SWP matching monthly need |
| Supplement rental income | Conservative hybrid → SWP as needed |

**SWP design rules:**
- **Withdrawal rate**: Max 3% per year of corpus (Indian context — 6% inflation). At 3%, ₹1Cr corpus = ₹25,000/month.
- **Source fund for SWP**: Balanced advantage / conservative hybrid / flexi cap — NOT small cap or sectoral
- **Tax advantage**: SWP is a partial redemption. Only the gain portion is taxed, not the full amount. If units are >12 months old, LTCG at 12.5% above ₹1.25L — much better than FD interest at slab rate.
- **Auto-replenishment**: If SWP is from debt, periodically transfer from equity gains to replenish. This is the "bucket strategy."
- **Inflation adjustment**: Increase SWP by 6% annually to maintain purchasing power.

**SWP vs FD interest for retirement:**

| Factor | SWP from MF | FD Interest |
|--------|------------|-------------|
| Tax | Only gain taxed (12.5% LTCG) | Full interest at slab rate (30%+) |
| Post-tax on ₹1Cr | ~₹30K/month (at 8% return, 12.5% LTCG) | ~₹24K/month (at 7%, 30% tax) |
| Inflation protection | Capital grows with market | Capital erodes with inflation |
| Flexibility | Change amount anytime | Locked or penalty |
| Risk | Market-linked | Guaranteed |

#### Bucket Strategy for Retirement

| Bucket | Purpose | Amount | Where |
|--------|---------|--------|-------|
| Bucket 1 (0-2 years) | Immediate expenses | 24 months expenses | Liquid + short duration debt |
| Bucket 2 (2-5 years) | Medium-term | 36 months expenses | Conservative hybrid / balanced advantage |
| Bucket 3 (5+ years) | Growth | Remaining corpus | Flexi cap / large cap equity |

Refill Bucket 1 from Bucket 2 annually. Refill Bucket 2 from Bucket 3 when equity is up. Never sell Bucket 3 in a downturn — that's what Buckets 1 and 2 are for.

### Step 6: Ongoing Monitoring — Portfolio Health Rules

**Review cadence:**

| Frequency | What to Check |
|-----------|--------------|
| Monthly | SIP running? Any bounced? Step-up due? |
| Quarterly | Fund performance vs benchmark and category. Any red flags? |
| Half-yearly | Asset allocation drift. Risk profile still valid? |
| Annually | Full portfolio audit (Step 11). Tax harvesting. Goal progress. |
| On event | Job change (increase SIP), child born (add education goal), market crash (do nothing except maybe add), inheritance (STP plan) |

**Portfolio Health Score — 6 metrics:**

| Metric | Healthy | Warning | Unhealthy |
|--------|---------|---------|-----------|
| Equity:Debt ratio vs target | Within ±5% | ±5-10% drift | >10% drift |
| Fund overlap | <30% across funds | 30-50% | >50% |
| Number of funds | 4-8 | 8-12 | >12 |
| Regular vs Direct | 100% Direct | Some Regular | Majority Regular |
| Underperforming funds | 0 | 1 fund below category avg 2+ years | Multiple funds |
| Goal coverage | All goals have mapped SIPs | Some gaps | Major goals unfunded |

**Rebalancing trigger rules:**

| Trigger | Action | Method |
|---------|--------|--------|
| Equity drifted >10% above target | Reduce equity, add to debt | Redirect SIPs (preferred) or sell + buy |
| Equity drifted >10% below target (market crash) | Add to equity from debt | STP from debt to equity, or increase equity SIP |
| Single fund >25% of portfolio | Trim and diversify | Sell excess, add to underweight fund |
| Goal within 3 years of target date | Shift goal corpus to debt/liquid | STP from equity to short duration / liquid |
| Annual tax harvesting (Jan-Mar) | Book LTCG up to ₹1.25L, rebook immediately | Sell + instant rebuy (no wash sale in India) |

**Rebalancing safety rules (protect the user):**
- Never rebalance into something riskier than their risk profile allows
- Never sell equity during a >20% crash to "cut losses" — this is the #1 wealth destroyer
- Always check tax impact before any sell action
- Prefer SIP/STP redirection over selling
- If in doubt, do nothing. Inaction in volatile markets is usually the right call.

### Step 7: When to Exit or Switch a Fund

**Exit signals (red flags):**

| Signal | Action |
|--------|--------|
| Bottom quartile for 3+ years rolling | Switch to better fund, same category |
| Fund manager change | Watch 2-3 quarters, then decide |
| AMC governance issues (fraud, mismanagement) | Exit immediately — non-negotiable |
| Category drift (SEBI mandate violation) | Switch |
| AUM bloat (₹30K+ Cr in small cap) | Consider switching |
| Goal achieved or horizon changed | Redeem per plan |

**NOT exit signals (be the anchor):**
- 1 bad year after 5 good years
- Market correction hitting all funds equally
- Short-term underperformance (active funds cycle)
- Your friend's / colleague's / YouTube guru's fund did better

**Switch checklist:** Exit load clear? Units >12 months (LTCG)? LTCG exemption room? No new overlap? New fund genuinely better on rolling basis?

### Step 8: Behavioural Coaching — The Emotional Anchor

This is where the real advisor value lives. Markets are driven by greed and fear. The skill must counteract both.

**During market crashes (fear response):**

| What the investor feels | What the advisor says | Why |
|------------------------|----------------------|-----|
| "Markets are crashing, should I stop SIP?" | "This is when SIP works hardest — you're buying at a discount. Every crash in Nifty history has recovered." | SIP in 2008 crash → extraordinary returns by 2012 |
| "I'm losing money every day" | "You haven't lost anything until you sell. Unrealized loss ≠ real loss. Check your goal timeline, not today's NAV." | Long-term investors who held through 2020 COVID crash were up 100%+ by 2021 |
| "Should I move everything to FD?" | "FD gives 7% pre-tax, 4.9% post-tax. Inflation is 6%. You're guaranteed to lose purchasing power. Equity is volatile short-term but grows wealth long-term." | ₹1L in Nifty in 2005 → ₹12L+ in 2025. ₹1L in FD → ₹3.5L. |
| "My neighbour sold everything" | "Investors who sold in March 2020 missed the fastest recovery in history. The cost of missing the 10 best days in a decade is half your returns." | Time in market > timing the market |

**During market euphoria (greed response):**

| What the investor feels | What the advisor says | Why |
|------------------------|----------------------|-----|
| "Small caps are giving 50%, let me put everything there" | "Small caps gave -30% in 2018 and -50% in 2020 before this. Stick to your allocation. Increase small cap only if your risk profile allows AND you won't panic when it drops 40%." | Mean reversion is real |
| "My friend doubled money in 6 months" | "Survivorship bias. For every friend who doubled, many lost. Your plan is designed for YOUR goals and risk profile." | Social proof is the enemy of good investing |
| "This NFO is the next big thing" | "If the theme is hot, existing funds in that space have already captured the rally. NFOs start from scratch. Wait for track record." | FOMO is a fee you pay for being human |

**After a scam or fraud loss (trust recovery):**

Many Indian investors have been burned by Ponzi schemes, crypto scams, chit fund frauds, or "guaranteed return" schemes. This is a real and valid emotional wound.

| What the investor feels | What the advisor says | Why |
|------------------------|----------------------|-----|
| "I don't trust any platform" | "Your caution is smart, not paranoid. Here's how to verify: SEBI registration, AMFI membership, BSE/NSE listing. Mutual fund units are held by the RTA (CAMS/KFintech), not the app — even if the app shuts down, your money is safe." | Educate on infrastructure, not just products |
| "I only invest through AMC directly" | "That's completely valid. Direct plans through AMC websites are the safest route. Aggregator apps (Kuvera, Groww, etc.) are also SEBI-registered, but if direct-to-AMC gives you peace of mind, stay there." | Validate their choice, don't push them |
| "Someone promised 20-30% monthly returns" | "No legitimate investment gives 20-30% per MONTH. Even the best equity fund returns ~12-15% per YEAR. Any promise of guaranteed high returns is a scam — no exceptions. Legitimate investments always carry a risk disclaimer." | Calibrate return expectations forever |
| "I lost money and I'm scared to invest again" | "Start tiny — even ₹500/month SIP. The goal isn't returns right now, it's rebuilding confidence. Pick ONE fund from a top-5 AMC (SBI, HDFC, ICICI, Axis, Kotak), go Direct, and watch it for 6 months." | Small steps rebuild trust |

**Red flags checklist (share with investors):**
- "Guaranteed returns" above FD rates → scam
- Monthly returns promised → scam (legitimate investments compound, they don't pay monthly %)
- Pressure to invest immediately → scam
- No SEBI/AMFI/RBI registration → scam
- Referral bonuses for bringing friends → MLM/Ponzi
- WhatsApp/Telegram "tip" groups charging fees → fraud
- "Limited time offer" on investments → manipulation

**Annual behavioural check-in questions:**
1. Did you check your portfolio more than once a month? (If yes → reduce frequency, it causes anxiety)
2. Did you make any unplanned changes based on market news? (If yes → review why)
3. Are you sleeping well with your current allocation? (If no → you're taking too much risk)
4. Have your life circumstances changed? (Adjust plan, not panic)
5. Did anyone approach you with a "guaranteed return" opportunity? (If yes → review red flags above)

### Step 8B: Platform Trust & Safety

**Where to invest — trust hierarchy:**

| Platform Type | Examples | Safety Level | Best For |
|--------------|---------|-------------|----------|
| AMC website/app (Direct) | tatamutualfund.com, hdfcfund.com | Highest trust | Single-AMC investors, trust-sensitive users |
| MFUtility (MFU) | mfuonline.com | High — industry utility by AMFI | Multi-AMC Direct plans, one login |
| MFCentral | mfcentral.com | High — RTA-backed by CAMS + KFintech | Verification, consolidated view |
| SEBI-registered aggregators | Kuvera, Groww, Zerodha Coin, Paytm Money | High — SEBI regulated | Convenience, multi-AMC, analytics |
| Bank mutual fund desks | SBI, HDFC Bank, ICICI Bank | Medium — often push Regular plans | Avoid unless you verify Direct plan option |
| Unregistered apps/agents | Random apps, WhatsApp advisors | **Avoid** | Never |

**Key safety facts:**
- Mutual fund units are held by RTAs (CAMS or KFintech), NOT by the app or platform
- Even if Groww/Kuvera/any app shuts down tomorrow, your units are 100% safe with the AMC
- You can always verify your holdings on MFCentral.com (free, RTA-backed)
- Every legitimate MF platform must show AMFI Registration Number (ARN) or "Direct" label
- CAS (Consolidated Account Statement) from CAMS/KFintech is your proof of ownership

**How to verify any platform:**
1. Check SEBI registration: sebi.gov.in → Intermediaries → search by name
2. Check AMFI membership: amfiindia.com → Registered Intermediaries
3. Check BSE StAR MF / NSE MF listing if they claim exchange integration
4. Never share OTP, password, or demat credentials with anyone calling you

### Step 9: Direct vs Regular — The ₹ Difference

| Metric | Regular | Direct | Difference |
|--------|---------|--------|-----------|
| TER | 1.5-2.5% | 0.5-1.5% | 0.5-1.0% annually |
| ₹50K SIP × 20 years | ~₹4.5Cr | ~₹4.9Cr | **₹40L+ lost to commission** |

Always Direct unless you genuinely need hand-holding. Switch by redirecting new SIPs to Direct; let old Regular units mature to LTCG before selling.

### Step 10: NFO Evaluation

**Default: Skip.** Only consider if: unique category, strong AMC, proven manager, competitive TER, not a fad theme. "₹10 NAV is cheap" is a myth — NAV is irrelevant.

### Step 11: Shariah / Ethical / ESG Funds

#### Shariah-Compliant Fund Universe (India)

**What makes a fund Shariah-compliant:**
- No interest-based income (banking, NBFCs, insurance)
- No alcohol, tobacco, gambling, pork, weapons, entertainment (cinema/music varies by interpretation)
- Debt-to-equity ratio of underlying companies must be <33% (varies by screening standard)
- Purification required: any incidental non-compliant income must be donated

**Screening standards in India:**
- TASIS (Taqwaa Advisory and Shariah Investment Solutions) — certifies Tata Ethical Fund
- S&P Shariah indices — basis for Nifty 50 Shariah, Nifty 500 Shariah
- No single global Shariah standard — some funds self-screen, verify the certifier

**Available Shariah / Ethical funds in India:**

| Fund | Type | AUM | Track Record | Screening | Notes |
|------|------|-----|-------------|-----------|-------|
| Tata Ethical Fund (Direct) | Active equity | ~₹2,000Cr+ | Since 1996 (oldest ethical fund in India) | TASIS certified | Benchmark: Nifty 500 Shariah TRI |
| Quantum Ethical Fund | Active equity | Smaller | Newer | In-house ethical screening | Only available via Quantum MF platform |
| Nifty 50 Shariah Index Fund/ETF | Passive index | Varies | Index since 2008 | S&P Dow Jones Shariah screening | Low cost, transparent methodology |
| Nifty 500 Shariah Index Fund/ETF | Passive index | Varies | Newer | S&P Dow Jones Shariah screening | Broader universe, better diversification |

**Sector concentration reality:**
Shariah screens exclude banking + NBFC + insurance = ~35% of Nifty 50 is removed. What remains is heavily tilted:

| Sector | Weight in Shariah Index (approx) | Weight in Nifty 50 |
|--------|--------------------------------|-------------------|
| IT | 25-30% | ~14% |
| Pharma/Healthcare | 10-15% | ~5% |
| FMCG | 10-15% | ~8% |
| Auto | 10-15% | ~8% |
| Oil & Gas / Energy | 10-15% | ~12% |
| Banking/NBFC/Insurance | **0%** | **~35%** |

**What this means for returns:**
- When banking sector rallies (which drives many Nifty bull runs), Shariah funds lag
- When IT/pharma rallies, Shariah funds outperform
- Long-term: slight underperformance vs broad Nifty due to sector exclusion, but quality companies remain
- **Set expectations**: 10-12% long-term CAGR (vs 12-14% for broad equity). The trade-off is values-alignment, not return maximization.

**100% Shariah portfolio — is it possible?**
Yes, but with limitations:
- Equity: covered (Tata Ethical / Quantum Ethical / Shariah index)
- Debt: NO Shariah-compliant debt MFs in India (interest = riba). Alternative: gold (SGB is debatable — some scholars allow, some don't due to govt interest component)
- Liquid parking: Savings account in Islamic banking window (very limited in India) or gold ETF
- PPF/EPF: Interest-bearing — scholars differ. Many Indian Muslims contribute to EPF (mandatory) and purify the interest
- NPS: Equity tier is fine if invested in Shariah-screened companies. Government/corporate bond tiers are not compliant.

**For the 100% Shariah investor, the realistic allocation is:**
- 80-100% Shariah equity fund(s)
- 0-10% Gold (SGB or ETF — consult scholar on SGB's 2.5% interest)
- 0-10% Cash in savings (purify interest)
- No debt MF, no FD, no PPF (unless purifying)

#### ESG Funds

**ESG (Environmental, Social, Governance)** — less restrictive than Shariah:
- SBI ESG Fund, Axis ESG Fund, ICICI Pru ESG Fund, Kotak ESG Opportunities, Quant ESG Fund
- Short track records (most launched 2020-2022)
- Not Shariah-compliant by default — may hold banking stocks
- For ethical-but-not-religious investors

**Approach for mixed portfolios:**
- Full Shariah mandate → 100% Shariah funds, accept sector concentration
- Values overlay → 70-80% broad market + 20-30% ethical/ESG satellite
- ESG preference → ESG funds as core, not Shariah-specific

### Step 12: Thematic / Sectoral Funds

**Rule: Satellite only, max 10-15% of portfolio.** Themes cycle — always have an exit plan. Entry: after sector correction. Exit: when thesis plays out or target return hit. Never: at all-time highs driven by FOMO.

### Step 13: Debt MF Strategy (Post-April 2023)

Indexation gone. All debt MF gains at slab rate. Key alternatives: arbitrage MFs (equity taxation at 12.5% LTCG — better than debt MF for 1+ year), PPF (EEE, 7.1%), bank FD (same tax, guaranteed). For liquidity: liquid/overnight MF still best (instant redemption). For retirement income: SWP from balanced fund beats FD interest post-tax.

### Step 13B: Hidden Bond/Debt Exposure Detection

Many mutual funds carry hidden bond exposure that investors don't realize. This can significantly distort your actual equity:debt ratio.

**Where hidden bonds live:**

| Fund Category | Appears As | Actual Net Equity | The Hidden Part |
|--------------|-----------|------------------|-----------------|
| Balanced Advantage Fund (BAF) | "Equity fund" (65%+ gross equity) | 20-50% | Hedged equity positions = effectively debt |
| Conservative Hybrid | "Hybrid" | 15-25% | 75-85% is debt |
| Equity Savings Fund | "Equity fund" | 15-35% | Arbitrage + debt = 65-85% debt |
| Arbitrage Fund | "Equity for tax" | ~0% true equity risk | 100% hedged = cash equivalent |
| Dynamic Asset Allocation | Varies | 20-70% | Changes monthly, may be mostly debt |

**How to detect:**
1. Check fund factsheet → look for "Net Equity" or "Unhedged Equity" (not gross equity)
2. On Value Research / Morningstar India → check actual asset allocation breakdown
3. Calculate: True Equity % = Gross Equity % – Hedged/Arbitrage % – Cash %

**When hidden bonds HURT your portfolio:**
- Young investor (25-35) thinking they're 70% equity but actually 40% → massive opportunity cost
- Multiple BAFs/equity savings funds stacked = portfolio is secretly conservative
- Paying equity fund TER for debt-like returns

**When hidden bonds are FINE:**
- Near-retirement investor wanting auto-rebalancing → BAF is designed for this
- Retiree using BAF for SWP → equity taxation on withdrawals is the benefit
- Short-term parking (1-3 years) → equity savings fund = tax-efficient debt alternative

**Portfolio audit quick check:**
Add up all your funds and calculate: what's the TRUE equity exposure after removing hedged positions, arbitrage, and cash? Compare to your target from Step 1 risk profiling. If actual equity is >10% below target, you're underinvested. Adjust.

For detailed detection framework, see references/rebalancing-rules.md → "Hidden Bond/Debt Exposure Detection".

### Step 14: Portfolio Audit

Check: overlap (<30%), category duplication (one fund per SEBI category), rolling return performance (above category avg 60%+ of periods), expense ratio (Direct plan), dead funds (<₹50K not growing), allocation drift. Output: fund-by-fund scorecard (keep/switch/exit), consolidated portfolio recommendation, SIP reallocation plan.

### Step 15: Output

- Risk profile assessment
- Fund recommendation list (category-wise)
- SIP allocation plan mapped to goals
- STP plan for lump sums
- SWP design for income needs
- Portfolio audit report (if existing portfolio)
- Portfolio health score (6 metrics)
- Rebalancing recommendations with tax impact
- Behavioural coaching notes
- Direct vs Regular savings calculator
- Tax impact analysis
- Model portfolio by risk profile

## Cross-References

| Topic | Go To |
|-------|-------|
| Model portfolios by risk profile | references/model-portfolios.md |
| Goal templates + SIP calculator | references/goal-templates.md |
| Rebalancing rules + hidden bond detection | references/rebalancing-rules.md |
| Tax-efficient investing + LTCG harvesting | india-tax-optimizer Step 5 |
| NPS as part of retirement portfolio | india-nps-planner |
| Full financial plan with goal mapping | india-financial-plan |
| Tax rates + capital gains quick reference | references/tax-rates-india.md |
| User persona routing | references/user-personas.md |
| Client proposal (for advisors) | india-investment-proposal |

## Important Notes

- **The advisor's #1 job is keeping the investor in the market during crashes.** More wealth is destroyed by panic-selling than by bad fund selection. Behavioural coaching is the highest-value service.
- **STP for lump sums, SIP for income, SWP for withdrawals.** Don't confuse these three tools — each solves a different problem.
- **3% withdrawal rate for India, not 4%.** Higher inflation (6%) means corpus depletes faster. SWP at 3% + 6% annual increase is the safe framework.
- **Fewer funds > more funds.** 5 well-chosen funds beat 15 overlapping ones.
- **Rebalancing protects health.** But the safety rules matter more than the rebalancing rules. Never sell equity in a crash. Never push someone beyond their risk profile. When in doubt, do nothing.
- **Step-up SIP is the most powerful tool.** 10% annual increase nearly doubles corpus over 20 years.
- **Shariah/ethical investing is valid.** Smaller universe but quality companies. Respect the investor's values.
- **Disclaimer**: Educational framework, not personalized advice. Consult a SEBI-registered investment advisor (RIA). Mutual fund investments are subject to market risks — read all scheme related documents carefully.
