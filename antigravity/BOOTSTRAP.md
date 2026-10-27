# Antigravity Bootstrap Procedure (`ai-rules`)

This file is read by an **Antigravity** agent (Antigravity IDE, Antigravity 2.0, or `agy` CLI). The user has pointed you at the `ai-rules` repository and asked you to install AI skills and rules into their target project. Follow these steps carefully.

---

## Step 0: Determine Options & Confirm Target

1. **Identify the target repository**:
   - The target repository is the current workspace root (unless the user specified a different target path).
   - Derive `<project_name>` from the target repository's directory name or package manifest (`pyproject.toml`, `package.json`, `Cargo.toml`, etc.), normalized to lowercase hyphenated form.
   - Print the target's absolute path and detected `<project_name>`.

2. **Resolve installation options**:
   Unless the user explicitly overrides an option in their prompt, use these defaults:
   - **`elephant-goldfish` (`default: ON`)**: Installs and stack-adapts the 5 Elephant/Goldfish workflow skills (`eg-brainstorm`, `eg-prd`, `eg-fix-bug`, `eg-new-feature`, `eg-precommit-review`) from [`https://github.com/ddmms/elephant-goldfish`](https://github.com/ddmms/elephant-goldfish) (branch `ddmms`).
   - **`interject` (`default: ON`)**: Installs the `/interject` rule (`.agents/rules/interject.md`), the `/interject` slash-command skill (`.agents/skills/interject/SKILL.md`), and the `/interject` section in `AGENTS.md` so the user can inject new information at any time and force the agent to rethink its approach from first principles.
   - **`dev-template` (`default: ON`)**: Contextualizes `antigravity/skills/dev-template/SKILL.md` with the target repository's stack profile and installs it to `.agents/skills/<project_name>-dev/SKILL.md`.
   - **`janus-core` (`default: AUTO-DETECT / OFF`)**: Installs the 10 STFC [`janus-core`](https://github.com/stfc/janus-core) atomistic simulation skills, execution rules, and `structure_inspector.py` tool. Auto-enabled if `janus-core` is found in the target's dependencies or explicitly requested (`janus-core=on`).
   - **`aiida-mlip` (`default: AUTO-DETECT / OFF`)**: Installs the 8 STFC [`aiida-mlip`](https://github.com/stfc/aiida-mlip) workflow and calculation skills and execution rules. Auto-enabled if `aiida-mlip` or `aiida` is found in dependencies or explicitly requested (`aiida-mlip=on`).
   - **`atomisticskills` (`default: AUTO-DETECT / OFF`)**: Installs the 6 entrypoint skills, execution rules, and reference catalogs from [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills) (MIT Learning Matter Lab, arXiv:2605.24002) covering 133 modular skills, 9 research workflows, and 11 MCP servers. Auto-enabled if `atomisticskills` is detected in dependencies or explicitly requested (`atomisticskills=on`).

3. **Check for existing files**:
   - Check if the target already has `.agents/rules/interject.md`, `.agents/skills/interject/SKILL.md`, `.agents/skills/<project_name>-dev/SKILL.md`, or `.agents/skills/eg-*/SKILL.md`.
   - Confirm with the user via `ask_question` before overwriting existing customizations.

---

## Step 1: Fetch Template Sources

### 1A. Fetch `ai-rules` files (if not reading from a local clone)
If you are reading this file from a local path, read `antigravity/rules/interject.md`, `antigravity/skills/interject/SKILL.md`, `antigravity/skills/dev-template/SKILL.md`, and `antigravity/agents-md-snippet.md` directly from that checkout.

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

### 1C. Fetch `janus-core`, `aiida-mlip`, and `atomisticskills` Capability Groups (when enabled)
When `janus-core`, `aiida-mlip`, or `atomisticskills` is requested or detected in the target stack:
- If reading from a local clone of `ai-rules`, read from `janus-core/`, `aiida-mlip/`, and `atomisticskills/` directly.
- If fetched remotely, copy from `/tmp/ai-rules/janus-core`, `/tmp/ai-rules/aiida-mlip`, and `/tmp/ai-rules/atomisticskills`.
- Upstream source references:
  - `janus-core`: [`https://github.com/stfc/janus-core`](https://github.com/stfc/janus-core) and [`https://stfc.github.io/janus-core/`](https://stfc.github.io/janus-core/)
  - `aiida-mlip`: [`https://github.com/stfc/aiida-mlip`](https://github.com/stfc/aiida-mlip) and [`https://stfc.github.io/aiida-mlip/`](https://stfc.github.io/aiida-mlip/)
  - `atomisticskills`: [`https://github.com/learningmatter-mit/AtomisticSkills`](https://github.com/learningmatter-mit/AtomisticSkills) and [`https://learningmatter-mit.github.io/AtomisticSkills/`](https://learningmatter-mit.github.io/AtomisticSkills/)

---

## Step 2: Inspect the Target Stack (When `elephant-goldfish` or `dev-template` is Enabled)

Read these files in the target repository if they exist (in parallel):
- `AGENTS.md` (or legacy `GEMINI.md` / `CLAUDE.md`) — existing conventions, commit policy, PR workflow, environment rules
- `pyproject.toml`, `requirements.txt`, `setup.py`, `Pipfile`, `tox.ini` (Python / `uv` / `micromamba` / `pytest` / `ruff`)
- `package.json`, `tsconfig.json`, `playwright.config.ts`, `vitest.config.ts`, `jest.config.js` (Node / Web)
- `Cargo.toml` (Rust), `go.mod` (Go), `pubspec.yaml` (Flutter/Dart), `Gemfile` (Ruby/Rails), `CMakeLists.txt` / `Makefile` / `justfile`
- `.pre-commit-config.yaml`, `.github/workflows/*.yml`, `Dockerfile`, `docker-compose.yml`
- Run `git log --oneline -10` (if the target has commits) to learn the commit message convention.

Derive and print the **Stack Profile**:
```text
STACK PROFILE
- Project name (<project_name>):
- Language(s) and framework(s):
- Package manager + environment manager (uv / micromamba / npm / cargo / etc.):
- Build backend (e.g., uv_build, hatchling, cargo, etc.):
- Linter & formatter + how to invoke:
- Type-checker + how to invoke (or "n/a"):
- Unit/integration test runner & coverage command:
- E2E / special test modes (xvfb-run, tox matrix, playwright, or "n/a"):
- Security scanner + how to invoke (or "n/a"):
- Dev server / entrypoint: command + URL (or "n/a"):
- Code-generation step required before tests + when (or "n/a"):
- CI/CD workflows (.github/workflows/*.yml):
- Existing PR workflow, code review process, or merge gates documented in AGENTS.md:
- Commit message convention from `git log`:
- Multi-tenancy / auth / scoping / domain concerns the reviewer should always check:
- Stack-specific gotchas:
```

Ask the user via `ask_question` to confirm or refine the **Stack Profile** before generating the skill files.

---

## Step 3: Install Enabled Rules & Skills

### 3A. Option 1 — `elephant-goldfish` Skills (Default: ON)
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

### 3B. Option 2 — `/interject` Rule & Skill (Default: ON)
1. **Install the Workspace Rule**:
   - Create `<target>/.agents/rules/` if it does not exist.
   - Copy `antigravity/rules/interject.md` to `<target>/.agents/rules/interject.md`.
2. **Install the Slash-Command Skill**:
   - Create `<target>/.agents/skills/interject/` if it does not exist.
   - Copy `antigravity/skills/interject/SKILL.md` to `<target>/.agents/skills/interject/SKILL.md`.

### 3C. Option 3 — `<project_name>-dev` Development Guide Skill (Default: ON)
1. Read `antigravity/skills/dev-template/SKILL.md`.
2. Replace `<project_name>`, `<Project Name>`, and all `<..._command>` placeholders with the concrete values from the confirmed Stack Profile (omitting inapplicable subsections cleanly).
3. Write the populated skill to `<target>/.agents/skills/<project_name>-dev/SKILL.md`.

*(Optional: If the `agy` CLI binary is available in `PATH`, also run `agy skills install .agents/skills/<skill-name> --scope workspace` for each installed skill. In Antigravity IDE and Antigravity 2.0, placing `SKILL.md` inside `.agents/skills/<skill-name>/` automatically registers the skill and its `/<skill-name>` slash command.)*

### 3D. Option 4 — `janus-core` Skills & Rules Group (When Enabled)
When `janus-core` is enabled (from STFC [`janus-core`](https://github.com/stfc/janus-core)):
1. Copy the 10 skills from `janus-core/skills/` into `<target>/.agents/skills/` (or copy the entire `janus-core/` folder to `<target>/janus-core/` and register `"janus-core/skills"` in `<target>/.agents/skills.json`).
2. Copy `janus-core/rules/janus-rules.md` to `<target>/.agents/rules/janus-rules.md`.
3. Copy `janus-core/tools/structure_inspector.py` to `<target>/tools/structure_inspector.py` (or `<target>/janus-core/tools/`).
4. Ensure `./janus-core/update.sh` is available in `<target>` for syncing future upstream updates.

### 3E. Option 5 — `aiida-mlip` Skills & Rules Group (When Enabled)
When `aiida-mlip` is enabled (from STFC [`aiida-mlip`](https://github.com/stfc/aiida-mlip)):
1. Copy the 8 skills from `aiida-mlip/skills/` into `<target>/.agents/skills/` (or copy the entire `aiida-mlip/` folder to `<target>/aiida-mlip/` and register `"aiida-mlip/skills"` in `<target>/.agents/skills.json`).
2. Copy `aiida-mlip/rules/aiida-mlip-rules.md` to `<target>/.agents/rules/aiida-mlip-rules.md`.
3. Ensure `./aiida-mlip/update.sh` is available in `<target>` for syncing future upstream updates.

### 3F. Option 6 — `atomisticskills` Skills & Rules Group (When Enabled)
When `atomisticskills` is enabled (from MIT Learning Matter Lab [`AtomisticSkills`](https://github.com/learningmatter-mit/AtomisticSkills)):
1. Copy the 6 entrypoint skills from `atomisticskills/skills/` into `<target>/.agents/skills/` (or copy the entire `atomisticskills/` folder to `<target>/atomisticskills/` and register `"atomisticskills/skills"` in `<target>/.agents/skills.json`).
2. Copy the rules in `atomisticskills/rules/*.md` to `<target>/.agents/rules/`.
3. Ensure `./atomisticskills/update.sh` is available in `<target>` for syncing future upstream updates.

---

## Step 4: Update `<target>/AGENTS.md`

Read `antigravity/agents-md-snippet.md` and tailor the enabled snippets (`<<<INTERJECT_SNIPPET_START>>>`, `<<<EG_SNIPPET_START>>>`, `<project_name>-dev`, `<<<JANUS_CORE_SNIPPET_START>>>`, `<<<AIIDA_MLIP_SNIPPET_START>>>`, and `<<<ATOMISTIC_SKILLS_SNIPPET_START>>>`) with the target project's Stack Profile values:

- If `<target>/AGENTS.md` already exists, inject or update the enabled sections cleanly without clobbering existing project rules.
- If `<target>/GEMINI.md` exists but `AGENTS.md` does not, preserve existing rules from `GEMINI.md` into `AGENTS.md` alongside the new snippets.
- If neither exists, create `<target>/AGENTS.md` containing the project overview, stack conventions, and the enabled snippets.

---

## Step 5: Sanity Check & Final Report

1. **Verify**:
   - If `interject` is enabled: `.agents/rules/interject.md` and `.agents/skills/interject/SKILL.md` exist and have valid formatting.
   - If `dev-template` is enabled: `.agents/skills/<project_name>-dev/SKILL.md` exists, has `name: <project_name>-dev` in its YAML frontmatter, and contains zero remaining `<...>` template placeholders.
   - If `elephant-goldfish` is enabled: all 5 `.agents/skills/eg-*/SKILL.md` files exist, start with valid YAML frontmatter (`name`, `description`), have zero remaining `[BOOTSTRAP: ...]` placeholders, and retain intact `<<<TEMPLATE_START>>> ... <<<TEMPLATE_END>>>`, `<<<COMPREHENSION_START>>>`, `<<<DESIGN_START>>>`, and `<<<READINESS_START>>>` markers.
   - If `janus-core` is enabled: all 10 `janus-*` skills exist, execution rules are placed, and `janus-core/update.sh` is executable.
   - If `aiida-mlip` is enabled: all 8 `aiida-mlip-*` skills exist, execution rules are placed, and `aiida-mlip/update.sh` is executable.
   - If `atomisticskills` is enabled: all 6 `atomisticskills-*` skills exist, execution rules are placed, and `atomisticskills/update.sh` is executable.
   - `AGENTS.md` documents the installed rules and skills.
   - Clean up `/tmp/ai-rules` and `/tmp/elephant-goldfish` if created.

2. **Report to the User**:
   - Summary of installed rules and skills.
   - Summary of `AGENTS.md` updates.
   - Quick usage cheatsheet (`/interject <new info>`, `/<project_name>-dev`, `/eg-brainstorm`, `/eg-prd`, `/eg-new-feature`, `/eg-fix-bug`, `/eg-precommit-review`, `/janus-core`, `/aiida-mlip-core`, `/atomisticskills-core`).
   - **Do NOT commit or push** unless the user explicitly asks you to stage or commit the changes.
