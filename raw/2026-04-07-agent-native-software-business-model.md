# Raw Research: agent native software business model

**Collected:** 2026-04-07  
**Sources:** 0 Reddit posts · 1 HN stories · 0 YouTube transcripts

---

## Hacker News

### Tell HN: We modeled the cost of boilerplate (it's ~80% of the budget) (score: 3, 0 comments)
URL: https://news.ycombinator.com/item?id=47260560

We spent the last month modeling software budgets to figure out why velocity often feels so low even with senior teams. The short answer seems to be structural: about 80% of engineering time goes to non-differentiating infrastructure (auth, pipelines, CRUD) rather than unique business logic.<p>We call it the &quot;Infrastructure Tax.&quot; We analyzed an anonymized $2.4M engineering spend, and honestly, the breakdown was depressing. Only about 20% of that budget went to features that actually differentiated the product. The rest? Auth flows, database provisioning, CI&#x2F;CD pipelines, and writing the same user schema for the 50th time. Even with modern frameworks, it feels like we&#x27;re constantly paying a toll just to get to the starting line.<p>To quantify this, we built a theoretical model (yeah, I know, models aren&#x27;t reality, but bear with me). We took a standard startup scenario:<p>- 5 developers
- $500k&#x2F;year combined cost (conservative inputs)
- Standard SaaS require…

