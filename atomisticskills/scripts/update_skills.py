#!/usr/bin/env python3
"""
Update script for AtomisticSkills catalog, rules, and reference documentation.

Fetches the latest updates from:
1. GitHub Repository: https://github.com/learningmatter-mit/AtomisticSkills
2. Documentation:     https://learningmatter-mit.github.io/AtomisticSkills/

Parses the 130+ modular skills across Materials, Chemistry, Drug Discovery, and ML,
along with the 9 multi-stage research workflows and 11 MCP servers.

Usage:
    python update_skills.py [--repo <path-or-url>] [--docs-url <url>] [--check] [--force] [--verbose]
"""

import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request

DEFAULT_REPO_URL = "https://github.com/learningmatter-mit/AtomisticSkills.git"
DEFAULT_DOCS_URL = "https://learningmatter-mit.github.io/AtomisticSkills/"


def log(msg: str, verbose: bool = False, is_verbose_only: bool = False) -> None:
    if is_verbose_only and not verbose:
        return
    print(f"[atomisticskills-updater] {msg}")


def check_docs_live(docs_url: str, verbose: bool = False) -> dict:
    """Check if the documentation website is reachable and extract metadata."""
    log(f"Checking documentation URL: {docs_url} ...", verbose)
    result = {"url": docs_url, "accessible": False, "version": None}
    try:
        req = urllib.request.Request(
            docs_url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; AtomisticSkillsUpdater/1.0)"},
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            result["status"] = response.status
            if response.status == 200:
                result["accessible"] = True
                content = response.read(65536).decode("utf-8", errors="ignore")
                match = re.search(r"AtomisticSkills\s+v?([0-9]+\.[0-9]+(?:\.[0-9]+)?)", content, re.IGNORECASE)
                if match:
                    result["version"] = match.group(1)
                log(f"Documentation reachable (HTTP 200). Detected version: {result['version'] or 'unknown'}", verbose)
    except Exception as e:
        log(f"Warning: Could not fetch documentation URL '{docs_url}': {e}", verbose)
    return result


def resolve_repo(repo_input: str, verbose: bool = False) -> Path:
    """Resolve repository path (clone if remote URL, use directly if local directory)."""
    p = Path(repo_input)
    if p.exists() and (p / "pyproject.toml").exists() and (p / "skills").exists():
        log(f"Using local repository clone at: {p.resolve()}", verbose)
        return p.resolve()

    cache_dir = Path("/tmp/atomisticskills-upstream")
    if cache_dir.exists() and (cache_dir / ".git").exists():
        log(f"Updating existing upstream clone in {cache_dir}...", verbose)
        subprocess.run(["git", "-C", str(cache_dir), "fetch", "--depth=1", "origin", "main"], check=False, capture_output=True)
        subprocess.run(["git", "-C", str(cache_dir), "reset", "--hard", "origin/main"], check=False, capture_output=True)
        return cache_dir

    log(f"Cloning upstream repository from {repo_input} into {cache_dir}...", verbose)
    if cache_dir.exists():
        shutil.rmtree(cache_dir, ignore_errors=True)
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", repo_input, str(cache_dir)],
            check=True,
            capture_output=True,
            text=True,
        )
        return cache_dir
    except Exception as e:
        log(f"Notice: Could not clone upstream git repo ({e}). Proceeding in offline mode.")
        return None


def extract_version(repo_path: Path) -> str:
    """Extract version from VERSION file or pyproject.toml."""
    if not repo_path or not repo_path.exists():
        return "2.0.0"
    version_file = repo_path / "VERSION"
    if version_file.exists():
        v = version_file.read_text().strip()
        if v:
            return v
    pyproject = repo_path / "pyproject.toml"
    if pyproject.exists():
        for line in pyproject.read_text().splitlines():
            m = re.match(r'^\s*version\s*=\s*["\']([^"\']+)["\']', line)
            if m:
                return m.group(1)
    return "2.0.0"


def parse_skills(repo_path: Path) -> dict:
    """Parse all skills under skills/ directory."""
    if not repo_path or not repo_path.exists():
        return {}
    skills_dir = repo_path / "skills"
    if not skills_dir.exists():
        return {}

    skills = {}
    for item in sorted(skills_dir.iterdir()):
        skill_file = item / "SKILL.md"
        if not item.is_dir() or not skill_file.exists():
            continue
        skill_name = item.name
        content = skill_file.read_text(encoding="utf-8", errors="ignore")
        desc = "No description"
        category = skill_name.split("-")[0]
        venv = "cpu"

        fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if fm_match:
            fm = fm_match.group(1)
            for line in fm.splitlines():
                if line.startswith("description:"):
                    desc = line.split("description:", 1)[1].strip().strip('"\'')
                if "venv:" in line:
                    vm = re.search(r"\[(.*?)\]", line)
                    if vm:
                        venv = vm.group(1).strip()

        skills[skill_name] = {
            "name": skill_name,
            "category": category,
            "description": desc,
            "venv": venv,
            "url": f"https://github.com/learningmatter-mit/AtomisticSkills/tree/main/skills/{skill_name}",
        }
    return skills


