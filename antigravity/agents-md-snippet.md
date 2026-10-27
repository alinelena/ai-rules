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

## 2. Elephant/Goldfish & Project Skills Snippet (Inject when `elephant-goldfish` or `dev-template` is enabled — default: ON)

```markdown
<<<EG_SNIPPET_START>>>
## Working with Antigravity (Project & Elephant/Goldfish Skills)

This project has installed workspace skills in `.agents/skills/`, including the project development guide (`<project_name>-dev`) and the five **Elephant/Goldfish** workflow skills (from [`ddmms/elephant-goldfish`](https://github.com/ddmms/elephant-goldfish)) inspired by [Dave Rensin's Elephant/Goldfish pattern](https://drensin.medium.com/elephants-goldfish-and-the-new-golden-age-of-software-engineering-c33641a48874):
- **Elephant**: The working session with full context (`AGENTS.md`, recent turns, architectural history).
- **Goldfish**: A fresh subagent spawned via `invoke_subagent` (`TypeName: "self"` or `"research"`, or `invoke_agent` in Gemini CLI) with **no prior context**, receiving only the seed, problem doc, design doc, or diff.

### Tool Mapping for Antigravity
When executing `.agents/skills/eg-*/SKILL.md` in Antigravity IDE / Antigravity 2.0:
- `invoke_agent` → `invoke_subagent` (`TypeName: "self"` for general/critic/reviewer goldfish, `TypeName: "research"` for read-only codebase/web exploration, `Model: "inherit"`)
- `ask_user` → `ask_question`
- `run_shell_command` → `run_command`
- `write_file` / `replace` → `write_to_file` / `replace_file_content`
- `google_web_search` / `web_fetch` → `search_web` / `read_url_content`

### Available Workspace Skills

| Intent | Slash Command / Trigger | Description |
|---|---|---|
| Project dev stack & commands | `/<project_name>-dev` | Environment (`micromamba` / `uv`), build backend, linting (`ruff`), testing (`pytest`), and CI/CD reference for `<project_name>`. |
| Early-stage concept design | `/eg-brainstorm` or `"Run eg-brainstorm for <rough idea>"` | Multiple goldfish in parallel generate divergent ideas across distinct lenses. All framing questions via `ask_question`. Hands off to `eg-prd` or `eg-new-feature`. |
| Product Requirements Doc | `/eg-prd` or `"Write an eg-prd for <feature>"` | Codebase grounding → structured gap-filling → parallel research goldfish → synthesized PRD. Saves to `[BOOTSTRAP: prd path, e.g. docs/prds/]`. |
| Bug fix flow | `/eg-fix-bug` or `"Run eg-fix-bug for <description \| #issue>"` | Problem doc → goldfish diagnosis check → failing test → fix → `eg-precommit-review` → test gate. |
| Feature flow | `/eg-new-feature` or `"Run eg-new-feature for <description>"` | Scope confirm → design doc → three-goldfish design check (comprehension + critic + readiness) → implement → `eg-precommit-review` → test gate. [BOOTSTRAP: one-line summary of stack-specific design rubric items.] |
| Independent review | `/eg-precommit-review` or `"Run eg-precommit-review"` | Local independent-reviewer loop on the pending diff ([BOOTSTRAP: pre-flight summary]). |
| Rethink on new info | `/interject <new info>` | Halts current plan, audits invalidated assumptions, and rethinks the approach from first principles. |

Each skill workflow stops short of committing. Authorize the commit explicitly when ready. [BOOTSTRAP: commit-policy reminder if the project has one]
<<<EG_SNIPPET_END>>>
```

## 3. Janus-Core Atomistic Skills Snippet (Inject when `janus-core` is enabled)

```markdown
<<<JANUS_CORE_SNIPPET_START>>>
## Janus-Core Atomistic Simulation Suite

This project integrates atomistic calculation skills and execution rules from STFC [`janus-core`](https://github.com/stfc/janus-core) (docs: [`https://stfc.github.io/janus-core/`](https://stfc.github.io/janus-core/)):

