# Raw Research: AI vibe coding security vulnerabilities

**Collected:** 2026-04-07  
**Sources:** 0 Reddit posts · 9 HN stories · 0 YouTube transcripts

---

## Hacker News

### Show HN: Vibecheck – lint for AI-generated code smells (JS/TS/Python) (score: 7, 4 comments)
URL: https://github.com/yuvrajangadsingh/vibecheck

I built a CLI that detects patterns AI coding tools leave behind: empty catch blocks, hardcoded secrets, as any everywhere, comments that restate the code, god functions, SQL concatenation.<p>24 rules across JS&#x2F;TS and Python. Zero config, runs offline, regex-based so it&#x27;s fast.<p><pre><code>  npx @yuvrajangadsingh&#x2F;vibecheck .
</code></pre>
Also ships as a GitHub Action for inline PR annotations and standalone binaries (no Node required).<p>Why: CodeRabbit found AI-generated PRs have 1.7x more issues than human PRs. Veracode says 45% of AI code samples have security vulnerabilities. &quot;Vibe coding&quot; is everywhere now but nobody&#x27;s linting for the patterns it produces.<p>This isn&#x27;t a replacement for ESLint. It catches things ESLint doesn&#x27;t look for, like catch blocks that only console.error without rethrowing, bare except: pass in Python, or mutable default arguments.

> I&#x27;m a little wary of this being regex-based; seems like it&#x27;d be too brittle for general use? But I really would need a tool like this to hook up to my vibecoding sessions.

