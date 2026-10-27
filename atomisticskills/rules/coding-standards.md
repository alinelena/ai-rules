---
trigger: always_on
description: Coding and project engineering standards for AtomisticSkills.
---

# AtomisticSkills Coding Standards

When authoring simulation scripts, data processing routines, or extending tools in [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills):

## 1. Global Guidelines
1. **Language**: All code and comments must be in **English**.
2. **Temporary Files**: All temporary log, validation, testing, and summary files must be created under `.agents/test` to maintain a clean project structure.
3. **Error Handling**: Avoid broad `try...except` blocks; ensure code output expectations are explicit, typed, and predictable.
4. **Cleanup**: After implementation changes, clean up temporary test code for deprecated functions.
5. **Reusability**: Search whether functionality already exists in standard packages (`ase`, `pymatgen`, `rdkit`, `mace-torch`, `fairchem-core`) before implementing custom helpers. Do not reinvent the wheel.
6. **Imports**: Use **absolute imports** for Python scripts and modules.
7. **MCP Stability**: If an MCP tool encounters an error, debug the tool root cause rather than writing ad-hoc throwaway scripts to bypass the failure.
8. **Security & Secrets**: Never hardcode API keys (e.g. `MP_API_KEY`, `OPENALEX_EMAIL`). Pass them via environment variables or local `.env` files.

## 2. Environment and Dependency Management
- **Environment Isolation**: Execute simulation scripts using the appropriate environment via the `venv/run` launcher (e.g. `cpu`, `mlip`, `fairchem`, `adit`, `diffcsp`, `mattergen`, `msms`, `reactot`, `scd`), or inside a configured conda/micromamba environment:
  - When using `micromamba`, run: `micromamba run -n janus python ...` (never use absolute paths for the python binary).
  - When using `uv`, run: `uv run --no-project python ...`
- **Dependency Versions**: Dependencies are managed per project in `venv/<project>/pyproject.toml` and committed `uv.lock`. Never arbitrarily force or mutate global system packages.

## 3. Documentation and Testing
- **Docstrings & Types**: Provide detailed docstrings and type annotations for all public functions and classes.
- **Testing**: Atomistic calculations and MCP tools must include `pytest`-based unit tests placed in `tests/`.

Upstream Reference: [AtomisticSkills Coding Standards](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/rules/coding-standards.md)

