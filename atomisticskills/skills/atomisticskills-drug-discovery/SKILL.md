---
name: atomisticskills-drug-discovery
description: Structure-based virtual screening, AutoDock Vina docking, OpenMM protein-ligand dynamics, MM/PBSA free energies, and ADMET profiling with AtomisticSkills (MIT Learning Matter Lab).
metadata:
  category: [drug-discovery, molecular-docking, therapeutics, openmm, admet]
---

# AtomisticSkills Drug Discovery Hub

The Drug Discovery suite in [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills) provides 19 modular skills and MCP tools covering structure-based virtual screening (HTVS), binding cavity detection, ligand/protein preparation, molecular docking, all-atom molecular dynamics, and endpoint binding free energies.

---

## 1. Structure Preparation & Cavity Detection

- **Protein Preparation**: [drug-protein-prep](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-protein-prep) cleans PDB structures, adds missing heavy atoms/residues via PDBFixer, assigns protonation states at physiological pH ($7.4$), and formats PDBQT targets.
- **Ligand Preparation**: [drug-ligand-prep](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-ligand-prep) generates low-energy 3D conformations from SMILES via RDKit, assigns Gasteiger charges, and defines rotatable torsion trees.
- **Binding Site & Pocket Detection**: [drug-pocket-detection](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-pocket-detection) and [drug-binding-site-definition](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-binding-site-definition) locate potential allosteric or orthosteric binding pockets and define grid bounding boxes for docking.

---

## 2. Molecular Docking & Pose Quality Control

- **AutoDock Vina Docking**: [drug-docking-vina](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-docking-vina) executes flexible ligand docking against rigid or flexible receptor active sites.
- **Redocking Validation**: [drug-redocking-rmsd](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-redocking-rmsd) validates the docking protocol by redocking co-crystallized ligands to verify heavy-atom $\text{RMSD} \le 2.0\text{ \AA}$.
- **Pose Validation & Interaction Analysis**: [drug-pose-validation](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-pose-validation) and [drug-docking-analysis](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-docking-analysis) profile hydrogen bonds, salt bridges, $\pi$-stacking, and hydrophobic contacts.

---

## 3. Protein-Ligand Dynamics & Binding Energetics

- **Solvated Molecular Dynamics**: [drug-protein-ligand-md](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-protein-ligand-md) runs explicit solvent (TIP3P) MD simulations using OpenMM with AMBER14SB and GAFF2 force fields.
- **Trajectory Stability**: [drug-trajectory-analysis](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-trajectory-analysis) computes ligand backbone RMSD, protein RMSF, and radius of gyration.
- **Endpoint Binding Free Energies**: [drug-mmpbsa-gbsa](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-mmpbsa-gbsa) computes MM/PBSA and MM/GBSA free energy estimates ($\Delta G_{\text{bind}}$) over equilibrium trajectory snapshots.

---

## 4. ADMET & Chemical Bioactivity

- **ADMET Profiling**: [drug-admet-prediction](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-admet-prediction) computes Lipinski's Rule of Five, Veber rules, topological polar surface area (TPSA), and Quantitative Estimate of Drug-likeness (QED).
- **Bioactivity Data Mining**: [drug-db-chembl](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-db-chembl) and [drug-db-pubchem](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-db-pubchem) retrieve historical $IC_{50}$, $K_i$, and $EC_{50}$ values.
- **Retrosynthetic Feasibility**: [drug-retrosynthesis](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-retrosynthesis) assesses synthetic accessibility for top-scoring leads.

---

## 5. Directory of All 19 Drug Discovery Skills

| Skill | Description | Upstream Repository Link |
| :--- | :--- | :--- |
| `drug-admet-prediction` | Physicochemical descriptors and drug-likeness (Ro5, QED) | [drug-admet-prediction](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-admet-prediction) |
| `drug-binding-site-definition` | Define 3D bounding boxes and docking grid coordinates | [drug-binding-site-definition](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-binding-site-definition) |
| `drug-bioactivity-assay` | Query target protein assays and biological testing data | [drug-bioactivity-assay](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-bioactivity-assay) |
| `drug-complex-system-builder` | Assemble solvated, neutralized protein-ligand systems | [drug-complex-system-builder](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-complex-system-builder) |
| `drug-db-chembl` | Query ChEMBL for curated target bioactivity (IC50, Ki) | [drug-db-chembl](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-db-chembl) |
| `drug-db-pdb` | Download and inspect crystal structures from RCSB PDB | [drug-db-pdb](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-db-pdb) |
| `drug-db-pubchem` | Search chemical identifiers, synonyms, and properties | [drug-db-pubchem](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-db-pubchem) |
| `drug-docking-analysis` | Analyze docking energy distributions and contact residue maps | [drug-docking-analysis](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-docking-analysis) |
| `drug-docking-vina` | Run AutoDock Vina molecular docking simulations | [drug-docking-vina](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-docking-vina) |
| `drug-ligand-prep` | 3D conformation generation and PDBQT formatting | [drug-ligand-prep](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-ligand-prep) |
| `drug-mmpbsa-gbsa` | Calculate MM/PBSA and MM/GBSA binding free energies | [drug-mmpbsa-gbsa](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-mmpbsa-gbsa) |
| `drug-molecular-fingerprints` | Compute Morgan, MACCS, and RDKit molecular fingerprints | [drug-molecular-fingerprints](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-molecular-fingerprints) |
| `drug-pocket-detection` | Detect binding cavities and cryptic pockets | [drug-pocket-detection](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-pocket-detection) |
| `drug-pose-validation` | Verify sterics, clashes, and strain of docked poses | [drug-pose-validation](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-pose-validation) |
| `drug-protein-ligand-md` | Run explicit solvent MD simulations with OpenMM | [drug-protein-ligand-md](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-protein-ligand-md) |
| `drug-protein-prep` | Clean PDB, repair missing residues, assign protonation | [drug-protein-prep](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-protein-prep) |
| `drug-redocking-rmsd` | Redock co-crystallized ligands to benchmark protocols | [drug-redocking-rmsd](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-redocking-rmsd) |
| `drug-retrosynthesis` | Retrosynthetic analysis and synthesis route scoring | [drug-retrosynthesis](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-retrosynthesis) |
| `drug-trajectory-analysis` | Analyze MD trajectories (RMSD, RMSF, contact persistence) | [drug-trajectory-analysis](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/drug-trajectory-analysis) |

Upstream Source: [AtomisticSkills Drug Discovery Repository](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills)