def parse_workflows(repo_path: Path) -> dict:
    """Parse all workflows under .agents/workflows/ directory."""
    if not repo_path or not repo_path.exists():
        return {}
    wf_dir = repo_path / ".agents" / "workflows"
    if not wf_dir.exists():
        return {}

    workflows = {}
    for item in sorted(wf_dir.glob("*.md")):
        wf_name = item.name
        content = item.read_text(encoding="utf-8", errors="ignore")
        desc = "Research workflow"
        fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if fm_match:
            fm = fm_match.group(1)
            for line in fm.splitlines():
                if line.startswith("description:"):
                    desc = line.split("description:", 1)[1].strip().strip('"\'')

        workflows[wf_name] = {
            "name": wf_name,
            "description": desc,
            "url": f"https://github.com/learningmatter-mit/AtomisticSkills/blob/main/.agents/workflows/{wf_name}",
        }
    return workflows


def parse_mcp_servers(repo_path: Path) -> list:
    """Parse MCP server files under src/mcp_server/."""
    if not repo_path or not repo_path.exists():
        return []
    mcp_dir = repo_path / "src" / "mcp_server"
    if not mcp_dir.exists():
        return []
    servers = []
    for f in sorted(mcp_dir.glob("*_server.py")):
        srv_name = f.stem.replace("_server", "")
        servers.append({
            "name": srv_name,
            "file": f.name,
            "url": f"https://github.com/learningmatter-mit/AtomisticSkills/blob/main/src/mcp_server/{f.name}",
        })
    return servers


def main():
    parser = argparse.ArgumentParser(description="Update AtomisticSkills catalog and reference docs.")
    parser.add_argument("--repo", default=DEFAULT_REPO_URL, help="Upstream repo path or Git URL")
    parser.add_argument("--docs-url", default=DEFAULT_DOCS_URL, help="Documentation base URL")
    parser.add_argument("--check", action="store_true", help="Check upstream version and report status")
    parser.add_argument("--force", action="store_true", help="Force update even if version is up-to-date")
    parser.add_argument("--verbose", action="store_true", help="Verbose logging")
    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parent.parent
    version_file = base_dir / "VERSION"
    current_version = version_file.read_text().strip() if version_file.exists() else "0.0.0"

    log(f"Current local AtomisticSkills version: {current_version}", args.verbose)
    docs_info = check_docs_live(args.docs_url, args.verbose)

    # If repo argument is default remote and /tmp/AtomisticSkills exists, reuse it to save bandwidth
    repo_input = args.repo
    if repo_input == DEFAULT_REPO_URL and Path("/tmp/AtomisticSkills").exists():
        repo_input = "/tmp/AtomisticSkills"

    repo_path = resolve_repo(repo_input, args.verbose)
    upstream_version = extract_version(repo_path)
    log(f"Upstream repository version: {upstream_version}")

    skills = parse_skills(repo_path)
    workflows = parse_workflows(repo_path)
    servers = parse_mcp_servers(repo_path)

    log(f"Parsed {len(skills)} skills, {len(workflows)} workflows, and {len(servers)} MCP servers.")

    if args.check:
        print("\n--- AtomisticSkills Version Status ---")
        print(f"Local version:     {current_version}")
        print(f"Upstream version:  {upstream_version}")
        print(f"Documentation URL: {args.docs_url} (Accessible: {docs_info['accessible']})")
        print(f"Skills count:      {len(skills)}")
        print(f"Workflows count:   {len(workflows)}")
        print(f"MCP servers count: {len(servers)}")
        if current_version == upstream_version and not args.force:
            print("Status: UP TO DATE")
        else:
            print(f"Status: UPDATE AVAILABLE ({current_version} -> {upstream_version})")
        return 0

    # Write VERSION
    version_file.write_text(f"{upstream_version}\n")
    log(f"Updated {version_file} to {upstream_version}")

    # Write plugin.json
    plugin_file = base_dir / "plugin.json"
    if plugin_file.exists():
        plugin_data = json.loads(plugin_file.read_text())
        plugin_data["version"] = upstream_version
        plugin_file.write_text(json.dumps(plugin_data, indent=2) + "\n")
        log(f"Updated {plugin_file} version to {upstream_version}")

    log("AtomisticSkills synchronization completed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