### Execution Rules
1. **Python Environment**: Run simulations in the `janus` environment (`micromamba run -n janus python` or `uv run --no-project python`).
2. **Headless Execution**: Always pass `--no-tracker` in scripts and automated pipelines to prevent CodeCarbon emission overhead.
3. **Cell Relaxation Filter**: Prefer `--filter FrechetCellFilter` for periodic geometry optimization.
4. **Structure Verification**: Validate structure geometry using `python janus-core/tools/structure_inspector.py <file>` before launching intensive calculations.

### Available Janus-Core Skills

| Skill | Slash Command | Scope |
| :--- | :--- | :--- |
| Foundation Guide | `/janus-core` | MLIP architectures (`mace_mp`, `sevennet`, `chgnet`, etc.), devices (`cpu`, `cuda`, `mps`, `xpu`), YAML workflows |
| Single Point | `/janus-singlepoint` | Static energy, forces, Cauchy stress tensors, and Hessians |
| Geometry Optimization | `/janus-geomopt` | Coordinate and unit cell relaxation (`FrechetCellFilter`, variable pressure) |
| Molecular Dynamics | `/janus-md` | NVE, NVT, NPT simulations, temperature ramps, PLUMED metadynamics |
| EOS & Elasticity | `/janus-eos-elasticity` | Energy-volume fitting, bulk modulus, full 6x6 $C_{ij}$ stiffness tensor |
| Phonons | `/janus-phonons` | Phonon dispersion curves, DOS, and vibrational thermodynamics via Phonopy |
| NEB | `/janus-neb` | Climbing Image NEB (CI-NEB), IDPP interpolation, reaction barriers |
| Descriptors | `/janus-descriptors` | MLIP invariant representations extraction (mean, per-atom, per-element) |
| Train MLIP | `/janus-train-mlip` | MACE foundation model training and transfer learning fine-tuning |
| Trajectory Analysis | `/janus-analysis` | MD observables (RDF $g(r)$, VAF, MSD, diffusion coefficients) |

To sync skills and reference docs with upstream releases: `./janus-core/update.sh`
<<<JANUS_CORE_SNIPPET_END>>>
```

## 4. AiiDA-MLIP Workflow Skills Snippet (Inject when `aiida-mlip` is enabled)

```markdown
<<<AIIDA_MLIP_SNIPPET_START>>>
## AiiDA-MLIP Workflow Suite

This project integrates automated provenance and high-throughput calculation workflows from STFC [`aiida-mlip`](https://github.com/stfc/aiida-mlip) (docs: [`https://stfc.github.io/aiida-mlip/`](https://stfc.github.io/aiida-mlip/)):

### Execution Rules
1. **Environment & Daemon**: Run commands in `janus` (`micromamba run -n janus verdi ...`) and ensure `verdi daemon status` is running.
2. **Execution Code**: Use the registered `janus@localhost` code.
3. **AiiDA ORM Data Types**: Pass inputs as `StructureData`, `ModelData`, or `JanusConfigfile`.
4. **Emissions**: Set `tracker: false` in configurations.

### Available AiiDA-MLIP Skills

| Skill | Slash Command | Scope |
| :--- | :--- | :--- |
| AiiDA-MLIP Foundation | `/aiida-mlip-core` | AiiDA profile setup, code configuration, `ModelData`, `JanusConfigfile` |
| Single Point Calc | `/aiida-mlip-singlepoint` | Provenance-tracked static calculations via `mlip.sp` |
| Geometry Optimization | `/aiida-mlip-geomopt` | Structure relaxation and variable-cell optimization via `mlip.opt` |
| Molecular Dynamics | `/aiida-mlip-md` | Trajectory and thermodynamic sampling via `mlip.md` |
| Phonons | `/aiida-mlip-phonons` | Lattice dynamics and thermal calculations via `mlip.ph` |
| Descriptors | `/aiida-mlip-descriptors` | Invariant representation featurization via `mlip.descriptors` |
| Train MLIP | `/aiida-mlip-train` | Provenance-tracked MACE training and fine-tuning via `mlip.train` |
| High-Throughput Workflows | `/aiida-mlip-workflows` | High-throughput workgraphs with `aiida-workgraph` (`build_ht_calc`) |

To sync skills and reference docs with upstream releases: `./aiida-mlip/update.sh`
<<<AIIDA_MLIP_SNIPPET_END>>>
```
