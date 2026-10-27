---
name: atomisticskills-core
description: Core guide for AtomisticSkills (MIT Learning Matter Lab). Architecture (Tools, Skills, Workflows), MCP server configuration, environment launcher (venv/run), and the complete 133-skill catalog.
metadata:
  category: [atomistic-simulation, multi-domain, mcp-framework]
---

# AtomisticSkills Core Framework & Catalog

The [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills) ecosystem (MIT Learning Matter Lab, arXiv:2605.24002) is an agentic framework decomposing computational discovery into three modular tiers:

1. **Tools** (`src/mcp_server/`): Low-level, strictly-typed Model Context Protocol (MCP) servers (structure relaxation, molecular dynamics, database queries, docking).
2. **Skills** (`skills/`): Mid-level modular guides and automated scripts executing focused atomistic calculations.
3. **Workflows** (`.agents/workflows/`): High-level multi-stage research campaigns chaining multiple skills to solve open-ended scientific challenges.

---

## 1. Environment and Execution Model

AtomisticSkills runs all calculations via the unified launcher `venv/run`:
```bash
venv/run <venv>[+<extra>] python skills/<skill-name>/scripts/<script>.py [args]
```

### Shared Environments & Stacks
- `cpu`: ASE, pymatgen, RDKit, pycalphad, MDAnalysis (database querying, structure handling, analysis).
- `mlip`: PyTorch, MACE-torch with `cuEquivariance`, MatGL (CHGNet, M3GNet), nvalchemi-toolkit.
- `fairchem`: PyTorch, `fairchem-core` (UMA, ESEN models), nvalchemi-toolkit.
- Research stacks: `mattergen`, `diffcsp`, `adit` (generative modeling), `msms` (mass spectrometry), `reactot` (optimal transport).

### Alternative Conda / Micromamba Execution
When running within a preconfigured environment:
```bash
micromamba run -n janus python <script>
# or
uv run --no-project python <script>
```

---

## 2. MCP Servers & CLI Fallback

AtomisticSkills provides 10+ standard MCP servers:
- `base`: Materials Project queries, structure edits, literature retrieval
- `mace`: Energy, forces, geometry relaxation, and MD with MACE foundation models
- `matgl`: CHGNet and M3GNet calculations
- `fairchem`: FairChem UMA and ESEN calculations
- `atomate2`: VASP DFT workflows
- `smol`: Cluster expansion and Monte Carlo
- `drugdisc`: AutoDock Vina, RDKit, OpenMM, binding site detection

Without an active MCP daemon, run tools via the unified CLI:
```bash
venv/run <venv> python -m src.mcp_server.cli <server> <tool> key=value ...
```

---

## 3. Complete Skills Catalog by Domain

AtomisticSkills includes 133 specialized skills across 5 core domains:

### Materials Science (`mat-*`, 57 Skills)
- [mat-elasticity](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-elasticity): Elastic tensor ($C_{ij}$) and VRH moduli with MLIPs.
- [mat-equation-of-state](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-equation-of-state): Energy-volume EOS fitting and bulk modulus.
- [mat-phonon](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-phonon): Phonon dispersion, DOS, and thermal properties via Phonopy.
- [mat-lammps-md](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-lammps-md): Large-scale molecular dynamics with LAMMPS and MLIPs.
- [mat-dft-vasp](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-dft-vasp): Density Functional Theory calculations via VASP and atomate2.
- [mat-phase-diagram](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-phase-diagram): Convex hull construction and phase stability.
- [mat-pourbaix-diagram](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-pourbaix-diagram): Electrochemical stability and Pourbaix diagrams.
- [mat-xrd-phase-analysis](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-xrd-phase-analysis): Experimental XRD pattern phase identification.
- [mat-defect-energy](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-defect-energy): Point defect formation energies and migration barriers.
- [mat-grain-boundary](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-grain-boundary): Coincident site lattice (CSL) grain boundary structures and energies.
- [mat-synthesis-recommendation](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-synthesis-recommendation): Experimental solid-state synthesis route recommendations.
*(Explore all 57 materials skills in `/atomisticskills-materials`)*

