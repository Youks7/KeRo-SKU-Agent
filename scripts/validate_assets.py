#!/usr/bin/env python3
"""Validate image files against platform/slot baselines and optional overrides."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageStat


RULES = {
    ("amazon", "main"): {"min_longest": 1000, "square": False, "white_background": True},
    ("tiktok-shop", "main"): {"min_width": 600, "min_height": 600, "square": True, "white_background": True},
    ("tiktok-shop", "variation"): {"min_width": 600, "min_height": 600, "square": True, "white_background": False},
}
SUPPORTED = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".gif", ".webp"}


def edge_whiteness(image: Image.Image) -> float:
    rgb = image.convert("RGB")
    width, height = rgb.size
    band = max(1, min(width, height) // 50)
    crops = [
        rgb.crop((0, 0, width, band)),
        rgb.crop((0, height - band, width, height)),
        rgb.crop((0, 0, band, height)),
        rgb.crop((width - band, 0, width, height)),
    ]
    means = [ImageStat.Stat(crop).mean for crop in crops]
    return sum(sum(channel for channel in mean) / 3 for mean in means) / len(means)


def validate(path: Path, platform: str, slot: str, args: argparse.Namespace) -> dict:
    result = {"file": str(path), "errors": [], "warnings": []}
    if path.suffix.lower() not in SUPPORTED:
        result["errors"].append(f"unsupported extension: {path.suffix}")
        return result

    try:
        with Image.open(path) as image:
            width, height = image.size
            result.update({"format": image.format, "width": width, "height": height})
            rule = dict(RULES.get((platform, slot), {}))
            if args.min_width:
                rule["min_width"] = args.min_width
            if args.min_height:
                rule["min_height"] = args.min_height
            if args.square:
                rule["square"] = True

            if width < rule.get("min_width", 0):
                result["errors"].append(f"width {width} < {rule['min_width']}")
            if height < rule.get("min_height", 0):
                result["errors"].append(f"height {height} < {rule['min_height']}")
            if max(width, height) < rule.get("min_longest", 0):
                result["warnings"].append(
                    f"longest side {max(width, height)} < recommended {rule['min_longest']}"
                )
            if rule.get("square") and width != height:
                result["errors"].append(f"image must be square; got {width}x{height}")
            if rule.get("white_background"):
                whiteness = edge_whiteness(image)
                result["edge_whiteness"] = round(whiteness, 2)
                if whiteness < 245:
                    result["warnings"].append(
                        "edge background is not near-white; visually verify the required white background"
                    )
            if image.mode in {"RGBA", "LA"}:
                result["warnings"].append("image contains an alpha channel; verify platform support")
    except Exception as exc:
        result["errors"].append(f"cannot read image: {exc}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--platform", required=True, choices=["amazon", "taobao", "tmall", "pinduoduo", "jd", "1688", "shopify", "tiktok-shop"])
    parser.add_argument("--slot", required=True)
    parser.add_argument("--min-width", type=int)
    parser.add_argument("--min-height", type=int)
    parser.add_argument("--square", action="store_true")
    args = parser.parse_args()

    files = [args.path] if args.path.is_file() else sorted(
        path for path in args.path.rglob("*") if path.is_file() and path.suffix.lower() in SUPPORTED
    )
    results = [validate(path, args.platform, args.slot, args) for path in files]
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 1 if any(result["errors"] for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())

