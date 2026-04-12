# VibeScan — Problem Statement

Vibe-coded apps are being shipped to real users, collecting real money, and getting hacked within days of launch. The attacker's job has never been easier: AI coding agents produce code that **passes functional tests and looks clean on the surface but omits the security checks experienced developers apply instinctively**. The developer doesn't know. The users don't know. The first sign of compromise is a cryptominer running at 100% CPU, or a stranger creating admin accounts on their database, or their API credits gone.

This is not a hypothetical risk. It is happening repeatedly, it is going viral, and no affordable tool exists that is built specifically for this failure mode.

---

## The Numbers

- **45%** of AI code samples contain security vulnerabilities — Veracode (source: raw/2026-04-07-ai-vibe-coding-security-vulnerabilities.md)
- **1.7×** more issues in AI-generated PRs vs. human PRs — CodeRabbit (source: raw/2026-04-07-ai-vibe-coding-security-vulnerabilities.md)
- **70–90%** of code at some companies is now AI-generated — Anthropic podcast (source: research_vibescan_2026-03-29.md)
- **8,436** upvotes: "AI-generated code contains more bugs and errors than human output" — r/technology (source: research_vibescan_2026-03-29.md)
- **9,523** upvotes: Huntarr security audit — 21 critical/high vulnerabilities, full account takeover via a single unauthenticated API endpoint — r/selfhosted (source: research_vibescan_2026-03-29.md)
- **2** critical CVEs (CVSS 9.8/10) found by one operator scanning vibe-coded production systems: CVE-2025-58434 (Flowise full account takeover), CVE-2025-61622 (Apache Pyfory RCE) — Bugbunny (source: raw/2026-04-07-ai-vibe-coding-security-vulnerabilities.md)

---

## Exact Failure Modes

These are not generic web security issues. They are patterns that AI coding agents produce **systematically** because they optimize for functionality, not security. Every item below is documented by an independent source:

**1. Unauthenticated API endpoints**
AI generates REST endpoints that work — but omits auth middleware. Result: any user can call POST /api/admin, POST /api/settings, or GET /api/user/:id for any ID. The Huntarr case: Sonarr, Radarr, and Prowlarr API keys exposed with a single curl command; full account takeover without a password. (source: research_vibescan_2026-03-29.md)

**2. Dependency version blindness — AI introduces known CVEs**
AI agents scaffold projects and pin dependency versions without checking CVE status. Real incident: a Next.js app was compromised via CVE-2025-29927 — the vulnerable version was chosen by Claude Code / OpenAI Codex. *"In traditional development, you review versions carefully. With AI-generated scaffolding, that step is easy to overlook."* A cryptominer ran for weeks before CPU anomaly detected it. (source: raw/2026-04-07-ai-vibe-coding-security-vulnerabilities.md)

**3. Hallucinated packages — typosquatting attack surface**
AI agents sometimes reference packages that don't exist. Attackers squat on these names with malicious packages. *"I ran a test on a bunch of AI-generated repos and found a crazy amount of them had severe structural flaws, like hallucinating fake packages that an attacker could easily squat."* (source: raw/2026-04-07-ai-vibe-coding-security-vulnerabilities.md)

**4. Subscription and authorization bypass**
AI implements feature-gating logic that can be bypassed by manipulating client-side state, URL parameters, or API payloads. Real victim quote: *"People bypassing the subscription, creating random stuff on DB."* App shut down permanently. (source: research_vibescan_2026-03-29.md)

**5. Hardcoded API keys and secrets**
AI writes working code by hardcoding credentials in source files rather than referencing environment variables — especially in prototypes that then get shipped. Security engineers report this as one of the first things they find. (source: raw/2026-04-07-ai-vibe-coding-security-vulnerabilities.md)

**6. Missing input validation and rate limiting**
*"AI forgets input sanitization and error handling unless you specifically ask for it every single time."* Auth endpoints with no rate limiting = trivial brute-force. SQL concatenation instead of parameterized queries = injection. (source: research_vibescan_2026-03-29.md)

**7. IDOR — Insecure Direct Object Reference**
AI generates resource endpoints like GET /api/invoice/:id that return data for any ID regardless of ownership. One user scanned their vibe-coded project with Strix and found IDOR vulnerabilities immediately on first run. (source: raw/2026-04-07-ai-vibe-coding-security-vulnerabilities.md)

**8. Empty catch blocks and swallowed errors**
AI wraps code in try/catch that console.errors without rethrowing, or bare `except: pass` in Python. Security-relevant errors (auth failures, permission checks) silently disappear. (source: raw/2026-04-07-ai-vibe-coding-security-vulnerabilities.md)

---

## What People Are Currently Doing About It

There are four workarounds in the wild. All of them are expensive, slow, or incomplete:

**Workaround 1: Manual review before merge**
Developers do a full line-by-line review of all AI output. This is the most common response. It directly negates the productivity benefit of AI coding — experienced devs are 19% *slower* with AI when accounting for review overhead. Quote: *"The AI is fast at scaffolding; the bottleneck is still us catching what it gets wrong. Nothing is easy unfortunately."* (source: raw/2026-04-07-ai-vibe-coding-security-vulnerabilities.md)

