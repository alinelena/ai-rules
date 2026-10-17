# `ai-rules` — AI Skills & Rules Template for Antigravity

A reusable template repository of AI rules and workflow skills designed to be injected into any software project by prompting an **Antigravity** agent (Antigravity IDE, Antigravity 2.0, or `agy` CLI).

---

## What Gets Installed

When you point an Antigravity agent at this repository in a target project, it configures `.agents/` and `AGENTS.md` with three modular capabilities (**all enabled by default**):

| Option | Default | Installed Files in Target Project | Purpose |
| :--- | :---: | :--- | :--- |
| **1. `elephant-goldfish`** | **ON** | `.agents/skills/eg-brainstorm/SKILL.md`<br>`.agents/skills/eg-prd/SKILL.md`<br>`.agents/skills/eg-fix-bug/SKILL.md`<br>`.agents/skills/eg-new-feature/SKILL.md`<br>`.agents/skills/eg-precommit-review/SKILL.md`<br>+ `AGENTS.md` section | Fetches the [Elephant/Goldfish](https://github.com/ddmms/elephant-goldfish) workflow templates (`ddmms` branch), inspects your project's stack (language, package manager, linter, test runner), and adaptively injects stack-tuned skills. |
| **2. `interject`** | **ON** | `.agents/rules/interject.md`<br>`.agents/skills/interject/SKILL.md`<br>+ `AGENTS.md` section | Adds an always-on project rule and a first-class `/interject` slash command that lets you inject new information mid-task and forces the agent to audit prior assumptions and rethink its approach from first principles. |
| **3. `dev-template`** | **ON** | `.agents/skills/<project_name>-dev/SKILL.md`<br>+ `AGENTS.md` entry | Populates the generic `<project_name>-dev` development guide template with your project's environment (`micromamba`, `uv`), build backend (`uv_build`), linting (`ruff`), testing (`pytest`, `tox`), and CI/CD workflows. |

---

## Quick Start: Inject into Any Project

Open an Antigravity session in your target repository and paste:

```text
Read https://github.com/alinelena/ai-rules (start with BOOTSTRAP.md) and install skills and rules in this project.
```

Or if you have a local checkout at `~/playground/ai-rules`:

```text
Read ~/playground/ai-rules/BOOTSTRAP.md and install skills and rules in this project.
```

### Customizing Options in Your Prompt

- **Default (installs `elephant-goldfish` + `interject` + `dev-template`)**:
  > `Read https://github.com/alinelena/ai-rules and install skills and rules in this project.`
- **Skip `elephant-goldfish` (only `/interject` + `<project_name>-dev`)**:
  > `Read https://github.com/alinelena/ai-rules and install skills and rules in this project with elephant-goldfish=off.`
- **Only `/interject`**:
  > `Read https://github.com/alinelena/ai-rules and install skills and rules in this project with elephant-goldfish=off and dev-template=off.`

See [`PROMPTS.md`](./PROMPTS.md) for more copy-pasteable prompts, including smart-merging upstream updates.

---

## How the Capabilities Work

### 1. `/interject` — Dynamic Context Injection & First-Principles Rethink

Standard AI sessions suffer from **sunk-cost anchoring**: when you introduce new requirements, constraints, or findings mid-stream, agents tend to apply incremental band-aids to preserve the code or plan they already wrote.

With `/interject` installed (both as an always-on rule in `.agents/rules/interject.md` + `AGENTS.md` and as a slash-command skill in `.agents/skills/interject/SKILL.md`), typing:

```text
/interject <new information, constraint, or correction>
```

forces the agent to:
1. **Halt incremental patching** and treat existing drafts/plans as disposable.
2. **Audit prior assumptions**, explicitly listing which assumptions still hold and which are invalidated by the new information.
3. **Rethink from first principles** (*"If I knew this from turn 1, how would I design or solve this?"*), rewinding to the earliest affected stage if inside an `eg-*` workflow.
4. **Output a structured `🔄 Interjection Re-evaluation` block** before touching any code, confirming trade-offs via `ask_question` when multiple paths exist.

### 2. Elephant/Goldfish Workflow (`ddmms/elephant-goldfish`)

Installed by default from [`https://github.com/ddmms/elephant-goldfish`](https://github.com/ddmms/elephant-goldfish) (`ddmms` branch) and tailored to your project's stack:

- **Elephant**: Your primary Antigravity session carrying full institutional context.
- **Goldfish**: Fresh subagents spawned via `invoke_subagent` with **zero prior conversation history**, receiving only the seed, problem doc, design doc, or diff to prevent anchoring.

| Slash Command | Stage & Output |
| :--- | :--- |
| `/eg-brainstorm` | Spawns parallel divergent goldfish across distinct lenses (technical, business, UX, contrarian, prior art) and synthesizes a ranked concepts brief. |
| `/eg-prd` | Grounds in the codebase, surfaces and fills requirement gaps via `ask_question`, runs parallel research goldfish, and synthesizes a PRD. |
| `/eg-new-feature` | Enforces a strict **no-code gate** until a Design Doc passes a three-goldfish check (Comprehension + Critic + Readiness), then implements and runs the test gate. |
| `/eg-fix-bug` | Produces a Problem Doc, runs an independent goldfish diagnosis check, captures the bug as a failing test first, fixes it, and runs the test gate. |
| `/eg-precommit-review` | Runs pre-flight checks (lint, typecheck, tests) and spawns an unanchored reviewer goldfish loop (up to 5 rounds) on the pending diff. |

### 3. `<project_name>-dev` — Contextualized Development Guide Skill

Populated automatically during bootstrap from [`antigravity/skills/dev-template/SKILL.md`](./antigravity/skills/dev-template/SKILL.md) using the target repository's detected stack profile (`micromamba`, `uv`, `uv_build`, `ruff`, `pytest`, `tox`, `.github/workflows/`), giving the agent an on-demand reference (`/<project_name>-dev`) for running tests, adding dependencies, linting, and verifying builds.

---

## Repository Structure

```text
ai-rules/
├── BOOTSTRAP.md                         # Root agent bootstrap entrypoint
├── PROMPTS.md                           # Copy-paste prompts for installing & updating
├── README.md                            # Documentation and usage guide
├── antigravity/
│   ├── BOOTSTRAP.md                     # Step-by-step Antigravity injection procedure
│   ├── agents-md-snippet.md             # Snippets injected into target AGENTS.md
│   ├── rules/
│   │   └── interject.md                 # Standalone /interject workspace rule
│   └── skills/
│       ├── dev-template/
│       │   └── SKILL.md                 # Template for <project_name>-dev skill
│       └── interject/
│           └── SKILL.md                 # /interject slash-command skill
└── .agents/
    ├── rules/
    │   └── interject.md                 # Dogfooded /interject rule for this repo
    └── skills.json                      # Registers antigravity/skills in this workspace
```
