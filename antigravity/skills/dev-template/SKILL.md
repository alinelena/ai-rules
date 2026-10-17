---
name: <project_name>-dev
description: >-
  Use this skill to understand the software engineering stack, project setup, and standard workflows for the <project_name> repository. Activate when you need to run tests, add dependencies, lint code, or manage the development environment.
---

# <Project Name> Development Guide

This skill outlines the software engineering practices, tooling stack, and local development setup for the `<project_name>` project.

## 1. Environment & Dependency Management
- **Environment**: Specify the environment manager (e.g., micromamba / conda / venv / direnv).
  - Prefix/activation command: `<environment_prefix_command>` (e.g. `micromamba run -n janus <command>` or `uv run --python /opt/micromamba/envs/janus/bin/python <command>`)
- **Dependencies**: Specify the package manager (e.g., `uv`, `poetry`, `pdm`, `npm`, `cargo`).
  - Install dependencies: `<install_command>` (e.g. `<env_prefix> uv pip install -e ".[test]"` or `<env_prefix> uv sync`)
  - Add new package: `<add_command>` (e.g. `<env_prefix> uv add <package>`)
- **Build System**: Specify the build backend configuration (for Python projects, prefer `uv_build` where applicable).
  ```toml
  [build-system]
  requires = ["<build_backend_package>"]
  build-backend = "<build_backend_module>"
  ```

## 2. Linting and Formatting
- **Linters & Formatters**: Specify the tools used (e.g., Ruff, Biome, ESLint, Prettier, Clippy).
  - Run linter: `<lint_command>` (e.g. `<env_prefix> uv run ruff check src tests`)
  - Run formatter: `<format_command>` (e.g. `<env_prefix> uv run ruff format src tests`)
  - Auto-fix issues: `<autofix_command>` (e.g. `<env_prefix> uv run ruff check --fix src tests`)
- **Pre-commit**: Specify pre-commit hook configuration and triggers (e.g., `.pre-commit-config.yaml`).

## 3. Testing & Verification
- **Framework**: Specify test runner and plugins (e.g., `pytest`, `pytest-qt`, `vitest`, `jest`, `cargo test`).
- **Running Tests**:
  - Full suite: `<test_command>` (e.g. `<env_prefix> uv run pytest`)
  - Single test: `<test_single_command>` (e.g. `<env_prefix> uv run pytest tests/test_feature.py -k test_name`)
- **Coverage**: Coverage tool and reporting command:
  - `<coverage_command>` (e.g. `<env_prefix> uv run pytest --cov=<module_name> --cov-report=term-missing`)
- **Special Execution Modes** (if applicable):
  - Headless UI / Display mocking: `<headless_command>` (e.g. `xvfb-run ...` or `QT_QPA_PLATFORM=offscreen ...`)
  - Database / External services / Docker fixtures: `<services_command>`
- **Matrix Testing**: Multi-version test runner (e.g., `tox`, `nox`).
  - `<matrix_command>` (e.g. `<env_prefix> tox`)

## 4. CI/CD Workflows
- **Test Matrix Workflow**: Location and summary of CI workflow (e.g. `.github/workflows/test.yml` running the test matrix on supported versions and uploading coverage).
- **Release / Publishing Workflow**: Location and summary of deployment/publishing pipeline (e.g. `.github/workflows/publish.yml` for PyPI Trusted Publishing / npm / container registry).

## 5. Local Execution & Debugging (Optional)
- **Run Application**: `<run_app_command>` (e.g. `<env_prefix> uv run <entrypoint>` or `npm run dev`)
- **Common Gotchas**: Any known quirks, environment variables, or platform-specific notes.
