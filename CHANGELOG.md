# Changelog

## 1.0.0-rc12 — Graphics responsibility split

- Refocused SpriteKit Game Designer & Developer on asset planning, technical specification, handoff, review, placeholders, and SpriteKit integration.
- Replaced the graphics-generation pipeline knowledge file with `08-GAME-ASSET-REQUIREMENTS-AND-INTEGRATION.md`.
- Added a standardized Asset Request Package and expected Asset Delivery Package contract.
- Removed polished game-graphics generation from the GPT's default responsibility and made image generation optional rather than core.
- Reworked T05A–T05E to test asset planning, handoff, review, placeholders, and integration.
- Added `prompt-25/GRAPHICS-RESPONSIBILITY-SPLIT.md`.

## 1.0.0-rc11 — Main-instruction asset-sheet guardrail

- Added a compact, explicit rule to `config/FINAL-INSTRUCTIONS.md` for classifying tiles, multi-tile structures, props, interactive objects, and effects.
- Prohibited claims that an image is grid-sliceable or `Production Ready` unless cell layout, footprint, anchor, visual overflow, and manifest data are explicitly defined or verified.
- Kept the detailed workflow in `knowledge/08-GAME-ASSET-REQUIREMENTS-AND-INTEGRATION.md` while making the essential behavior globally authoritative.
- Recompacted the instruction to remain below the 8,000-character Builder limit.
- Added `prompt-24/MAIN-INSTRUCTION-ASSET-GUARDRAIL.md`.

## 1.0.0-rc10 — T05B practical asset-sheet refinement

- Refined T05B after reviewing real generated prototype sheets.
- Distinguished Ground Tile, Wall/Edge Tile, Multi-tile Structure, Prop, Interactive Object, Animated Effect, and Signage.
- Separated canvas size, logical footprint, anchor point, visual bounds, and visual overflow.
- Required machine-readable manifests or deterministic cell maps for programmatic slicing.
- Required separate sheets or atlases when geometry, anchor, animation, or slicing rules are incompatible.
- Added explicit failure conditions for mixed unclassified assets and baked-in headings, captions, row separators, or guide lines.
- Clarified that an image alone cannot prove exact grid placement, alpha, dimensions, or slicing reliability.
- Added `prompt-23/T05B-PRACTICAL-TEST-REFINEMENT.md`.

## 1.0.0-rc9 — Technical language and localization boundary

- Enforced English for code, identifiers, code comments, tests and technical project documentation.
- Preserved the user's language for chat responses.
- Allowed explicitly requested Swedish or other localized user-facing game text.
- Added guidance to separate game copy from technical code through localization resources.
- Added regression test T20 for Swedish chat plus English technical artifacts and Swedish in-game strings.
- Reconstructed and incorporated the PLAN3 Prompt 4 instruction gate that was described for rc8.
- Added `prompt-21/PLAN3-PROMPT-4-REPORT.md` and `prompt-22/LANGUAGE-CONSISTENCY-REPORT.md`.

## 1.0.0-rc7 — [PLAN3 Prompt 3]

- Ersatt det breda grafiktestet T05 med fem avgränsade tester T05A–T05E.
- Infört separata tester för Design Sheet, Prototype Tile Sheet, assetvalidering, Production Candidate Package och SpriteKit-integration.
- Lagt till automatiska underkännandekriterier som hindrar presentationsark från att godkännas som rena tilesets.
- Utökat maskinläsbara testfall med `failure_conditions`.
- Uppdaterat testresultatmall, preflightmått och externa verifieringshänvisningar.
- Testpaketet innehåller nu 19 testfall, varav 12 är kritiska.
- Lagt till `prompt-20/PLAN3-PROMPT-3-REPORT.md`.
- Huvudinstruktionen och antalet knowledge-filer är oförändrade.

## 1.0.0-rc6 — [PLAN3 Prompt 2]

