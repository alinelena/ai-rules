---
trigger: always_on
description: Scientific research protocol and planning standards for AtomisticSkills.
---

# Atomistic Research Standards

When performing atomistic simulations, screening campaigns, or property predictions using the [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills) ecosystem (MIT Learning Matter Lab):

## 0. Intent Classification & Triggering
Before starting a formal research plan, classify the user's intent:

1. **Direct Property Query**: Single-step requests for specific data or structures.
   - *Example*: "What is the lattice constant of Nickel?" or "Give me the structure of Aspirin."
   - **Action**: Use the appropriate database skill or MCP tool directly (`mat-db-mp` or `drug-db-pubchem`) and provide the answer. **Do NOT** create a research directory or a `research_plan.md`.

2. **Computational Research Task**: Multi-stage scientific objectives requiring new data generation, simulation-based verification, or screening workflows.
   - *Examples*:
     - "Screen for high-selectivity candidates for CO2 direct air capture."
     - "Calculate the elastic tensor and mechanical stability for a quaternary Heusler alloy."
     - "Benchmark and fine-tune an MLIP model on custom defect configurations."
   - **Action**: Trigger the **Research Protocol** (Steps 1-3 below).

3. **Broad Literature Synthesis & Review**: High-level questions requesting conceptual overviews, pros/cons, or state-of-the-art summaries without specifying a computational objective.
   - *Examples*: "What are the pros and cons of halide solid electrolytes?" or "Summarize recent progress in generative crystal diffusion models."
   - **Action**: Provide a detailed technical synthesis directly in chat without creating a research plan. At the end, ask: *"Would you like me to initiate a formal research project with atomistic simulations to verify these properties for a specific system?"*

---

## Research Protocol

1. **Define Research Directory**:
   - For every computational research task, establish a dedicated directory for storing results (structures, simulation outputs, downloaded papers, data, checkpoints): `./research/<YYYY-MM-DD>_<short_description>`.
   - All intermediate and final simulation files must reside in this directory.

2. **Create Research Plan (Artifact)**:
   - Your first priority is to strategize before running simulations.
   - Create the research plan as an Artifact named `research_plan.md`.
   - **Literature Review**: Reference relevant literature from arXiv, bioRxiv, or PubChem.
   - **MLIP Registry Check**: Check if existing foundation models (`MACE-MP-0`, `CHGNet`, `SevenNet`, `MatterSim`, `FairChem UMA`) cover the chemical system before planning fine-tuning.
   - **Conceptual Planning & Skill Mapping**: Map conceptual steps directly to specific AtomisticSkills (`mat-*`, `chem-*`, `drug-*`, `ml-*`).
   - Include clear stop/pivot criteria (e.g. if energy above convex hull > 0.1 eV/atom or dynamic instability detected, prune branch).

3. **Execution & Provenance Tracking**:
   - Maintain a centralized candidates tracking table (`candidates_tracking.csv`) with `candidate_id`, `formula`, `source`, `space_group`, and calculated properties (`e_above_hull`, `bandgap`, `bulk_modulus`).
   - Run computations using the unified launcher `venv/run <venv> python skills/<skill>/scripts/<script>.py` or via connected MCP servers (`base`, `mace`, `matgl`, `fairchem`, `atomate2`, `drugdisc`, `smol`).
   - Keep simulations reproducible with pinned seeds and recorded parameters.

Upstream Reference: [AtomisticSkills Research Standards](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/rules/research-standards.md)

