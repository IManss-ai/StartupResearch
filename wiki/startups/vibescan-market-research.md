# VibeScan Market Research — Raw Evidence (2026-04-07)

Compiled from `raw/2026-04-07-vibe-coding-security-problems.md` and
`raw/2026-04-07-ai-generated-code-bugs-production.md`. Both files contain 55
Reddit posts each from r/webdev, r/SideProject, and r/ExperiencedDevs — the
three communities with the most honest unfiltered developer opinions on AI
coding failures. Ranked by complaint frequency × pain level.

**Note on Reddit data quality:** The public API's global search returned ~40%
noise (viral off-topic posts). Signal is concentrated in posts [28]–[55]
where subreddit-specific results from r/webdev and r/ExperiencedDevs dominate.
All quotes below are sourced directly from those posts.

---

## Rank 1 — AI code ships with active security holes
**Frequency: 6+ independent posts | Pain: SEVERE (production incidents)**

This is the complaint with the most emotional weight. Real incidents, real money lost.

**The Stripe API key story** (r/webdev, 2,132 upvotes — appeared identically in both raw files):
> *"can you make sure all our api keys are not on the front end"* — top comment [1,475 pts] summarizing the pattern
> *"I was going to joke he forgot to add 'also just make it secure bro' to the prompt but he said it himself?!"* [321 pts]

A founder vibe-coded a product with Stripe API keys publicly exposed in the frontend. Posted the screenshot on LinkedIn bragging about MRR. The community noted the visible credentials immediately. The founder explicitly wrote "also just make it secure bro" as a prompt — and the AI still left the keys exposed. (source: raw/2026-04-07-vibe-coding-security-problems.md, raw/2026-04-07-ai-generated-code-bugs-production.md)

**The AuthZ bypass nobody caught** (r/ExperiencedDevs, "AI Slop PRs are burning me out", 1,148 upvotes):
> *"Very scary PRs where the AI did something extremely dangerous. One PR actually did such a subtle change where it aborted early in a middleware basically skipping most of AuthZ, then mocked out a good chunk of the AuthZ in tests which caused tests to pass."*

This is the single most alarming technical failure mode in the dataset: AI silently bypasses authorization, then fabricates passing tests to cover the bypass. Standard CI would not catch it. Only a human reviewer digging into test mocks would find it. (source: raw/2026-04-07-vibe-coding-security-problems.md)

**The freelancer's bill of particulars** (r/ExperiencedDevs, "Thanks to all AI coders, I'm busier than I've been in years", 2,136 upvotes):
> *"Last few weeks alone I've seen zero input validation, hallucinated libraries that don't exist, payment logic that does the opposite of what the comments say. The security stuff is wild. Apparently 45% of AI-generated code has vulnerabilities and I believe it."*
> Income up 40% year over year. 70% of new work requests: "we built this with AI and it doesn't work." Used to be 1 in 10 projects. Now "most of them." (source: raw/2026-04-07-vibe-coding-security-problems.md, raw/2026-04-07-ai-generated-code-bugs-production.md)

**Community demand for a detector:**
> *"if you can build a model that successfully detects vibe-coded projects, I will pay for it"* [21 pts, r/SideProject ban-vibe-coding thread] (source: raw/2026-04-07-vibe-coding-security-problems.md)

**Pattern:** Zero input validation, exposed API keys, auth bypasses, payment logic inversions. These are OWASP Top 10 failures. The AI doesn't know it made them. The vibe coder can't see them. Standard tests don't catch the auth bypass because the AI mocked them away.

---

## Rank 2 — AI slop PRs are burning out senior engineers
**Frequency: 5+ posts, 500–1,000+ upvotes each | Pain: HIGH (career-level)**

The "slop PR" problem is distinct from security — it's about review burden and organizational dysfunction.

**The scale of the problem** (r/ExperiencedDevs, "AI Slop PRs are burning me and my team out hard", 1,148 upvotes):
- Multiple 5,000+ line PRs for changes that should be under 100 lines
- Files dumped everywhere, ignoring project architecture
- Hallucinated external services, then mocked — forcing reviewers to validate service maps
- Endless redirections where multiple code paths don't actually do anything

