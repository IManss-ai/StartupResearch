# Research Session — KZ Payroll & E-Commerce Compliance
**Date:** 2026-04-12
**Focus:** New territory — KZ payroll automation gap created by 2026 Tax Code + Kaspi seller tools

---

## 1. Market Overview

Kazakhstan's new Tax Code (effective Jan 1, 2026) is the biggest payroll disruption in years: 7 special tax regimes cut to 3, progressive IPN scale introduced, взаимозачет (offset mechanism) abolished, and 185 business types forced off simplified regime. Every KZ company with employees must recalculate payroll from scratch. No affordable, always-current SaaS tool exists for this — just expensive 1C, human outsourcing, or dumb calculators.

---

## 2. Real Problems Found

### Problem A: Payroll Calculation Has Become Dangerously Complex (5 sources)
- **profitraining.kz** (training site): *"Using last year's Excel tables will cause account freezes and massive fines. Manual calculation with 7 salary thresholds in Excel is Russian roulette with the tax authority."* — Selling a paid course specifically for "Salary 2026: correct calculation without fines."
- **mybuh.kz** (accounting portal): Documents the full complexity — IPN, OPV, SO, OSMS, new progressive thresholds at 7/20/40/50 MZP, взаимозачет mechanism abolished Jan 1, 2026. Any single error cascades through all deductions.
- **pro1c.kz** + **1cbit.kz**: Both published emergency articles + "cheat sheets" for 2026 payroll, confirming accountants are confused.
- **b1.ru/EY Kazakhstan**: Tax legislation updates confirm March 1 notification deadline and automatic transfers to general regime.
- **primeminister.kz** (official): "If notification not submitted by March 1 — automatically transferred to general regime from Jan 1, 2026." (same window as SafeBiz KZ deregistration crisis)

### Problem B: Forced Regime Transition Means New Payroll Obligations (4 sources)
- Thousands of businesses on "упрощенка" forced to general regime — now must do full payroll accounting for the first time
- VAT threshold halved, 185 activity types removed from simplified eligibility
- New restriction: if founder of an LLP on simplified regime, you can't also have an IE on simplified — forced restructuring
- Source: mybuh.kz analysis, trustme.kz tax guide, bcc.kz legislation overview, moore-global.com

### Problem C: Kaspi Seller Pain (3 sources) — **MARKET ALREADY SERVED**
- 18,000+ buyer complaints in 2025, complaints up 50% YoY (kz.kursiv.media)
- Seller pain: mandatory Kaspi drop-off queues, order cancellations, no direct delivery
- **BUT: AWW.kz already exists** — AI platform for Kaspi seller automation (repricing, WhatsApp, analytics). Skip this market.

---

## 3. Competitor Gaps

| Solution | What it does | Gap |
|---|---|---|
| **1C Бухгалтерия 8 KZ** | Full accounting suite | Too expensive (license + ITS subscription + setup), requires dedicated accountant, overkill for 3-10 employee companies |
| **MyBuh.kz** | Accounting outsourcing from 8,000 KZT/month | Human service, not software — you're dependent on someone else, no real-time visibility |
| **inbuh.kz / mybuh.kz calculators** | Free one-off salary calculators | Stateless — no employee database, no monthly workflow, no e-Salyq export |
| **Global SaaS (Deel, Rippling, etc.)** | Global payroll | Don't support KZ-specific deductions (OPV, OSMS, ENPF formats), no e-Salyq integration |
| **profitraining.kz** | Training courses on correct 2026 calculation | Education only — doesn't automate anything |

**The gap:** A simple, always-current KZ payroll SaaS for companies with 1–30 employees. Enter employees + salaries → get correct 2026 deductions calculated → export e-Salyq ready data. Updates automatically when law changes.

---

## 4. Money Signals

- **profitraining.kz** is selling a paid online course specifically for "correct salary 2026 without fines" — people pay to understand this. Full accountant course: 160,000 KZT.
- **MyBuh.kz** charges 8,000 KZT/month minimum for outsourced accounting — businesses already pay this.
- **1C license + ITS subscription** in Kazakhstan: ~50,000–200,000 KZT/year depending on version, plus ~15,000 KZT/month ITS for updates.
- The training market itself is a payment signal: if someone sells a course on how to do payroll correctly, there's a buyer who would rather have a tool that just does it correctly.
- Target price: 3,000–7,000 KZT/month is well below 1C cost and MyBuh.kz outsourcing.

---

## 5. Startup Idea Hypotheses