- Infört valideringsmodell med fyra uttryckliga statusvärden.
- Klargjort att `Inte verifierad` blockerar klassificering som Production Ready.
- Definierat Production Artifact Package med README, output, manifest, integrationsguide och valideringsrapport.
- Lagt till reproducerbar programmatisk efterbearbetning för canvas, grid, alpha, beskärning och export.
- Utökat SpriteKit-integrationskraven för atlas, target membership, anchor point, animationer och scenverifiering.
- Lagt till regler för assetmanifest, källor och licensstatus.
- Lagt till `prompt-19/PLAN3-PROMPT-2-REPORT.md`.
- Huvudinstruktionen och antalet knowledge-filer är oförändrade.

## 1.0.0-rc5 — [PLAN3 Prompt 1]

- Infört Asset Maturity Model med fyra nivåer i grafik- och assetkunskapen.
- Infört separat Asset Type Classification.
- Definierat presentation kontra teknisk produktion och rena sheet-krav.
- Utökat teknisk assetspecifikation med grid, alpha, pivot, atlas, TV-läsbarhet och isometriska krav.
- Klargjort att `Production Ready` kräver faktisk SpriteKit- och scenverifiering.
- Lagt till `prompt-18/PLAN3-PROMPT-1-REPORT.md`.
- Huvudinstruktionen och antalet knowledge-filer är oförändrade.

## 1.0.0-rc4 — [PLAN3] tillagd

- Lagt till `PLAN3.md` för produktionssäker grafik- och assethantering.
- Definierat fyra mognadsnivåer: Design Sheet, Prototype Asset, Production Candidate och Production Ready.
- Definierat assetklassificering, teknisk assetspecifikation, valideringsmodell och Production Artifact Package.
- Planerat uppdelning av grafiktest T05 i T05A–T05E.
- Planerat genomförandet i fem promptar utan att öka antalet knowledge-filer i detta steg.
- Uppdaterat README och projektstatus.

## 1.0.0-rc3 — Instruktionsgräns och täckningskontroll

- Kortat `config/FINAL-INSTRUCTIONS.md` från 10 635 till 7 707 Unicode-tecken.
- Verifierat att instruktionen ligger under gränsen 8 000 tecken med 293 teckens marginal.
- Behållit 16 knowledge-filer av maximalt 20.
- Flyttat inga styrande regler ur instruktionen; detaljerade procedurer ligger fortsatt i knowledge-filerna.
- Lagt till `prompt-17/INSTRUCTION-COMPACTION-REPORT.md` med täckningsmatris och mätmetod.
- Uppdaterat status och installationsunderlag.

## 1.0.0-rc2 — Git- och CI-stöd

- Lagt till `knowledge/16-VERSION-CONTROL-AND-CI.md`.
- Utökat huvudinstruktionen med projektspecifik `.gitignore` och GitHub Actions.
- Lagt till `.gitignore`, delade Xcode-schemes och CI-workflow i referensprojektet.
- CI kör macOS XCTest och bygger tvOS Simulator utan code signing.
- Dokumenterat secrets, signering, distribution, självhostade runners och kvarstående verifiering.
- Uppdaterat kunskapsmanifestet från 15 till 16 filer.

## 1.0.0-rc1 — [PLAN2 Prompt 15]

- Förstärkte bildgenereringsflödet med obligatorisk teknisk assetspecifikation före generering.
- Lade till eftergranskning av perspektiv, skala, transparens, pivot, tile-skarvar och frame-konsistens.
- Lade till uttryckligt skydd mot zip-slip/path traversal samt krav på separat arbetsmapp och oförändrat originalarkiv.
- Normaliserade versionshistoriken och tog bort dubbla huvudrubriker.
- Märkte äldre Prompt 1–2-dokument som historiska och ersatta.
- Lade till releasekandidatrapport, installationsguide och verifieringschecklista.
- Statisk preflight och zip-integritet är godkända.
- Faktisk GPT Preview, Xcode-build/XCTest, controllerprovning och fysisk Apple TV-test återstår före slutlig 1.0.0.


## 0.14.0 — [PLAN2 Prompt 14]

### Tillagt

