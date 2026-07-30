# T05B Practical Test Refinement

## Basis

Two generated T05B images were reviewed. Both established a coherent isometric science-fiction style, but neither image alone proved that it was a deterministic, programmatically sliceable tile sheet. The sheets mixed ground tiles, props, multi-tile structures, interactive objects, effects, and signage. Apparent size differences could represent either intentional multi-tile footprints or visual overflow, but this was not documented.

## Changes

- Added explicit gameplay-geometry classifications.
- Distinguished canvas size, logical footprint, visual bounds, anchor point, and visual overflow.
- Required footprints such as `1x1`, `1x2`, `2x1`, or `2x2` for multi-tile content.
- Required a machine-readable manifest or deterministic cell map.
- Required incompatible asset categories to be exported separately.
- Prohibited headings, captions, row separators, guides, and presentation decoration in the technical PNG.
- Clarified that generated imagery must be marked `Not verified` for exact slicing until the actual file is measured or deterministically post-processed.
- Added localization guidance for embedded signage.

## Result

T05B now tests the complete prototype asset delivery rather than aesthetic image quality alone. A visually coherent sheet may still pass as a visual Prototype Asset, but it cannot pass as programmatically sliceable without layout metadata and validation.
