#!/usr/bin/env python3
"""Validate the identity-locked creative direction system and sunglasses regressions."""

from __future__ import annotations

from itertools import combinations
from pathlib import Path

import yaml
from project_config import PLATFORM_SKILL_NAMES


ROOT = Path(__file__).resolve().parents[1]
CREATIVE = ROOT / "shared" / "creative-direction-system.md"
SCHEMA = ROOT / "shared" / "sku-context-schema.md"
FIXTURE = ROOT / "tests" / "creative-direction" / "sunglasses-directions.yaml"
REAL_FIXTURE_REPORT = ROOT / "tests" / "real-sku" / "REAL_SUNGLASSES_REGRESSION.md"
REAL_FIXTURE_VALIDATOR = ROOT / "scripts" / "validate_real_sku_fixture.py"


def require(text: str, markers: tuple[str, ...], label: str, errors: list[str]) -> None:
    for marker in markers:
        if marker not in text:
            errors.append(f"{label}: missing {marker!r}")


def main() -> int:
    errors: list[str] = []

    if not CREATIVE.is_file():
        errors.append("missing shared/creative-direction-system.md")
    else:
        require(
            CREATIVE.read_text(encoding="utf-8-sig"),
            (
                "渐进式素材收集",
                "产品图诊断与多视图统一",
                "参考详情页语义分段",
                "参考抽象报告",
                "CREATIVE_CONTEXT",
                "三个差异化方向",
                "任意两个方向至少有三个维度不同",
                "策划—提示词—生成分离",
                "视觉质量闸门",
                "表现真实性",
                "参考与权利",
                "repair-required",
                "断点续作",
                "唯一权威状态文件",
                "state_revision",
                "商品身份严格，视觉表达自由",
            ),
            "creative system",
            errors,
        )
        creative_text = CREATIVE.read_text(encoding="utf-8-sig")
        stage_markers = (
            "渐进式素材收集",
            "产品图诊断与多视图统一",
            "参考详情页语义分段",
            "CREATIVE_CONTEXT",
            "三个差异化方向",
            "策划—提示词—生成分离",
            "视觉质量闸门",
            "断点续作",
        )
        positions = [creative_text.find(marker) for marker in stage_markers]
        if any(position < 0 for position in positions) or positions != sorted(positions):
            errors.append("creative workflow stages are missing or out of order")

    if not SCHEMA.is_file():
        errors.append("missing shared/sku-context-schema.md")
    else:
        require(
            SCHEMA.read_text(encoding="utf-8-sig"),
            (
                "SKU_CONTEXT V2",
                "IDENTITY_CONTRACT",
                "CREATIVE_CONTEXT",
                "immutable_traits",
                "bounded_traits",
                "view_confidence",
                "reference_abstraction_reports",
                "creative_freedom_by_slot",
                "F0",
                "F1",
                "F2",
                "F3",
                "持久化合同",
                "state_revision",
                "platform_contexts",
                "active_platform_context_id",
                "planned_units",
            ),
            "schema",
            errors,
        )

    for name in PLATFORM_SKILL_NAMES:
        skill_dir = ROOT / "skills" / name
        skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8-sig")
        require(
            skill_text,
            ("CREATIVE_CONTEXT", "三个差异化", "F0–F3", "references/creative-direction-system.md"),
            f"{name} skill",
            errors,
        )
        rules = (skill_dir / "references" / "platform-rules.md").read_text(encoding="utf-8-sig")
        require(
            rules,
            ("## 槽位级创意机会", "严格身份槽位", "受控创意槽位", "自由创意槽位"),
            f"{name} rules",
            errors,
        )

    if not FIXTURE.is_file():
        errors.append("missing sunglasses creative direction fixture")
    else:
        data = yaml.safe_load(FIXTURE.read_text(encoding="utf-8-sig"))
        identity = data.get("identity_contract", {})
        anchors = set(identity.get("immutable_traits", []))
        required_anchors = {"镜片外轮廓", "鼻梁", "铰链", "镜腿起点", "Logo 位置", "镜片色调"}
        if not required_anchors <= anchors:
            errors.append(f"sunglasses fixture missing identity anchors: {sorted(required_anchors - anchors)}")
        directions = data.get("creative_context", {}).get("directions", [])
        if len(directions) != 3:
            errors.append("sunglasses fixture must define exactly three directions")
        else:
            fields = ("thesis", "visual_world", "product_role", "camera_and_light", "narrative_arc")
            for direction in directions:
                for field in fields:
                    if not direction.get(field):
                        errors.append(f"direction {direction.get('id')} missing {field}")
                if len(direction.get("identity_anchors", [])) < 2:
                    errors.append(f"direction {direction.get('id')} must use at least two identity anchors")
                if not direction.get("suitable_slots") or not direction.get("unsuitable_slots"):
                    errors.append(f"direction {direction.get('id')} lacks slot boundaries")
            for left, right in combinations(directions, 2):
                differences = sum(left.get(field) != right.get(field) for field in fields)
                if differences < 3:
                    errors.append(f"directions {left.get('id')} and {right.get('id')} differ in only {differences} dimensions")
        forbidden = "\n".join(data.get("facts", {}).get("prohibited_claims", []))
        for claim in ("偏光", "UV", "防蓝光", "具体材质"):
            if claim not in forbidden:
                errors.append(f"sunglasses fixture does not prohibit unverified claim: {claim}")

    if not REAL_FIXTURE_VALIDATOR.is_file():
        errors.append("missing external real-SKU fixture validator")
    if not REAL_FIXTURE_REPORT.is_file():
        errors.append("missing real sunglasses regression report")
    else:
        require(
            REAL_FIXTURE_REPORT.read_text(encoding="utf-8-sig"),
            (
                "真实墨镜外部夹具回归",
                "正面、四分之三侧面和背面",
                "不复制到公开仓库",
                "身份合同",
                "三个方向",
                "F0",
                "F1",
                "F2",
                "F3",
                "repair-required",
                "并不证明任意图像模型一定能生成同款成图",
            ),
            "real sunglasses regression",
            errors,
        )

    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1

    print("[PASS] creative workflow, identity contract, reference abstraction, and slot freedom are wired")
    print("[PASS] all eight platform skills expose strict, controlled, and free creative slots")
    print("[PASS] sunglasses directions are identity-anchored and materially distinct")
    print("[PASS] real-sunglasses regression records an external private fixture without committing images")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
