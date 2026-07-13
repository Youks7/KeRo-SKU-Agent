#!/usr/bin/env python3
"""Validate the one-entry workflow, stage-gated loading, and shared-source layout."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PLATFORMS = (
    "sku-taobao",
    "sku-tmall",
    "sku-pinduoduo",
    "sku-jd",
    "sku-1688",
    "sku-amazon",
    "sku-shopify",
    "sku-tiktok-shop",
)
EXPECTED_SHARED = {
    "core-safety.md",
    "per-unit-production.md",
    "core-qa.md",
    "sku-context-schema.md",
    "competitor-research.md",
}


def require(text: str, markers: tuple[str, ...], label: str, errors: list[str]) -> None:
    for marker in markers:
        if marker not in text:
            errors.append(f"{label}: missing {marker!r}")


def main() -> int:
    errors: list[str] = []
    router = ROOT / "SKU详情页导演Skill" / "sku-detail-page-director"
    router_text = (router / "SKILL.md").read_text(encoding="utf-8-sig")
    require(
        router_text,
        (
            "作为用户唯一入口",
            "在同一任务中使用 `$sku-product-core`",
            "不要让用户另开任务或重新粘贴资料",
            "不要只返回 Skill 名称让用户自己再次调用",
            "用户确认方向后",
        ),
        "router",
        errors,
    )
    router_agent = yaml.safe_load((router / "agents" / "openai.yaml").read_text(encoding="utf-8-sig"))
    default_prompt = router_agent.get("interface", {}).get("default_prompt", "")
    require(default_prompt, ("$sku-detail-page-director", "同一任务", "不要让我重复调用"), "router default_prompt", errors)

    stage_gate = "只有用户确认方向并进入正式生产时，才完整读取"
    for name in PLATFORMS:
        text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8-sig")
        require(
            text,
            (
                stage_gate,
                "references/per-unit-production.md",
                "没有上下文时先使用 `$sku-product-core`",
                "未安装时执行最小事实与保真检查",
            ),
            name,
            errors,
        )

    core = (ROOT / "skills" / "sku-product-core" / "SKILL.md").read_text(encoding="utf-8-sig")
    require(
        core,
        (
            "references/core-qa.md",
            "references/sku-context-schema.md",
            "references/competitor-research.md",
            "只有用户要求竞品扫描",
        ),
        "sku-product-core",
        errors,
    )

    actual_shared = {path.name for path in (ROOT / "shared").glob("*.md")}
    if actual_shared != EXPECTED_SHARED:
        errors.append(
            f"shared source set mismatch: missing={sorted(EXPECTED_SHARED - actual_shared)}, "
            f"extra={sorted(actual_shared - EXPECTED_SHARED)}"
        )

    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1

    print("[PASS] one-entry router continues through core and marketplace direction stages")
    print("[PASS] all eight platform skills defer the full production contract until direction approval")
    print("[PASS] canonical shared sources are explicit and orphan-free")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