- `prompt-14/TEST-PACK.md` med 15 realistiska testfall.
- `prompt-14/TEST-CASES.json` för maskinläsbar regressionstestning.
- `prompt-14/TEST-EXECUTION-RESULTS.md` för Preview-resultat.
- `prompt-14/PREFLIGHT-REPORT.md` med full statisk granskning.
- `prompt-14/PREFLIGHT-METRICS.json`.
- `prompt-14/ISSUE-REGISTER.md` med prioriterade åtgärder inför 1.0.

### Resultat

- Statisk preflight godkänd med åtgärdspunkter.
- Inga P0-blockerare identifierades.
- Preview-, Xcode-, controller- och fysisk Apple TV-verifiering kvarstår.
- Dokumentstatus, slutnamn och nästa steg har korrigerats.

## 0.13.0 — [PLAN2 Prompt 13]

### Tillagt

- Praktiskt fil- och zip-funktionstest.
- Kontrollerad testfixture med input- och outputarkiv.
- Inventering, SHA-256-kontroll och `unzip -t`-resultat.
- `prompt-13/FUNCTION-TEST-REPORT.md` med resultat, bevis och begränsningar.

### Resultat

- Samtliga kontroller i Prompt 13 godkändes.
- Zip-arbetsflödet kan användas i den fortsatta GPT-processen.

## 0.12.0 — [PLAN2 Prompt 12]

### Tillagt

- Slutligt GPT-namn och kort beskrivning.
- Slutredigerad instruktion för GPT-byggaren.
- Manifest för de 15 kunskapsfilerna.
- Rekommenderad funktionskonfiguration.
- Prioriterade samtalsstartare.
- Praktisk builder-checklista.

### Beslut

- Slutligt namn är **SpriteKit Game Designer & Developer**.
- Referensprojektet behålls i builder-paketet men laddas inte som permanent kärnkunskap.
- Webbsökning, Kodtolkare och dataanalys samt bildgenerering ska aktiveras.
- Actions skjuts upp.

## 0.11.0 — [PLAN2 Prompt 11]

- Aktualiserade referensprojektets README.
- Lade till `TECHNICAL-DESIGN.md` med lager, uppdateringsflöde, pausmodell och teststrategi.
- Lade till `ARCHITECTURE-REVIEW.md` med styrkor, begränsningar och rekommendationer.
- Lade till `MANUAL-TEST-PLAN.md` för Xcode, macOS, controller, tvOS-simulator och fysisk Apple TV.
- Lade till `RELEASE-CHECKLIST.md`.
- Lade till `KNOWN-ISSUES.md` med kvarstående verifiering och medvetna begränsningar.
- Godkände projektet som pedagogisk referens, inte som generell spelmotor.
- Markerade Prompt 11 som klar och Prompt 12 som nästa steg.

## 0.10.0 — [PLAN2 Prompt 10]

- Lade till `SceneCoordinator` som central scenskapare.
- Lade till `GameWorld` med testbar rörelse och begränsning utan SpriteKit-beroende.
- Lade till `GameSession` med explicita pausorsaker.
- Lade till pausoverlay för användarpaus, controllerfrånkoppling och inaktiv app.
- Kopplade SwiftUI scene phase till paus och återupptagning.
- Refaktorerade `GameScene` till adapter mellan input, domänmodell och presentation.
- Lade till macOS XCTest-target och grundläggande tester.
- Dokumenterade återstående manuell Xcode-, controller- och Apple TV-verifiering.
- Markerade Prompt 10 som klar och Prompt 11 som nästa steg.

## 0.9.0 — [PLAN2 Prompt 9]

- Lade till ett minimalt Xcode-referensprojekt under `reference-project/`.
- Lade till separata app-targets för tvOS och macOS med delad SpriteKit-kod.
- Lade till `GameScene` med enkel top-down-rörelse och tydlig nodstruktur.
- Lade till semantiskt inputlager med `PlayerIntent` och `InputSource`.
- Lade till polling av vanlig spelkontroll via GameController.
- Lade till radial dead zone, normalisering och flankdetektering för knappar.
- Lade till tangentbordsadapter för macOS som utvecklingshjälp.
- Lade till hantering och diagnostik för controlleranslutning och frånkoppling.
- Dokumenterade vad som kräver manuell byggning och testning i Xcode.
- Markerade Prompt 9 som klar och Prompt 10 som nästa steg.

