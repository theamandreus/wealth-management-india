# User Persona Routing Guide

How to identify the user type and route them to the right skill + section.

## Persona Detection & Routing

### 1. First-Time Investor ("I want to start investing")

**Signals:** "beginner", "new to investing", "where do I start", "first time", "don't know anything about MF", "how to invest"

**What they need (in order):**
1. Emergency fund check → 6 months expenses in Liquid Fund FIRST
2. Insurance check → Term life (10-15x income) + Health cover (₹15-25L family floater)
3. Basic risk profiling → india-mutual-fund-advisor Step 1 (simplified)
4. Starter portfolio → references/model-portfolios.md → "First-Time Investor Starter Portfolios"
5. One or two SIPs → Nifty 50 Index + Flexi Cap (that's it, don't overwhelm)

**What they DON'T need:** 15-step MF advisory, STP/SWP, NFO evaluation, thematic funds, rebalancing
**Tone:** Simple, reassuring, no jargon. Define every term.
**Key message:** "Start small, start early. A ₹5K SIP in Nifty 50 Index is better than waiting 2 years to find the 'perfect' fund."

---

### 2. Specific Investment Seeker ("Should I invest in X?")

**Signals:** "which ELSS fund", "best small cap fund", "is NFO worth it", "SGB or gold ETF", "NPS vs PPF", "debt fund or FD", "Shariah fund options"

**Route by topic:**
| Query | Skill + Section |
|-------|----------------|
| ELSS / tax saving fund | india-tax-optimizer Step 3 + india-mutual-fund-advisor Step 2 |
| NPS questions | india-nps-planner (dedicated skill) |
| Small/mid/large cap fund | india-mutual-fund-advisor Step 2 (fund selection) + Step 3 (allocation) |
| SGB / gold | references/model-portfolios.md (gold allocation section) |
| Debt fund vs FD | india-mutual-fund-advisor Step 13 (post-2023 debt strategy) |
| Shariah / ethical | india-mutual-fund-advisor Step 11 |
| NFO | india-mutual-fund-advisor Step 10 |
| International fund | references/model-portfolios.md (international allocation) |

**What they need:** Direct answer to their specific question, then context on how it fits their overall portfolio.
**What they DON'T need:** Full financial plan. Answer the question first, then offer broader review.

---

### 3. Portfolio Review Seeker ("Review my portfolio")

**Signals:** "review my mutual funds", "is my portfolio good", "portfolio review", "too many funds", "my holdings are...", "CAS statement"

**What they need (in order):**
1. List all holdings with current values
2. Portfolio health score → references/rebalancing-rules.md → 6 metrics
3. Hidden bond exposure check → references/rebalancing-rules.md → "Hidden Bond/Debt Exposure Detection"
4. Fund overlap analysis → Flag >30% overlap between any two funds
5. Underperformer identification → Any fund below category average for 2+ rolling years
6. Direct vs Regular check → Flag Regular plan funds (commission drag)
7. Fund-by-fund verdict: Keep / Switch / Exit
8. Consolidated recommendation with SIP reallocation

**Related skills:** india-mutual-fund-advisor Step 14 (portfolio audit) + Step 6 (health score) + Step 7 (exit signals)

**Key questions to ask:**
- "Can you share your full holdings with amounts?"
- "What are your goals and timelines?"
- "When did you last review this portfolio?"

---

### 4. First-Time MF User with Short-Term Goals ("Save for X in 1-3 years")

**Signals:** "save for wedding", "house down payment in 2 years", "vacation fund", "car purchase", "short term", "1-2 year goal", "safe investment"

**Critical rule:** Money needed within 3 years should NEVER be in equity.

**Route to:** references/goal-templates.md → "Short-Term Goal Portfolios"

| Horizon | Recommendation |
|---------|---------------|
| <6 months | Savings account or Liquid Fund |
| 6-12 months | Liquid Fund + Overnight Fund |
| 1-2 years | Short Duration Debt MF + Arbitrage Fund |
| 2-3 years | Short Duration + Conservative Hybrid (max 30% equity) |

**What they DON'T need:** SIP in small cap, ELSS, thematic funds, or any equity-heavy product
**Key message:** "For goals under 3 years, safety of capital matters more than growth. A -20% market drop right before your goal date is devastating."

---

### 5. Rebalancing Seeker ("Should I rebalance?")

**Signals:** "rebalance portfolio", "asset allocation drifted", "too much in equity", "too much in debt", "market went up should I sell", "market crashed should I move to FD"

**Route to:** references/rebalancing-rules.md (comprehensive guide)

**Quick decision tree:**
1. Has allocation drifted >10% from target? → Yes = rebalance. No = leave it.
2. Is any goal within 3 years? → Yes = shift that goal's corpus to debt.
3. Is this emotional (fear/greed) or systematic (scheduled review)? → If emotional, DON'T rebalance. Read india-mutual-fund-advisor Step 8 (behavioural coaching) first.
4. Method: Prefer SIP redirection (tax-free) over selling (tax event).

**Key message:** "Rebalancing is a scheduled, unemotional process. If you're reacting to market news, it's not rebalancing — it's panic."

