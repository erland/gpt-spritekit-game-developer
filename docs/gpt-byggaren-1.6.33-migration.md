# Migration to GPT Byggaren 1.6.33

Status: **IN PROGRESS — inventory and engine preflight complete; runtime migration not completed**.

## 1. Inventory — completed
- Existing project was migrated to GPT Byggaren 1.5.0; `assistant/instructions.md` is the canonical monolithic instruction.
- Historical `config/FINAL-INSTRUCTIONS.md` is retained byte-identically.
- 16 Knowledge files and `reference-project/` must be preserved, including Swift/SpriteKit/tvOS, controller interaction, macOS tests and asset-handling rules.
- `gpt-project.yaml`, `runtime-distribution-registry.yaml` and CI still describe the old Chat + Custom GPT build.
- Current project version (`VERSION`) must not be changed merely because the build engine is upgraded.

## 2. Project model — pending
- Define common behavior, capabilities, artifact contracts, workspace/state and tool contracts.
- Analyse whether a common core plus independent skills is justified; suggested candidates are *game design*, *SpriteKit/tvOS implementation* and *project verification/delivery*. Keep monolithic instruction until behavioral traceability is reviewed.
- Preserve all original sections in a traceability matrix; never replace the instruction with a heading-only reconstruction.

## 3. Engine — preflight passed, installation in project pending
- Attached official `gpt-byggaren-engine-1.6.33.zip` passed the **original** `scripts/selftest_distribution_engine.py --source .` on 2026-10-30.
- Stages: source 62 files, materialize 62 files, SHA-256 for 62 files, original installer, six-archive smoke build — all passed.
- Adopt a **pinned** 1.6.33 engine dependency, not `latest` or `main`.
- Use only original engine installer/build/validators and do not improvise another packager.

## 4. Five peer distributions — pending
- Targets to assess/build: Chat, OpenAI Plugin, Claude Projects, Claude Skills and OpenCode.
- `custom_gpt` is a legacy format; do not silently treat it as a sixth peer runtime.
- Separate *package validity* from real runtime capability. Host-dependent Xcode, controller or file-editing capabilities must remain documented as host dependencies.
- Retain original ZIP ingest safety, detailed technical instructions and all 16 Knowledge documents.

## 5. Documentation and hygiene — pending
- Align `README.md`, `PROJECT.md`, `STATUS.md`, development plan and migration checklist with actual results.
- Audit superseded `scripts/build_distributions.py`, validators, runtime registry and the 1.5 compatibility files. Remove only after equivalent original-engine validation passes.
- Ensure PR/release workflows use pinned engine and validate output archives. A GitHub Release tag determines release version.

## 6. Final verification — pending
- Run lint, project validators, original-engine build, all five archive checks, resource isolation and migration traceability.
- Check that the reference Swift project stays unchanged, then perform platform-dependent Xcode checks separately on macOS.
- Require a complete project ZIP plus five validated distributions before marking migration complete.

## Verification scope
The engine smoke test proves the supplied motor works, **not** that this repository has been migrated. No claims of five generated SpriteKit distributions or release-readiness are made in this stage.
