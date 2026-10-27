---
name: atomisticskills-materials
description: Materials science calculations, phase diagrams, defect thermodynamics, crystal mechanics, and DFT with AtomisticSkills (MIT Learning Matter Lab).
metadata:
  category: [materials-science, dft, crystallography, thermodynamics]
---

# AtomisticSkills Materials Science Hub

The Materials Science suite in [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills) provides 57 modular skills and MCP tools covering crystal mechanics, lattice dynamics, phase equilibrium, point/planar defects, and ab initio DFT workflows.

---

## 1. Core Simulation Capabilities

### Elasticity & Mechanical Stability
- **Skill**: [mat-elasticity](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-elasticity)
- **Goal**: Calculate the full 6x6 elastic stiffness tensor ($C_{ij}$), compliance matrix ($S_{ij}$), and Voigt-Reuss-Hill bulk modulus ($B$), shear modulus ($G$), Young's modulus ($E$), and Poisson's ratio ($\nu$).
- **Tool / Script**: `calculate_elasticity.py` using `MatCalc` or `janus-core`.
- **Related**: [mat-equation-of-state](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-equation-of-state) for Birch-Murnaghan EOS fitting.

### Phonons & Lattice Dynamics
- **Skill**: [mat-phonon](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-phonon)
- **Goal**: Harmonic phonon band structures, vibrational density of states (DOS), dynamical stability (checking imaginary modes), and thermal properties ($C_v$, $S$, Helmholtz free energy).
- **Engine**: Phonopy integration with MLIP force engines (`MACE`, `MatGL`, `SevenNet`).
- **Related**: [mat-qha-thermal-expansion](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-qha-thermal-expansion) for quasi-harmonic approximation and thermal expansion coefficient $\alpha(T)$.

### Large-Scale Molecular Dynamics
- **Skill**: [mat-lammps-md](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-lammps-md)
- **Goal**: Microsecond or million-atom simulations via LAMMPS with MLIP pair styles (`pair_style mace`).
- **Related**: [mat-diffusion-analysis](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-diffusion-analysis) for Mean Squared Displacement (MSD) and Arrhenius tracer diffusion coefficients.

### First-Principles DFT (VASP)
- **Skill**: [mat-dft-vasp](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-dft-vasp)
- **Tool**: `atomate2` MCP server.
- **Workflows**: Standard static, relaxation, band structure, and projected DOS workflows through automated Custodian error handling and atomate2 job pipelines.

---

## 2. Phase Stability & Thermodynamics

- **Convex Hull & Stability**: [mat-phase-diagram](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-phase-diagram) computes energy above convex hull ($E_{\text{hull}}$) against Materials Project reference phases.
- **Electrochemical Stability**: [mat-pourbaix-diagram](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-pourbaix-diagram) evaluates pH-potential stability windows and aqueous corrosion resistance.
- **CALPHAD Modeling**: [mat-calphad-phase-diagram](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-calphad-phase-diagram) and [mat-calphad-property-diagram](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-calphad-property-diagram) use `pycalphad` with thermodynamic database (`.tdb`) files.
- **Battery Intercalation**: [mat-intercalation-voltage](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-intercalation-voltage) calculates average open-circuit voltages (OCV) across lithiation/delithiation stages.

---

## 3. Defects & Microstructure

- **Point Defects**: [mat-defect-energy](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-defect-energy) calculates vacancy, interstitial, and antisite formation energies with chemical potential corrections.
- **Grain Boundaries**: [mat-grain-boundary](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-grain-boundary) constructs coincident site lattice (CSL) tilt and twist grain boundaries and computes interface excess energies ($\gamma_{\text{GB}}$).
- **Surface Adsorption & Wulff Shapes**: [mat-surface-adsorption](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-surface-adsorption) and [mat-surface-energy](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-surface-energy).

---

## 4. Characterization & Synthesizability

- **XRD Pattern Analysis**: [mat-xrd-phase-analysis](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-xrd-phase-analysis) and [mat-xrd-refinement](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-xrd-refinement) identify experimental powder diffraction peaks against CIF databases.
- **Synthesis Planning**: [mat-synthesis-recommendation](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-synthesis-recommendation) extracts precursor combinations and solid-state firing temperatures from historical literature recipes.

