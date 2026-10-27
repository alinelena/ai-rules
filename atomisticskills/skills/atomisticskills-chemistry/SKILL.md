---
name: atomisticskills-chemistry
description: Molecular chemistry, conformer search, ORCA DFT, transition states, reaction kinetics, and MOF gas sorption with AtomisticSkills (MIT Learning Matter Lab).
metadata:
  category: [molecular-chemistry, dft, reaction-kinetics, gas-sorption, spectroscopy]
---

# AtomisticSkills Chemistry & Sorption Hub

The Chemistry suite in [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills) provides 25 modular skills and MCP tools for molecular modeling, electronic structure via ORCA DFT, reaction barriers and transition states, spectroscopy, and porous framework gas sorption.

---

## 1. Conformer Generation & Thermochemistry

- **Conformer Search**: [chem-conformer-search](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-conformer-search) uses RDKit ETKDG algorithms, relaxes geometries with MLIPs (`mace_off`, `ani2x`), and ranks states with Boltzmann weighting $\exp(-\Delta E / k_B T)$.
- **Thermochemistry**: [chem-thermochemistry](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-thermochemistry) calculates zero-point vibrational energy (ZPE), enthalpy $H(T)$, entropy $S(T)$, and Gibbs free energy $G(T)$ from harmonic vibrational frequencies.
- **Vibrational Analysis**: [chem-vibration](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-vibration) and [chem-bond-dissociation](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-bond-dissociation) compute homolytic/heterolytic BDEs for all single bonds.

---

## 2. Ab Initio Molecular DFT (ORCA)

- **Static Calculations**: [chem-dft-orca-singlepoint](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-dft-orca-singlepoint) evaluates ground and excited state electronic energies.
- **Geometry Optimization**: [chem-dft-orca-optimization](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-dft-orca-optimization) finds molecular energy minima.
- **Advanced Spectroscopic Properties**: [chem-dft-orca-advanced-calculation](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-dft-orca-advanced-calculation) computes polarizabilities, TD-DFT excitation spectra, and NMR shielding constants.

---

## 3. Reaction Kinetics & Transition States

- **Transition State Optimization**: [chem-ts-optimization](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-ts-optimization) uses saddle-point search algorithms to optimize transition states with exactly one imaginary vibrational frequency.
- **Intrinsic Reaction Coordinate**: [chem-irc-verification](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-irc-verification) verifies that forward and backward IRC paths connect the TS to intended reactants and products.
- **Reaction Pathways (NEB)**: [chem-neb-barrier](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-neb-barrier) computes activation barriers via Climbing Image NEB.
- **Optimal Transport Reaction Mapping**: [chem-react-ot](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-react-ot) maps atom-to-atom correspondence across complex chemical transformations.

---

## 4. Gas Sorption & MOF Screening

- **Widom Insertion**: [chem-sorption-widom](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-sorption-widom) computes Henry's adsorption coefficients and infinite-dilution heats of adsorption.
- **Grand Canonical Monte Carlo (GCMC)**: [chem-sorption-gcmc](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-sorption-gcmc) calculates full adsorption isotherms (loading vs pressure) for CO2, N2, H2, or CH4 in metal-organic frameworks.
- **Framework Relaxation**: [chem-sorption-relax](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-sorption-relax) and database mining via [chem-db-mof](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-db-mof) and [chem-db-qmof](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-db-qmof).

---

## 5. Directory of All 25 Chemistry Skills

| Skill | Description | Upstream Repository Link |
| :--- | :--- | :--- |
| `chem-bond-dissociation` | Homolytic and heterolytic BDE calculations | [chem-bond-dissociation](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-bond-dissociation) |
| `chem-conformer-search` | ETKDG generation + MLIP relaxation + Boltzmann weights | [chem-conformer-search](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-conformer-search) |
| `chem-db-mof` | MOF database queries (QMOF, ARC-MOF) | [chem-db-mof](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-db-mof) |
| `chem-db-qmof` | Quantum MOF database queries via MPContribs | [chem-db-qmof](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-db-qmof) |
| `chem-db-spectra` | Search experimental IR, MS, and UV-Vis spectra | [chem-db-spectra](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-db-spectra) |
| `chem-dft-orca-advanced-calculation` | TD-DFT, polarizability, and spectroscopic properties | [chem-dft-orca-advanced-calculation](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-dft-orca-advanced-calculation) |
| `chem-dft-orca-optimization` | Molecular geometry optimization via ORCA | [chem-dft-orca-optimization](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-dft-orca-optimization) |
| `chem-dft-orca-singlepoint` | ORCA DFT single-point calculations | [chem-dft-orca-singlepoint](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-dft-orca-singlepoint) |
| `chem-docking-void` | VOID guest-host docking in molecular cages | [chem-docking-void](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-docking-void) |
| `chem-hazard-toxicity` | Chemical hazard and toxicity prediction | [chem-hazard-toxicity](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-hazard-toxicity) |
| `chem-irc-verification` | Intrinsic Reaction Coordinate path validation | [chem-irc-verification](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-irc-verification) |
| `chem-msms-predict` | Predict tandem mass spectra using ICEBERG | [chem-msms-predict](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-msms-predict) |
| `chem-neb-barrier` | Minimum energy paths and activation barriers | [chem-neb-barrier](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-neb-barrier) |
| `chem-nmr-analysis` | 1H NMR deconvolution via Wasserstein distance | [chem-nmr-analysis](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-nmr-analysis) |
| `chem-nmr-predict` | Fast empirical 1H/13C NMR spectrum prediction | [chem-nmr-predict](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-nmr-predict) |
| `chem-react-ot` | Optimal transport atom-to-atom reaction mapping | [chem-react-ot](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-react-ot) |
| `chem-similarity-search` | Molecular fingerprint similarity search | [chem-similarity-search](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-similarity-search) |
| `chem-solution-md` | Solvated molecular dynamics simulations | [chem-solution-md](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-solution-md) |
| `chem-sorption-gcmc` | Grand Canonical Monte Carlo adsorption isotherms | [chem-sorption-gcmc](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-sorption-gcmc) |
| `chem-sorption-relax` | Relax porous host frameworks with MLIPs | [chem-sorption-relax](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-sorption-relax) |
| `chem-sorption-widom` | Widom test particle insertion for Henry's law | [chem-sorption-widom](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-sorption-widom) |
| `chem-spectrum-matcher` | Match experimental and simulated spectra | [chem-spectrum-matcher](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-spectrum-matcher) |
| `chem-thermochemistry` | Enthalpy, entropy, Gibbs energy, and ZPE | [chem-thermochemistry](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-thermochemistry) |
| `chem-ts-optimization` | Saddle-point transition state geometry search | [chem-ts-optimization](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-ts-optimization) |
| `chem-vibration` | Harmonic vibrational frequencies and normal modes | [chem-vibration](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/chem-vibration) |

Upstream Source: [AtomisticSkills Chemistry Repository](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills)

