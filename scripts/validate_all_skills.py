#!/usr/bin/env python3
"""Validate every KeRo SKU skill and emit human or JSON results."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIRS = [
    ROOT / "SKU详情页导演Skill" / "sku-detail-page-director",
    *sorted(path.parent for path in (ROOT / "skills").glob("*/SKILL.md")),
]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LOCAL_LINK_RE = re.compile(r"\[[^\]]+\]\((?!https?://|#)([^)]+)\)")


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8-sig")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        raise ValueError("missing YAML frontmatter")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a mapping")
    return data, text


def validate_skill(skill_dir: Path) -> dict:
    result = {"skill": skill_dir.name, "path": str(skill_dir), "errors": [], "warnings": []}
    skill_file = skill_dir / "SKILL.md"
    agent_file = skill_dir / "agents" / "openai.yaml"

    if not skill_file.is_file():
        result["errors"].append("missing SKILL.md")
        return result

    try:
        frontmatter, text = parse_frontmatter(skill_file)
    except Exception as exc:  # validation should report every package
        result["errors"].append(str(exc))
        return result

    keys = set(frontmatter)
    if keys != {"name", "description"}:
        result["errors"].append(f"frontmatter keys must be name,description; got {sorted(keys)}")

    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not isinstance(name, str) or not NAME_RE.fullmatch(name) or len(name) > 64:
        result["errors"].append(f"invalid skill name: {name!r}")
    if name != skill_dir.name:
        result["errors"].append(f"folder/name mismatch: {skill_dir.name!r} != {name!r}")
    if not isinstance(description, str) or not description.strip():
        result["errors"].append("description is empty")
    elif len(description) > 1024:
        result["errors"].append("description exceeds 1024 characters")

    line_count = len(text.splitlines())
    result["line_count"] = line_count
    if line_count > 500:
        result["errors"].append(f"SKILL.md exceeds 500 lines: {line_count}")

    for raw_target in LOCAL_LINK_RE.findall(text):
        target = raw_target.split("#", 1)[0].strip().replace("%20", " ")
        if target and not (skill_dir / target).is_file():
            result["errors"].append(f"broken local reference: {raw_target}")

    if not agent_file.is_file():
        result["errors"].append("missing agents/openai.yaml")
    else:
        try:
            agent_data = yaml.safe_load(agent_file.read_text(encoding="utf-8-sig")) or {}
            interface = agent_data.get("interface", {})
            short = interface.get("short_description", "")
            prompt = interface.get("default_prompt", "")
            if not 25 <= len(short) <= 64:
                result["errors"].append(
                    f"short_description must be 25-64 characters; got {len(short)}"
                )
            if f"${name}" not in prompt:
                result["errors"].append(f"default_prompt must mention ${name}")
        except Exception as exc:
            result["errors"].append(f"invalid agents/openai.yaml: {exc}")

    references = skill_dir / "references"
    if references.is_dir():
        for reference in references.glob("*.md"):
            lines = reference.read_text(encoding="utf-8-sig").splitlines()
            if len(lines) > 100 and not any(
                heading.strip().lower() in {"## 目录", "## contents", "## table of contents"}
                for heading in lines[:40]
            ):
                result["warnings"].append(
                    f"long reference lacks a top-level contents section: {reference.name} ({len(lines)} lines)"
                )
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of human-readable output")
    args = parser.parse_args()

    results = [validate_skill(path) for path in SKILL_DIRS]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for result in results:
            status = "PASS" if not result["errors"] else "FAIL"
            print(f"[{status}] {result['skill']} ({result.get('line_count', '?')} lines)")
            for error in result["errors"]:
                print(f"  ERROR: {error}")
            for warning in result["warnings"]:
                print(f"  WARN: {warning}")

    return 1 if any(result["errors"] for result in results) else 0


if __name__ == "__main__":
    sys.exit(main())

