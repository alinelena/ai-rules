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
| **4. `janus-core`** | **Optional** | `janus-core/skills/janus-*/SKILL.md`<br>`janus-core/rules/janus-rules.md`<br>`janus-core/tools/structure_inspector.py` | Full skill group and execution rules for STFC [janus-core](https://github.com/stfc/janus-core) (MLIP atomistic simulations: singlepoint, geomopt, md, eos-elasticity, phonons, neb, descriptors, train-mlip, analysis) with an automated sync script. |
| **5. `aiida-mlip`** | **Optional** | `aiida-mlip/skills/aiida-mlip-*/SKILL.md`<br>`aiida-mlip/rules/aiida-mlip-rules.md` | Full skill group and execution rules for STFC [aiida-mlip](https://github.com/stfc/aiida-mlip) (AiiDA provenance workflows: singlepoint, geomopt, md, phonons, descriptors, train, ht_workgraph) with an automated sync script. |
| **6. `atomisticskills`** | **Optional** | `atomisticskills/skills/atomisticskills-*/SKILL.md`<br>`atomisticskills/rules/*.md`<br>`atomisticskills/update.sh` | 130+ modular skills, 9 research workflows, and 11 MCP servers from [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills) (MIT Learning Matter Lab, arXiv:2605.24002) spanning materials discovery, chemistry, drug discovery, and ML potentials with an automated sync script. |

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
- **Include Janus-Core (`janus-core=on`)**:
  > `Read https://github.com/alinelena/ai-rules and install skills and rules in this project with janus-core=on.`
- **Include AiiDA-MLIP (`aiida-mlip=on`)**:
  > `Read https://github.com/alinelena/ai-rules and install skills and rules in this project with aiida-mlip=on.`
- **Include AtomisticSkills (`atomisticskills=on`)**:
  > `Read https://github.com/alinelena/ai-rules and install skills and rules in this project with atomisticskills=on.`
- **Complete Atomistic & Simulation Suite (`janus-core=on` + `aiida-mlip=on` + `atomisticskills=on`)**:
  > `Read https://github.com/alinelena/ai-rules and install all atomistic simulation and workflow skills in this project with janus-core=on, aiida-mlip=on, and atomisticskills=on.`

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

### 4. Janus-Core Atomistic Simulation Suite (`stfc/janus-core`)

Installed from the [`janus-core`](https://github.com/alinelena/ai-rules/tree/main/janus-core) capability group, grounded in STFC [`janus-core`](https://github.com/stfc/janus-core) (docs: [`https://stfc.github.io/janus-core/`](https://stfc.github.io/janus-core/)):

- **Multi-MLIP Foundation**: Support for `mace_mp`, `mace_off`, `sevennet`, `chgnet`, `nequip`, `deepmd`, `orb`, `mattersim`, `upet`, `fairchem`.
- **10 Modular Skills**:
  - `/janus-core`: Foundation guide, architecture selection, devices (`cpu`, `cuda`, `mps`, `xpu`), YAML workflows, Context7 live docs.
  - `/janus-singlepoint`: Static single-point energy, forces, stress, Hessians.
  - `/janus-geomopt`: Coordinate and unit cell relaxation (`FrechetCellFilter`, variable pressure).
  - `/janus-md`: Microcanonical (NVE), canonical (NVT), and isothermal-isobaric (NPT) dynamics, temperature ramps, PLUMED metadynamics.
  - `/janus-eos-elasticity`: Equation of state ($E-V$ fitting, bulk modulus) and 6x6 elasticity stiffness matrix ($C_{ij}$, VRH averages).
  - `/janus-phonons`: Phonon dispersion curves, DOS, and vibrational thermodynamics via Phonopy.
  - `/janus-neb`: Climbing Image NEB (CI-NEB), IDPP interpolation, reaction barrier heights.
  - `/janus-descriptors`: MLIP invariant representation extraction.
  - `/janus-train-mlip`: MACE model training and transfer learning fine-tuning.
  - `/janus-analysis`: MD observables (RDF $g(r)$, VAF/VACF, MSD, diffusion coefficients).
- **Structure Inspector**: `janus-core/tools/structure_inspector.py` for pre-simulation verification.
- **Upstream Sync**: Keep all skills updated via `./janus-core/update.sh` (or `./janus-core/update.sh --check`).

### 5. AiiDA-MLIP Automated Workflows (`stfc/aiida-mlip`)

Installed from the [`aiida-mlip`](https://github.com/alinelena/ai-rules/tree/main/aiida-mlip) capability group, grounded in STFC [`aiida-mlip`](https://github.com/stfc/aiida-mlip) (docs: [`https://stfc.github.io/aiida-mlip/`](https://stfc.github.io/aiida-mlip/)):

- **Automated Provenance & HPC Workflows**: Bridges `janus-core` with AiiDA's database and daemon infrastructure.
- **8 Modular Skills**:
  - `/aiida-mlip-core`: Profile setup (`verdi presto`), code registration (`janus@localhost`), `ModelData`, `JanusConfigfile`.
  - `/aiida-mlip-singlepoint`: Static calculation job (`mlip.sp`).
  - `/aiida-mlip-geomopt`: Optimization and cell relaxation job (`mlip.opt`).
  - `/aiida-mlip-md`: Molecular dynamics simulation job (`mlip.md`).
  - `/aiida-mlip-phonons`: Phonon calculations job (`mlip.ph`).
  - `/aiida-mlip-descriptors`: Invariant feature extraction job (`mlip.descriptors`).
  - `/aiida-mlip-train`: MACE model training and fine-tuning job (`mlip.train`).
  - `/aiida-mlip-workflows`: High-throughput workgraphs with `aiida-workgraph` (`build_ht_calc`) across structure directories.
- **Upstream Sync**: Keep all skills updated via `./aiida-mlip/update.sh` (or `./aiida-mlip/update.sh --check`).

### 6. AtomisticSkills Discovery & Simulation Suite (`learningmatter-mit/AtomisticSkills`)

Installed from the [`atomisticskills`](https://github.com/alinelena/ai-rules/tree/main/atomisticskills) capability group, grounded in MIT Learning Matter Lab [`AtomisticSkills`](https://github.com/learningmatter-mit/AtomisticSkills) (docs: [`https://learningmatter-mit.github.io/AtomisticSkills/`](https://learningmatter-mit.github.io/AtomisticSkills/), paper: arXiv:2605.24002):

- **Comprehensive Multi-Domain Architecture**: 133 modular skills, 9 multi-stage research workflows, and 11 Model Context Protocol (MCP) servers across materials science, molecular chemistry, drug discovery, and machine learning foundation models.
- **6 Entrypoint Skills**:
  - `/atomisticskills-core`: Architecture guide, MCP servers (`base`, `mace`, `matgl`, `fairchem`, `atomate2`, `drugdisc`, `smol`), launcher (`venv/run`), and the complete 133-skill directory.
  - `/atomisticskills-materials`: Materials discovery, crystal mechanics ($C_{ij}$), phonons, VASP DFT via atomate2, CALPHAD, Pourbaix diagrams, XRD phase analysis/refinement, and synthesis recommendation (57 skills).
  - `/atomisticskills-chemistry`: Conformer generation, ORCA DFT, transition state optimization, IRC verification, reaction kinetics, and MOF gas sorption (GCMC, Widom insertion) (25 skills).
  - `/atomisticskills-drug-discovery`: Structure-based virtual screening, cavity detection, AutoDock Vina docking, OpenMM all-atom MD, MM/PBSA free energies, and ADMET profiling (19 skills).
  - `/atomisticskills-ml`: Foundation MLIP model selection, MACE/FairChem/MatGL fine-tuning, generative crystal diffusion (MatterGen, DiffCSP, ADIT), and committee uncertainty (16 skills).
  - `/atomisticskills-workflows`: Autonomous multi-stage campaigns (Materials Discovery, Drug HTVS, MOF CO2 DAC screening, Generative Halides, Active Learning MLIP loops).
- **Execution Rules**: Standardized research protocol (`research-standards.md`), coding guidelines (`coding-standards.md`), and environment runtime mappings (`mcp-environments.md`).
- **Upstream Sync**: Keep all skills and reference catalogs synchronized with upstream releases via `./atomisticskills/update.sh` (or `./atomisticskills/update.sh --check`).

---

## Repository Structure

```text
ai-rules/
├── BOOTSTRAP.md                         # Root agent bootstrap entrypoint
├── PROMPTS.md                           # Copy-paste prompts for installing & updating
├── README.md                            # Documentation and usage guide
├── antigravity/                         # Core Antigravity bootstrap group
│   ├── BOOTSTRAP.md                     # Step-by-step Antigravity injection procedure
│   ├── agents-md-snippet.md             # Snippets injected into target AGENTS.md
│   ├── rules/
│   │   └── interject.md                 # Standalone /interject workspace rule
│   └── skills/
│       ├── dev-template/
│       │   └── SKILL.md                 # Template for <project_name>-dev skill
│       └── interject/
│           └── SKILL.md                 # /interject slash-command skill
├── janus-core/                          # Janus-Core skills & rules capability group
│   ├── README.md                        # Documentation for janus-core group
│   ├── plugin.json                      # Antigravity plugin manifest
│   ├── VERSION                          # Upstream version tracker
│   ├── update.sh                        # One-command updater from GitHub & docs
│   ├── rules/                           # Janus-Core execution rules
│   │   ├── AGENTS.md
│   │   └── janus-rules.md
│   ├── scripts/
│   │   ├── update_skills.py             # Zero-dependency upstream parser & updater
│   │   └── update.sh
│   ├── tools/
│   │   └── structure_inspector.py       # Atomic structure inspector CLI/JSON
│   └── skills/                          # 10 specialized Janus-Core skills
│       ├── janus-core/
│       ├── janus-singlepoint/
│       ├── janus-geomopt/
│       ├── janus-md/
│       ├── janus-eos-elasticity/
│       ├── janus-phonons/
│       ├── janus-neb/
│       ├── janus-descriptors/
│       ├── janus-train-mlip/
│       └── janus-analysis/
├── aiida-mlip/                          # AiiDA-MLIP skills & rules capability group
│   ├── README.md                        # Documentation for aiida-mlip group
│   ├── plugin.json                      # Antigravity plugin manifest
│   ├── VERSION                          # Upstream version tracker
│   ├── update.sh                        # One-command updater from GitHub & docs
│   ├── rules/                           # AiiDA-MLIP execution rules
│   │   ├── AGENTS.md
│   │   └── aiida-mlip-rules.md
│   ├── scripts/
│   │   ├── update_skills.py             # Zero-dependency upstream parser & updater
│   │   └── update.sh
│   └── skills/                          # 8 specialized AiiDA-MLIP skills
│       ├── aiida-mlip-core/
│       ├── aiida-mlip-singlepoint/
│       ├── aiida-mlip-geomopt/
│       ├── aiida-mlip-md/
│       ├── aiida-mlip-phonons/
│       ├── aiida-mlip-descriptors/
│       ├── aiida-mlip-train/
│       └── aiida-mlip-workflows/
├── atomisticskills/                     # AtomisticSkills suite capability group
│   ├── README.md                        # Documentation for atomisticskills group
│   ├── plugin.json                      # Antigravity plugin manifest
│   ├── VERSION                          # Upstream version tracker (2.0.0)
│   ├── update.sh                        # One-command updater from GitHub & docs
│   ├── rules/                           # Atomistic research, coding & MCP rules
│   │   ├── AGENTS.md
│   │   ├── research-standards.md
│   │   ├── coding-standards.md
│   │   ├── mcp-environments.md
│   │   └── workflow-standards.md
│   ├── scripts/
│   │   └── update_skills.py             # Upstream parser & sync script
│   └── skills/                          # 6 domain-level entrypoint skills
│       ├── atomisticskills-core/
│       ├── atomisticskills-materials/
│       ├── atomisticskills-chemistry/
│       ├── atomisticskills-drug-discovery/
│       ├── atomisticskills-ml/
│       └── atomisticskills-workflows/
└── .agents/
    ├── rules/
    │   └── interject.md                 # Dogfooded /interject rule for this repo
    └── skills.json                      # Registers antigravity, janus-core, aiida-mlip & atomisticskills skills
```
