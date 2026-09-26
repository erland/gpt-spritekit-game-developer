#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]

def main() -> int:
    errors=[]
    status=yaml.safe_load((ROOT/"migration-status-1.5.yaml").read_text(encoding="utf-8"))
    project=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
    registry=yaml.safe_load((ROOT/"runtime-distribution-registry.yaml").read_text(encoding="utf-8"))
    canonical=(ROOT/project["instructions"]["canonical"]).read_bytes()
    legacy=(ROOT/project["instructions"]["legacy_source"]).read_bytes()
    text=canonical.decode("utf-8")
    version=(ROOT/"VERSION").read_text(encoding="utf-8").strip()
    readme=(ROOT/"README.md").read_text(encoding="utf-8")

    progress=status.get("progress",{})
    if progress.get("last_completed_step")!=7:
        errors.append("migration last_completed_step must be 7")
    if progress.get("completed_steps")!=list(range(1,8)):
        errors.append("migration completed_steps must be exactly 1..7")
    if status.get("final_readiness",{}).get("migration_steps_complete")!=7:
        errors.append("final readiness must declare 7/7")
    if canonical!=legacy:
        errors.append("canonical instruction diverges from legacy instruction")
    if version!="1.0.0":
        errors.append(f"VERSION changed: {version!r}")
    if len(text)>8000:
        errors.append(f"canonical instruction exceeds 8000 characters: {len(text)}")

    actual=sorted(p.name for p in (ROOT/"knowledge").glob("*.md"))
    if len(actual)!=16:
        errors.append(f"expected exactly 16 Knowledge files, found {len(actual)}")

    if registry.get("active_targets")!=["chat","custom-gpt"]:
        errors.append(f"unexpected active targets: {registry.get('active_targets')}")
    for name in ("claude","opencode","openai_plugin"):
        if name not in registry.get("inactive_targets",{}):
            errors.append(f"missing inactive runtime decision: {name}")

    critical=[
        "tvOS är produktplattform",
        "macOS är officiell utvecklings- och testplattform",
        "Den senaste kompletta åtkomliga projektzippen är sanningskällan.",
        "Säkerhetsgranska arkivvägar mot zip-slip/path traversal",
        "ändra aldrig originalarkivet",
        "Påstå aldrig att något är byggt, testat eller verifierat om det inte är det.",
        "workflowt måste verifieras i en faktisk Actions-körning.",
    ]
    for marker in critical:
        if marker not in text:
            errors.append(f"canonical behavior marker missing: {marker}")

    if "7/7 komplett" not in readme:
        errors.append("README does not state completed GPT Builder 1.5 migration")

    if errors:
        print("GPT BUILDER 1.5 MIGRATION: FAIL")
        for e in errors: print("-",e)
        return 1

    print("GPT BUILDER 1.5 MIGRATION: PASS")
    print("7/7 complete; VERSION 1.0.0; 16 Knowledge; zip safety/SpriteKit/tvOS/testing/CI behavior preserved")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
