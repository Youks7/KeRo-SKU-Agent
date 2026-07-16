#!/usr/bin/env python3
"""Validate the reference-detail-page migration contract and regression cases."""

from __future__ import annotations

import hashlib
from itertools import combinations
from pathlib import Path

import yaml
from PIL import Image

from project_config import PLATFORM_SKILL_NAMES


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "tests" / "reference_migration_cases.yaml"
MIGRATION_SKILL = ROOT / "skills" / "sku-reference-migration"
FORWARD_REPORT = ROOT / "tests" / "FORWARD_TEST_REPORT.md"
VISUAL_FIXTURE = ROOT / "tests" / "reference-page" / "synthetic-competitor-long-page.png"
VISUAL_FIXTURE_SHA256 = "AFB03900B8B930EA0588740355B615770A35804B0D81EDA90F57E4515164F2F0"
DIRECTION_FIELDS = (
    "creative_thesis",
    "visual_world",
    "product_role",
    "camera_and_light",
    "graphic_system",
    "narrative_rhythm",
)


def require(text: str, markers: tuple[str, ...], label: str, errors: list[str]) -> None:
    for marker in markers:
        if marker not in text:
            errors.append(f"{label}: missing {marker!r}")


def validate_contract(errors: list[str]) -> None:
    skill_text = (MIGRATION_SKILL / "SKILL.md").read_text(encoding="utf-8-sig")
    canonical = (ROOT / "shared" / "reference-migration-system.md").read_text(encoding="utf-8-sig")
    schema = (ROOT / "shared" / "sku-context-schema.md").read_text(encoding="utf-8-sig")
    production = (ROOT / "shared" / "per-unit-production.md").read_text(encoding="utf-8-sig")
    agent = (ROOT / ".codex" / "agents" / "kero-sku-director.toml").read_text(encoding="utf-8-sig")
    router = (ROOT / "SKU详情页导演Skill" / "sku-detail-page-director" / "SKILL.md").read_text(encoding="utf-8-sig")
    forward_report = FORWARD_REPORT.read_text(encoding="utf-8-sig")

    require(
        skill_text,
        (
            "references/reference-migration-system.md",
            "REFERENCE_MIGRATION_CONTEXT",
            "M1｜结构迁移",
            "M2｜视觉语言迁移",
            "M3｜创意再诠释",
            "keep / adapt / replace / discard",
            "用户确认迁移方向前",
        ),
        "migration skill",
        errors,
    )

    if not VISUAL_FIXTURE.is_file():
        errors.append("visual reference-page fixture is missing")
    else:
        actual_hash = hashlib.sha256(VISUAL_FIXTURE.read_bytes()).hexdigest().upper()
        if actual_hash != VISUAL_FIXTURE_SHA256:
            errors.append("visual reference-page fixture hash does not match the reviewed artifact")
        try:
            with Image.open(VISUAL_FIXTURE) as image:
                if image.format != "PNG" or image.size != (1000, 4000):
                    errors.append(
                        f"visual reference-page fixture must be a 1000x4000 PNG; got {image.format} {image.size}"
                    )
        except OSError as exc:
            errors.append(f"visual reference-page fixture cannot be decoded: {exc}")
    require(
        canonical,
        (
            "rights_status",
            "semantic_modules[]",
            "reference_visual_tokens",
            "module_mapping[]",
            "target_evidence_ids",
            "platform_migrations",
            "任意两个方向至少",
            "整张长图不作为最终生成控制图",
            "creative_context_overrides",
        ),
        "canonical migration contract",
        errors,
    )
    require(
        schema,
        (
            "reference_migration_context:",
            "platform_migrations:",
            "platform_native_units:",
            "migration_mode: null  # M1 / M2 / M3",
            "target_platform_context_id",
            "reference_migration_status",
        ),
        "SKU_CONTEXT schema",
        errors,
    )
    require(
        production,
        (
            "参考迁移：N/A，或 migration_id + source_module_id",
            "迁移模式：M1 / M2 / M3 / N/A",
            "与参考模块的差异 / 原创性检查",
            "当前平台的 `reference_migration_context.platform_migrations[]` 必须已经批准",
        ),
        "production contract",
        errors,
    )
    require(
        agent,
        ("$sku-reference-migration", "REFERENCE_MIGRATION_CONTEXT", "M1", "M2", "M3", "先建立稳定的目标平台上下文"),
        "agent",
        errors,
    )
    require(
        router,
        ("$sku-reference-migration", "platform_migrations", "先识别平台", "基于已确认目标平台的模块映射"),
        "router",
        errors,
    )
    require(
        forward_report,
        (
            "V1.5 reference-detail-page migration forward test",
            "synthetic-competitor-long-page.png",
            "1000 × 4000",
            "segmented eight purchasing-question modules",
            "ORBIT SHADE",
            "HINGE STUDY",
            "competitor-analysis",
            "prohibited M2",
            "PASS FOR ACTUAL LONG-IMAGE INTAKE AND PLANNING",
        ),
        "reference migration forward report",
        errors,
    )

    expected_platform_marker = "若有已批准的 `REFERENCE_MIGRATION_CONTEXT`"
    for name in PLATFORM_SKILL_NAMES:
        text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8-sig")
        require(text, (expected_platform_marker, "覆盖来源页面"), name, errors)


