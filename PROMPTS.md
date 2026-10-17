# `ai-rules` Injection & Maintenance Prompts

Copy and paste any of the prompts below into an Antigravity session opened in your target project.

---

## 1. Default Install (Elephant/Goldfish + `/interject` Rule & Skill)

 installs both the stack-adapted [Elephant/Goldfish](https://github.com/ddmms/elephant-goldfish) workflow skills and the `/interject` rule & slash command:

```text
Read https://github.com/alinelena/ai-rules (specifically BOOTSTRAP.md and antigravity/BOOTSTRAP.md) and install the skills and rules in this project with default options (elephant-goldfish enabled + /interject rule and skill enabled).
```

*(Or if `ai-rules` is cloned locally at `~/playground/ai-rules`):*

```text
Read ~/playground/ai-rules/BOOTSTRAP.md and install the skills and rules in this project.
```

---

## 2. Install Only `/interject` (Skip Elephant/Goldfish)

If you only want the `/interject` rule and slash command without the 5 `eg-*` skills:

```text
Read https://github.com/alinelena/ai-rules/blob/main/antigravity/BOOTSTRAP.md and install only the /interject rule and skill in this project (disable elephant-goldfish).
```

---

## 3. Install Only Elephant/Goldfish (Skip `/interject`)

```text
Read https://github.com/alinelena/ai-rules/blob/main/antigravity/BOOTSTRAP.md and install only the elephant-goldfish skills from https://github.com/ddmms/elephant-goldfish in this project (skip /interject).
```

---

## 4. Update an Already-Bootstrapped Project

To pull the latest `/interject` rules from `ai-rules` and the latest upstream workflow logic from `ddmms/elephant-goldfish` while preserving your target project's local stack commands:

```text
Update this project's AI skills and rules from https://github.com/alinelena/ai-rules and https://github.com/ddmms/elephant-goldfish (branch ddmms):
1. Refresh `.agents/rules/interject.md` and `.agents/skills/interject/SKILL.md` from `ai-rules`.
2. Diff our local `.agents/skills/eg-*/SKILL.md` files against the upstream templates in `ddmms/elephant-goldfish`, merging any new workflow logic while preserving all of our project-specific test, lint, and stack commands.
3. Update `AGENTS.md` snippets if needed and report the changes without committing.
```
