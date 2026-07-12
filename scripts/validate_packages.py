#!/usr/bin/env python3
"""Verify built .skill archives byte-for-byte against their source directories."""

from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGES = ROOT / "packages"
SKILL_DIRS = [
    ROOT / "SKU详情页导演Skill" / "sku-detail-page-director",
    *sorted(path.parent for path in (ROOT / "skills").glob("*/SKILL.md")),
]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def validate(skill_dir: Path) -> list[str]:
    archive = PACKAGES / f"{skill_dir.name}.skill"
    errors: list[str] = []
    if not archive.is_file():
        return [f"missing package: {archive.name}"]

    expected = {
        source.relative_to(skill_dir.parent).as_posix(): source.read_bytes()
        for source in skill_dir.rglob("*")
        if source.is_file()
    }
    with zipfile.ZipFile(archive) as package:
        actual_names = {entry.filename for entry in package.infolist() if not entry.is_dir()}
        if actual_names != set(expected):
            errors.append(
                f"file set mismatch: missing={sorted(set(expected) - actual_names)}, "
                f"extra={sorted(actual_names - set(expected))}"
            )
        for name in actual_names & set(expected):
            package_data = package.read(name)
            if package_data != expected[name]:
                errors.append(
                    f"content mismatch {name}: package={digest(package_data)} source={digest(expected[name])}"
                )
    return errors


def main() -> int:
    failed = False
    for skill_dir in SKILL_DIRS:
        errors = validate(skill_dir)
        if errors:
            failed = True
            print(f"[FAIL] {skill_dir.name}")
            for error in errors:
                print(f"  {error}")
        else:
            print(f"[PASS] {skill_dir.name}")

    router_package = PACKAGES / "sku-detail-page-director.skill"
    legacy_package = ROOT / "SKU详情页导演Skill" / "SKU详情页导演Skill.skill"
    if router_package.read_bytes() != legacy_package.read_bytes():
        failed = True
        print("[FAIL] legacy router package does not match packages/sku-detail-page-director.skill")
    else:
        print("[PASS] legacy router package matches the standalone router package")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

