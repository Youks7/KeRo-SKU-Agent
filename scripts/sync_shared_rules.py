#!/usr/bin/env python3
"""Copy the canonical safety contract into every standalone skill package."""

from __future__ import annotations

import hashlib
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "shared" / "core-safety.md"
TARGETS = [
    ROOT / "SKU详情页导演Skill" / "sku-detail-page-director" / "references" / "common-safety.md",
    *[
        ROOT / "skills" / name / "references" / "common-safety.md"
        for name in (
            "sku-taobao",
            "sku-tmall",
            "sku-pinduoduo",
            "sku-jd",
            "sku-1688",
            "sku-amazon",
            "sku-shopify",
            "sku-tiktok-shop",
        )
    ],
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> int:
    if not SOURCE.is_file():
        raise SystemExit(f"Missing canonical source: {SOURCE}")

    source_hash = sha256(SOURCE)
    print(f"Source {SOURCE.relative_to(ROOT)} {source_hash}")

    for target in TARGETS:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SOURCE, target)
        target_hash = sha256(target)
        status = "OK" if target_hash == source_hash else "MISMATCH"
        print(f"[{status}] {target.relative_to(ROOT)} {target_hash}")
        if status != "OK":
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