## 0.8.0 — [PLAN2 Prompt 8]

- Skapat sju konsekvent strukturerade genreprofiler.
- Lagt till genrespecifik vägledning för kärnloop, designrisker, tekniska risker, prototyp, utvecklingsordning, playtest, simulering, tvOS/controller, SpriteKit och assets.
- Genomfört konsistenskontroll mot den gemensamma genreprofilmallen.
- Uppdaterat `PLAN2.md`, `PROJECT-STATUS.md` och `README.md`.

# Changelog

## 1.0.0-rc10 — T05B practical asset-sheet refinement

- Refined T05B after reviewing real generated prototype sheets.
- Distinguished Ground Tile, Wall/Edge Tile, Multi-tile Structure, Prop, Interactive Object, Animated Effect, and Signage.
- Separated canvas size, logical footprint, anchor point, visual bounds, and visual overflow.
- Required machine-readable manifests or deterministic cell maps for programmatic slicing.
- Required separate sheets or atlases when geometry, anchor, animation, or slicing rules are incompatible.
- Added explicit failure conditions for mixed unclassified assets and baked-in headings, captions, row separators, or guide lines.
- Clarified that an image alone cannot prove exact grid placement, alpha, dimensions, or slicing reliability.
- Added `prompt-23/T05B-PRACTICAL-TEST-REFINEMENT.md`.

## 0.7.0 — [PLAN2 Prompt 7]

### Tillagt

- `knowledge/08-GAME-ASSET-REQUIREMENTS-AND-INTEGRATION.md`
  - art direction och prioriterad assetplan,
  - separata pipelines för pixel art och högupplöst 2D,
  - tekniska assetspecifikationer och bildgenereringsflöde,
  - tilesets, isometriska assets, sprites och animationer,
  - UI, bakgrunder, effekter, namngivning och texture atlases,
  - SpriteKit-integration och TV-läsbarhetskontroll,
  - checklistor, vanliga fel och projektdokumentation.

### Ändrat

- Markerade Prompt 7 som genomförd i `PLAN2.md`.
- Uppdaterade `PROJECT-STATUS.md` med Prompt 8 som nästa steg.
- Uppdaterade `README.md` till version 0.7.0.

## 0.6.0 — [PLAN2 Prompt 6]

### Tillagt

- `knowledge/06-PROJECT-ZIP-WORKFLOW.md`
  - inventering och val av sanningskälla,
  - säkert arbete i kopia,
  - avgränsad förändringshantering,
  - städning, versionering och zipverifiering,
  - hantering av saknade och motstridiga projektfiler,
  - kontinuitet mellan zip-baserade arbetsomgångar.
- `knowledge/07-TESTING-AND-RELEASE.md`
  - testpyramid för domänlogik och SpriteKit-integration,
  - macOS-, Xcode-, tvOS- och fysisk Apple TV-verifiering,
  - controller-, TV-, prestanda- och stabilitetstestning,
  - playtesting och releasekriterier,
  - standardiserad och ärlig testredovisning.

### Ändrat

- Markerade Prompt 6 som genomförd i `PLAN2.md`.
- Uppdaterade `PROJECT-STATUS.md` med Prompt 7 som nästa steg.
- Uppdaterade `README.md` till version 0.6.0.

## 0.5.0 — [PLAN2 Prompt 5]

### Tillagt

- `knowledge/04-TVOS-SPRITEKIT-ARCHITECTURE.md`
  - rekommenderade arkitekturlager och nodhierarki,
  - spelloop, tid och uppdateringsordning,
  - testbar spellogik utanför `SKScene`,
  - tillstånd, fysik, rörelse, kamera och animation,
  - lokal sparning och delad kod mellan tvOS och macOS,
  - prestanda och SpriteKit-lämplighetsbedömning.