---

### 6. Tax Question Asker ("How to save tax?")

**Signals:** "save tax", "80C", "old vs new regime", "tax planning", "LTCG", "tax harvesting", "ITR", "tax on mutual fund", "which regime"

**Route by specificity:**
| Query | Skill |
|-------|-------|
| General "how to save tax" | india-tax-optimizer (full workflow) |
| "80C" specific | india-tax-optimizer Step 3 (includes merged 80C optimizer content) |
| "Old vs New regime" | india-tax-optimizer Step 2 + references/tax-rates-india.md |
| NPS tax benefit | india-nps-planner Step 4 |
| Home loan tax benefit | india-home-loan-planner (dedicated skill) |
| Health insurance 80D | india-health-insurance Step 2 |
| Capital gains / LTCG / STCG | india-tax-optimizer Step 5 + references/tax-rates-india.md |
| "Which regime for ₹X income" | references/tax-rates-india.md → Decision Rule section |

---

### 7. Goal-Based Planner ("I want to plan for X")

**Signals:** "retirement plan", "child education", "FIRE", "financial plan", "can I retire at 45", "how much SIP for 1 crore", "goal planning"

**Route by goal:**
| Goal | Primary Skill | Reference |
|------|-------------|-----------|
| Full financial plan | india-financial-plan | references/goal-templates.md |
| Retirement / FIRE | india-financial-plan Step 3 | references/goal-templates.md → FIRE section |
| Child education | india-financial-plan Step 4 | references/goal-templates.md → Education section |
| SIP amount needed | india-mutual-fund-advisor Step 4 | references/goal-templates.md → SIP Calculator |
| House purchase | india-home-loan-planner | references/goal-templates.md → House section |
| Multiple goals at once | india-financial-plan (full plan) | All references |

---

### 8. Advisor / RIA User ("I'm advising a client")

**Signals:** "my client", "prospect meeting", "advisory practice", "SEBI RIA", "proposal for client", "client presentation"

**Route to:** india-investment-proposal (dedicated skill for advisors)

**Also useful:**
- india-mutual-fund-advisor (full framework to apply with clients)
- references/model-portfolios.md (share with clients as allocation templates)
- india-financial-plan (client onboarding workflow)

---

### 9. Shariah / Ethical Investor ("I only invest in Shariah-compliant funds")

**Signals:** "Shariah", "halal", "ethical fund", "Tata Ethical", "Quantum Ethical", "no interest", "Islamic investing", "riba-free"

**Route to:** india-mutual-fund-advisor Step 11 (Shariah deep-dive) → references/model-portfolios.md → "Shariah-Compliant Model Portfolios"

**What they need:**
1. Validation that Shariah investing is respected and supported
2. Complete list of available Shariah funds in India
3. Honest limitations (sector concentration, no debt MFs, fewer options)
4. Shariah-specific model portfolio for their SIP amount
5. Guidance on grey areas (SGB interest, EPF, PPF) — present both views, don't prescribe

**What they DON'T need:** Pressure to add conventional funds "for diversification". Respect the mandate.
**Tone:** Non-judgmental, informed. Acknowledge the constraint is values-driven, not ignorance.
**Common overlap:** Often also Persona #1 (first-timer) or #10 (scam recovery). Handle both.

---

### 10. Scam Recovery Investor ("I got burned before")

**Signals:** "lost money in scheme", "got scammed", "don't trust apps", "crypto scam", "chit fund loss", "Ponzi", "money chain", "guaranteed returns trap"

**Route to:** india-mutual-fund-advisor Step 8 (scam recovery section) → Step 8B (platform trust)

**What they need:**
1. Validation that their caution is smart (not excessive)
2. Red flags checklist to avoid future scams
3. Platform trust hierarchy (AMC direct → MFU → SEBI aggregators)
4. Explanation that MF units are held by RTA, not the app
5. Tiny-SIP restart plan (₹500-1000) to rebuild confidence
6. Legitimate return expectations by asset class

**What they DON'T need:** Being told to "just trust the system." Trust must be earned through education.
**Tone:** Empathetic, patient, never dismissive. Their loss was real.

---

## Persona Overlap Handling

Most users are a mix. Common combos:

| Combo | Approach |
|-------|---------|
| First-timer + tax saver | Start with 80C education → recommend ELSS SIP → expand to broader portfolio |
| Goal planner + MF beginner | Map goals first → pick simplest portfolio for their risk profile → 2-3 funds max |
| Portfolio reviewer + rebalancer | Audit first → identify issues → rebalance only what's needed |
| Tax question + goal planning | Answer tax question directly → then offer to connect to broader financial plan |
| Shariah investor + first-timer | Shariah model portfolio (starter) → one fund (Tata Ethical) → keep it simple |
| Shariah investor + scam recovery | Validate caution → platform trust education → Shariah starter SIP (₹500-1K) → scale up |
| Scam recovery + first-timer | Red flags education → AMC direct route → tiny SIP → build confidence over 6 months |

**Default rule:** Always answer the immediate question first. Then offer the broader context. Never force a full financial plan on someone who just wants to know "which ELSS fund."
