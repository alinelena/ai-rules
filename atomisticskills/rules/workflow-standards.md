---
trigger: model_decision
description: Rules to implement and execute multi-stage atomistic research workflows.
---

# Workflow Standards for AtomisticSkills

High-level multi-stage research campaigns in [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills) are implemented as workflows within `.agents/workflows/`.

## What is an Atomistic Workflow?

Workflows differ from single-step skills or atomic MCP tools:
1. **High-Level Objective**: Defines an end-to-end campaign objective (e.g., discover a novel halide solid electrolyte, screen 10,000 MOFs for CO2 DAC, or perform small-molecule virtual screening).
2. **Scientific Scope**: Mimics the methodology of a scientific research paper, with clear stage gates, failure recovery, and validation criteria.
3. **Skill Chaining**: Sequences multiple modular skills (`mat-*`, `chem-*`, `drug-*`, `ml-*`) and MCP tools in an automated pipeline.

## Standard Workflow Format

Each workflow file uses Markdown with YAML frontmatter:

```markdown
---
description: Concise one-sentence summary of the workflow's research objective.
---

# <Workflow Title>

## 1. Initial Setup
Follow the initialization protocol in research-standards.md.
- Create timestamped directory: `research/YYYY-MM-DD_<project_name>`
- Define objective and target properties.

## 2. Candidate Generation / Database Mining
Retrieve or generate candidate structures:
- Skills: `mat-db-mp`, `chem-db-mof`, `ml-generative-mattergen`, etc.

## 3. Screening Funnel
Define sequential filtering stages:
- **Tier 1 (Rapid Screening)**: Fast MLIP relaxation or geometric filters.
- **Tier 2 (Refined Calculations)**: Elasticity, bandgap, sorption isotherm, or docking affinity.
- **Tier 3 (Validation)**: DFT recalculation, NEB barriers, or experimental comparison.

## 4. Documentation and Decision Making
- Central CSV tracking table (`candidates_tracking.csv`).
- Synthesis and experimental viability assessment.
```

Upstream Reference: [AtomisticSkills Workflow Standards](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/rules/workflow-standards.md)

