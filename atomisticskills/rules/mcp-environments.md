---
trigger: always_on
description: MCP server runtime mapping and Python environment standards for AtomisticSkills.
---

# MCP Server and Environment Runtime Rules

AtomisticSkills runs all skill scripts and MCP servers through the unified launcher `venv/run`, or in targeted isolated environments.

## 1. Shared Environments

| Environment | Primary Packages | GPU Required | Associated MCP Servers |
| :--- | :--- | :--- | :--- |
| `cpu` | ASE, pymatgen, RDKit, pycalphad, MDAnalysis (no torch) | No | `base`, `atomate2`, `drugdisc`, `smol` |
| `mlip` | PyTorch, MACE-torch + cuEquivariance, MatGL, nvalchemi-toolkit | Yes (or MPS/CPU fallback) | `mace`, `matgl` |
| `fairchem` | PyTorch, fairchem-core, nvalchemi-toolkit | Yes | `fairchem` |

### Specialized Research Stacks

| Stack | Used By | Description |
| :--- | :--- | :--- |
| `adit` | `ml-generative-adit` | All-dielectric inverse design & periodic generative models |
| `diffcsp` | `ml-generative-diffcsp` | Crystal structure prediction with diffusion |
| `mattergen` | `ml-generative-mattergen` | Microsoft MatterGen materials generation model |
| `msms` | `chem-msms-predict` | Mass spectrometry prediction (ICEBERG) |
| `reactot` | `chem-react-ot` | Chemical reaction optimal transport mapping |
| `scd` | `ml-property-predict-scd` | Superconductivity property prediction models |

### Optional Extras
Environments support optional extras specified as `<venv>+<extra>`:
- `openmm`: OpenMM and PDBFixer for molecular dynamics and protein preparation.
- `docking`: AutoDock Vina for receptor-ligand docking.
- `pymol`: PyMOL open-source visualization.
- `void`: VOID guest docking.
- `transport`: AMSET and BoltzTraP2 for electronic transport properties.

## 2. Server Runtime Mapping

| MCP Server | Runtime | Host Command / CLI Fallback |
| :--- | :--- | :--- |
| `base` | `cpu` | `venv/run cpu python -m src.mcp_server.cli base <tool> key=val` |
| `mace` | `mlip` | `venv/run mlip python -m src.mcp_server.cli mace <tool> key=val` |
| `matgl` | `mlip` | `venv/run mlip python -m src.mcp_server.cli matgl <tool> key=val` |
| `fairchem` | `fairchem` | `venv/run fairchem python -m src.mcp_server.cli fairchem <tool> key=val` |
| `drugdisc` | `cpu+docking+openmm` | `venv/run cpu+docking+openmm python -m src.mcp_server.cli drugdisc <tool> key=val` |
| `atomate2` | `cpu` | `venv/run cpu python -m src.mcp_server.cli atomate2 <tool> key=val` |
| `smol` | `cpu` | `venv/run cpu python -m src.mcp_server.cli smol <tool> key=val` |

### Alternative Package / Runner Invocation
- When running in a conda/micromamba environment: `micromamba run -n janus python <script>`
- When running via uv: `uv run --no-project python <script>`

Upstream Reference: [AtomisticSkills MCP Environments](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/rules/mcp-environments.md)
