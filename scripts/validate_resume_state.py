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


def resolve_workflow(workflow: dict[str, Any], label: str) -> str:
    current_stage = workflow.get("current_stage")
    resume_from = workflow.get("resume_from")
    if not isinstance(current_stage, str) or not current_stage.strip():
        raise ValueError(f"{label}.current_stage must be a non-empty string")
    if resume_from is not None and (not isinstance(resume_from, str) or not resume_from.strip()):
        raise ValueError(f"{label}.resume_from must be null or a non-empty string")
    completed_stages = workflow.get("completed_stages", [])
    if not isinstance(completed_stages, list) or not all(isinstance(item, str) for item in completed_stages):
        raise ValueError(f"{label}.completed_stages must be a string list")
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
        by_id[context_id] = context
    if active_id not in by_id:
        raise ValueError("active_platform_context_id does not match a persisted platform context")

    active = by_id[active_id]
    direction_state = active.get("direction_state", {})
    if not isinstance(direction_state, dict):
        raise ValueError(f"platform context {active_id} has invalid direction_state")
    return active["workflow_state"], active_id, direction_state.get("selected_direction")


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

    active_workflow, active_id, selected_direction = select_active_workflow(canonical, global_workflow)
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
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"[FAIL] {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
