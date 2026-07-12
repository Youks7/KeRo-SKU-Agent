#!/usr/bin/env python3
"""Validate the static trigger-regression corpus."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "tests" / "trigger_cases.yaml"


def main() -> int:
    data = yaml.safe_load(CASES.read_text(encoding="utf-8-sig")) or {}
    discovered = {"sku-detail-page-director"}
    discovered.update(path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md"))
    errors: list[str] = []

    missing = discovered - set(data)
    extra = set(data) - discovered
    if missing:
        errors.append(f"missing skill cases: {sorted(missing)}")
    if extra:
        errors.append(f"unknown skill cases: {sorted(extra)}")

    owners: dict[str, list[str]] = defaultdict(list)
    for skill, groups in data.items():
        positive = groups.get("should_trigger", [])
        negative = groups.get("should_not_trigger", [])
        if len(positive) < 10:
            errors.append(f"{skill}: expected at least 10 positive cases, got {len(positive)}")
        if len(negative) < 5:
            errors.append(f"{skill}: expected at least 5 negative cases, got {len(negative)}")
        if len(positive) != len(set(positive)):
            errors.append(f"{skill}: duplicate positive cases")
        if len(negative) != len(set(negative)):
            errors.append(f"{skill}: duplicate negative cases")
        for phrase in positive:
            owners[phrase].append(skill)

    for phrase, skills in owners.items():
        if len(skills) > 1:
            errors.append(f"positive phrase is owned by multiple skills: {phrase!r} -> {skills}")

    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1

    print(f"[PASS] {len(data)} skills, {sum(len(v['should_trigger']) for v in data.values())} positive cases, "
          f"{sum(len(v['should_not_trigger']) for v in data.values())} negative cases")
    print("Static corpus validated. Model-level trigger behavior still requires forward testing in clean sessions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

