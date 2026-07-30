# Changelog

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

## 0.7.0 — [PLAN2 Prompt 7]

### Tillagt

- `knowledge/08-GAME-ART-AND-ASSET-PIPELINE.md`
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