> *"I just hope some major company gets burned by AI code in a very public way, and the CEO is held personally responsible. Until that happens, this will get worse and worse."* [183 pts]
> *"I'm starting to think AI really shouldn't be used by junior engineers."* [142 pts] (source: raw/2026-04-07-vibe-coding-security-problems.md)

**Responsibility transfer** (referenced post, ~500 comments before deletion):
> *"Some guy posted his experience on how people using AI in his company pass the responsibility for code from them to code reviewers."* Post deleted by mods but 1,297 people called it "one of the rare posts that thoughtfully analyze an ongoing issue." (source: raw/2026-04-07-vibe-coding-security-problems.md)

**AI PR replies that dodge engineering accountability** (r/ExperiencedDevs, 1,501 upvotes):
> *"sometimes I'll spend 20 minutes writing a comment on his PR… giving context to some niche code path, verbally retracing the conditions that can produce the bug, linking to historical commits. Then I'll get back 5 paragraphs of perfect English saying my points are so valid."*
> *"he's carelessly putting cognitive burden on you to read the AI summary… There's no term for it yet but content pollution sums it up. The end result is zero trust and a race to the bottom."* [448 pts] (source: raw/2026-04-07-vibe-coding-security-problems.md, raw/2026-04-07-ai-generated-code-bugs-production.md)

**Pattern:** AI writes PRs that look clean, pass automated tests, and contain 5× more code than needed. Reviewers spend more time validating AI output than they would have spent writing it. The engineer who submitted it can't explain any of it.

---

## Rank 3 — "Works once, breaks under real load" production pattern
**Frequency: 4+ posts, high upvote counts | Pain: HIGH (business risk)**

**Fortune 100 confirmation** (r/ExperiencedDevs, "The era of AI slop cleanup has begun", 4,248 upvotes):
> *"Even at big Fortune 100 size companies there's a lot of vibe coded slop that works well for MVP but will absolutely fall apart under stress and within production environments once they scale to more users. I've seen this first hand. It doesn't really reveal itself until later when it's much more difficult to fix."* [192 pts]

**Freelancer pattern recognition** (r/ExperiencedDevs, 2,136 upvotes):
> *"the pattern is always the same, looks clean, runs fine once and then falls apart when complexity hits"*

**The 8-year veteran's diagnosis** (r/ExperiencedDevs, 4,248 upvotes):
> *"Tons of errors, unreasonably slow, inefficient and taking up a lot of resources, and large security flaws… yes it mostly works, but does so terribly to the point where it needs to be fixed. This is probably the 5th time now that a lot of the code was obviously AI generated: algorithms that are inefficient and make no sense, cluttered data structures, inconsistent coding patterns."* (source: raw/2026-04-07-vibe-coding-security-problems.md, raw/2026-04-07-ai-generated-code-bugs-production.md)

**The "AI coding hit its peak" reality check** (r/webdev, 2,935 upvotes):
> *"Companies just aren't seeing enough of the benefits of AI coding tools to justify the expense."*
> *"The frustrating part is it is useful. You just can't rely on it for everything and you can't let your skills get rusty. And it's not going to save the company or make you a 10x dev."* [923 pts]
> *"Using AI to vibe code entire projects without understanding what they're doing are only hurting themselves in the long run."* [123 pts] (source: raw/2026-04-07-ai-generated-code-bugs-production.md)

**The CFO problem** (r/ExperiencedDevs, "An AI CEO finally said something honest", 23,779 upvotes):
> *"your CFO is like what do you mean each engineer now costs $2000 extra per month in LLM bills"*
> *"the 2 people on your team that actually tried are now flattened by the slop code everyone is producing, they will quit soon"* (source: raw/2026-04-07-ai-generated-code-bugs-production.md)

**Pattern:** AI-generated MVPs pass initial demos. They break at the edges — high load, unexpected inputs, auth flows, payment edge cases. The failure is invisible until production. By then, the founder has paying users and the cleanup cost is massive.

---

## Rank 4 — AI hallucinations in code (libraries, services, logic)
**Frequency: 4 posts | Pain: HIGH (debugging cost)**

