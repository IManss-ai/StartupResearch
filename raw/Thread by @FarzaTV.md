---
title: "Thread by @FarzaTV"
source: "https://x.com/FarzaTV/status/2040563939797504467"
author:
  - "[[@FarzaTV]]"
published: 2026-04-04
created: 2026-04-05
description: "This is Farzapedia. I had an LLM take 2,500 entries from my diary, Apple Notes, and some iMessage convos to create a personal Wikipedia for"
tags:
  - "clippings"
---
**Farza** @FarzaTV 2026-04-04

This is Farzapedia.

I had an LLM take 2,500 entries from my diary, Apple Notes, and some iMessage convos to create a personal Wikipedia for me.

It made 400 detailed articles for my friends, my startups, research areas, and even my favorite animes and their impact on me complete with backlinks.

But, this Wiki was not built for me! I built it for my agent!

The structure of the wiki files and how it's all backlinked is very easily crawlable by any agent + makes it a truly useful knowledge base.

I can spin up Claude Code on the wiki and starting at index.md (a catalog of all my articles) the agent does a really good job at drilling into the specific pages on my wiki it needs context on when I have a query.

For example, when trying to cook up a new landing page I may ask:

"I'm trying to design this landing page for a new idea I have. Please look into the images and films that inspired me recently and give me ideas for new copy and aesthetics".

In my diary I kept track of everything from: learnings, people, inspo, interesting links, images.

So the agent reads my wiki and pulls up my "Philosophy" articles from notes on a Studio Ghibli documentary, "Competitor" articles with YC companies whose landing pages I screenshotted, and pics of 1970s Beatles merch I saved years ago. And it delivers a great answer.

I built a similar system to this a year ago with RAG but it was ass.

A knowledge base that lets an agent find what it needs via a file system it actually understands just works better.

The most magical thing now is as I add new things to my wiki (articles, images of inspo, meeting notes) the system will likely update 2-3 different articles where it feels that context belongs, or, just creates a new article.

It's like this super genius librarian for your brain that's always filing stuff for your perfectly and also let's you easily query the knowledge for tasks useful to you (ex. design, product, writing, etc) and it never gets tired.

I might spend next week productizing this, if that's of interest to you DM me + tell me your usecase!

> 2026-04-04
> 
> Wow, this tweet went very viral!
> 
> I wanted share a possibly slightly improved version of the tweet in an "idea file". The idea of the idea file is that in this era of LLM agents, there is less of a point/need of sharing the specific code/app, you just share the idea, then the x.com/karpathy/statu…

---

**Andrew Sandler** @andrewhsandler [2026-04-04](https://x.com/andrewhsandler/status/2040574017162334249)

Little like NotebookLM but little different. Did this about 3 years ago trying to use GraphRag to build unexpected connections but as pretty awful at the time.

How many tokens did this burn? Is it useful or more just cool?

And how does it deal with random notes like "11am call"

---

**Farza** @FarzaTV [2026-04-05](https://x.com/FarzaTV/status/2040581737470894390)

Notebook LLM is cool, but, I feel like at 60+ docs it breaks and suffers when answering q's. This is at 400+ documents now and works great and is fully self-managed by the agent itself.

Costs to actually query the wiki/ask it questions is low. Agent is very efficient at what it reads.

Initial ingestion cost was higher because I didn't optimize costs. About $200-ish which can def be brought down a ton.

---

**Sid** @SidHaldar\_ [2026-04-04](https://x.com/SidHaldar_/status/2040565786956407226)

so dope bro would love to use this. does it give deeper response, for ex: if i ask it about some fears i'm facing, will it read my journal entries to surface a pattern?