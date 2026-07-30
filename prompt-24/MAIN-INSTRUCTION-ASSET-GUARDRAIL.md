# Main-instruction asset-sheet guardrail

## Release

`1.0.0-rc11`

## Purpose

The practical T05B run showed that the detailed knowledge rules were not sufficient as the only enforcement layer. This change promotes the essential asset-sheet distinction into the GPT main instruction.

## Added authoritative behavior

The GPT must:

- distinguish tiles, multi-tile structures, props, interactive objects, and effects;
- avoid claiming that an image is grid-sliceable or `Production Ready` unless cell layout, logical footprint, anchor, visual overflow, and manifest data are explicitly defined or verified;
- continue using the detailed validation and packaging workflow in `knowledge/08-GAME-ASSET-REQUIREMENTS-AND-INTEGRATION.md`.

## Scope

This is a behavioral strengthening, not merely a test adjustment. The test suite and knowledge base remain the detailed implementation and verification layers, while `config/FINAL-INSTRUCTIONS.md` is now the global guardrail.

## Static verification

- Final instruction: 7,846 Unicode characters.
- Builder limit: 8,000 characters.
- Remaining margin: 154 characters.
- Knowledge files: 16 of 20.