**Workaround 2: `npm audit` as a post-generation step**
Some teams run dependency audits manually after each AI generation cycle. Catches CVEs in known packages but misses logic-layer auth bugs, hallucinated packages, and application-level vulnerabilities. Requires remembering to run it. (source: raw/2026-04-07-ai-vibe-coding-security-vulnerabilities.md)

**Workaround 3: Dedicated security review sessions in a fresh context**
*"The building session won't catch its own mistakes."* Developers open a new AI context and ask it to audit what they just built. Non-systematic. Depends on asking the right questions. Misses what neither the developer nor the AI thinks to check. (source: raw/2026-04-07-ai-vibe-coding-security-vulnerabilities.md)

**Workaround 4: Hiring a penetration tester**
One-time audits cost hundreds to thousands of dollars. Only done pre-launch if the founder has funding or a serious enterprise client. The solo founder or non-technical indie hacker never does this until after they get hacked. (source: research_vibescan_2026-03-29.md)

**What nobody does:** Automated, continuous security scanning specifically designed for AI-generated failure modes, at a price a solo founder can pay. This tool does not exist.

---

## Why Existing Solutions Fail

| Tool | Price | Why It Fails for This Problem |
|------|-------|-------------------------------|
| SonarQube | $150+/mo | Enterprise pricing. Generic rule set built for human code. Does not target AI failure modes. No auth-bypass or subscription-bypass detection. |
| Snyk | $100+/mo | Scans dependencies, not application logic. Misses IDOR, auth bypass, missing rate limiting. |
| CodeRabbit | $12–19/mo per user | Per-user pricing. Reviews PRs but does not specialize in vibe-coding patterns. Gets expensive at team scale. |
| CodeVibes | $8–20/mo | **Closest competitor.** Generic AI code scanner. Public GitHub repos only. Runs standard rules — not a vibe-coding-specific rule set. No auth-bypass or subscription-bypass detection. Already making money — proves the market. |
| Vibecheck (HN, score 7) | Free / open source | Regex-based, offline. Catches surface patterns (empty catch blocks, hardcoded secrets) but misses logic-layer vulnerabilities. *"Regex-based seems too brittle for general use."* No business model. |
| SafeVibe | Free / open source | Community database of 36 vulnerability patterns with LLM audit prompts. Manual workflow — user must read docs and craft prompts. No automated scan. |
| Strix, vibe-pen-tester, Bugbunny | Free / early beta | Open source or pre-revenue. Dynamic testing (actual exploitation), not static analysis. High false-positive risk, requires more setup. Not productized for solo founders. |
| Anthropic / OpenAI code review | Enterprise only | Not available at indie price points. Requires enterprise contract. Built for large engineering teams, not solo founders. |

**The consistent gap:** Every tool either costs $100+/mo (wrong price point), scans only dependencies (wrong scope), uses generic rules (wrong target), or is a free hobby project with no production reliability. None of them say *"This is the specific set of ways AI coding agents break security, and here is whether your app has those holes right now."*

---

## Why Now

Three things converged in 2025–2026:

1. **Volume crossed a threshold.** 70–90% of code at some companies is now AI-generated. The attack surface created by vibe-coding is orders of magnitude larger than it was two years ago.

2. **The incidents went public.** The Huntarr post (9,523 upvotes), the "vibe coder gets hacked loses Popeyes job" story (100K+ views), the CEO deletes production database story (3,921 upvotes) — these are not edge cases. They are recurring viral events that prime the target market to buy.

3. **Five independent builders shipped prototypes in the last 90 days.** Vibecheck, SafeVibe, Strix, vibeappscanner, Bugbunny — all built specifically for this problem, all launched in early 2026. None are productized or monetized. This is the classic signal: the problem is real and clear enough that multiple people are trying to solve it, but no one has captured the market yet.

---

## Target Customer (Sharply Defined)

The person who gets hacked is a founder who:
- Built their app with Cursor, Claude Code, Bolt, Lovable, or v0
- Has at least one paying user (their app is live, not a prototype)
- Does not have a background in security engineering
- Merged AI output without deep review because *"it passed the tests and looked fine"*
- Would have paid $15/mo to avoid the incident
- Will pay $15/mo after it happens to make sure it doesn't happen again

This is not a developer who doesn't care about security. This is a developer who **cannot see the vulnerabilities** in AI-generated code because the code looks clean, passes tests, and works — until a stranger exploits it.

---

## Confidence: HIGH

- Problem in **15+ independent sources** across Reddit, HN, YouTube, and two industry reports
- **Two hard statistics:** 45% of AI code samples have vulnerabilities (Veracode), 1.7× issue rate vs. human PRs (CodeRabbit)
- **Real incidents documented:** cryptominer deployment, Huntarr full account takeover, SaaS shutdown, production database deletion
- **Direct CVEs found:** CVE-2025-58434 and CVE-2025-61622 (both 9.8/10) from vibe-coded production systems
- **Live competitor (CodeVibes)** proves willingness to pay at $8–20/mo
- **Five independent builders** launched competing tools in the last 90 days — market signal without a clear winner yet
- **Anthropic and OpenAI** shipped enterprise-tier code review in response to the same problem

---

## Related Articles

- [[startups/dev-pain-points]]
- [[startups/pg-synthesis]]
- [[people/karpathy-coding-thesis]]
- [[index]]
