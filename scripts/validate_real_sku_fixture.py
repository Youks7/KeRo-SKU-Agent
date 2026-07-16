#!/usr/bin/env python3
"""Validate external real-SKU image inputs without copying private assets into the repo."""

from __future__ import annotations

import argparse
import hashlib
import struct
from pathlib import Path


MIN_BYTES = 50_000
MIN_EDGE = 800


def image_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(32)
        if header.startswith(b"\x89PNG\r\n\x1a\n"):
            return struct.unpack(">II", header[16:24])
        if header[:2] != b"\xff\xd8":
            raise ValueError(f"{path.name}: only PNG and JPEG are supported")
        handle.seek(2)
        while True:
            prefix = handle.read(1)
            if not prefix:
                break
            if prefix != b"\xff":
                continue
            marker = handle.read(1)
            while marker == b"\xff":
                marker = handle.read(1)
            if marker in {bytes([value]) for value in range(0xC0, 0xC4)} | {
                bytes([value]) for value in range(0xC5, 0xC8)
            } | {bytes([value]) for value in range(0xC9, 0xCC)} | {
                bytes([value]) for value in range(0xCD, 0xD0)
            }:
                length = struct.unpack(">H", handle.read(2))[0]
                payload = handle.read(length - 2)
                height, width = struct.unpack(">HH", payload[1:5])
                return width, height
            length_bytes = handle.read(2)
            if len(length_bytes) != 2:
                break
            length = struct.unpack(">H", length_bytes)[0]
            handle.seek(length - 2, 1)
    raise ValueError(f"{path.name}: could not read image dimensions")


def inspect(role: str, path: Path) -> tuple[str, int, int, int, str]:
    if not path.is_file():
        raise ValueError(f"{role}: file does not exist")
    size = path.stat().st_size
    if size < MIN_BYTES:
        raise ValueError(f"{role}: file is too small to be a production image ({size} bytes)")
    width, height = image_size(path)
    if min(width, height) < MIN_EDGE:
        raise ValueError(f"{role}: shortest edge is below {MIN_EDGE}px ({width}x{height})")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return role, width, height, size, digest


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check a front, three-quarter, and back view from one external real-SKU fixture."
    )
    parser.add_argument("--front", type=Path, required=True)
    parser.add_argument("--three-quarter", type=Path, required=True)
    parser.add_argument("--back", type=Path, required=True)
    args = parser.parse_args()

    try:
        results = [
            inspect("front", args.front),
            inspect("three-quarter", args.three_quarter),
            inspect("back", args.back),
        ]
        hashes = [result[4] for result in results]
        if len(set(hashes)) != len(hashes):
            raise ValueError("view files are not distinct")
    except (OSError, ValueError, struct.error) as exc:
        print(f"[FAIL] {exc}")
        return 1

    for role, width, height, size, digest in results:
        print(f"[PASS] {role}: {width}x{height}, {size} bytes, sha256={digest[:12]}")
    print("[PASS] external real-SKU input gate passed; private images were read in place and not copied")
    print("[INFO] this gate validates input integrity, not generated-image identity fidelity")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
