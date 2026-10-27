---
name: atomisticskills-ml
description: Machine learning interatomic potentials (MACE, FairChem, MatGL), generative materials discovery (MatterGen, DiffCSP, ADIT), and fine-tuning with AtomisticSkills (MIT Learning Matter Lab).
metadata:
  category: [machine-learning, foundation-models, generative-ai, mlip-finetuning, uncertainty]
---

# AtomisticSkills Machine Learning Hub

The Machine Learning suite in [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills) provides 16 modular skills and MCP tools covering foundation MLIP model selection, fine-tuning, generative crystal design, active learning uncertainty, and high-performance inference.

---

## 1. Foundation Potentials Selection & Benchmarking

- **Foundation Models Guide**: [ml-foundation-potentials](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-foundation-potentials) provides systematic decision trees for choosing between `MACE-MP-0` (equivariant message-passing), `CHGNet` (crystal Hamiltonian graph neural net), `SevenNet` (scalable 7-element models), and `FairChem UMA/ESEN` (multi-domain foundation potentials).
- **MLIP Benchmarking**: [ml-mlip-benchmark](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-mlip-benchmark) evaluates energy/force RMSE against DFT references.
- **Inference Speed Profiling**: [ml-mlip-speed](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-mlip-speed) profiles throughput in atom-steps per second across CPU and GPU hardware.
- **Hardware Acceleration**: [ml-mlip-nvalchemi](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-mlip-nvalchemi) integrates NVIDIA `nvalchemi-toolkit` and `cuEquivariance` for optimized tensor operations.

---

## 2. Fine-Tuning & Transfer Learning

- **MACE Fine-Tuning**: [ml-mace-finetune](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-mace-finetune) fine-tunes foundation MACE checkpoints on user-provided DFT configurations with energy, force, and stress loss weighting.
- **FairChem Fine-Tuning**: [ml-fairchem-finetune](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-fairchem-finetune) trains and fine-tunes Universal Materials Accelerator (UMA) and Equivariant Sliced Equivariant Networks (ESEN).
- **MatGL Fine-Tuning**: [ml-matgl-finetune](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-matgl-finetune) fine-tunes graph neural network potentials.
- **AutoML**: [ml-mlip-automl](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-mlip-automl) searches optimal hyperparameters (learning rate, cutoff radius, loss weights).

---

## 3. Generative AI for Materials Design

- **Microsoft MatterGen**: [ml-generative-mattergen](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-generative-mattergen) produces novel crystalline materials conditioned on target composition, space group, or physical properties using score-based diffusion models.
- **DiffCSP**: [ml-generative-diffcsp](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-generative-diffcsp) generates periodic crystal structures conditioned on formula and space-group symmetry constraints.
- **ADIT**: [ml-generative-adit](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-generative-adit) applies all-dielectric inverse design transformers for periodic dielectric lattices and nanophotonic structures.

---

## 4. Active Learning & Uncertainty Quantification

- **Committee Ensembles**: [ml-committee-uncertainty](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-committee-uncertainty) computes ensemble variance across $N$ models:
  $$\sigma_F = \sqrt{\frac{1}{N}\sum_{i=1}^N \|F_i - \bar{F}\|^2}$$
  Structures where $\sigma_F > \sigma_{\text{threshold}}$ are automatically routed to DFT for relabeling.
- **Bayesian Optimization**: [ml-bayesian-optimization](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-bayesian-optimization) guides expensive experiments or ab initio simulations to maximize target material figures of merit.
- **Superconductivity Prediction**: [ml-property-predict-scd](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-property-predict-scd) predicts critical temperature $T_c$.

---

## 5. Directory of All 16 Machine Learning Skills

| Skill | Description | Upstream Repository Link |
| :--- | :--- | :--- |
| `ml-bayesian-optimization` | Iterative black-box optimization of materials properties | [ml-bayesian-optimization](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-bayesian-optimization) |
| `ml-cluster-expansion` | Train cluster expansion for lattice Monte Carlo | [ml-cluster-expansion](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-cluster-expansion) |
| `ml-committee-uncertainty` | MACE committee ensemble uncertainty quantification | [ml-committee-uncertainty](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-committee-uncertainty) |
| `ml-fairchem-finetune` | Fine-tune FairChem potentials (UMA, ESEN) | [ml-fairchem-finetune](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-fairchem-finetune) |
| `ml-foundation-potentials` | Decision tree for selecting foundation MLIP models | [ml-foundation-potentials](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-foundation-potentials) |
| `ml-generative-adit` | All-dielectric inverse design transformer | [ml-generative-adit](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-generative-adit) |
| `ml-generative-diffcsp` | Crystal structure prediction with diffusion models | [ml-generative-diffcsp](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-generative-diffcsp) |
| `ml-generative-mattergen` | Microsoft MatterGen crystal generative diffusion | [ml-generative-mattergen](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-generative-mattergen) |
| `ml-mace-finetune` | Fine-tune MACE models on custom DFT datasets | [ml-mace-finetune](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-mace-finetune) |
| `ml-matgl-finetune` | Fine-tune MatGL graph neural network potentials | [ml-matgl-finetune](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-matgl-finetune) |
| `ml-mlip-automl` | Hyperparameter search for potential training | [ml-mlip-automl](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-mlip-automl) |
| `ml-mlip-benchmark` | Energy/force RMSE and parity benchmarking | [ml-mlip-benchmark](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-mlip-benchmark) |
| `ml-mlip-nvalchemi` | High-throughput CUDA acceleration with cuEquivariance | [ml-mlip-nvalchemi](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-mlip-nvalchemi) |
| `ml-mlip-speed` | Benchmark MD throughput in atom-steps per second | [ml-mlip-speed](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-mlip-speed) |
| `ml-property-predictor` | Rapid composition-to-property screening models | [ml-property-predictor](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-property-predictor) |
| `ml-property-predict-scd` | Predict superconducting critical temperature $T_c$ | [ml-property-predict-scd](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/ml-property-predict-scd) |

Upstream Source: [AtomisticSkills ML Repository](https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills)