- `knowledge/05-CONTROLLER-AND-TV-UX.md`
  - semantisk inputmodell, dead zones och knapphantering,
  - menyfokus, paus och controllerfrånkoppling,
  - lokal multiplayer och controllerassignment,
  - TV-läsbarhet, safe areas, feedback och tillgänglighet,
  - controller- och TV-testmatris.

### Ändrat

- Markerade Prompt 5 som genomförd i `PLAN2.md`.
- Uppdaterade `PROJECT-STATUS.md` med Prompt 6 som nästa steg.

## 0.4.0 — [PLAN2 Prompt 4]

### Tillagt

- `knowledge/01-GPT-ROLE-AND-PRINCIPLES.md`
  - kombinerad GPT-roll,
  - kvalitetsmål,
  - prioriterings- och resonemodell,
  - användarprofil och kommunikationsnivå,
  - regler för antaganden och framdrift.
- `knowledge/02-GAME-DESIGN-FOUNDATIONS.md`
  - kärnupplevelse och kärnloop,
  - mål, feedback, progression och svårighetskurva,
  - scope, riskprototyper och vertical slices,
  - balans, simulering och playtesting.
- `knowledge/03-INSPIRATION-AND-DIFFERENTIATION.md`
  - abstrakt referensspelsanalys,
  - differentieringsmetod,
  - likhetsriskkontroll,
  - mall för projektdokumentation.

### Ändrat

- Uppdaterat `PLAN2.md` med genomförd Prompt 4.
- Uppdaterat `PROJECT-STATUS.md` med nästa steg.

## 0.3.0 — 2026-07-29

### Tillagt

- Genomfört `[PLAN2 Prompt 3]`.
- Slutlig struktur för version 1.0:s kunskapsbas.
- Tydligt ansvar och avgränsning för varje kunskapsfil.
- Gemensam mall för kunskapsfiler.
- Gemensam mall för genreprofiler.
- Läsordning och beroenden för olika arbetsfall.
- Regler och kontrollmatris mot överlappande innehåll.

### Beslutat

- Svenska kunskapsfiler med engelska tekniska termer.
- Lokal multiplayer ingår som stöd, inte som krav i referensprojektet.
- Lokal sparning ingår i version 1.0; Game Center och molnsparning senareläggs.
- Både pixel art och högupplöst 2D stöds.
- Referensprojektet blir top-down och isometriskt stöd separeras.

### Uppdaterat

- `DECISIONS.md`, `OPEN-QUESTIONS.md`, `PLAN2.md`, `PROJECT-STATUS.md` och `README.md`.

## 0.2.0 — Prompt 2

- Beslutade Q-003 och registrerade D-008:
  - tvOS är produktplattform,
  - macOS är officiell utvecklings- och testplattform,
  - iOS och iPadOS är frivilliga framtida mål.
- Uppdaterade Prompt 1:s plattformsavgränsning.
- Skapade första kompletta huvudinstruktionen i `prompt-02/MAIN-INSTRUCTIONS.md`.
- Fastställde standardprofilen erfaren programvaruutvecklare med begränsad spelutvecklingserfarenhet.
- Fastställde ingen obligatorisk onboardingintervju.
- Lade till beteenderegler för:
  - genreanalys och prototyper,
  - inspirationsspel och differentiering,
  - SpriteKit-teknikgrind,
  - grafik och assets,
  - tvOS/controllerkrav,
  - zip-baserat arbete,
  - testredovisning,
  - dokumentation och projektkontinuitet.
- Markerade Prompt 3 som nästa arbetsomgång.

## 0.1.0 — Prompt 1

- Lade till ursprunglig `[PLAN]`.
- Skapade `[PLAN2]` med 16 huvudsakliga arbetsomgångar och senare verkliga zip-cykler.
- Fastställde arbetsnamnet **Apple TV 2D Game Studio**.
- Definierade syfte, målgrupp och positionering.
- Definierade primära och exkluderade användningsområden.
- Fastställde Swift, SpriteKit och tvOS som standardspår.
- Fastställde att grafik- och assetstöd ingår i samma GPT.
- Dokumenterade första beslut och öppna kontrollfrågor.
