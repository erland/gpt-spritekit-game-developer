# Projektstatus

## Projekt

Skapa GPT:n **SpriteKit Game Designer & Developer** enligt `[PLAN]`, `[PLAN2]` och grafikförbättringsplanen `[PLAN3]`.

## Aktuell version

`1.0.0-rc12`

## Aktuell fas

Prompt 15 är genomförd som releasekandidat. Grafikansvaret har därefter renodlats i rc12. Git/CI-stöd är tillagt och huvudinstruktionen är fortsatt under Buildergränsen och innehåller nu en explicit styrregel för tekniska asset sheets. Projektet är ännu inte fullt externt verifierat. `[PLAN3 Prompt 1–4]` are implemented. T05B has also been refined after practical image-generation testing, and its core classification and verification rule is now enforced directly by the main instruction as well as the knowledge base.

## Genomfört

- Prompt 1–14: genomförda enligt `PLAN2.md`.
- Prompt 15:
  - åtgärdat P1-01 och P1-02 i huvudinstruktionen,
  - aktualiserat dokumenthygien och status,
  - normaliserat changelog,
  - märkt historiska dokument,
  - skapat installations- och extern verifieringsguide,
  - paketerat och integritetstestat releasekandidat.

## Git/CI-tillägg

- Ny kunskapsfil `16-VERSION-CONTROL-AND-CI.md`.
- Projektspecifik `.gitignore`.
- Delade macOS- och tvOS-schemes.
- GitHub Actions för macOS XCTest och tvOS Simulator-build.
- Faktisk Actions-körning återstår.

## Instruktions- och knowledge-budget

- Huvudinstruktion: 7 846 av 8 000 Unicode-tecken.
- Knowledge-filer: 16 av 20.
- Detaljer: `prompt-17/INSTRUCTION-COMPACTION-REPORT.md`.

## Kvarstående extern verifiering

- GPT Preview T01–T04, T05A–T05E och T06–T15.
- Xcode-build för macOS och tvOS.
- XCTest.
- Controllerprovning.
- Fysisk Apple TV-testning och TV-läsbarhet.

## Nästa beslut

Efter extern verifiering:

- skapa `1.0.0` om testerna godkänns utan nödvändiga ändringar, eller
- skapa en ny releasekandidat efter korrigeringar.

## Statusmarkering

- `[PLAN2 Prompt 1–14 KLARA]`
- `[PLAN2 Prompt 15 KLAR SOM RELEASEKANDIDAT]`
- `[EXTERN VERIFIERING ÅTERSTÅR]`

## PLAN3

- `PLAN3.md` definierar en produktionssäker grafik- och assetpipeline.
- `[PLAN3 Prompt 1–4]` are implemented.
- T05B has been refined based on practical Preview output.


## PLAN3 Prompt 1

- Fyra mognadsnivåer har införts.
- Assettyp och mognadsnivå dokumenteras separat.
- Presentationsark skiljs uttryckligen från rena tekniska sheets.
- Teknisk assetspecifikation har utökats, inklusive isometriska krav.
- Huvudinstruktion och antal knowledge-filer är oförändrade.


## PLAN3 Prompt 2

- Infört explicit valideringsstatus där `Inte verifierad` aldrig räknas som godkänd.
- Definierat minsta valideringsområden och krav på angiven kontrollmetod.
- Definierat Production Artifact Package med output, manifest, integration och rapport.
- Infört reproducerbar programmatisk efterbearbetning för grid, alfa, canvas och exportsheets.
- Utökat SpriteKit-integrationen med target membership, atlas, anchor point, manifest och scenverifiering.
- Huvudinstruktion och antal knowledge-filer är oförändrade.


## PLAN3 Prompt 3

- Ursprungliga T05 har ersatts av fem separata tester: T05A–T05E.
- Varje grafiktest har positiva förväntningar och automatiska underkännandekriterier.
- Design Sheet, Prototype Tile Sheet, validering, Production Candidate Package och SpriteKit-integration provas separat.
- Ett presentationsark får inte godkännas som rent tileset, texture atlas eller Production Ready.
- Testpaketet innehåller nu 20 testfall, varav 13 är kritiska.

## Language consistency

- Chat language follows the user.
- Code, comments, identifiers, tests and technical documentation use English.
- Explicitly requested in-game text may be Swedish or another language and should remain localizable.

## T05B practical-test refinement

- A visual asset collection is no longer accepted as a programmatically sliceable tile sheet by appearance alone.
- Ground tiles, wall/edge tiles, multi-tile structures, props, interactive objects, animated effects, and signage must be classified.
- Canvas size, logical footprint, anchor point, and visual overflow are separate required concepts.
- Mixed geometry or animation requirements should result in separate sheets or atlases.
- T05B now requires a machine-readable manifest or deterministic cell map.
- Headings, captions, row separators, guide lines, and other presentation decoration are forbidden in the technical PNG.

## rc12 graphics responsibility split

- The GPT specifies and integrates graphics but is no longer the primary polished-graphics generator.
- Asset Request Package and Asset Delivery Package are the handoff contract.
- T05A–T05E now test planning, handoff, review, placeholders, and integration.