### Chemistry & Sorption (`chem-*`, 25 Skills)
- [chem-conformer-search](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-conformer-search): RDKit ETKDG conformer generation, MLIP relaxation, and Boltzmann ranking.
- [chem-dft-orca-optimization](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-dft-orca-optimization): Molecular geometry optimization using ORCA DFT.
- [chem-ts-optimization](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-ts-optimization): Transition state geometry search and frequency verification.
- [chem-neb-barrier](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-neb-barrier): CI-NEB minimum energy pathways and activation barriers.
- [chem-thermochemistry](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-thermochemistry): Enthalpy, entropy, and Gibbs free energy calculations.
- [chem-sorption-gcmc](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-sorption-gcmc): Grand Canonical Monte Carlo gas adsorption isotherms in MOFs.
- [chem-sorption-widom](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-sorption-widom): Widom test particle insertion for Henry coefficients.
- [chem-nmr-predict](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-nmr-predict): 1H/13C NMR chemical shift and spectrum prediction.
*(Explore all 25 chemistry skills in `/atomisticskills-chemistry`)*

### Drug Discovery (`drug-*`, 19 Skills)
- [drug-docking-vina](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-docking-vina): Receptor-ligand molecular docking using AutoDock Vina.
- [drug-pocket-detection](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-pocket-detection): Cavity and binding pocket detection on protein structures.
- [drug-ligand-prep](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-ligand-prep): Ligand 3D protonation, conformer generation, and PDBQT conversion.
- [drug-protein-prep](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-protein-prep): Missing residue repair and protonation via PDBFixer.
- [drug-mmpbsa-gbsa](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-mmpbsa-gbsa): MM/PBSA and MM/GBSA binding free energy calculation.
- [drug-protein-ligand-md](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-protein-ligand-md): Solvated all-atom molecular dynamics with OpenMM.
- [drug-admet-prediction](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-admet-prediction): Drug-likeness heuristics (Lipinski Ro5, Veber, QED).
*(Explore all 19 drug discovery skills in `/atomisticskills-drug-discovery`)*

### Machine Learning & Foundation Models (`ml-*`, 16 Skills)
- [ml-foundation-potentials](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-foundation-potentials): Guide for selecting MACE, CHGNet, SevenNet, FairChem potentials.
- [ml-mace-finetune](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-mace-finetune): Fine-tuning MACE foundation models on custom DFT datasets.
- [ml-fairchem-finetune](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-fairchem-finetune): Fine-tuning FairChem UMA/ESEN models.
- [ml-generative-mattergen](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-generative-mattergen): Generative diffusion for novel crystal structures.
- [ml-generative-diffcsp](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-generative-diffcsp): Diffusion-based crystal structure prediction with space groups.
- [ml-generative-adit](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-generative-adit): All-dielectric inverse design transformer for periodic lattices.
- [ml-committee-uncertainty](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-committee-uncertainty): Ensemble committee uncertainty quantification.
*(Explore all 16 ML skills in `/atomisticskills-ml`)*

### Multi-Stage Research Campaigns (9 Workflows)
- [materials-discovery](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows/materials-discovery.md): Generative candidate discovery to synthesizability.
- [generative-halide-discovery](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows/generative-halide-discovery.md): Solid-state halide electrolytes.
- [drug-hit-finding-htvs](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows/drug-hit-finding-htvs.md): High-throughput virtual screening.
- [mof-co2-dac-screening](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows/mof-co2-dac-screening.md): MOFs for CO2 direct air capture.
- [sorption-discovery](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows/sorption-discovery.md): Porous materials for gas separation.
- [mlip-benchmark-finetune](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows/mlip-benchmark-finetune.md): Benchmark, fine-tune, and distill MLIPs.
*(Explore all 9 workflows in `/atomisticskills-workflows`)*

---

## 4. Upstream Synchronization

Keep all skills, rules, and reference catalogs in sync with upstream releases:
```bash
./atomisticskills/update.sh
# or dry-run check:
./atomisticskills/update.sh --check
```

Upstream Source: [https://github.com/learningmatter-mit/AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills)
Documentation: [https://learningmatter-mit.github.io/AtomisticSkills/](https://learningmatter-mit.github.io/AtomisticSkills/)