### H1: KZ Payroll SaaS ("ZarplatKZ" / "PayCalc KZ") — MEDIUM-HIGH
**What:** Web app for KZ SMBs (1–30 employees). Input: employee list, salaries, regime, deductions. Output: correct monthly IPN/OPV/SO/OSMS breakdown per 2026 rules + formatted data for e-Salyq filing. Auto-updates when law changes.

**Why this fits Mansur:**
- No KZ-specific SaaS competitor found
- 2026 law change is the forcing function — perfect timing
- B2B, recurring monthly need, clear willingness to pay
- Local advantage: KZ tax rules are hyperlocal, global tools don't support them

**Risks:**
- 1C has deep market penetration — accountants are trained on it
- Buyer is the accountant, not the CEO — need accountant distribution
- Law changes frequently — maintenance overhead is real
- **Confidence: MEDIUM-HIGH** (3+ sources confirm problem, payment signal exists, no direct SaaS competitor found, but distribution to accountants is hard)

### H2: SafeBiz KZ → Payroll Module (add-on to existing product) — HIGH
**What:** After solving the emergency re-registration crisis (SafeBiz KZ v1), the same businesses that transitioned from simplified to general regime now need ongoing payroll help. Build payroll calculation as SafeBiz KZ v2 (Phase 2 after regime identification).

**Why stronger than standalone:**
- Same buyer (business owner who just recovered their SNR)
- Natural upsell: "You've identified your new regime — now let's calculate your first payroll correctly"
- You already have the codebase + Telegram distribution
- No cold-start problem

**Confidence: HIGH** — same channel, same buyer, logical next step

### H3: KZ Tax Regime Advisor Bot (Telegram) — MEDIUM
**What:** Telegram bot that answers "which tax regime should I be on in 2026?" + calculates tax burden comparison across regimes. Freemium → paid for personalized analysis.

**Why interesting:**
- "How to choose a tax regime in 2026" had official government announcement + EY/Moore articles = high search volume
- Telegram is native distribution for KZ market
- Simple to build, clear use case

**Risks:** Hard to monetize, likely becomes a lead-gen tool rather than standalone revenue
**Confidence: MEDIUM** (problem confirmed, payment unclear at small scale)

---

## 6. My Recommended Next Step

**Don't build a new product. Add payroll to SafeBiz KZ.**

The 2026 tax code payroll disruption is a confirmed, real problem with payment signals. But the strongest move is not starting a new startup — it's extending SafeBiz KZ, which already has:
- A codebase
- Telegram distribution
- The same target buyer (KZ SMBs navigating 2026 tax changes)

**Concrete next action:** Talk to 3 SafeBiz KZ users and ask: "After you figured out your regime, what was the next hardest thing — calculating your first payroll correctly?" If they say yes, build the payroll calculator as SafeBiz KZ v2 (after the Deadline Dashboard).

If you want a standalone new product: H1 (KZ Payroll SaaS) is valid but needs accountant interviews first — they are the gatekeepers to this buyer.

---

## Sources
- [profitraining.kz — Salary 2026 course](https://profitraining.kz/zarplata2026/)
- [mybuh.kz — 2026 Tax Code full breakdown](https://mybuh.kz/useful/nalogovyy-kodeks-2026-polnyy-razbor-izmeneniy-dlya-biznesa-rk-.html)
- [mybuh.kz — Payroll taxes 2026 (OUR vs simplified comparison)](https://mybuh.kz/useful/nalogi-s-zarplaty-2026-v-kazakhstane.html)
- [primeminister.kz — March 1 notification deadline](https://primeminister.kz/en/news/how-to-choose-a-tax-regime-in-2026-entrepreneurs-must-submit-a-notification-by-march-1-30979)
- [b2b.telecom.kz — New tax regimes from 2026](https://b2b.telecom.kz/en/news/ismet/kakie-nalogovye-rezhimy-budut-dejstvovat-v-kazahstane-s-2026-goda)
- [b1.ru — Kazakhstan tax legislation changes 2026](https://b1.ru/en/insights/tax-messenger/kazakhstan-tax-legislation-changes-30-october-2025/)
- [kz.kursiv.media — Marketplace complaints up 50%](https://kz.kursiv.media/2025-10-28/svan-zhaloby-kazahstancev-na-marketplejsy-vyrosli-pochti-na-50/)
- [aww.kz — Kaspi seller AI automation](https://aww.kz/en/journal/kak-otkryt-magazin-kaspi/)
- [trustme.kz — 2026 tax changes full guide](https://trustme.kz/nalogi_kazakhstan_2026/)
- [moore-global.com/kazakhstan — New Tax Code key changes](https://kazakhstan.moore-global.com/new-tax-code-key-changes/)
