# `atomisticskills` — AI Skills & Rules Group for Antigravity

This directory contains a complete, self-contained capability group of **AI Skills**, **Execution Rules**, **Reference Catalogs**, and **Upstream Synchronizers** for [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills) (MIT Learning Matter Lab, arXiv:2605.24002, version 2.0.0+).

---

## What Is Included

### 1. Modular Skills Group (`atomisticskills/skills/`)

| Skill | Slash Command | Capabilities & Scope |
| :--- | :--- | :--- |
| **`atomisticskills-core`** | `/atomisticskills-core` | Core framework architecture (Tools, Skills, Workflows), MCP server configuration (`base`, `mace`, `matgl`, `fairchem`, `atomate2`, `drugdisc`, `smol`), environment launcher (`venv/run`), and the complete 133-skill directory. |
| **`atomisticskills-materials`** | `/atomisticskills-materials` | Materials science hub: 57 skills covering crystal elasticity, phonons, EOS, LAMMPS MD, VASP DFT via atomate2, phase diagrams, CALPHAD, Pourbaix diagrams, XRD phase analysis/refinement, and synthesis recommendation. |
| **`atomisticskills-chemistry`** | `/atomisticskills-chemistry` | Molecular chemistry & sorption hub: 25 skills covering RDKit conformer search, ORCA DFT, transition state optimization, IRC verification, reaction kinetics, and MOF gas sorption (GCMC, Widom insertion). |
| **`atomisticskills-drug-discovery`** | `/atomisticskills-drug-discovery` | Therapeutics & screening hub: 19 skills covering cavity/pocket detection, protein/ligand preparation, AutoDock Vina docking, pose validation, OpenMM MD, MM/PBSA free energies, and ADMET prediction. |
| **`atomisticskills-ml`** | `/atomisticskills-ml` | Machine learning & foundation models hub: 16 skills covering foundation MLIP selection, MACE/FairChem/MatGL fine-tuning, generative diffusion (MatterGen, DiffCSP, ADIT), and committee uncertainty. |
| **`atomisticskills-workflows`** | `/atomisticskills-workflows` | Campaign orchestration hub: 9 multi-stage end-to-end research workflows for materials discovery, drug hit finding HTVS, CO2 direct air capture, and active learning MLIP loops. |

### 2. Multi-Agent Execution Rules (`atomisticskills/rules/`)

- `research-standards.md`: Intent classification (Direct Property Query, Computational Research Task, Broad Literature Synthesis), research workspace setup (`./research/<date>_<topic>`), artifact research plan workflow, and candidate tracking.
- `coding-standards.md`: Code quality, language conventions, MCP stability, and sandbox cleanliness.
- `mcp-environments.md`: Environment mapping for `cpu`, `mlip`, `fairchem`, and research stacks (`adit`, `diffcsp`, `mattergen`, `msms`, `reactot`, `scd`), plus launcher rules.
- `workflow-standards.md`: Chaining atomic skills into end-to-end research campaigns.
- `AGENTS.md`: Agent protocol reference.

### 3. Upstream Synchronization (`atomisticskills/update.sh` and `atomisticskills/scripts/update_skills.py`)

A synchronization tool that verifies and keeps skills, rules, and reference catalogs aligned with:
- **Upstream GitHub Repository**: [`https://github.com/learningmatter-mit/AtomisticSkills`](https://github.com/learningmatter-mit/AtomisticSkills)
- **Documentation**: [`https://learningmatter-mit.github.io/AtomisticSkills/`](https://learningmatter-mit.github.io/AtomisticSkills/)

---

## 3-Tier Architecture

```
High-Level Workflows (.agents/workflows/)
  └── Materials Discovery, Drug HTVS, MOF CO2 DAC, Generative Halides, MLIP Finetuning
        │
Mid-Level Skills (skills/)
  ├── Materials Science (57 skills: mat-*)
  ├── Chemistry & Sorption (25 skills: chem-*)
  ├── Drug Discovery (19 skills: drug-*)
  ├── Machine Learning (16 skills: ml-*)
  └── General Research (16 skills: general-*)
        │
Low-Level MCP Servers (src/mcp_server/)
  ├── base (Materials Project queries, structures, literature)
  ├── mace / matgl / fairchem (MLIP energies, forces, relaxation, MD)
  ├── atomate2 (VASP DFT calculations)
  ├── drugdisc (Vina docking, PDBFixer, OpenMM)
  └── mattergen / diffcsp / adit (Generative crystal generation)
```

---

## How to Run Calculations

1. **Via the unified launcher**:
   ```bash
   venv/run <venv>[+<extra>] python skills/<skill-name>/scripts/<script>.py [args]
   ```
2. **Via micromamba**:
   ```bash
   micromamba run -n janus python <script>
   ```
3. **Via uv**:
   ```bash
   uv run --no-project python <script>
   ```

---

## How to Update

To inspect upstream version and changes:
```bash
./atomisticskills/update.sh --check
```

To sync rules, catalogs, and metadata:
```bash
./atomisticskills/update.sh
```

---

## Upstream References

- Repository: [`https://github.com/learningmatter-mit/AtomisticSkills`](https://github.com/learningmatter-mit/AtomisticSkills)
- Documentation: [`https://learningmatter-mit.github.io/AtomisticSkills/`](https://learningmatter-mit.github.io/AtomisticSkills/)
- Scientific Paper: *AtomisticSkills: Modular Agentic Skills for Atomistic Science and Simulation*, arXiv:2605.24002.