def validate_case_structure(case: dict, evidence_registry: dict, errors: list[str]) -> None:
    case_id = case.get("id", "<missing>")
    source = case.get("source", {})
    migration = case.get("migration", {})
    rights = source.get("rights_status")
    mode = migration.get("migration_mode")
    if rights not in {"self-owned", "authorized", "competitor-analysis", "unknown"}:
        errors.append(f"{case_id}: invalid rights_status {rights!r}")
    if mode not in {"M1", "M2", "M3"}:
        errors.append(f"{case_id}: invalid migration_mode {mode!r}")
    if rights in {"competitor-analysis", "unknown"} and mode == "M2":
        errors.append(f"{case_id}: M2 is forbidden for {rights}")

    mappings = migration.get("module_mapping")
    if not isinstance(mappings, list) or not mappings:
        errors.append(f"{case_id}: migration requires a non-empty module_mapping")
        return
    for mapping in mappings:
        if mapping.get("action") not in {"keep", "adapt", "replace", "discard"}:
            errors.append(f"{case_id}: invalid mapping action")
        if mapping.get("action") != "discard" and not mapping.get("target_evidence_ids"):
            errors.append(f"{case_id}: non-discard mapping lacks target evidence")
        if mapping.get("action") != "discard":
            unknown_evidence = set(mapping.get("target_evidence_ids", [])) - set(evidence_registry)
            if unknown_evidence:
                errors.append(f"{case_id}: mapping cites unknown evidence ids {sorted(unknown_evidence)}")
            if mapping.get("handling_mode") not in {"F0", "F1", "F2", "F3"}:
                errors.append(f"{case_id}: non-discard mapping lacks a valid F0-F3 handling_mode")


def validate_semantics(cases_by_id: dict[str, dict], errors: list[str]) -> None:
    authorized = cases_by_id["authorized-page-m2"]
    if authorized["source"]["rights_status"] not in {"self-owned", "authorized"}:
        errors.append("authorized-page-m2: source does not permit M2")

    competitor = cases_by_id["competitor-page-m3"]
    excluded = set(competitor["migration"].get("excluded_elements", []))
    required_excluded = {"competitor product", "competitor logo", "competitor model", "competitor copy"}
    if not required_excluded <= excluded:
        errors.append("competitor-page-m3: protected competitor elements are not fully excluded")

    remap = cases_by_id["taobao-to-amazon-remap"]["migration"]
    if remap.get("copied_source_constraints") is not False:
        errors.append("taobao-to-amazon-remap: source constraints must not be copied")
    mappings = remap.get("module_mapping", [])
    native_units = remap.get("platform_native_units", [])
    slots = {mapping.get("target_slot") for mapping in mappings}
    if not {"Amazon Main Image", "Amazon secondary image", "Amazon A+ module"} <= slots:
        errors.append("taobao-to-amazon-remap: target Amazon slot coverage is incomplete")
    if not all(mapping.get("platform_override") for mapping in mappings):
        errors.append("taobao-to-amazon-remap: every target unit needs a platform override")
    if not native_units or any("source_module_id" in unit for unit in native_units):
        errors.append("taobao-to-amazon-remap: platform-native units must remain outside source mappings")
    main = next((mapping for mapping in mappings if mapping.get("target_slot") == "Amazon Main Image"), {})
    if main.get("handling_mode") != "F0":
        errors.append("taobao-to-amazon-remap: Amazon Main Image must use F0 in the fixture")

    gate = cases_by_id["direction-approval-gate"]["migration"]
    directions = gate.get("migration_directions", [])
    if gate.get("approval_status") != "pending" or gate.get("formal_prompt_allowed") is not False:
        errors.append("direction-approval-gate: pending approval must block formal prompts")
    if len(directions) != 3:
        errors.append("direction-approval-gate: exactly three directions are required")
    for left, right in combinations(directions, 2):
        difference = sum(left.get(field) != right.get(field) for field in DIRECTION_FIELDS)
        if difference < 3:
            errors.append(
                f"direction-approval-gate: {left.get('id')} and {right.get('id')} differ in only {difference} dimensions"
            )


def main() -> int:
    errors: list[str] = []
    validate_contract(errors)
    data = yaml.safe_load(CASES.read_text(encoding="utf-8-sig")) or {}
    if data.get("version") != 1:
        errors.append("reference migration cases version must be 1")
    cases = data.get("cases", [])
    evidence_registry = data.get("target_sku_evidence", {})
    if not isinstance(evidence_registry, dict) or not evidence_registry:
        errors.append("reference migration cases require a target_sku_evidence registry")
    cases_by_id = {case.get("id"): case for case in cases if isinstance(case, dict)}
    expected_ids = {
        "authorized-page-m2",
        "competitor-page-m3",
        "taobao-to-amazon-remap",
        "direction-approval-gate",
    }
    if set(cases_by_id) != expected_ids:
        errors.append(
            f"reference migration case ids mismatch: missing={sorted(expected_ids - set(cases_by_id))}, "
            f"extra={sorted(set(cases_by_id) - expected_ids)}"
        )
    for case in cases_by_id.values():
        validate_case_structure(case, evidence_registry, errors)
    if expected_ids <= set(cases_by_id):
        validate_semantics(cases_by_id, errors)

    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1
    print("[PASS] reference migration contract is wired through Skill, Agent, router, schema, production, and platforms")
    print("[PASS] M1/M2/M3 rights, evidence binding, cross-platform remap, and direction gate fixtures are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
