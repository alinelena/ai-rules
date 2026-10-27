---
name: atomisticskills-workflows
description: High-level multi-stage autonomous research campaigns and workflow orchestration with AtomisticSkills (MIT Learning Matter Lab).
metadata:
  category: [research-campaigns, workflow-orchestration, multi-stage, end-to-end]
---

# AtomisticSkills Research Campaign Workflows

Workflows in [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills) represent high-level, multi-stage research campaigns. While individual skills solve focused atomic tasks (e.g. relaxing a unit cell, calculating an elastic constant, running a docking simulation), workflows chain these skills together into comprehensive discovery protocols mimicking full scientific journal articles.

---

## 1. Directory of the 9 Autonomous Research Workflows

| Workflow | Research Objective | Key Chained Skills | Upstream Workflow Link |
| :--- | :--- | :--- | :--- |
| **Materials Discovery** | Generative creation, thermodynamic filtering, and synthesizability assessment of novel crystals. | `mat-db-mp`, `ml-generative-mattergen`, `mat-phase-diagram`, `mat-elasticity`, `mat-synthesis-recommendation` | [materials-discovery.md](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows/materials-discovery.md) |
| **Generative Halide Discovery** | Discovery of novel high-conductivity solid-state electrolytes (SSEs) for solid-state Li-ion batteries. | `ml-generative-diffcsp`, `mat-electrochemical-window`, `mat-diffusion-analysis`, `mat-neb-barrier` | [generative-halide-discovery.md](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows/generative-halide-discovery.md) |
| **Drug Hit Finding HTVS** | End-to-end structure-based virtual screening from target retrieval through docking, MD, and ADMET. | `drug-db-pdb`, `drug-pocket-detection`, `drug-docking-vina`, `drug-protein-ligand-md`, `drug-mmpbsa-gbsa`, `drug-admet-prediction` | [drug-hit-finding-htvs.md](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows/drug-hit-finding-htvs.md) |
| **MOF CO2 DAC Screening** | High-throughput direct air capture (DAC) screening of metal-organic frameworks for low-concentration CO2 capture. | `chem-db-mof`, `chem-sorption-widom`, `chem-sorption-gcmc`, `chem-sorption-relax` | [mof-co2-dac-screening.md](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows/mof-co2-dac-screening.md) |
| **Porous Sorption Discovery** | Gas separation and storage screening across porous frameworks for H2, CH4, or volatile organics. | `chem-db-qmof`, `chem-sorption-widom`, `chem-sorption-gcmc` | [sorption-discovery.md](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows/sorption-discovery.md) |
| **MLIP Benchmark & Finetune** | Active learning loop: sample PES with high-T MD, evaluate committee uncertainty, and fine-tune foundation MLIPs. | `mat-sample-pes-by-md`, `ml-committee-uncertainty`, `mat-dft-vasp`, `ml-mace-finetune`, `ml-mlip-benchmark` | [mlip-benchmark-finetune.md](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows/mlip-benchmark-finetune.md) |
| **Image to XRD Phase** | Digitize experimental powder XRD plot image and identify constituent crystalline phases. | `mat-xrd-digitizer`, `mat-db-mp`, `mat-xrd-calculator`, `mat-xrd-phase-analysis`, `mat-xrd-refinement` | [image-to-xrd-phase.md](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows/image-to-xrd-phase.md) |
| **Reaction to NMR Quantification** | Predict reaction products and quantify yields via Wasserstein deconvolution of crude 1H NMR spectra. | `chem-react-ot`, `chem-nmr-predict`, `chem-nmr-analysis` | [reaction-to-nmr-quantification.md](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows/reaction-to-nmr-quantification.md) |
| **NMR Reaction Kinetics** | Extract rate constants ($k$) and mole fraction trajectories from time-series 1H NMR spectra. | `chem-nmr-predict`, `chem-nmr-analysis` | [nmr-reaction-kinetics.md](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows/nmr-reaction-kinetics.md) |

---

## 2. Standard Workflow Execution Protocol

When a user initiates an open-ended research question that matches an end-to-end workflow:
1. **Initialize Workspace**: Follow [research-standards](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/rules/research-standards.md) and create `./research/<YYYY-MM-DD>_<project_name>/`.
2. **Draft Research Plan**: Formulate an artifact `research_plan.md` mapping out the workflow stages, pass/fail thresholds, and fallback branches.
3. **Tracking & Provenance**: Create `candidates_tracking.csv` to record intermediate screening metrics across stages.
4. **Execution**: Launch stages sequentially, discarding non-viable candidates at early inexpensive tiers before allocating expensive DFT, all-atom MD, or GCMC resources.

Upstream Source: [AtomisticSkills Workflows Directory](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows)

