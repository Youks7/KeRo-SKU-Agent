#!/usr/bin/env python3
"""Copy canonical shared contracts into standalone skill packages."""

from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLATFORM_NAMES = (
    "sku-taobao",
    "sku-tmall",
    "sku-pinduoduo",
    "sku-jd",
    "sku-1688",
    "sku-amazon",
    "sku-shopify",
    "sku-tiktok-shop",
)
CONTRACTS = {
    ROOT / "shared" / "core-safety.md": [
        ROOT / "SKU详情页导演Skill" / "sku-detail-page-director" / "references" / "common-safety.md",
        *[
            ROOT / "skills" / name / "references" / "common-safety.md"
            for name in PLATFORM_NAMES
        ],
    ],
    ROOT / "shared" / "per-unit-production.md": [
        ROOT / "skills" / name / "references" / "per-unit-production.md"
        for name in PLATFORM_NAMES
    ],
    ROOT / "shared" / "core-qa.md": [
        ROOT / "skills" / "sku-product-core" / "references" / "core-qa.md",
    ],
    ROOT / "shared" / "sku-context-schema.md": [
        ROOT / "skills" / "sku-product-core" / "references" / "sku-context-schema.md",
    ],
    ROOT / "shared" / "competitor-research.md": [
        ROOT / "skills" / "sku-product-core" / "references" / "competitor-research.md",
    ],
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail on missing or drifted targets without modifying files",
    )
    args = parser.parse_args()

    for source, targets in CONTRACTS.items():
        if not source.is_file():
            raise SystemExit(f"Missing canonical source: {source}")

        source_hash = sha256(source)
        print(f"Source {source.relative_to(ROOT)} {source_hash}")

        for target in targets:
            if args.check:
                if not target.is_file():
                    print(f"[MISSING] {target.relative_to(ROOT)}")
                    return 1
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
            target_hash = sha256(target)
            status = "OK" if target_hash == source_hash else "MISMATCH"
            print(f"[{status}] {target.relative_to(ROOT)} {target_hash}")
            if status != "OK":
                return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
