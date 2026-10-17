# Snippets to Inject into Target `AGENTS.md`

During bootstrap, tailor and inject the enabled sections below into the target repository's `AGENTS.md` (do not include the outer markdown markers).

## 1. `/interject` Rule Snippet (Inject when `interject` is enabled — default: ON)

```markdown
<<<INTERJECT_SNIPPET_START>>>
## Rule: `/interject` — Dynamic Context Injection & Rethink

Whenever a user prompt starts with or contains `/interject <new information, constraint, or correction>`:
1. **Halt & Drop Sunk-Cost Bias**: Immediately stop incremental patching on the current approach. Treat all prior plans, assumptions, and in-flight drafts as disposable if the new information warrants a better path.
2. **Audit Assumptions**: Explicitly identify which previous assumptions, architectural choices, or plan steps are invalidated or changed by the new information.
3. **Rethink from First Principles**: Re-architect the solution from scratch ("If we knew this from turn 1, what is the cleanest design?"). If inside an `eg-*` workflow, rewind to the earliest affected stage (Seed, PRD, Problem Doc, or Design Doc).
4. **Output `🔄 Interjection Re-evaluation`**: Before editing any files, print:
   - **New Information**: Concise summary of the injected context.
   - **Invalidated / Changed**: Prior assumptions or steps being discarded/modified.
   - **Rethought Approach**: Revised first-principles plan.
   - **Impact on In-Flight Work**: What existing changes are kept, refactored, or reverted.
5. **Confirm or Proceed**: Use `ask_question` if the rethink introduces trade-offs or multiple directions; otherwise execute the revised approach directly.

*(Full rule details in [`.agents/rules/interject.md`](.agents/rules/interject.md) and slash command skill in [`.agents/skills/interject/SKILL.md`](.agents/skills/interject/SKILL.md).)*
<<<INTERJECT_SNIPPET_END>>>
```

## 2. Elephant/Goldfish Snippet (Inject when `elephant-goldfish` is enabled — default: ON)

```markdown
<<<EG_SNIPPET_START>>>
## Working with Antigravity (Elephant/Goldfish Skills)

This project has installed five **Elephant/Goldfish** skills in `.agents/skills/` (from [`ddmms/elephant-goldfish`](https://github.com/ddmms/elephant-goldfish)) inspired by [Dave Rensin's Elephant/Goldfish pattern](https://drensin.medium.com/elephants-goldfish-and-the-new-golden-age-of-software-engineering-c33641a48874):
- **Elephant**: The working session with full context (`AGENTS.md`, recent turns, architectural history).
- **Goldfish**: A fresh subagent spawned via `invoke_subagent` (`TypeName: "self"` or `"research"`, or `invoke_agent` in Gemini CLI) with **no prior context**, receiving only the seed, problem doc, design doc, or diff.

### Tool Mapping for Antigravity
When executing `.agents/skills/eg-*/SKILL.md` in Antigravity IDE / Antigravity 2.0:
- `invoke_agent` → `invoke_subagent` (`TypeName: "self"` for general/critic/reviewer goldfish, `TypeName: "research"` for read-only codebase/web exploration, `Model: "inherit"`)
- `ask_user` → `ask_question`
- `run_shell_command` → `run_command`
- `write_file` / `replace` → `write_to_file` / `replace_file_content`
- `google_web_search` / `web_fetch` → `search_web` / `read_url_content`

### Available Workflow Skills

| Intent | Slash Command / Trigger | Description |
|---|---|---|
| Early-stage concept design | `/eg-brainstorm` or `"Run eg-brainstorm for <rough idea>"` | Multiple goldfish in parallel generate divergent ideas across distinct lenses. All framing questions via `ask_question`. Hands off to `eg-prd` or `eg-new-feature`. |
| Product Requirements Doc | `/eg-prd` or `"Write an eg-prd for <feature>"` | Codebase grounding → structured gap-filling → parallel research goldfish → synthesized PRD. Saves to `[BOOTSTRAP: prd path, e.g. docs/prds/]`. |
| Bug fix flow | `/eg-fix-bug` or `"Run eg-fix-bug for <description \| #issue>"` | Problem doc → goldfish diagnosis check → failing test → fix → `eg-precommit-review` → test gate. |
| Feature flow | `/eg-new-feature` or `"Run eg-new-feature for <description>"` | Scope confirm → design doc → three-goldfish design check (comprehension + critic + readiness) → implement → `eg-precommit-review` → test gate. [BOOTSTRAP: one-line summary of stack-specific design rubric items.] |
| Independent review | `/eg-precommit-review` or `"Run eg-precommit-review"` | Local independent-reviewer loop on the pending diff ([BOOTSTRAP: pre-flight summary]). |
| Rethink on new info | `/interject <new info>` | Halts current plan, audits invalidated assumptions, and rethinks the approach from first principles. |

Each skill workflow stops short of committing. Authorize the commit explicitly when ready. [BOOTSTRAP: commit-policy reminder if the project has one]
<<<EG_SNIPPET_END>>>
```

