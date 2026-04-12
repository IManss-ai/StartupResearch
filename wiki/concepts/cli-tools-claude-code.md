# CLI Tools for Claude Code Workflows

**Source:** `raw/CLI tools for Claude code.md` — Claude conversation, 2026-04-05

---

## Why CLIs Multiply Agent Capability

Claude Code runs in a terminal and can execute any CLI tool directly. This creates a closed feedback loop: write code → run it → read errors → fix → repeat — with no human copy-pasting. The agent chains tools the same way a senior dev would: `build → test → lint → fix → commit`.

---

## Essential Tools (Ranked by Impact for This Stack)

### Priority Install
| Tool | What it does | Why it matters |
|------|-------------|----------------|
| `gh` | GitHub CLI | Claude Code can push, create PRs, manage repos automatically |
| `rg` (ripgrep) | Fast codebase search | Replaces grep; Claude uses constantly to find function definitions |
| `jq` | JSON parsing from terminal | Query startup research output, API responses without opening files |
| `fzf` | Fuzzy interactive search | Search history, files, branches interactively |
| `tmux` | Terminal multiplexer | Run dev server + Claude Code + git in parallel panes |

### Secondary
| Tool | What it does |
|------|-------------|
| `fd` | Faster `find` |
| `bat` | `cat` with syntax highlighting |
| `zoxide` | Smart `cd` — learns frequent dirs, `z safebiz` instead of full path |
| `pgcli` | Postgres CLI with autocomplete (better than raw `psql`) |
| `supabase` CLI | Manage Supabase projects, run migrations locally |
| `uv` | Replaces `pip` + `venv`, very fast |
| `tsx` | Run TypeScript directly without compiling |

---

## Install Commands (WSL2/Ubuntu)

```bash
# Core tools
sudo apt update && sudo apt install -y ripgrep fd-find fzf tmux jq bat

# GitHub CLI
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update && sudo apt install gh -y

# Zoxide
curl -sSfL https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh | sh
echo 'eval "$(zoxide init bash)"' >> ~/.bashrc && source ~/.bashrc
```

---

## Telling Claude Code to Use These Tools

Add to `CLAUDE.md` in each project:

```markdown
## Available CLI Tools
- rg: use instead of grep for all codebase searches
- jq: use for any JSON parsing or filtering
- gh: use for all GitHub operations (push, PR, issues)
- fzf: available for interactive selection if needed
- tmux: terminal is likely inside a tmux session
- zoxide: use `z` instead of `cd` for navigation
```

---

## Key Usage Patterns

```bash
# rg — find function across codebase
rg "taxRegime" ~/safebiz-kz --type ts

# jq — query research output
cat results.json | jq '.ideas[] | select(.confidence == "HIGH")'

# fzf — interactive file open
find ~/safebiz-kz -type f | fzf

# gh — create PR from terminal
gh pr create --title "Add tax calculator" --body "Closes #12"

# tmux — 3-pane dev setup
# Pane 1: npm run dev | Pane 2: Claude Code | Pane 3: git
```

---

## Related Articles
- [[people/karpathy-coding-thesis]] — Karpathy on CLI-native agents as the native AI interface
- [[people/farzatv-personal-wiki]] — agent wiki system that benefits from these tools
- [[index]] — master wiki index
