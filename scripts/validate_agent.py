#!/usr/bin/env python3
"""Validate the KeRo SKU custom agent and its behavioral contract."""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
AGENT_FILE = ROOT / ".codex" / "agents" / "kero-sku-director.toml"
CASES_FILE = ROOT / "tests" / "agent_cases.yaml"
INSTALLER_FILE = ROOT / "scripts" / "install_kero_sku.ps1"
EXPECTED_SKILLS = (
    "sku-detail-page-director",
    "sku-product-core",
    "sku-taobao",
    "sku-tmall",
    "sku-pinduoduo",
    "sku-jd",
    "sku-1688",
    "sku-amazon",
    "sku-shopify",
    "sku-tiktok-shop",
)
REQUIRED_INSTRUCTION_MARKERS = (
    "SKU_CONTEXT",
    "方向确认",
    "不得编造",
    "缺失",
    "用户指定的项目目录",
)
REQUIRED_CASE_MARKERS = {
    "unknown-marketplace": ("SKU_CONTEXT", "sku-detail-page-director", "方向确认前"),
    "known-amazon-without-context": ("sku-product-core", "sku-amazon", "编造"),
    "reuse-confirmed-context": ("复用已确认事实", "重新提交全部资料"),
    "direction-approval-gate": ("等待用户确认方向", "正式逐素材生产 Prompt"),
    "missing-platform-skill": ("缺失的 Skill 名称", "模拟不存在的完整平台规则"),
    "multi-marketplace-routing": ("共享基础 SKU_CONTEXT", "独立目标上下文", "通用详情页"),
    "project-file-isolation": ("用户指定项目目录", "原始产品素材", "Agent 安装目录"),
}


def skill_path(name: str) -> Path:
    if name == "sku-detail-page-director":
        return ROOT / "SKU详情页导演Skill" / name / "SKILL.md"
    return ROOT / "skills" / name / "SKILL.md"


def validate_agent(errors: list[str]) -> None:
    if not AGENT_FILE.is_file():
        errors.append(f"missing agent file: {AGENT_FILE.relative_to(ROOT)}")
        return

    try:
        data = tomllib.loads(AGENT_FILE.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        errors.append(f"invalid agent TOML: {exc}")
        return

    required_keys = {"name", "description", "developer_instructions"}
    missing = required_keys - set(data)
    if missing:
        errors.append(f"agent is missing required keys: {sorted(missing)}")

    name = data.get("name")
    if name != "kero-sku-director":
        errors.append(f"unexpected agent name: {name!r}")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append(f"invalid agent name format: {name!r}")

    description = data.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append("agent description is empty")

    instructions = data.get("developer_instructions")
    if not isinstance(instructions, str) or not instructions.strip():
        errors.append("agent developer_instructions are empty")
        return

    for skill in EXPECTED_SKILLS:
        if f"${skill}" not in instructions:
            errors.append(f"agent instructions do not mention ${skill}")
    for marker in REQUIRED_INSTRUCTION_MARKERS:
        if marker not in instructions:
            errors.append(f"agent instructions are missing marker: {marker!r}")


def validate_dependencies(errors: list[str]) -> None:
    for skill in EXPECTED_SKILLS:
        path = skill_path(skill)
        if not path.is_file():
            errors.append(f"missing Skill dependency: {path.relative_to(ROOT)}")


def validate_cases(errors: list[str]) -> None:
    if not CASES_FILE.is_file():
        errors.append(f"missing behavioral contract: {CASES_FILE.relative_to(ROOT)}")
        return

    try:
        data = yaml.safe_load(CASES_FILE.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        errors.append(f"invalid agent cases YAML: {exc}")
        return

    if not isinstance(data, dict):
        errors.append("agent cases root must be a mapping")
        return
    if data.get("version") != 1:
        errors.append("agent cases version must be 1")
    if data.get("agent") != "kero-sku-director":
        errors.append("agent cases target must be kero-sku-director")
    if tuple(data.get("required_skill_dependencies", ())) != EXPECTED_SKILLS:
        errors.append("agent cases Skill dependency list is incomplete or out of order")

    cases = data.get("cases")
    if not isinstance(cases, list) or len(cases) < 7:
        errors.append("agent cases must define at least seven scenarios")
        return

    ids: set[str] = set()
    cases_by_id: dict[str, dict] = {}
    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            errors.append(f"agent case {index} must be a mapping")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"agent case {index} has no id")
        elif case_id in ids:
            errors.append(f"duplicate agent case id: {case_id}")
        else:
            ids.add(case_id)
            cases_by_id[case_id] = case
        if not isinstance(case.get("input"), str) or not case["input"].strip():
            errors.append(f"agent case {case_id or index} has no input")
        expected = case.get("expected")
        if not isinstance(expected, dict):
            errors.append(f"agent case {case_id or index} has no expected mapping")
            continue
        for key in ("must", "must_not"):
            values = expected.get(key)
            if not isinstance(values, list) or not values or not all(
                isinstance(value, str) and value.strip() for value in values
            ):
                errors.append(f"agent case {case_id or index} has invalid expected.{key}")

    required_ids = set(REQUIRED_CASE_MARKERS)
    if ids != required_ids:
        errors.append(
            "agent case ids do not match the required behavior set: "
            f"missing={sorted(required_ids - ids)}, extra={sorted(ids - required_ids)}"
        )

    for case_id, markers in REQUIRED_CASE_MARKERS.items():
        case = cases_by_id.get(case_id)
        if not case:
            continue
        expected = case.get("expected", {})
        statements = [
            value
            for key in ("must", "must_not")
            for value in expected.get(key, [])
            if isinstance(value, str)
        ]
        contract_text = "\n".join(statements)
        for marker in markers:
            if marker not in contract_text:
                errors.append(f"agent case {case_id} is missing required semantic marker: {marker!r}")


def validate_installer(errors: list[str]) -> None:
    if not INSTALLER_FILE.is_file():
        errors.append(f"missing installer: {INSTALLER_FILE.relative_to(ROOT)}")
        return
    text = INSTALLER_FILE.read_text(encoding="utf-8-sig")
    if "kero-sku-director.toml" not in text:
        errors.append("installer does not install kero-sku-director.toml")
    for skill in EXPECTED_SKILLS:
        if f'"{skill}"' not in text:
            errors.append(f"installer does not declare Skill dependency: {skill}")


def main() -> int:
    errors: list[str] = []
    validate_agent(errors)
    validate_dependencies(errors)
    validate_cases(errors)
    validate_installer(errors)

    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1

    print("[PASS] custom agent TOML contains the required identity and orchestration rules")
    print("[PASS] all ten Skill dependencies exist and are explicitly declared")
    print("[PASS] behavioral contract covers routing, approval, recovery, and file isolation")
    print("[PASS] installer declares the Agent and all Skill dependencies")
    return 0


if __name__ == "__main__":
    sys.exit(main())
