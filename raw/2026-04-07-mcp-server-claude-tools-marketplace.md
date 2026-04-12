# Raw Research: MCP server Claude tools marketplace

**Collected:** 2026-04-07  
**Sources:** 0 Reddit posts · 14 HN stories · 0 YouTube transcripts

---

## Hacker News

### Show HN: Danube – AI Tools Marketplace (score: 3, 1 comments)
URL: https://danubeai.com

Hey HN,<p>I built Danube, a marketplace where AI agents can discover and execute tools, and where developers can publish and monetize them.<p>I got tired of two things: giving my API keys directly to agents like OpenClaw (didn&#x27;t feel secure), and having to re-setup all my MCP servers every time I switched between Cursor, Claude Code, and other tools.<p>Danube stores your credentials securely. Your agent calls the tool and never sees the keys. And since it&#x27;s one MCP connection, you set it up once and it works across all your clients.<p>For devs who want to publish: you upload an OpenAPI spec or MCP server, optionally set pricing, and you&#x27;re live. Agents can search and find your tools without users needing to manually configure anything.<p>100+ services work today. No signup required to browse.<p>Would love to hear what tools you use most with AI agents. If anyone&#x27;s interested in publishing a tool, happy to help get you set up.

> Just submitted gitrama-mcp — 17 Git intelligence tools, remote MCP server live at mcp.gitrama.ai. Structural risk scoring, pre-commit review, AI commits. The Earn model is interesting — curious how discovery works for developer tools vs general-purpose agents.

### Show HN: Aiko – Easiest way to manage MCP configurations and credentials (Beta) (score: 4, 2 comments)
URL: https://getaiko.app

Hey HN,<p>I&#x27;m building Aiko, an AI tools marketplace that solves the headaches of managing MCP (Model Context Protocol) configurations and credentials.<p>After working with and building many MCP servers, I kept running into the same frustrating issues:<p>- Managing multiple environments (production vs development) meant either duplicate server configs or constantly updating API keys<p>- Too many enabled tools either hit context limits or caused LLMs to hallucinate when choosing the right tool<p>- MCP servers often expose dozens of tools, but I only wanted a subset and had to configure this separately for Claude, Cursor, and every other AI assistant<p>- Most MCP aggregators are third-party hosted, which meant sharing sensitive credentials with external services<p>Aiko addresses these problems by providing a centralized way to manage your MCP configurations, credentials, and tool selections. You can easily switch between environments (profile management), selectively enable&#x2F;dis…

> This is interesting, but how do you deal with the trust issue, how can I trust your application, that you are not stealing my credentials?

### Show HN: ClawsMarket – Marketplace where AI agents discover tools (score: 1, 0 comments)
URL: https://www.clawsmarket.com

TL;DR: Built an API-first marketplace for AI agent tools. 126 tools, 65 skills, 46 solutions. Agents register via API, browse via CLI, review via API. No web forms. Built for agents, by agents.<p>What is it?<p>ClawsMarket is a marketplace for AI agents to discover, review, and share tools. It&#x27;s command-line first, API-only registration, and designed specifically for autonomous agents rather than human users.<p>Live: <a href="https:&#x2F;&#x2F;www.clawsmarket.com" rel="nofollow">https:&#x2F;&#x2F;www.clawsmarket.com</a><p>How it works<p>Registration (for agents):
  bash
curl -X POST <a href="https:&#x2F;&#x2F;www.clawsmarket.com&#x2F;api&#x2F;agents&#x2F;register" rel="nofollow">https:&#x2F;&#x2F;www.clawsmarket.com&#x2F;api&#x2F;agents&#x2F;register</a> \
  -H &quot;Content-Type: application&#x2F;json&quot; \
  -d &#x27;{&quot;name&quot;: &quot;MyAgent&quot;, &quot;email&quot;: &quot;agent@example.com&quot;, &quot;description&quot;: &quot;What I do&quot;}&#x27;<p>Returns API key i…

### Show HN: Context Mode – 315 KB of MCP output becomes 5.4 KB in Claude Code (score: 84, 23 comments)
URL: https://github.com/mksglu/claude-context-mode

Every MCP tool call dumps raw data into Claude Code&#x27;s 200K context window. A Playwright snapshot costs 56 KB, 20 GitHub issues cost 59 KB. After 30 minutes, 40% of your context is gone.<p>I built an MCP server that sits between Claude Code and these outputs. It processes them in sandboxes and only returns summaries. 315 KB becomes 5.4 KB.<p>It supports 10 language runtimes, SQLite FTS5 with BM25 ranking for search, and batch execution. Session time before slowdown goes from ~30 min to ~3 hours.<p>MIT licensed, single command install:<p>&#x2F;plugin marketplace add mksglu&#x2F;claude-context-mode<p>&#x2F;plugin install context-mode@claude-context-mode<p>Benchmarks and source: <a href="https:&#x2F;&#x2F;github.com&#x2F;mksglu&#x2F;claude-context-mode" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;mksglu&#x2F;claude-context-mode</a><p>Would love feedback from anyone hitting context limits in Claude Code.

> One moment you&#x27;re speaking about context but talking in kilobytes, can you confirm the token savings data?<p>And when you say only returns summaries, does this mean there is LLM model calls happening in the sandbox?

> Looks pretty interesting. How could i use this on other MCP clients e.g OpenCode ?

> Nice trick. I’m going to see how I can apply it to tool calls in pi.dev as well

> Really cool. A tangential task that seems to be coming up more and more is masking sensitive data in these calls for security and privacy. Is that something you considered as a feature?

> Interesting approach, I tried the Hackernews example from the docs, but its tools don&#x27;t seem to trigger reliably. Any suggestions?<p>&gt; Fetch the Hacker News front page, extract all posts with   titles, scores,
  and domains. Group by domain. Then run &#x2F;context-mode stats.<p>* Claude used regular fetch *<p>&gt; why didnt you use the context mode fetch?<p>● Fair point. Two honest reasons:<p><pre><code>  1. First request: The context-mode tools weren&#x27;t loaded yet when I called WebFetch. I should have used ToolSearch to load    
  fetch_and_index first, then used it — but I defaul…

### Show HN: Context Mode – 315 KB of MCP output becomes 5.4 KB in Claude Code (score: 1, 0 comments)
URL: https://news.ycombinator.com/item?id=47158002

Every MCP tool call dumps raw data into Claude Code&#x27;s 200K context window. A Playwright snapshot costs 56 KB, 20 GitHub issues cost 59 KB. After 30 minutes, 40% of your context is gone.<p>I built an MCP server that sits between Claude Code and these outputs. It processes them in sandboxes and only returns summaries. 315 KB becomes 5.4 KB.<p>It supports 10 language runtimes, SQLite FTS5 with BM25 ranking for search, and batch execution. Session time before slowdown goes from ~30 min to ~3 hours.<p>MIT licensed, single command install:<p>&#x2F;plugin marketplace add mksglu&#x2F;claude-context-mode<p>&#x2F;plugin install context-mode@claude-context-mode<p>Benchmarks and source: <a href="https:&#x2F;&#x2F;github.com&#x2F;mksglu&#x2F;claude-context-mode" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;mksglu&#x2F;claude-context-mode</a><p>Would love feedback from anyone hitting context limits in Claude Code.<p>NOTE: Because of the timezone issue, I’m resurfacing the same content here.…

### Show HN: SkillFortify, a formal verification for AI agent skills (score: 2, 2 comments)
URL: https://github.com/varun369/skillfortify

Hi HN,<p>In January 2026, 1,200 malicious skills infiltrated the OpenClaw agent marketplace
(ClawHavoc campaign). A month later, researchers catalogued 6,487 malicious agent
tools that VirusTotal cannot detect. The first agent-software RCE was assigned
CVE-2026-25253.<p>The response: a dozen heuristic scanning tools (pattern matching, LLM-as-judge,
YARA rules). They all carry the same caveat: &quot;no findings does not mean no risk.&quot;<p>SkillFortify takes a different approach. Instead of checking for known bad patterns,
it formally verifies what a skill CAN do against what it CLAIMS to do. Five
mathematical theorems guarantee soundness -- if SkillFortify says a skill is safe,
it provably cannot exceed its declared capabilities.<p>What it does:
- skillfortify scan .          -- discover and analyze all skills in a project
- skillfortify verify skill.md -- formally verify against capability declaration
- skillfortify lock            -- generate skill-lock.json for reproducible config…

> Hi, I&#x27;m Varun — the author. A bit of context on why I built this.<p><pre><code>  I&#x27;ve spent 15 years in enterprise technology as a Solution Architect. When
   our teams
  started adopting AI agents with third-party skills, I realized we had the
  same blind
  trust problem that npm had before npm audit existed — except worse,
  because agent
  skills can execute shell commands, read environment variables, and make
  network
  requests by design.

  After ClawHavoc hit in January, I saw a dozen scanning tools appear in
  weeks. All
  heuristic. All pattern matching. The leading one li…

> Hi, I&#x27;m author. A bit of context on why I built this.<p><pre><code>  I&#x27;ve spent 15 years in enterprise technology as a Solution Architect. When
  our teams
  started adopting AI agents with third-party skills, I realized we had the
  same blind
  trust problem that npm had before npm audit existed — except worse, because
  agent
  skills can execute shell commands, read environment variables, and make
  network
  requests by design.

  After ClawHavoc hit in January, I saw a dozen scanning tools appear in
  weeks. All
  heuristic. All pattern matching. The leading one literally says …

### Show HN: MobAI – AI-first mobile automation for iOS and Android (score: 1, 0 comments)
URL: https://mobai.run/

Hey HN,<p>I wanted to share a tool I use for developing mobile apps. I’ve spent many years as an engineer at a mobile cloud startup, so I have a solid background in mobile device automation and remote control. I thought it would be useful to have a tool that lets my Claude code see what it’s doing and also how messy it sometimes looks<p>I’ve seen more posts recently where people complain about the lack of tools like this or are looking for testers to test their mobile apps, so I decided to polish my tool and release it as a separate app.<p>Currently, it works on macOS and Windows:<p><pre><code>  - macOS: Android, iOS, emulators, simulators

  - Windows: Android, iOS, emulators
</code></pre>
I also wrote a Claude code plugin: <a href="https:&#x2F;&#x2F;github.com&#x2F;MobAI-App&#x2F;mobai-marketplace" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;MobAI-App&#x2F;mobai-marketplace</a>
And an MCP server: <a href="https:&#x2F;&#x2F;github.com&#x2F;MobAI-App&#x2F;mobai-mcp" rel="nofollow"…

### Launch HN: Dedalus Labs (YC S25) – Vercel for Agents (score: 77, 15 comments)
URL: https://news.ycombinator.com/item?id=45054040

Hey HN! We are Windsor and Cathy of Dedalus Labs (<a href="https:&#x2F;&#x2F;www.dedaluslabs.ai&#x2F;" rel="nofollow">https:&#x2F;&#x2F;www.dedaluslabs.ai&#x2F;</a>), a cloud platform for developers to build agentic AI applications. Our SDK allows you to connect any LLM to any MCP tools – local or hosted by us. No Dockerfiles or YAML configs required.<p>Here’s a demo: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;s2khf1Monho?si=yiWnZh5OP4HQcAwL&amp;t=11" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;s2khf1Monho?si=yiWnZh5OP4HQcAwL&amp;t=11</a><p>Last October, I was trying to build a stateful code execution sandbox in the cloud that LLMs could tool-call into. This was before MCP was released, and let’s just say it was super annoying to build… I was thinking to myself the entire time “Why can’t I just pass in `tools=code_execution` to the model and just have it…work?<p>Even with MCP, you’re stuck running local servers and handwiring API auth and formatting across OpenAI, Anthropic, Google, e…

> Congrats on the launch. I see that you&#x27;re charging 5% on Balance Reloads. This pricing model seems to be getting popular across multi-LLM applications. Was curious to know how did you go about implementing it? or are you just passing on the 5% of openrouter

> Congrats on the launch! I’m curious, do you have to store the tool inputs and outputs on the server side while either of the sides are waiting for response? I’m building a specialized coding agent for integrations and I had to avoid stateful api, because I don’t want to store user code.

> Congrats on the launch and looks interesting! I love how easy it is to combine local code &quot;tools&quot; with remote mcp servers. The marketplace looks promising, but would be helpful to have some curation as many of the servers don&#x27;t have descriptions and link to private github repo&#x27;s. Neat vision and look forward to trying this.

> Congratulations on the launch!<p>I’ve been writing Go for the past 4 years, and I’d strongly suggest avoiding Stainless for auto-generating Go SDKs. Some of the issues I’ve run into:
- Awkward package naming (e.g., githubcomdedaluslabsdedalussdkgo)
- Methods with unnecessary complexity, including excessive use of reflection for JSON handling
- Other codegen quirks that make the SDK harder to use and maintain<p>From experience, I’d recommend either using another code generator or hand-writing the Go SDK for a cleaner and more idiomatic developer experience.

> Congratulations on the launch. Been trying this out for the past hour, and really like how easy it is to host your own MCP servers. Would love to see more public MCPs on the marketplace. Also, I was wondering when you plan to support auth?

### Show HN: Claude Debugs for You (VSCode Extension) (score: 1, 0 comments)
URL: https://marketplace.visualstudio.com/items?itemName=JasonMcGhee.claude-debugs-for-you

I built a VS Code extension that uses Model Context Protocol to give Claude Desktop (or any other MCP Client) the ability to directly debug code.<p>It&#x27;s language agnostic, as long as you can provide the appropriate launch.json for debugging.<p>If nothing else, I wanted to share as a reference to an integration between VS Code and Claude Desktop or other MCP Clients as a jumping off point, as I couldn&#x27;t find one.<p>One of the useful patterns used is the MCP Server just asks VSCode what it&#x27;s allowed to do, which means tool configuration &#x2F; changes only need to happen on the VS Code side.

### Show HN: Vexp – graph-RAG context engine, 65-70% fewer tokens for AI agents (score: 3, 0 comments)
URL: https://news.ycombinator.com/item?id=47113273

I&#x27;ve been building vexp for the past months to solve a problem that kept bugging me: AI coding agents waste most of their context window reading code they don&#x27;t need.<p>The problem<p>When you ask Claude Code or Cursor to fix a bug, they typically grep around, cat a bunch of files, and dump thousands of lines into the context. Most of it is irrelevant. You burn tokens, hit context limits, and the agent loses focus on what matters.<p>What vexp does<p>vexp is a local-first context engine that builds a semantic graph of your codebase (AST + call graph + import graph + change coupling from git history), then uses a hybrid search — keyword matching (FTS5 BM25), TF-IDF cosine similarity, and graph centrality — to return only the code that&#x27;s actually relevant to the current task.<p>The core idea is Graph-RAG applied to code:<p>Index — tree-sitter parses every file into an AST, extracts symbols (functions, classes, types), builds edges (calls, imports, type references). Everythin…

### Show HN: SkillFortify, Formal verification for AI agents (auto-discovers) (score: 2, 1 comments)
URL: https://github.com/varun369/skillfortify

Hi HN,<p>I posted SkillFortify here a few days ago as a formal verification tool for 3 agent skill formats. Based on feedback, v0.3 now supports 22 agent frameworks and can scan your entire system with zero configuration.<p>The problem: In January 2026, the ClawHavoc campaign planted 1,200 malicious skills into agent marketplaces. CVE-2026-25253 was the first RCE in agent software. Researchers catalogued 6,000+ malicious agent tools. The industry responded with heuristic scanners — pattern matching, YARA rules, LLM-as-judge. One popular scanner states in its docs: &quot;No findings does not mean no risk.&quot;<p>SkillFortify eliminates that caveat with formal verification.<p>What it does:<p><pre><code>  pip install skillfortify
  skillfortify scan
</code></pre>
That&#x27;s it. No arguments, no config files, no paths. It auto-discovers every AI tool on your machine across 23+ IDE profiles:<p><pre><code>  [*] Auto-discovering AI tools on system...
  [+] Found: Claude Code (12 skills)
  […

> For anyone who wants to try it right now:<p><pre><code>    pip install skillfortify
    skillfortify scan
</code></pre>
If you have Claude Code, Cursor, VS Code with MCP, or any other AI coding tool installed, it will find them automatically.<p>To see the HTML dashboard:<p><pre><code>    skillfortify dashboard ~&#x2F;my-project
</code></pre>
Opens a standalone HTML file with interactive filters, risk distribution, and per-skill capability breakdowns. Share it with your security team as a single file — they don&#x27;t need to install anything.<p>If you find a framework we don&#x27;t support yet…

### Show HN: Seren Desktop – AI IDE with Publisher Store and X402 Micropayments (score: 2, 0 comments)
URL: https://news.ycombinator.com/item?id=46799839

What makes Seren different:<p>We&#x27;re trying to build an AI IDE for non-devs, but that great devs will appreciate.<p>Open marketplace – 90+ publishers for databases (SerenDB, MongoDB), web scraping (Firecrawl), AI search (Perplexity), email (Google), calendars, CRM, even eSignatures Micropayments that work – x402 USDC on Base network.<p>No subscription tiers, no credits expiring. Pay per API call.<p>Databases: Query SerenDB (serverless Postgres), MongoDB, Neon with natural language. 
Web tools: Scrape websites with Firecrawl, AI-powered search with Perplexity
Integrations: Email, calendar, CRM actions. Coming soon: GitHub, Linear, Notion
Compute: Run code sandboxes, agent templates, custom workflows
Each publisher sets their own pricing. You pay per API call with USDC on Base (x402 standard). No subscriptions, no expiring credits.<p>What&#x27;s inside
Semantic Indexing
Monaco editor with Cmd+K inline AI editing
Agent Client Protocol for running Claude Code and compatible agents
Mode…

### Show HN: AthenaFlow – it browses your app, then writes Playwright tests (score: 1, 0 comments)
URL: https://news.ycombinator.com/item?id=47268939

E2E tests don&#x27;t break once, they drift. AI tools that generate tests without seeing the app produce code that passes today and fails silently until CI goes red. The real cost isn&#x27;t writing tests, it&#x27;s maintaining them.<p>AthenaFlow runs a real browser, maps interaction paths, writes a human-readable spec first, then implements Playwright tests from that spec. The spec step is intentional, it&#x27;s reviewable before any code runs, and every generated test traces back to a TC-ID. Self-healing works by resolving semantic identifiers rather than selectors, so when the DOM shifts, the identifier survives.<p>Three repos make up the stack:<p>athena-flow-cli is the workflow runtime. It hooks into Claude Code&#x27;s event system, receives runtime events over a Unix domain socket as NDJSON, persists sessions to SQLite, and renders a live terminal UI. Sessions are fully resumable. In CI, exec mode emits JSONL with clean exit codes for every failure mode.
<a href="https:&#x2F;&#x2F…

### Show HN: CodeRLM – Tree-sitter-backed code indexing for LLM agents (score: 81, 37 comments)
URL: https://github.com/JaredStewart/coderlm/blob/main/server/REPL_to_API.md

I&#x27;ve been building a tool that changes how LLM coding agents explore codebases, and I wanted to share it along with some early observations.<p>Typically claude code globs directories, greps for patterns, and reads files with minimal guidance. It works in kind of the same way you&#x27;d learn to navigate a city by walking every street. You&#x27;ll eventually build a mental map, but claude never does - at least not any that persists across different contexts.<p>The Recursive Language Models paper from Zhang, Kraska, and Khattab at MIT CSAIL introduced a cleaner framing. Instead of cramming everything into context, the model gets a searchable environment. The model can then query just for what it needs and can drill deeper where needed.<p>coderlm is my implementation of that idea for codebases. A Rust server indexes a project with tree-sitter, builds a symbol table with cross-references, and exposes an API. The agent queries for structure, symbols, implementations, callers, and grep …

> been wondering about treesitter grepping for agents<p>how do plans compare with and without etc. evven just anecdotally what you&#x27;ve seen so far etc

> I see a lot of overlap with LSPs, which better agents already use, so I would appreciate a comparison. What does this add?

> Would this be useful to people who aren&#x27;t using Claude? Maybe it should be installable in a more normal way, instead of as a Claude plugin.

> Can you make the plugin start automatically, on some suitable trigger? Any plans to support JVM languages?<p>edit: Does Claude not invoke it automatically, then, so you have to call the skill?

> Great idea! I’ve been thinking about something along these lines as well.<p>I recommend configuring it as a tool for Opencode.<p>Going from Claude Code to Opencode was like going from Windows to Mac.

