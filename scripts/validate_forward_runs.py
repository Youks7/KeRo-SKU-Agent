#!/usr/bin/env python3
"""Validate the eight recorded single-agent marketplace forward runs."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "tests" / "forward-runs"
MARKERS = {
    "taobao.md": ["Main 1:1 or 3:4", "SKU property image", "Mobile detail modules"],
    "tmall.md": ["SPU/SKU map", "Brand story", "Qualification module"],
    "pinduoduo.md": ["SKU—price—image matrix", "Exposure image", "lowest-price SKU"],
    "jd.md": ["Parameter—evidence matrix", "compatibility", "Warranty"],
    "1688.md": ["Procurement data gaps", "MOQ", "OEM/ODM", "production"],
    "amazon.md": ["Main Image", "Secondary", "A+ modules"],
    "shopify.md": ["PDP map", "Add to Cart", "HTML", "metafield"],
    "tiktok-shop.md": ["PDP Main Image", "Variation image", "Shop Ads", "Shoppable Photo"],
}
COMMON = ["## Input preservation", "## Direction proposal", "## Confirmed", "## QA result", "Pass"]
FORBIDDEN_AFFIRMATIVE = [
    "UV400 polarized",
    "certified eye protection",
    "food-grade",
    "10,000 units per day",
    "factory area of",
]


def main() -> int:
    errors: list[str] = []
    texts: dict[str, str] = {}
    for filename, markers in MARKERS.items():
        path = RUNS / filename
        if not path.is_file():
            errors.append(f"missing run: {filename}")
            continue
        text = path.read_text(encoding="utf-8-sig")
        texts[filename] = text
        for marker in [*COMMON, *markers]:
            if marker not in text:
                errors.append(f"{filename}: missing marker {marker!r}")
        for phrase in FORBIDDEN_AFFIRMATIVE:
            if phrase.casefold() in text.casefold():
                errors.append(f"{filename}: contains forbidden affirmative phrase {phrase!r}")
        if "blocked" not in text and "human-review" not in text:
            errors.append(f"{filename}: lacks evidence-gating status")

    if len({text for text in texts.values()}) != len(texts):
        errors.append("two platform outputs are byte-identical")

    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1

    print(f"[PASS] {len(texts)} marketplace forward-run records")
    print("[PASS] common workflow stages, platform markers, evidence gating, and forbidden-claim checks")
    print("LIMITATION: eight historical final-output runs share one agent; V1.4 direction gating and V1.5 migration planning were independently tested, but actual F2 fidelity and real-image migration outputs remain unverified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