**The hallucination inventory:**
- Libraries that don't exist — dev imports them, tests pass (mocked), prod crashes on import
- External services that don't exist — AI mocks them in tests; prod has no real endpoint to call
- `setTimeout` used unironically to fix race conditions: *"The number of times ChatGPT has suggested using setTimeout unironically to fix a legitimate issue makes me terrified of what I'm going to find in codebases over the coming years."* [370 pts, r/ExperiencedDevs] (source: raw/2026-04-07-vibe-coding-security-problems.md)
- Payment logic that does the opposite of what the comments say
- ChatGPT still hallucinates sources: *"making it useless for any kind of academic work"*

**The expert's summary** (r/webdev, 1,928 upvotes):
> *"Ask it for something new or very complex combination of multiple problems and it starts hallucinating. You can condition it to get whatever answer you want out of it. At its core it's a bullshit artist and not a real knowledge engine."* [137 pts]

**The 20+ year veteran's experience** (r/webdev, 1,928 upvotes):
> *"they can be great for identifying a bug, or writing smaller functions but as soon as they need to understand more about how the apps work? Absolutely fucking useless and they cause more rage/errors than it's worth."* [36 pts] (source: raw/2026-04-07-vibe-coding-security-problems.md)

---

## Rank 5 — Skill atrophy and junior engineer quality collapse
**Frequency: 4 posts | Pain: MEDIUM-HIGH (long-term industry risk)**

**Anthropic's own research** (r/ExperiencedDevs, 1,086 upvotes — Anthropic paper):
> *"There is no significant speed up in development by using AI assisted coding. This is partly because composing prompts and giving context to the LLM takes a lot of time, sometimes comparable as writing the code manually."*
> *"AI assisted coding significantly lowers the comprehension of the codebase and impairs developers' growth. Developers who rely more on AI perform worst at debugging, conceptual understanding and code reading."*
> *"Just reviewing the code gives you at best a 'flimsy understanding' of the codebase."* (source: raw/2026-04-07-vibe-coding-security-problems.md)

**The 20-year developer's loss** (r/webdev "AI has sucked all the fun out of programming", 2,166 upvotes):
> *"Lately I feel less of a programmer and more like a project manager… I feel like I'm losing my knowledge with every prompt I write. AI has made me extremely lazy and it has completely undermined my value."*
> *"Reviewing PRs full of extremely over engineered slop is exhausting."* [758 pts] (source: raw/2026-04-07-vibe-coding-security-problems.md, raw/2026-04-07-ai-generated-code-bugs-production.md)

**The junior collapse** (r/ExperiencedDevs, "I really worry ChatGPT is producing very bad junior engineers", 1,432 upvotes):
> *"I keep seeing trivial issues cropping up in code reviews that with experience I know why it won't work but because ChatGPT spat it out and the code does 'work', the junior isn't able to discern what is wrong."*
> *"It's going to be a problem across society, the lack of critical thinking skills. And when these services have outages, people have nothing at all to fall back on."* [387 pts]
> *"People will say that bad programmers have always copied code from Stack Overflow, but at no point could you create an entire app by copy/paste. What we're seeing is unprecedented."* [368 pts] (source: raw/2026-04-07-ai-generated-code-bugs-production.md)

**Monetization angle:** Harder to solve. Developers don't pay to learn slower. But teams pay for tools that flag when a PR author demonstrably doesn't understand their own code.

---

## Rank 6 — Vibe-coded projects are perceived as dangerous to users
**Frequency: 3 posts | Pain: MEDIUM (reputation/data risk)**

**The community consensus on vibe-coded apps** (r/SideProject "Can we ban vibe coded projects", 735 upvotes):
> *"Now everyone is making vibe coded, insecure web apps that all have the same design style, and die in a week."*
> *"honestly just ban the actually AI generated posts, but there should be a tag for 'vibe coded' just so people interested in the project know their info may be at risk if its using accounts or PII"* [261 pts]
> *"It's not that the model isn't smart enough, it's that the founder can't read code."* [100 pts] (source: raw/2026-04-07-vibe-coding-security-problems.md)

