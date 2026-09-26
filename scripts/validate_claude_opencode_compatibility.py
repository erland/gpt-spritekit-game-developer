#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]

def main() -> int:
    errors=[]
    project=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
    contract=yaml.safe_load((ROOT/"gpt-builder-1.5-contract.yaml").read_text(encoding="utf-8"))
    assessment=(ROOT/"docs/claude-opencode-compatibility.md").read_text(encoding="utf-8")

    claude=project["runtime"]["claude"]
    if claude.get("enabled") is not False: errors.append("claude must remain disabled")
    if claude.get("compatibility")!="reduced": errors.append("claude compatibility must be reduced")
    if claude.get("activation")!="not_active": errors.append("claude activation must be not_active")
    if claude.get("blocker")!="deterministic_project_edit_xcode_test_and_zip_parity_not_guaranteed":
        errors.append("claude blocker mismatch")

    opencode=project["runtime"]["opencode"]
    if opencode.get("enabled") is not False: errors.append("opencode must remain disabled")
    if opencode.get("compatibility")!="equivalent": errors.append("opencode compatibility must be equivalent")
    if opencode.get("activation")!="not_active": errors.append("opencode activation must be not_active")
    if opencode.get("blocker")!="distribution_and_regression_not_implemented":
        errors.append("opencode blocker mismatch")

    for runtime,expected in (("claude","reduced"),("opencode","equivalent")):
        c=contract["runtime_policy"]["inactive"][runtime]
        if c.get("compatibility")!=expected or c.get("activation")!="not_active":
            errors.append(f"{runtime} contract status mismatch")

    for marker in [
        "senaste kompletta projektzip som sanningskälla",
        "säker zip-slip/path traversal-kontroll",
        "faktiskt redigera ett komplett projektträd",
        "Xcode/tvOS build/test",
        "Workspace-, fil- och kodorienteringen matchar kärnflödet väl",
    ]:
        if marker not in assessment:
            errors.append(f"assessment missing marker: {marker}")

    if errors:
        print("CLAUDE/OPENCODE COMPATIBILITY: FAIL")
        for e in errors: print("-",e)
        return 1
    print("CLAUDE/OPENCODE COMPATIBILITY: PASS")
    print("Claude=reduced/not active; OpenCode=equivalent/not active.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
