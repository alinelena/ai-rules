# `ai-rules` Injection & Maintenance Prompts

Copy and paste any of the prompts below into an Antigravity session opened in your target project.

---

## 1. Default Install (Elephant/Goldfish + `/interject` + `<project_name>-dev`)

Installs the stack-adapted [Elephant/Goldfish](https://github.com/ddmms/elephant-goldfish) workflow skills, the `/interject` rule & slash command, and the contextualized `<project_name>-dev` development skill:

```text
Read https://github.com/alinelena/ai-rules (specifically BOOTSTRAP.md and antigravity/BOOTSTRAP.md) and install the skills and rules in this project with default options.
```

*(Or if `ai-rules` is cloned locally at `~/playground/ai-rules`):*

```text
Read ~/playground/ai-rules/BOOTSTRAP.md and install the skills and rules in this project.
```

---

## 2. Selective Install Options

You can toggle any of the three components (`elephant-goldfish`, `interject`, `dev-template`) in your prompt:

- **Skip Elephant/Goldfish (install only `/interject` and `<project_name>-dev`)**:
  ```text
  Read https://github.com/alinelena/ai-rules/blob/main/antigravity/BOOTSTRAP.md and install the skills and rules in this project with elephant-goldfish=off.
  ```

- **Install only `/interject`**:
  ```text
  Read https://github.com/alinelena/ai-rules/blob/main/antigravity/BOOTSTRAP.md and install only the /interject rule and skill in this project (elephant-goldfish=off, dev-template=off).
  ```

- **Install with `janus-core` (`janus-core=on`)**:
  ```text
  Read https://github.com/alinelena/ai-rules/blob/main/antigravity/BOOTSTRAP.md and install the skills and rules in this project with janus-core=on.
  ```

- **Install with `aiida-mlip` (`aiida-mlip=on`)**:
  ```text
  Read https://github.com/alinelena/ai-rules/blob/main/antigravity/BOOTSTRAP.md and install the skills and rules in this project with aiida-mlip=on.
  ```

- **Install with `atomisticskills` (`atomisticskills=on`)**:
  ```text
  Read https://github.com/alinelena/ai-rules/blob/main/antigravity/BOOTSTRAP.md and install the skills and rules in this project with atomisticskills=on.
  ```

- **Install Complete Atomistic Simulation Stack (`janus-core=on` + `aiida-mlip=on` + `atomisticskills=on`)**:
  ```text
  Read https://github.com/alinelena/ai-rules/blob/main/antigravity/BOOTSTRAP.md and install all skills and rules in this project with janus-core=on, aiida-mlip=on, and atomisticskills=on.
  ```

---

## 3. Update an Already-Bootstrapped Project

To pull the latest `/interject` and `dev-template` updates from `ai-rules` plus the latest upstream workflow logic from `ddmms/elephant-goldfish` while preserving your target project's local stack commands:

```text
Update this project's AI skills and rules from https://github.com/alinelena/ai-rules and https://github.com/ddmms/elephant-goldfish (branch ddmms):
1. Refresh `.agents/rules/interject.md` and `.agents/skills/interject/SKILL.md` from `ai-rules`.
2. Diff our local `.agents/skills/<project_name>-dev/SKILL.md` and `.agents/skills/eg-*/SKILL.md` files against the upstream templates in `ai-rules` and `ddmms/elephant-goldfish`, merging any new workflow sections while preserving all of our project-specific test, lint, and stack commands.
3. Update `AGENTS.md` snippets if needed and report the changes without committing.
```

---

## 4. Install or Update Janus-Core Skills Group

To equip a project with the STFC [`janus-core`](https://github.com/stfc/janus-core) (docs: [`https://stfc.github.io/janus-core/`](https://stfc.github.io/janus-core/)) MLIP calculation skills, execution rules, and inspector tools:

```text
Read https://github.com/alinelena/ai-rules and install the janus-core skills group (singlepoint, geomopt, md, eos-elasticity, phonons, neb, descriptors, train-mlip, analysis) and execution rules into this project.
```

To sync skills and reference docs with the latest upstream [`janus-core`](https://github.com/stfc/janus-core) release:

```bash
./janus-core/update.sh
```

---

## 5. Install or Update AiiDA-MLIP Skills Group

To equip a project with the STFC [`aiida-mlip`](https://github.com/stfc/aiida-mlip) (docs: [`https://stfc.github.io/aiida-mlip/`](https://stfc.github.io/aiida-mlip/)) calculation skills, workgraphs, and execution rules:

```text
Read https://github.com/alinelena/ai-rules and install the aiida-mlip skills group (singlepoint, geomopt, md, phonons, descriptors, train, workflows) and execution rules into this project.
```

To sync skills and reference docs with the latest upstream [`aiida-mlip`](https://github.com/stfc/aiida-mlip) release:

```bash
./aiida-mlip/update.sh
```

---

## 6. Install or Update AtomisticSkills Group

To equip a project with the MIT Learning Matter Lab [`AtomisticSkills`](https://github.com/learningmatter-mit/AtomisticSkills) (docs: [`https://learningmatter-mit.github.io/AtomisticSkills/`](https://learningmatter-mit.github.io/AtomisticSkills/), paper: arXiv:2605.24002) multi-domain simulation suite:

```text
Read https://github.com/alinelena/ai-rules and install the atomisticskills group (materials, chemistry, drug-discovery, ml foundation models, workflows) and execution rules into this project.
```

To sync skills, rules, and reference catalogs with the latest upstream [`AtomisticSkills`](https://github.com/learningmatter-mit/AtomisticSkills) repository:

```bash
./atomisticskills/update.sh
# or dry-run check:
./atomisticskills/update.sh --check
```
