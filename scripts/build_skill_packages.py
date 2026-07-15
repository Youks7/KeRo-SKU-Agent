#!/usr/bin/env python3
"""Synchronize, validate, and build deterministic standalone .skill archives."""

from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGES = ROOT / "packages"
SKILL_DIRS = [
    ROOT / "SKU详情页导演Skill" / "sku-detail-page-director",
    *sorted(path.parent for path in (ROOT / "skills").glob("*/SKILL.md")),
]
FIXED_TIME = (1980, 1, 1, 0, 0, 0)


def run(script: str) -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / script)], check=True)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def build(skill_dir: Path) -> Path:
    archive = PACKAGES / f"{skill_dir.name}.skill"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as output:
        for source in sorted(path for path in skill_dir.rglob("*") if path.is_file()):
            relative = source.relative_to(skill_dir.parent).as_posix()
            info = zipfile.ZipInfo(relative, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            output.writestr(info, source.read_bytes())
    return archive


def clean_generated_packages() -> None:
    """Remove generated deliverables so renamed skills cannot leave stale packages."""
    PACKAGES.mkdir(parents=True, exist_ok=True)
    for path in PACKAGES.iterdir():
        if path.is_file() and (
            path.suffix == ".skill"
            or path.name in {"SHA256SUMS.txt", "kero-sku-skills-v1.3-bundle.zip"}
        ):
            path.unlink()


def main() -> int:
    run("sync_shared_rules.py")
    run("validate_agent.py")
    run("validate_all_skills.py")
    run("validate_orchestration.py")
    run("validate_production_protocol.py")
    run("validate_trigger_cases.py")
    run("validate_forward_runs.py")
    clean_generated_packages()

    built = [build(skill_dir) for skill_dir in SKILL_DIRS]
    lines = [f"{sha256(path)}  {path.name}" for path in built]
    sums = PACKAGES / "SHA256SUMS.txt"
    sums.write_text("\n".join(lines) + "\n", encoding="utf-8")

    bundle = PACKAGES / "kero-sku-skills-v1.3-bundle.zip"
    with zipfile.ZipFile(bundle, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as output:
        for source in [*built, sums]:
            info = zipfile.ZipInfo(source.name, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            output.writestr(info, source.read_bytes())
    lines.append(f"{sha256(bundle)}  {bundle.name}")
    sums.write_text("\n".join(lines) + "\n", encoding="utf-8")

    router_package = next(path for path in built if path.name == "sku-detail-page-director.skill")
    legacy_package = ROOT / "SKU详情页导演Skill" / "SKU详情页导演Skill.skill"
    shutil.copyfile(router_package, legacy_package)

    for line in lines:
        print(line)
    print(f"Built {len(built)} packages and one bundle in {PACKAGES}")
    print(f"Updated legacy router package: {legacy_package.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
