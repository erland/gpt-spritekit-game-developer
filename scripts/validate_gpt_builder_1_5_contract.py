#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]

def main() -> int:
    errors=[]
    contract=yaml.safe_load((ROOT/"gpt-builder-1.5-contract.yaml").read_text(encoding="utf-8"))
    project=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
    canonical=(ROOT/project["instructions"]["canonical"]).read_bytes()
    legacy=(ROOT/project["instructions"]["legacy_source"]).read_bytes()
    text=canonical.decode("utf-8")
    version=(ROOT/"VERSION").read_text(encoding="utf-8").strip()

    if contract["builder"]["target_version"]!="1.5.0":
        errors.append("target builder version must be 1.5.0")
    if contract["builder"]["behavior_preserving"] is not True:
        errors.append("migration must remain behavior-preserving")
    if canonical!=legacy:
        errors.append("canonical instruction diverges from legacy instruction")
    if version!="1.0.0":
        errors.append(f"VERSION changed during migration: {version!r}")

    knowledge=list((ROOT/"knowledge").glob("*.md"))
    if len(knowledge)!=16:
        errors.append(f"expected exactly 16 Knowledge files, found {len(knowledge)}")

    markers=[
        "tvOS är produktplattform",
        "macOS är officiell utvecklings- och testplattform",
        "Den senaste kompletta åtkomliga projektzippen är sanningskällan.",
        "Säkerhetsgranska arkivvägar mot zip-slip/path traversal",
        "ändra aldrig originalarkivet",
        "Påstå aldrig att något är byggt, testat eller verifierat om det inte är det.",
        "workflowt måste verifieras i en faktisk Actions-körning.",
    ]
    for marker in markers:
        if marker not in text:
            errors.append(f"canonical instruction missing behavior marker: {marker}")

    b=contract["behavior"]
    required_true=[
        "tvos_is_product_platform",
        "macos_is_official_dev_test_platform",
        "controller_without_touch_mouse_keyboard_required",
        "tv_distance_readability_required",
        "zip_slip_path_traversal_review_required",
        "work_in_separate_folder",
        "never_modify_original_archive",
        "distinguish_executed_tests_from_static_and_manual_checks",
        "never_claim_tested_if_not_tested",
        "ci_requires_actual_workflow_verification",
    ]
    for key in required_true:
        if b.get(key) is not True:
            errors.append(f"{key} must be true")

    if errors:
        print("GPT BUILDER 1.5 CONTRACT: FAIL")
        for e in errors: print("-",e)
        return 1
    print("GPT BUILDER 1.5 CONTRACT: PASS")
    print("VERSION 1.0.0; 16 Knowledge; zip safety/SpriteKit/tvOS/assets/testing/CI behavior preserved")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