---

## 5. Directory of All 57 Materials Skills

| Skill | Description | Upstream Repository Link |
| :--- | :--- | :--- |
| `mat-amorphization` | Melt-quench MD protocol for amorphous structures | [mat-amorphization](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-amorphization) |
| `mat-calphad-phase-diagram` | Multi-component T-x phase diagrams with CALPHAD | [mat-calphad-phase-diagram](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-calphad-phase-diagram) |
| `mat-calphad-property-diagram` | Equilibrium phase fractions vs temperature | [mat-calphad-property-diagram](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-calphad-property-diagram) |
| `mat-db-mp` | Materials Project database querying via MP API | [mat-db-mp](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-db-mp) |
| `mat-db-nist-janaf` | NIST Chemistry WebBook & JANAF thermochemistry | [mat-db-nist-janaf](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-db-nist-janaf) |
| `mat-db-optimade` | OPTIMADE federation queries across materials databases | [mat-db-optimade](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-db-optimade) |
| `mat-defect-energy` | Point defect formation energies and migration | [mat-defect-energy](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-defect-energy) |
| `mat-defect-energy-dft` | Ab initio charged defect formation calculations | [mat-defect-energy-dft](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-defect-energy-dft) |
| `mat-dft-electronic-transport` | AMSET and BoltzTraP2 carrier transport | [mat-dft-electronic-transport](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-dft-electronic-transport) |
| `mat-dft-electron-phonon` | EPW electron-phonon coupling | [mat-dft-electron-phonon](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-dft-electron-phonon) |
| `mat-dft-ferroelectric` | Spontaneous polarization via Berry phase | [mat-dft-ferroelectric](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-dft-ferroelectric) |
| `mat-dft-lobster` | COHP bonding analysis via LOBSTER | [mat-dft-lobster](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-dft-lobster) |
| `mat-dft-mixing-functionals` | Meta-GGA, hybrid, and dispersion corrections | [mat-dft-mixing-functionals](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-dft-mixing-functionals) |
| `mat-dft-vasp` | VASP calculations via atomate2 | [mat-dft-vasp](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-dft-vasp) |
| `mat-dielectric-response` | High-frequency and static dielectric tensors | [mat-dielectric-response](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-dielectric-response) |
| `mat-diffusion-analysis` | MSD, jump frequency, and diffusion coefficients | [mat-diffusion-analysis](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-diffusion-analysis) |
| `mat-disorder` | Special Quasirandom Structures (SQS) generation | [mat-disorder](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-disorder) |
| `mat-edi-mobility` | Electron/hole mobility prediction | [mat-edi-mobility](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-edi-mobility) |
| `mat-elasticity` | Elastic tensor $C_{ij}$ and mechanical moduli | [mat-elasticity](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-elasticity) |
| `mat-electrochemical-window` | Redox stability window for electrolytes | [mat-electrochemical-window](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-electrochemical-window) |
| `mat-electronic-structure` | Band structure and projected density of states | [mat-electronic-structure](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-electronic-structure) |
| `mat-elemental-energies` | Reference elemental ground state energies | [mat-elemental-energies](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-elemental-energies) |
| `mat-epw-mobility` | First-principles mobility via electron-phonon coupling | [mat-epw-mobility](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-epw-mobility) |
| `mat-equation-of-state` | Birch-Murnaghan EOS fitting | [mat-equation-of-state](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-equation-of-state) |
| `mat-grain-boundary` | CSL grain boundary modeling and interfacial energy | [mat-grain-boundary](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-grain-boundary) |
| `mat-grand-canonical-mc` | Semi-grand canonical MC with cluster expansion | [mat-grand-canonical-mc](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-grand-canonical-mc) |
| `mat-intercalation-voltage` | Battery open circuit voltage curves | [mat-intercalation-voltage](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-intercalation-voltage) |
| `mat-ionic-substitution` | Data-mined ionic substitution for new structures | [mat-ionic-substitution](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-ionic-substitution) |
| `mat-kinetic-monte-carlo` | Lattice KMC for ion transport and phase changes | [mat-kinetic-monte-carlo](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-kinetic-monte-carlo) |
| `mat-lammps-md` | Large-scale LAMMPS MD with MLIPs | [mat-lammps-md](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-lammps-md) |
| `mat-lattice-thermal-conductivity`| Lattice thermal conductivity via ShengBTE / Phono3py | [mat-lattice-thermal-conductivity](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-lattice-thermal-conductivity) |
| `mat-magnetic-density` | Spin polarization and collinear/noncollinear magnetism | [mat-magnetic-density](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-magnetic-density) |
| `mat-md-monitors` | On-the-fly thermodynamic and structural monitors | [mat-md-monitors](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-md-monitors) |
| `mat-md-probability-density` | 3D ion diffusion probability densities from MD | [mat-md-probability-density](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-md-probability-density) |
| `mat-melting-point` | Solid-liquid coexistence melting point simulation | [mat-melting-point](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-melting-point) |
| `mat-phase-diagram` | Convex hull phase stability calculation | [mat-phase-diagram](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-phase-diagram) |
| `mat-phase-field-conservative`| Cahn-Hilliard spinodal decomposition modeling | [mat-phase-field-conservative](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-phase-field-conservative) |
| `mat-phase-field-non-conservative`| Allen-Cahn grain growth simulation | [mat-phase-field-non-conservative](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-phase-field-non-conservative) |
| `mat-phonon` | Phonon band structures, DOS, and thermal properties | [mat-phonon](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-phonon) |
| `mat-pourbaix-diagram` | Aqueous electrochemical stability (Pourbaix) | [mat-pourbaix-diagram](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-pourbaix-diagram) |
| `mat-qha-thermal-expansion` | Quasi-harmonic thermal expansion and $C_p$ | [mat-qha-thermal-expansion](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-qha-thermal-expansion) |
| `mat-raman-spectra` | Raman intensity and vibrational spectra | [mat-raman-spectra](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-raman-spectra) |
| `mat-random-structure-search` | Ab initio random structure searching (AIRSS) | [mat-random-structure-search](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-random-structure-search) |
| `mat-reaction-network` | Chemical reaction networks and synthesis paths | [mat-reaction-network](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-reaction-network) |
| `mat-sample-pes-by-md` | Active learning PES sampling via high-T MD | [mat-sample-pes-by-md](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-sample-pes-by-md) |
| `mat-solid-free-energy` | Absolute free energies of solids via thermodynamic integration | [mat-solid-free-energy](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-solid-free-energy) |
| `mat-stability` | Stability classification against chemical potential bounds | [mat-stability](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-stability) |
| `mat-structure-novelty` | Structure fingerprinting and novelty detection | [mat-structure-novelty](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-structure-novelty) |
| `mat-surface-adsorption` | Adsorption site identification and binding energies | [mat-surface-adsorption](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-surface-adsorption) |
| `mat-surface-energy` | Slab model surface energies and Wulff crystal shapes | [mat-surface-energy](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-surface-energy) |
| `mat-synthesis-extraction` | Synthesis condition extraction from paper texts | [mat-synthesis-extraction](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-synthesis-extraction) |
| `mat-synthesis-recommendation` | Recommend solid-state reaction conditions | [mat-synthesis-recommendation](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-synthesis-recommendation) |
| `mat-wannier-tight-binding` | Wannier90 tight-binding Hamiltonians | [mat-wannier-tight-binding](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-wannier-tight-binding) |
| `mat-xrd-calculator` | Theoretical powder XRD simulation from CIFs | [mat-xrd-calculator](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-xrd-calculator) |
| `mat-xrd-digitizer` | Digitize 2D plot images of experimental XRD spectra | [mat-xrd-digitizer](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-xrd-digitizer) |
| `mat-xrd-phase-analysis` | Identify crystalline phases from experimental XRD | [mat-xrd-phase-analysis](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-xrd-phase-analysis) |
| `mat-xrd-refinement` | Rietveld refinement parameter optimization | [mat-xrd-refinement](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/mat-xrd-refinement) |

Upstream Source: [AtomisticSkills Materials Repository](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills)

