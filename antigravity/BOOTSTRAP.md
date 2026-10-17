# Antigravity Bootstrap Procedure (`ai-rules`)

This file is read by an **Antigravity** agent (Antigravity IDE, Antigravity 2.0, or `agy` CLI). The user has pointed you at the `ai-rules` repository and asked you to install AI skills and rules into their target project. Follow these steps carefully.

---

## Step 0: Determine Options & Confirm Target

1. **Identify the target repository**:
   - The target repository is the current workspace root (unless the user specified a different target path).
   - Print the target's absolute path.

2. **Resolve installation options**:
   Unless the user explicitly overrides an option in their prompt, use these defaults:
   - **`elephant-goldfish` (`default: ON`)**: Installs and stack-adapts the 5 Elephant/Goldfish workflow skills (`eg-brainstorm`, `eg-prd`, `eg-fix-bug`, `eg-new-feature`, `eg-precommit-review`) from [`https://github.com/ddmms/elephant-goldfish`](https://github.com/ddmms/elephant-goldfish) (branch `ddmms`).
   - **`interject` (`default: ON`)**: Installs the `/interject` rule (`.agents/rules/interject.md`), the `/interject` slash-command skill (`.agents/skills/interject/SKILL.md`), and the `/interject` section in `AGENTS.md` so the user can inject new information at any time and force the agent to rethink its approach from first principles.

3. **Check for existing files**:
   - Check if the target already has `.agents/rules/interject.md`, `.agents/skills/interject/SKILL.md`, or `.agents/skills/eg-*/SKILL.md`.
   - Confirm with the user via `ask_question` before overwriting existing customizations (offer to **Install / Update all enabled defaults**, **Install only `/interject`**, **Install only `elephant-goldfish`**, or **Abort**).

---

## Step 1: Fetch Template Sources

### 1A. Fetch `ai-rules` files (if not reading from a local clone)
If you are reading this file from a local path, read `antigravity/rules/interject.md`, `antigravity/skills/interject/SKILL.md`, and `antigravity/agents-md-snippet.md` directly from that checkout.

If you fetched this file remotely, clone or download `ai-rules` into a temporary directory (or your scratch directory):
```sh
git clone --depth 1 https://github.com/alinelena/ai-rules.git /tmp/ai-rules
```

### 1B. Fetch `ddmms/elephant-goldfish` (when `elephant-goldfish` is enabled — default: ON)
Fetch the upstream `ddmms/elephant-goldfish` templates (branch `ddmms`) into `/tmp/elephant-goldfish`:
```sh
rm -rf /tmp/elephant-goldfish
git clone --depth 1 -b ddmms https://github.com/ddmms/elephant-goldfish.git /tmp/elephant-goldfish
```
*(Fallback if `git clone` is unavailable: use `gh api "repos/ddmms/elephant-goldfish/contents/<PATH>?ref=ddmms" -H 'Accept: application/vnd.github.raw'` or `curl -fsSL "https://raw.githubusercontent.com/ddmms/elephant-goldfish/ddmms/<PATH>"` for `gemini/BOOTSTRAP.md`, `gemini/gemini-md-snippet.md`, and `gemini/commands/eg-{brainstorm,prd,fix-bug,new-feature,precommit-review}.md`.)*

---

## Step 2: Install Option 2 — `/interject` Rule & Skill (Default: ON)

If `interject` is enabled:

1. **Install the Workspace Rule**:
   - Create `<target>/.agents/rules/` if it does not exist.
   - Copy `antigravity/rules/interject.md` to `<target>/.agents/rules/interject.md`.

2. **Install the Slash-Command Skill**:
   - Create `<target>/.agents/skills/interject/` if it does not exist.
   - Copy `antigravity/skills/interject/SKILL.md` to `<target>/.agents/skills/interject/SKILL.md`.
   - This registers `/interject` as a first-class slash command in the Antigravity chat input box while `.agents/rules/interject.md` ensures the `/interject` protocol is always active in the agent's context.

---

## Step 3: Install Option 1 — `elephant-goldfish` Skills (Default: ON)

If `elephant-goldfish` is enabled, follow the adaptive injection workflow from `/tmp/elephant-goldfish/gemini/BOOTSTRAP.md` tailored for Antigravity:

### 3.1 Inspect the Target Stack
Read these files in the target repository if they exist (in parallel):
- `AGENTS.md` (or legacy `GEMINI.md` / `CLAUDE.md`) — existing conventions, commit policy, PR workflow, environment rules
- `pyproject.toml`, `requirements.txt`, `setup.py`, `Pipfile` (Python / `uv` / `micromamba` / `pytest` / `ruff`)
- `package.json`, `tsconfig.json`, `playwright.config.ts`, `vitest.config.ts`, `jest.config.js` (Node / Web)
- `Cargo.toml` (Rust), `go.mod` (Go), `pubspec.yaml` (Flutter/Dart), `Gemfile` (Ruby/Rails), `CMakeLists.txt` / `Makefile` / `justfile`
- `.pre-commit-config.yaml`, `.github/workflows/*.yml`, `Dockerfile`, `docker-compose.yml`
- Run `git log --oneline -10` (if the target has commits) to learn the commit message convention.

Derive and print the **Stack Profile**:
```text
STACK PROFILE
- Language(s) and framework(s):
- Package manager + environment manager (uv / micromamba / npm / cargo / etc.):
- Linter + how to invoke:
- Type-checker + how to invoke (or "n/a"):
- Unit/integration test runner + how to invoke:
- E2E test runner + how to invoke (or "n/a"):
- Security scanner + how to invoke (or "n/a"):
- Dev server: command + URL (or "n/a"):
- Code-generation step required before tests + when (or "n/a"):
- Existing PR workflow, code review process, or merge gates documented in AGENTS.md:
- Commit message convention from `git log`:
- Multi-tenancy / auth / scoping / domain concerns the reviewer should always check:
- Stack-specific gotchas:
```

Ask the user via `ask_question` to confirm or refine the **Stack Profile** before generating the skill files.

### 3.2 Contextualize & Adapt the 5 `eg-*` Skills for Antigravity
Using `/tmp/elephant-goldfish/gemini/commands/eg-{brainstorm,prd,fix-bug,new-feature,precommit-review}.md` as templates:

1. **Replace all `[BOOTSTRAP: ...]` placeholders** with concrete commands and paths from the confirmed Stack Profile:
   - `eg-brainstorm` save path: `docs/eg-brainstorms/<slug>-<YYYY-MM-DD>.md` (or `notes/eg-brainstorms/...`)
   - `eg-prd` save path: `docs/prds/<slug>-<YYYY-MM-DD>.md` (or `docs/specs/...`)
   - `[BOOTSTRAP: lint command]`, `[BOOTSTRAP: typecheck command]`, `[BOOTSTRAP: unit test command]`, `[BOOTSTRAP: e2e test command]`
   - `[BOOTSTRAP: test tier picks]`, `[BOOTSTRAP: stack-specific Hunt for items]`, `[BOOTSTRAP: commit message style note]`

2. **Ensure Antigravity Tool Compatibility**:
   In each generated `.agents/skills/eg-<name>/SKILL.md`, ensure tool instructions work natively in Antigravity IDE / Antigravity 2.0 (while remaining compatible with `agy` / Gemini CLI):
   - Subagents: Use `invoke_subagent` (`TypeName: "self"` or `"research"`, `Model: "inherit"`) (or `invoke_agent` in Gemini CLI).
   - User questions: Use `ask_question` (or `ask_user` in Gemini CLI).
   - Terminal commands: Use `run_command` (or `run_shell_command` in Gemini CLI).
   - File edits: Use `write_to_file` and `replace_file_content` (or `write_file` and `replace` in Gemini CLI).
   - Web research: Use `search_web` and `read_url_content` (or `google_web_search` and `web_fetch` in Gemini CLI).

3. **Write Skill Files**:
   Write the five completed skills to:
   - `<target>/.agents/skills/eg-brainstorm/SKILL.md`
   - `<target>/.agents/skills/eg-prd/SKILL.md`
   - `<target>/.agents/skills/eg-fix-bug/SKILL.md`
   - `<target>/.agents/skills/eg-new-feature/SKILL.md`
   - `<target>/.agents/skills/eg-precommit-review/SKILL.md`

   *(Optional: If the `agy` CLI binary is available in `PATH`, also run `agy skills install .agents/skills/<skill-name> --scope workspace` for each installed skill. In Antigravity IDE and Antigravity 2.0, placing `SKILL.md` inside `.agents/skills/<skill-name>/` automatically registers the skill and its `/<skill-name>` slash command.)*

---

## Step 4: Update `<target>/AGENTS.md`

Read `antigravity/agents-md-snippet.md` and tailor the enabled snippets (`<<<INTERJECT_SNIPPET_START>>>` and/or `<<<EG_SNIPPET_START>>>`) with the target project's `[BOOTSTRAP: ...]` values:

- If `<target>/AGENTS.md` already exists, inject or update the enabled sections cleanly without clobbering existing project rules.
- If `<target>/GEMINI.md` exists but `AGENTS.md` does not, preserve existing rules from `GEMINI.md` into `AGENTS.md` alongside the new snippets.
- If neither exists, create `<target>/AGENTS.md` containing the project overview, stack conventions, and the enabled snippets.

---

## Step 5: Sanity Check & Final Report

1. **Verify**:
   - If `interject` is enabled: `.agents/rules/interject.md` and `.agents/skills/interject/SKILL.md` exist and have valid formatting.
   - If `elephant-goldfish` is enabled: all 5 `.agents/skills/eg-*/SKILL.md` files exist, start with valid YAML frontmatter (`name`, `description`), have zero remaining `[BOOTSTRAP: ...]` placeholders, and retain intact `<<<TEMPLATE_START>>> ... <<<TEMPLATE_END>>>`, `<<<COMPREHENSION_START>>>`, `<<<DESIGN_START>>>`, and `<<<READINESS_START>>>` markers.
   - `AGENTS.md` documents the installed rules and skills.
   - Clean up `/tmp/ai-rules` and `/tmp/elephant-goldfish` if created.

2. **Report to the User**:
   - Summary of installed rules (`.agents/rules/interject.md`) and skills (`.agents/skills/interject/`, `.agents/skills/eg-*/`).
   - Summary of `AGENTS.md` updates.
   - Quick usage cheatsheet (`/interject <new info>`, `/eg-brainstorm`, `/eg-prd`, `/eg-new-feature`, `/eg-fix-bug`, `/eg-precommit-review`).
   - **Do NOT commit or push** unless the user explicitly asks you to stage or commit the changes.

