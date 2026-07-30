# Graphics responsibility split

## Implemented

The GPT now owns planning, specification, handoff, review, deterministic placeholders, and SpriteKit integration. Polished graphics generation and visual iteration are delegated to a separate Game Graphics Creator.

## Shared contract

The developer GPT produces an Asset Request Package. The graphics GPT returns an Asset Delivery Package. Both use stable English identifiers, machine-readable specifications, explicit maturity levels, and measurable validation criteria.

## Test impact

T05A–T05E now validate the revised responsibility boundary rather than direct image generation.
