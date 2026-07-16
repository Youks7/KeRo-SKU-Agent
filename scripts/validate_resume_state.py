#!/usr/bin/env python3
"""Validate and resolve the single-source resume contract for a SKU project."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTEXT_DIR = ROOT / "tests" / "resume"
FALLBACK_CONTEXT_DIR = DEFAULT_CONTEXT_DIR / "no-explicit-resume"
MULTI_PLATFORM_CONTEXT_DIR = DEFAULT_CONTEXT_DIR / "multi-platform"
DIRECTION_GATE_CONTEXT_DIR = DEFAULT_CONTEXT_DIR / "direction-gate"
REFERENCE_MIGRATION_CONTEXT_DIR = DEFAULT_CONTEXT_DIR / "reference-migration"
STAGE_ORDER = (
    "intake",
    "product_core",
    "reference_analysis",
    "platform_planning",
    "directions",
    "direction_approval",
    "production",
    "qa",
)


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError(f"{path.name} root must be an object")
    return data


def validate_workflow_vocabulary(workflow: dict[str, Any], label: str) -> None:
    current_stage = workflow.get("current_stage")
    if not isinstance(current_stage, str) or not current_stage.strip():
        raise ValueError(f"{label}.current_stage must be a non-empty string")
    if current_stage not in STAGE_ORDER:
        raise ValueError(f"{label}.current_stage is not in the standard stage vocabulary")
    completed_stages = workflow.get("completed_stages", [])
    if not isinstance(completed_stages, list) or not all(isinstance(item, str) for item in completed_stages):
        raise ValueError(f"{label}.completed_stages must be a string list")
    unknown_completed = set(completed_stages) - set(STAGE_ORDER)
    if unknown_completed:
        raise ValueError(f"{label}.completed_stages contains unknown stages: {sorted(unknown_completed)}")


def resolve_workflow(workflow: dict[str, Any], label: str) -> str:
    validate_workflow_vocabulary(workflow, label)
    current_stage = workflow["current_stage"]
    resume_from = workflow.get("resume_from")
    if resume_from is not None and (not isinstance(resume_from, str) or not resume_from.strip()):
        raise ValueError(f"{label}.resume_from must be null or a non-empty string")
    completed_stages = workflow.get("completed_stages", [])
    completed_stage_set = set(completed_stages)
    next_stage = next((stage for stage in STAGE_ORDER if stage not in completed_stage_set), None)
    if next_stage not in ("production", "qa", None):
        return next_stage

    planned_units = workflow.get("planned_units", [])
    completed_units = workflow.get("completed_units", [])
    if not isinstance(planned_units, list) or not all(isinstance(item, str) for item in planned_units):
        raise ValueError(f"{label}.planned_units must be a string list")
    if not isinstance(completed_units, list) or not all(isinstance(item, str) for item in completed_units):
        raise ValueError(f"{label}.completed_units must be a string list")
    completed_unit_set = set(completed_units)

    if next_stage == "production":
        if resume_from:
            return resume_from
        for unit in planned_units:
            if unit not in completed_unit_set:
                return unit
        return "production"
    if next_stage == "qa":
        unfinished_units = [unit for unit in planned_units if unit not in completed_unit_set]
        if unfinished_units:
            raise ValueError(f"{label} marks production complete with unfinished planned_units")
        return resume_from or "qa"
    if next_stage is None and any(unit not in completed_unit_set for unit in planned_units):
        raise ValueError(f"{label} marks all stages complete with unfinished planned_units")
    if current_stage not in completed_stage_set:
        return current_stage
    return "complete"


def select_active_workflow(
    canonical: dict[str, Any], global_workflow: dict[str, Any]
) -> tuple[dict[str, Any], str | None, Any]:
    contexts = canonical.get("platform_contexts", [])
    if contexts in (None, []):
        selected = canonical.get("creative_context", {}).get("selected_direction")
        return global_workflow, None, selected
    if not isinstance(contexts, list):
        raise ValueError("platform_contexts must be a list")

    active_id = canonical.get("active_platform_context_id")
    if not isinstance(active_id, str) or not active_id:
        raise ValueError("multi-platform state requires active_platform_context_id")
    by_id: dict[str, dict[str, Any]] = {}
    for index, context in enumerate(contexts):
        if not isinstance(context, dict):
            raise ValueError(f"platform_contexts[{index}] must be an object")
        context_id = context.get("context_id")
        if not isinstance(context_id, str) or not context_id:
            raise ValueError(f"platform_contexts[{index}].context_id must be a non-empty string")
        if context_id in by_id:
            raise ValueError(f"duplicate platform context id: {context_id}")
        for field in ("target", "production", "workflow_state", "qa"):
            if not isinstance(context.get(field), dict):
                raise ValueError(f"platform context {context_id} has no {field} object")
        validate_workflow_vocabulary(context["workflow_state"], f"platform context {context_id}.workflow_state")
        by_id[context_id] = context
    if active_id not in by_id:
        raise ValueError("active_platform_context_id does not match a persisted platform context")

    active = by_id[active_id]
    direction_state = active.get("direction_state", {})
    if not isinstance(direction_state, dict):
        raise ValueError(f"platform context {active_id} has invalid direction_state")
    return active["workflow_state"], active_id, direction_state.get("selected_direction")


def collect_target_evidence_ids(canonical: dict[str, Any]) -> set[str]:
    evidence_ids: set[str] = set()
    product_identity = canonical.get("product_identity", {})
    facts = canonical.get("facts", {})
    for value in product_identity.get("source_images", []) if isinstance(product_identity, dict) else []:
        if isinstance(value, str) and value:
            evidence_ids.add(value)
        elif isinstance(value, dict):
            for key in ("id", "image_id", "evidence_id"):
                if isinstance(value.get(key), str) and value[key]:
                    evidence_ids.add(value[key])
    for value in facts.get("evidence_sources", []) if isinstance(facts, dict) else []:
        if isinstance(value, str) and value:
            evidence_ids.add(value)
        elif isinstance(value, dict):
            for key in ("id", "source_id", "evidence_id"):
                if isinstance(value.get(key), str) and value[key]:
                    evidence_ids.add(value[key])
    for value in facts.get("verified", []) if isinstance(facts, dict) else []:
        if isinstance(value, str) and value:
            evidence_ids.add(value)
        elif isinstance(value, dict):
            for key in ("id", "fact_id", "evidence_id"):
                if isinstance(value.get(key), str) and value[key]:
                    evidence_ids.add(value[key])
    for value in facts.get("claim_evidence_map", []) if isinstance(facts, dict) else []:
        if not isinstance(value, dict):
            continue
        for key in ("id", "claim_id", "evidence_id"):
            if isinstance(value.get(key), str) and value[key]:
                evidence_ids.add(value[key])
        nested = value.get("evidence_ids", [])
        if isinstance(nested, list):
            evidence_ids.update(item for item in nested if isinstance(item, str) and item)
    return evidence_ids


def validate_reference_migrations(canonical: dict[str, Any], active_id: str | None) -> None:
    migration_context = canonical.get("reference_migration_context")
    if migration_context in (None, {}):
        return
    if not isinstance(migration_context, dict):
        raise ValueError("reference_migration_context must be an object")
    migrations = migration_context.get("platform_migrations")
    if not isinstance(migrations, list):
        raise ValueError("reference_migration_context.platform_migrations must be a list")
    source = migration_context.get("source", {})
    rights_status = source.get("rights_status") if isinstance(source, dict) else None
    if rights_status not in {"self-owned", "authorized", "competitor-analysis", "unknown"}:
        raise ValueError("reference migration has invalid rights_status")
    evidence_ids = collect_target_evidence_ids(canonical)
    platform_contexts = {
        item.get("context_id"): item
        for item in canonical.get("platform_contexts", [])
        if isinstance(item, dict)
    }
    migration_by_platform: dict[str, dict[str, Any]] = {}
    for index, migration in enumerate(migrations):
        if not isinstance(migration, dict):
            raise ValueError(f"platform_migrations[{index}] must be an object")
        target_id = migration.get("target_platform_context_id")
        if not isinstance(target_id, str) or target_id not in platform_contexts:
            raise ValueError("reference migration target does not match a persisted platform context")
        if target_id in migration_by_platform:
            raise ValueError(f"duplicate reference migration target: {target_id}")
        migration_by_platform[target_id] = migration

        migration_mode = migration.get("migration_mode")
        if migration_mode not in {"M1", "M2", "M3"}:
            raise ValueError("reference migration has invalid M1/M2/M3 mode")
        if rights_status in {"competitor-analysis", "unknown"} and migration_mode == "M2":
            raise ValueError(f"M2 is forbidden for rights_status={rights_status}")

        mappings = migration.get("module_mapping")
        if not isinstance(mappings, list):
            raise ValueError("reference migration module_mapping must be a list")
        for mapping_index, mapping in enumerate(mappings):
            if not isinstance(mapping, dict):
                raise ValueError(f"module_mapping[{mapping_index}] must be an object")
            action = mapping.get("action")
            if action not in {"keep", "adapt", "replace", "discard"}:
                raise ValueError("reference migration has invalid mapping action")
            if action == "discard":
                continue
            if mapping.get("handling_mode") not in {"F0", "F1", "F2", "F3"}:
                raise ValueError("non-discard mapping requires a valid F0-F3 handling_mode")
            mapping_evidence = mapping.get("target_evidence_ids")
            if not isinstance(mapping_evidence, list) or not all(
                isinstance(value, str) and value for value in mapping_evidence
            ):
                raise ValueError("target_evidence_ids must be a string list")
            if not mapping_evidence and mapping.get("status") != "blocked":
                raise ValueError("non-blocked mapping requires target evidence")
            unknown_evidence = set(mapping_evidence) - evidence_ids
            if unknown_evidence:
                raise ValueError(f"mapping cites unknown target evidence: {sorted(unknown_evidence)}")

        platform = platform_contexts[target_id]
        direction_state = platform.get("direction_state", {})
        overrides = platform.get("creative_context_overrides")
        selected = migration.get("selected_direction")
        approval = migration.get("approval_status")
        platform_stage = platform["workflow_state"].get("current_stage")
        if platform_stage in {"production", "qa"} and approval != "approved":
            raise ValueError("production cannot resume before reference migration approval")
        if approval == "approved":
            if not mappings:
                raise ValueError("approved reference migration requires a non-empty module_mapping")
            if not selected:
                raise ValueError("approved reference migration has no selected_direction")
            if not isinstance(direction_state, dict) or direction_state.get("approval_status") != "approved":
                raise ValueError("approved reference migration conflicts with platform approval status")
            if direction_state.get("selected_direction") != selected:
                raise ValueError("reference migration direction conflicts with platform direction_state")
            if not isinstance(overrides, dict) or overrides.get("selected_direction") != selected:
                raise ValueError("reference migration direction conflicts with creative_context_overrides")

    if active_id is not None and active_id not in migration_by_platform:
        raise ValueError("active platform has no persisted reference migration")


def resolve_resume(context_dir: Path) -> tuple[str, list[str]]:
    canonical_path = context_dir / "SKU_CONTEXT.json"
    if not canonical_path.is_file():
        raise ValueError("missing authoritative SKU_CONTEXT.json")

    canonical = load_json(canonical_path)
    if canonical.get("sku_context_version") != 2:
        raise ValueError("SKU_CONTEXT.json must use sku_context_version 2")
    global_workflow = canonical.get("workflow_state")
    if not isinstance(global_workflow, dict):
        raise ValueError("SKU_CONTEXT.json has no workflow_state object")
    revision = global_workflow.get("state_revision")
    if not isinstance(revision, int) or isinstance(revision, bool) or revision < 1:
        raise ValueError("workflow_state.state_revision must be a positive integer")
    validate_workflow_vocabulary(global_workflow, "global workflow_state")

    active_workflow, active_id, selected_direction = select_active_workflow(canonical, global_workflow)
    validate_reference_migrations(canonical, active_id)
    resume_point = resolve_workflow(active_workflow, "active workflow_state")
    current_stage = active_workflow.get("current_stage")

    warnings: list[str] = []
    index_path = context_dir / "project-state.json"
    if index_path.is_file():
        index = load_json(index_path)
        index_revision = index.get("state_revision")
        if not isinstance(index_revision, int) or isinstance(index_revision, bool):
            raise ValueError("project-state.json state_revision must be an integer")
        if index_revision > revision:
            raise ValueError("project-state.json is ahead of authoritative SKU_CONTEXT.json")
        if index_revision < revision:
            warnings.append("ignored stale project-state.json")
        else:
            if index.get("current_stage") != current_stage:
                raise ValueError("same-revision project-state.json conflicts with current_stage")
            if index.get("selected_direction") != selected_direction:
                raise ValueError("same-revision project-state.json conflicts with selected_direction")
            if index.get("active_platform_context_id") != active_id:
                raise ValueError("same-revision project-state.json conflicts with active platform context")

    return resume_point, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "context_dir",
        nargs="?",
        type=Path,
        default=DEFAULT_CONTEXT_DIR,
        help="Directory containing authoritative SKU_CONTEXT.json and optional project-state.json",
    )
    args = parser.parse_args()
    requested = args.context_dir.resolve()
    cases: list[tuple[Path, str | None]] = [(requested, None)]
    if requested == DEFAULT_CONTEXT_DIR.resolve():
        cases = [
            (DEFAULT_CONTEXT_DIR, "taobao-detail-02"),
            (FALLBACK_CONTEXT_DIR, "taobao-detail-02"),
            (MULTI_PLATFORM_CONTEXT_DIR, "amazon-a-plus-02"),
            (DIRECTION_GATE_CONTEXT_DIR, "direction_approval"),
            (REFERENCE_MIGRATION_CONTEXT_DIR, "amazon-secondary-02"),
        ]

    try:
        for context_dir, expected in cases:
            resume_point, warnings = resolve_resume(context_dir.resolve())
            if expected is not None and resume_point != expected:
                raise ValueError(
                    f"{context_dir.name}: expected resume point {expected!r}, got {resume_point!r}"
                )
            for warning in warnings:
                print(f"[WARN] {context_dir.name}: {warning}")
            print(f"[PASS] {context_dir.name}: authoritative state resolved resume_from={resume_point}")
        if requested == DEFAULT_CONTEXT_DIR.resolve():
            gate_fixture = load_json(REFERENCE_MIGRATION_CONTEXT_DIR / "SKU_CONTEXT.json")
            gate_fixture["platform_contexts"][0]["direction_state"]["approval_status"] = "pending"
            try:
                validate_reference_migrations(gate_fixture, "amazon-us")
            except ValueError as exc:
                if "platform approval status" not in str(exc):
                    raise
                print("[PASS] reference-migration: pending platform approval cannot resume production")
            else:
                raise ValueError("pending platform approval was accepted for production")
            rights_fixture = load_json(REFERENCE_MIGRATION_CONTEXT_DIR / "SKU_CONTEXT.json")
            rights_fixture["reference_migration_context"]["platform_migrations"][0]["migration_mode"] = "M2"
            try:
                validate_reference_migrations(rights_fixture, "amazon-us")
            except ValueError as exc:
                if "M2 is forbidden" not in str(exc):
                    raise
                print("[PASS] reference-migration: competitor M2 cannot resume production")
            else:
                raise ValueError("competitor M2 was accepted for production")
            evidence_fixture = load_json(REFERENCE_MIGRATION_CONTEXT_DIR / "SKU_CONTEXT.json")
            evidence_fixture["reference_migration_context"]["platform_migrations"][0]["module_mapping"][0]["target_evidence_ids"] = ["FAKE-EVIDENCE"]
            try:
                validate_reference_migrations(evidence_fixture, "amazon-us")
            except ValueError as exc:
                if "unknown target evidence" not in str(exc):
                    raise
                print("[PASS] reference-migration: invented evidence ids cannot resume production")
            else:
                raise ValueError("invented target evidence was accepted for production")
            verified_fact_fixture = load_json(REFERENCE_MIGRATION_CONTEXT_DIR / "SKU_CONTEXT.json")
            verified_fact_fixture["reference_migration_context"]["platform_migrations"][0]["module_mapping"][0]["target_evidence_ids"] = ["FACT-COLOR"]
            validate_reference_migrations(verified_fact_fixture, "amazon-us")
            print("[PASS] reference-migration: verified fact ids can bind target modules")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"[FAIL] {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
