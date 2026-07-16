#!/usr/bin/env python3
"""Verify that every marketplace skill preserves the full per-unit production contract."""

from __future__ import annotations

import hashlib
from pathlib import Path

from project_config import PLATFORM_SKILL_NAMES


ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "shared" / "per-unit-production.md"

CONTRACT_MARKERS = (
    "整页生产总控",
    "逐单元强制模板",
    "Prompt：",
    "Negative Prompt：",
    "产品处理模式：F0 / F1 / F2 / F3",
    "创意命题：",
    "槽位创意自由度：",
    "身份锚点：",
    "参考抽象：",
    "发布闸门：",
    "文案位置与安全区：",
    "后期排版：",
    "镜头矩阵：",
    "产品一致性质检：",
    "通用 Prompt 拦截自检：",
    "来源图片 ID",
    "生成工具能力：",
    "禁止主张 / 缺失证据：",
    "ready / human-review / direction-only / blocked / repair-required",
    "PRODUCT_CUTOUT_ZONE",
    "F2｜身份条件编辑 / 重构",
    "不得把裸词 `logo`、`text`、`label`、`product packaging` 一刀切列为负面词",
)

SKILL_MARKERS = (
    "references/per-unit-production.md",
    "Prompt",
    "Negative Prompt",
    "处理模式",
    "文案位置",
    "后期排版",
    "镜头矩阵",
    "产品一致性质检",
    "通用 Prompt 拦截",
    "逐单元完整生产记录",
)

FIXTURES = (
    ROOT / "tests" / "production-protocol" / "taobao-detail-screen.md",
    ROOT / "tests" / "production-protocol" / "shopify-component-section.md",
    ROOT / "tests" / "production-protocol" / "mode-b-reference-edit.md",
    ROOT / "tests" / "production-protocol" / "sunglasses-f2-reconstruction.md",
)

FIXTURE_MARKERS = (
    "整页生产总控",
    "平台槽位 / 模块类型：",
    "销售任务：",
    "发布状态：",
    "本单元依赖：",
    "禁止主张 / 缺失证据：",
    "文案位置与安全区：",
    "产品处理模式：",
    "创意命题：",
    "槽位创意自由度：",
    "身份锚点：",
    "参考抽象：",
    "发布闸门：",
    "生成工具能力：",
    "镜头矩阵：",
    "Prompt：",
    "Negative Prompt：",
    "后期排版：",
    "产品一致性质检：",
    "通用 Prompt 拦截自检：",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def missing_markers(text: str, markers: tuple[str, ...]) -> list[str]:
    return [marker for marker in markers if marker not in text]


def main() -> int:
    if not CANONICAL.is_file():
        print(f"[FAIL] missing canonical protocol: {CANONICAL.relative_to(ROOT)}")
        return 1

    canonical_text = CANONICAL.read_text(encoding="utf-8-sig")
    canonical_missing = missing_markers(canonical_text, CONTRACT_MARKERS)
    if canonical_missing:
        print(f"[FAIL] canonical protocol missing markers: {canonical_missing}")
        return 1

    canonical_hash = digest(CANONICAL)
    failed = False
    for name in PLATFORM_SKILL_NAMES:
        skill_dir = ROOT / "skills" / name
        skill_file = skill_dir / "SKILL.md"
        protocol_file = skill_dir / "references" / "per-unit-production.md"
        errors: list[str] = []

        if not skill_file.is_file():
            errors.append("missing SKILL.md")
        else:
            skill_text = skill_file.read_text(encoding="utf-8-sig")
            missing = missing_markers(skill_text, SKILL_MARKERS)
            if missing:
                errors.append(f"SKILL.md missing markers: {missing}")

        if not protocol_file.is_file():
            errors.append("missing references/per-unit-production.md")
        elif digest(protocol_file) != canonical_hash:
            errors.append("production protocol differs from canonical shared source")

        if errors:
            failed = True
            print(f"[FAIL] {name}")
            for error in errors:
                print(f"  {error}")
        else:
            print(f"[PASS] {name}")

    for fixture in FIXTURES:
        if not fixture.is_file():
            failed = True
            print(f"[FAIL] missing regression fixture: {fixture.relative_to(ROOT)}")
            continue
        fixture_text = fixture.read_text(encoding="utf-8-sig")
        missing = missing_markers(fixture_text, FIXTURE_MARKERS)
        if missing:
            failed = True
            print(f"[FAIL] {fixture.relative_to(ROOT)} missing markers: {missing}")
        else:
            print(f"[PASS] {fixture.relative_to(ROOT)}")

    mode_a = (ROOT / "tests" / "production-protocol" / "taobao-detail-screen.md").read_text(encoding="utf-8-sig")
    mode_b = (ROOT / "tests" / "production-protocol" / "mode-b-reference-edit.md").read_text(encoding="utf-8-sig")
    mode_f2 = (ROOT / "tests" / "production-protocol" / "sunglasses-f2-reconstruction.md").read_text(encoding="utf-8-sig")
    mode_a_prompt = mode_a.split("Prompt：", 1)[1].split("\n", 1)[0]
    if "Do not generate any product or product-specific feature" not in mode_a_prompt:
        failed = True
        print("[FAIL] F1 fixture does not isolate background generation from product identity")
    if any(token in mode_a_prompt.casefold() for token in ("sunglasses", "black frame", "hinge", "lens", "logo", "packaging")):
        failed = True
        print("[FAIL] F1 background Prompt leaks product-specific identity details")
    if not all(marker in mode_a for marker in ("环境色匹配", "接触影", "边缘溢色", "台座透视", "repair-required")):
        failed = True
        print("[FAIL] F1 fixture does not test color matching, contact shadow, edge spill, perspective, and repair routing")
    if "F1 只能更换环境与合成条件，不能创造新的产品视角" not in canonical_text:
        failed = True
        print("[FAIL] canonical protocol does not prevent F1 from inventing a new product view")
    if "只支持单图参考编辑：不得使用 F2" not in canonical_text:
        failed = True
        print("[FAIL] canonical protocol allows F2 without the required multi-view tool path")
    mode_b_prompt = mode_b.split("Prompt：", 1)[1].split("\n", 1)[0]
    mode_b_negative = mode_b.split("Negative Prompt：", 1)[1].split("\n", 1)[0]
    if not all(marker in mode_b_prompt for marker in ("unique identity reference", "Preserve the exact existing product", "Logo placement", "packaging text")):
        failed = True
        print("[FAIL] F2 Prompt does not explicitly preserve existing product, Logo, and packaging text")
    if any(token in mode_b_negative.split(", ") for token in ("logo", "text", "label", "product packaging")):
        failed = True
        print("[FAIL] F2 fixture uses a bare negative token that conflicts with preserving existing product elements")
    f2_prompt = mode_f2.split("Prompt：", 1)[1].split("\n", 1)[0]
    if not all(marker in f2_prompt for marker in ("front.jpg", "side.jpg", "hinge.jpg", "identity contract", "preserve")):
        failed = True
        print("[FAIL] sunglasses F2 fixture does not bind all identity views and the identity contract")
    if not all(marker in mode_f2 for marker in ("镜片外轮廓", "鼻梁", "铰链", "镜腿起点", "Logo", "镜片色调", "human-review")):
        failed = True
        print("[FAIL] sunglasses F2 fixture lacks identity landmarks or human review gate")

    if not failed:
        print("[PASS] full Prompt, Negative Prompt, handling, copy, layout, shot, fidelity, and generic-prompt gates are enforced")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
