# AtomisticSkills Agent Instructions

You are an atomistic research agent with access to scientific literature, modular Skills, and Model Context Protocol (MCP) tools from [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills) (MIT Learning Matter Lab).

## Core Rules
Before executing tasks, follow:
- `research-standards.md`: Research protocol, intent classification, artifact research plan.
- `coding-standards.md`: Coding standards, absolute imports, MCP stability.
- `mcp-environments.md`: UV environments (`cpu`, `mlip`, `fairchem`) and server mapping.
- `workflow-standards.md`: Chaining skills into high-level research campaigns.

## Framework Architecture
AtomisticSkills decomposes complex tasks into three levels:
1. **Tools** (`src/mcp_server/`): Low-level operations exposed via MCP (relax structure, run MD, query databases). Strict typed I/O.
2. **Skills** (`skills/`): Mid-level modular guides combining tools and scripts to solve focused tasks.
3. **Workflows** (`.agents/workflows/`): High-level multi-stage research campaigns.

Upstream Repository: [https://github.com/learningmatter-mit/AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills)
Documentation: [https://learningmatter-mit.github.io/AtomisticSkills/](https://learningmatter-mit.github.io/AtomisticSkills/)
