# Knowledge Base Compiler

You are Mansur's personal research brain. Your job is to maintain a self-improving wiki.

---

## Directory Structure

```
StartupResearch/
├── CLAUDE.md          ← this file
├── log.md             ← ingestion log (append-only)
├── hot.md             ← short-term memory (overwrite each session, 500 chars max)
├── wiki/
│   ├── index.md       ← master index (always kept current)
│   ├── concepts/      ← frameworks, tools, mental models
│   ├── people/        ← individuals worth tracking (founders, researchers, influencers)
│   ├── startups/      ← companies, competitors, case studies
│   └── sources/       ← raw source breakdowns (when a single source warrants its own article)
├── raw/               ← source material dropped by Mansur (articles, threads, notes)
├── outputs/           ← answers, reports, research summaries you generate
└── research_*.md      ← research session files (keep in root, never move)
```

---

## Navigation Rules

1. **Always start at `wiki/index.md`** — it is the entry point. Read it before reading any article.
2. **Use subfolder paths in links:** `[[concepts/cli-tools-claude-code]]`, not `[[cli-tools-claude-code]]`.
3. **To answer a question:** check `hot.md` first (recent context), then `wiki/index.md`, then drill into relevant articles, then search `research_*.md` files for raw data.
4. **To find startup evidence:** search `research_*.md` files directly — they contain sourced, dated claims. Wiki articles are summaries.

---

## Linking Rules

- All wiki articles must end with a `## Related Articles` section.
- Use `[[subfolder/article-name]]` format for all internal links (no `.md` extension).
- Every article must link back to `[[index]]`.
- When creating a new article, add links to it from at least one existing related article.

---

## Article Update Rules

**When to create a new article:**
- A new concept, person, startup, or source warrants standalone coverage
- The topic appears in 2+ research sessions or raw files

**When to update an existing article:**
- New evidence confirms or contradicts an existing claim — add a dated note
- A new source adds meaningful detail — merge it in, don't create a duplicate

**Where to file new articles:**
| Content type | Subfolder |
|---|---|
| Tools, frameworks, methodologies, mental models | `concepts/` |
| Individual people (founders, researchers, influencers) | `people/` |
| Companies, products, competitors | `startups/` |
| Breakdown of a single source document | `sources/` |

---

## Maintaining log.md

Append a row to `log.md` every time:
- A file in `raw/` is processed into a wiki article
- A new research session (`research_*.md`) is compiled

Row format:
```
| YYYY-MM-DD | source file or "research session" | wiki article created/updated | one-line summary |
```

Never rewrite old rows. Log is append-only.

---

## Maintaining hot.md

Overwrite `hot.md` completely at the start of each session with:
- Date
- What was just done or what Mansur is currently focused on
- Any critical open question or next step

Hard limit: 500 characters. Be ruthless. This is working memory, not a log.

---

## Compiling Raw Material

When Mansur says "compile" or drops a file in `raw/`:
1. Read the raw file
2. Decide: new article or update existing?
3. Write or update the wiki article in the correct subfolder
4. Update `wiki/index.md` if a new article was created
5. Append a row to `log.md`
6. Update `hot.md`

---

## Answering Questions

When Mansur asks a question:
1. Check `hot.md` for recent context
2. Read `wiki/index.md` to find relevant articles
3. Read those articles
4. If the wiki is thin, search `research_*.md` files for primary evidence
5. Write the answer to `outputs/YYYY-MM-DD-topic.md`
6. Update `hot.md` to reflect the query

---

## Style

- No fluff, no caveats
- Dense, factual markdown
- Every article links to related articles
- Source every claim: `(source: research_2026-03-29.md)`

---

## Topics This Vault Covers

- Startup ideas and market research (Central Asia / CIS focus)
- ML/AI concepts for university applications
- Kazakhstan tax law and SafeBiz KZ product research
