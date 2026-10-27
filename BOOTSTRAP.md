# `ai-rules` — Agent Bootstrap Entrypoint

You are an AI coding agent reading the `ai-rules` template repository because the user asked you to install skills and rules into their current project.

## Target Platform: Antigravity (Default)

We currently focus on **Google Antigravity** (Antigravity IDE, Antigravity 2.0, and `agy` CLI).

Read and execute the full procedure in [`antigravity/BOOTSTRAP.md`](./antigravity/BOOTSTRAP.md):
- **If reading from a local clone**: Open `antigravity/BOOTSTRAP.md` directly.
- **If fetching remotely via GitHub**:
  ```sh
  git clone --depth 1 https://github.com/alinelena/ai-rules.git /tmp/ai-rules
  ```
  Then read `/tmp/ai-rules/antigravity/BOOTSTRAP.md` and follow every step.

## Default Options Summary

Unless the user explicitly specified otherwise in their prompt, install **all three** by default:
1. **`elephant-goldfish` (`default: ON`)**: Fetches and stack-adapts the 5 Elephant/Goldfish workflow skills (`eg-brainstorm`, `eg-prd`, `eg-fix-bug`, `eg-new-feature`, `eg-precommit-review`) from [`https://github.com/ddmms/elephant-goldfish`](https://github.com/ddmms/elephant-goldfish) (branch `ddmms`) into `.agents/skills/eg-*/SKILL.md`.
2. **`interject` (`default: ON`)**: Installs the `/interject` rule into `.agents/rules/interject.md`, the `/interject` slash-command skill into `.agents/skills/interject/SKILL.md`, and updates `AGENTS.md` so the user can inject new information via `/interject` at any point and force the agent to audit prior assumptions and rethink its approach from first principles.
3. **`dev-template` (`default: ON`)**: Contextualizes `antigravity/skills/dev-template/SKILL.md` with the target repository's stack profile (`micromamba`, `uv`, `ruff`, `pytest`, CI/CD) and installs it to `.agents/skills/<project_name>-dev/SKILL.md`.
4. **`janus-core` (`optional group`)**: Provisions the 10 STFC `janus-core` atomistic simulation skills (`janus-core`, `janus-singlepoint`, `janus-geomopt`, `janus-md`, `janus-eos-elasticity`, `janus-phonons`, `janus-neb`, `janus-descriptors`, `janus-train-mlip`, `janus-analysis`), execution rules, and `structure_inspector.py` tool from `janus-core/` into `.agents/`, with automated synchronization via `janus-core/update.sh`.
5. **`aiida-mlip` (`optional group`)**: Provisions the 8 STFC `aiida-mlip` workflow and calculation skills (`aiida-mlip-core`, `aiida-mlip-singlepoint`, `aiida-mlip-geomopt`, `aiida-mlip-md`, `aiida-mlip-phonons`, `aiida-mlip-descriptors`, `aiida-mlip-train`, `aiida-mlip-workflows`) and execution rules from `aiida-mlip/` into `.agents/`, with automated synchronization via `aiida-mlip/update.sh`.