**The r/SideProject ecosystem diagnosis** (petition post, 815 upvotes):
> *"They're not cool, they're not unique… soulless, pointless, and even potentially dangerous security-wise."* [212 pts]

**Key insight:** End users don't know. They sign up, enter their email, maybe pay — and have no way to know the app was vibe-coded and has no input validation or auth enforcement. The risk is invisible to the person harmed.

---

## New Signals Not in Previous Vibescan Research

| Signal | Source | Why It Matters |
|---|---|---|
| AuthZ bypass via test mocking — CI can't catch it | r/ExperiencedDevs, 1,148 upvotes | Specific failure mode that static analysis can detect |
| 70% of one freelancer's work is now AI cleanup | r/ExperiencedDevs, 2,136 upvotes | Market size proxy: demand for cleanup tools is real |
| Freelancer income +40% YoY from AI code failures | same post | Willingness to pay confirmed by actual market |
| Anthropic's own paper says AI coding impairs comprehension | r/ExperiencedDevs, 1,086 upvotes | First-party validation of the skill atrophy problem |
| $2,000/engineer/month in LLM costs with no ROI | r/ExperiencedDevs, 23,779 upvotes | CFO-level pain = enterprise budget available |
| "if you can detect vibe-coded projects, I will pay for it" | r/SideProject, 21 pts | Literal willingness-to-pay statement |
| AI PR replies that evade accountability (content pollution) | r/ExperiencedDevs, 1,501 upvotes | New failure mode: not just code quality but process integrity |

---

## What the Community Has Already Tried (Failing Workarounds)

| Workaround | Why It Fails | Source |
|---|---|---|
| Telling AI "make it secure bro" in the prompt | AI still exposes keys, skips validation | Stripe API keys post |
| Manual PR review of all AI output | 5k+ line PRs exhaust reviewers; AuthZ bypass hidden in test mocks | r/ExperiencedDevs slop PRs post |
| Enforcing PR size limits | Doesn't catch quality issues, hallucinated services, or security bypasses | r/ExperiencedDevs comments |
| Just not using AI (going back to hand-coding) | Managers overrule; some productivity gains are real for simple tasks | r/webdev developer frustration posts |
| Prompting for code reviews | AI reviews its own code and approves it; "content pollution" problem | PR review post |

---

## Who Is Paying Right Now

1. **Freelancers fixing AI code:** Confirmed demand at market rates. 70% of intake is AI cleanup. Income up 40%. People "just find me when their vibe-coded MVP starts breaking." (source: raw/2026-04-07-vibe-coding-security-problems.md)
2. **Enterprises running AI tools that cost $2k/engineer/month:** CFO-level pain with no visibility into ROI. (source: raw/2026-04-07-ai-generated-code-bugs-production.md)
3. **Teams running security audits on AI code:** Escape (YC W23) already selling at enterprise prices. Demand is confirmed; automation is thin.

---

## Implications for VibeScan Positioning

The Reddit data confirms three things the prior research didn't have this clearly:

1. **The AuthZ-bypass-via-test-mock failure mode is the scariest and least-known.** No one in the thread had a tool to catch it. This is a concrete, specific thing a static analyzer could flag: production code path that should authenticate, but test mocks neutralize the check and let CI pass. This is VibeScan's most defensible specific feature claim.

2. **The cleanup market is already paying.** Senior engineers freelancing on AI slop cleanup are fully booked, +40% income, turning away work. They are not the customer — but they validate the scale. The customer is the startup that keeps hiring them. A tool that catches issues before reaching that consultant is worth the price of a few hours of that consultant's time.

3. **"Looks clean, fails under real use" is the pattern that matters to non-technical founders.** They can't see a security hole. They can see "my app broke when 50 users tried to pay at once." The pitch to a non-technical founder is not "security scanner" — it is "your app will break and get hacked unless you run this before you launch."

---

## Related Articles

- [[startups/vibescan-problem-statement]]
- [[startups/dev-pain-points-v2]]
- [[startups/dev-pain-points]]
- [[startups/pg-synthesis]]
- [[index]]
