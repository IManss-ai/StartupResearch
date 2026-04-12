# Farzapedia: Personal Wiki as Agent Knowledge Base

**Source:** `raw/Thread by @FarzaTV.md` — @FarzaTV on X, 2026-04-04

---

## Core Concept

Build a personal wiki not for yourself to read — but for your AI agent to navigate. The file-system structure (backlinked markdown files + an `index.md` catalog) is natively crawlable by agents. The agent starts at `index.md`, identifies relevant articles, and drills in only as needed.

**This is the architecture of this very vault.**

---

## How It Works

1. Feed raw personal data (diary entries, notes, iMessages) to an LLM
2. LLM compiles 400+ structured articles: people, projects, research areas, inspiration
3. Every article has backlinks to related articles
4. `index.md` is the catalog — the agent's entry point
5. When adding new material, the agent updates 2-3 existing articles or creates a new one

---

## Why It Beats RAG

| RAG | File-system Wiki |
|-----|-----------------|
| Breaks at 60+ docs | Works at 400+ docs |
| Black-box retrieval | Agent understands structure, navigates deliberately |
| Requires embedding infrastructure | Zero infra — plain markdown files |
| Hard to self-update | Agent can write and update articles itself |

Farza's initial ingestion cost: ~$200 (unoptimized). Query cost: low — agent is selective about what it reads.

---

## Startup Signal

Farza considered productizing this ("DM me + tell me your usecase"). The demand signal was strong enough that the tweet went viral. This is essentially what Mansur is building here.

**Opportunity framing:** The "personal Wikipedia for agents" is a workflow pattern, not a product yet. First mover who packages this for a specific professional vertical (lawyers, founders, researchers) owns that niche.

---

## Related Articles
- [[people/karpathy-coding-thesis]] — Karpathy on CLI-native agents and bespoke software era
- [[concepts/cli-tools-claude-code]] — CLI tools that make agent workflows like this faster
- [[index]] — master wiki index