> Yeah, this is a common problem, I have been thinking about it a fair bit.<p>I ran into a related problem at scale though: deterministic linters catch syntax and obvious anti-patterns, but they miss the harder stuff. Logic bugs that pass all the rules. Spec drift. Security issues hiding in otherwise &quot;clean&quot; code.<p>So I built Caliper to layer AI review on top of deterministic checks. It reads your coding conventions (CLAUDE.md, .cursor&#x2F;rules, whatever you use) and compiles them into checks that run after each AI turn—free and instant. Then optionally an AI layer evaluates changes…

### Show HN: SafeVibe, a collaborative database to fix security gaps in vibe coding (score: 2, 0 comments)
URL: https://safevibee.vercel.app/

We know that security is often the weak point in vibe coding.<p>To help the community catch common issues before deployment, I built SafeVibe.<p>It is a free, non-commercial, and collaborative &quot;observatory&quot; for tracking security vulnerabilities specifically found in AI-generated applications.<p>What it does:<p>-Vulnerability list: a database of common security issues observed in vibe-coded apps (seeded with 36 issues gathered from recent discussions).
-Fixes: clear guidance on how to patch or mitigate each specific vulnerability.
-LLM Audit Prompts: you can select specific vulnerabilities and the site generates a prompt you can paste into your LLM&#x2F;agent to audit your code for those exact problems.<p>This is a community project and completely open to contributions. I’d love your feedback on the current data and the audit prompts.

### Show HN: Enter your domain and my open-source agent will hack it (score: 14, 3 comments)
URL: https://github.com/usestrix/strix

I built an open-source AI agent for security testing to find and fix vulnerabilities in your code.<p>I’ve noticed how bad security vulnerabilities have gotten with everyone shipping AI code slop, so I wanted to build something that allows for vibe-coding at full speed without compromising security.<p>Traditional security tools aren’t effective, and manual pen-testing can’t keep up with the rapidly growing AI code<p>This tool runs your code dynamically, finds vulnerabilities, and validates them through actual exploitation.<p>You can either run it against your codebase or enter your (or someone else’s) domain to scan for vulnerabilities.<p>Good luck, have fun, hack responsibly!

> very cool, just hacked my own site and found IDOR vulnerabilities.

> ahmedallam3 A bit of a segue so bear with me. I just realized that a lot of people have a set it up once mindset. (Their API keys are probably being used without their consent and stored in multiple databases somewhere).<p>There is real niche here, and I&#x27;d swear to that. A ton of poorly made sites are flooding the internet.<p>(By poorly made, I mean <i>Vibe Coded</i>.)<p>I use AI much more now than I ever did in the last year as I have come to refine my process. (Not having it take the steering; I like a front seat buddy holding the map ha ha.)<p>Platforms that allow this to be done as ea…

> this is pretty insane stuff tbh, just found SQL injection vulnerabilities in one of my vibe coded projects!

### AI coding agents accidentally introduced vulnerable dependencies (score: 7, 16 comments)
URL: https://news.ycombinator.com/item?id=47387054

Recently we discovered something unexpected on one of our servers: a cryptominer running in the background.<p>The machine was hosting a web service built using Next.js. The first sign of trouble was unusually high CPU usage. Even during low traffic periods, the server was consistently running near 100% utilization. After inspecting running processes and network activity, we found a background process downloading and executing a mining binary.<p>ROOT CAUSE<p>The entry point was CVE-2025-29927, a vulnerability in Next.js that allows middleware protections to be bypassed. This enabled an attacker to reach internal endpoints that were assumed to be protected. Once they hit the exposed endpoint, they executed a script that pulled down the miner.<p>HOW &quot;VIBE CODING&quot; FAILED US<p>This application was largely generated using AI-assisted tools (Claude Code and OpenAI Codex). This workflow—often called &quot;vibe coding&quot;—involved describing the desired functionality and letting the…

> Hi HN — author here.<p>This incident showed how AI-generated code can inadvertently introduce vulnerabilities. The cryptominer ran because a dependency version chosen by an AI coding agent had a known CVE.<p>Containarium now runs centralized pentests and vulnerability checks for all applications on the platform to prevent similar attacks.<p>Curious if others have similar workflows or lessons learned with AI-generated projects.

> The attack chain you described highlights a gap that most teams overlook: AI-generated code passes functional tests but skips the &quot;why this version?&quot; review that experienced developers do instinctively.<p>I think the real issue is visibility. When AI generates a project, every dependency choice is implicit — there&#x27;s no PR comment explaining why it pinned next@14.1.0 instead of 14.2.1. In a human workflow, someone would have caught that during review.<p>Two things that have helped in my workflow:
1. Running `npm audit` as a post-generation step before even testing functionality
2…

> I think some folks are very quick to drop rigor and care as &quot;traditional practices&quot; as if we&#x27;re talking about churning butter by hand. One thing that might be valuable to keep in mind is that LLM tooling might feel like an expert, but generally has the decisionmaking skills of a junior. In that light, the rigor and best practices that were already (hopefully) part of software engineering practice are even more important.<p>&gt; In traditional development, you review versions carefully. With AI-generated scaffolding, that step is easy to overlook.<p>If in &quot;traditional develo…

> This is what we do. We use AI for drafting but we never merge without doing a manual review of dependencies. 
Every package version is pinned explicitly, and our CI always runs a dependency scan before deploy.<p>The AI is fast at scaffolding, the bottleneck is still us catching what it gets wrong. NOthing is easy unfortunately

> This is terrifying but not surprising. I shipped unauthenticated admin endpoints once in a project that was extensively planned out with AI. The volume of code AI generates makes it really easy for vulnerabilities to slip through because review gets lighter as output gets faster. The two things that actually help: dedicated security review sessions in a fresh context (the building session won&#x27;t catch its own mistakes), and monitoring for unusual patterns like the CPU spike that caught this. If your first sign of compromise is high CPU, at least something was watching.

### Security with Vibe Coding Platforms (score: 1, 1 comments)
URL: https://news.ycombinator.com/item?id=47251354

I do a ton of vibe coding, but after looking closely at the code my agents were spitting out, I got curious. I ran a test on a bunch of AI-generated repos and found that a crazy amount of them had severe structural flaws (like hallucinating fake packages that an attacker could easily squat).
So, I&#x27;m building an automated firewall for vibe coding. It’s an automated security reviewer specifically designed to catch the vulnerabilities that AI coding agents accidentally write. 
I&#x27;m currently looking for developers who are shipping fast with AI to roast my MVP. If you&#x27;re down to test it on one of your repos, let me know!

> The security angle is one of the most underappreciated risks in vibe coding. When developers don&#x27;t understand the code that gets generated, they can&#x27;t assess whether it&#x27;s introducing vulnerabilities — hallucinated packages, insecure patterns, broken auth — and your finding that a &quot;crazy amount&quot; of AI-generated repos have severe structural flaws matches what a lot of teams are discovering in production.<p>This connects directly to a core principle from the Agile Vibe Coding Manifesto (<a href="https:&#x2F;&#x2F;agilevibecoding.org" rel="nofollow">https:&#x2F;&#x2F;agile…

### I Vibe-Coded an AI Pen Tester–Now It's Roasting My Security Flaws (score: 7, 3 comments)
URL: https://news.ycombinator.com/item?id=43414134

https:&#x2F;&#x2F;github.com&#x2F;firetix&#x2F;vibe-pen-tester<p>I combined vibe-coding (chat-based coding) with my cybersecurity experience to build an autonomous AI pen tester. It’s smarter than traditional scanners, thinks like a human, and definitely isn’t shy about pointing out vulnerabilities. Feedback welcome!

> Noice

> Here is a clickable link <a href="http:&#x2F;&#x2F;github.com&#x2F;firetix&#x2F;vibe-pen-tester" rel="nofollow">http:&#x2F;&#x2F;github.com&#x2F;firetix&#x2F;vibe-pen-tester</a>

> nice

### Show HN: Scan vibe coded apps for security vulnerabilities (score: 1, 1 comments)
URL: https://vibeappscanner.com/

I&#x27;m a security engineer and started playing around with AI coding tools last year. I noticed a lot of basic security issues: exposed api keys, missing input sanitization, no rate limiting etc. So I built this to scan for them automatically.

> Hello, I am a security researcher. I found critical issues on your site. Do you have a bug bounty program.

### Bugbunny: Securing VibeCoded Apps (score: 6, 0 comments)
URL: https://news.ycombinator.com/item?id=45721704

Security has always been an after thought, especially with the current vibecoding trend. I have spent the past year working on an autonomous pentest agent for vibe coded apps, now you do not need to wait for days or spend thousands to get your app audited. I have used the agent to detect vulnerabilities in large production systems and have been able to get over 15 CVEs in the process. some examples below<p>CVE-2025-58434 (9.8&#x2F;10) - Flowise Full Account take over<p>CVE-2025-61622 (9.8&#x2F;10) - Apache Pyfory RCE<p>A lot more pending CVEs.<p>Right now the service is currently in beta stage, I am currently seeking feedback and its free for anyone to pentest there vibe coded app<p>The URL is: bugbunny.ai<p>Please let me know what you think if you find it useful.

### Show HN: Xpaper – A Chrome extension to turn your X feed into a newsletter (score: 1, 0 comments)
URL: https://github.com/laiso/xpaper

Hi HN,<p>I built Xpaper (<a href="https:&#x2F;&#x2F;github.com&#x2F;laiso&#x2F;xpaper" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;laiso&#x2F;xpaper</a>), an open-source Chrome extension that curates and summarizes your X (Twitter) timeline into a clean, readable newsletter format.<p>Like many of you, I wanted to distance myself from the endless scrolling of Twitter, but completely quitting wasn&#x27;t an option—I still needed to extract the signal from the noise. I built this to solve that exact dilemma.<p>I took a specific technical approach that I thought HN might find interesting:<p>1. *No Backend, Pure DOM Scraping:* 
I didn&#x27;t want to mess with the restrictive official API or run a fragile scraping backend. Instead, the extension reads the timeline directly from the DOM in your active tab. Since it only processes what&#x27;s already visible locally on your screen for personal use, it operates cleanly within the browser environment.<p>2. *Cloud LLMs for Best UX, Local LLM…

