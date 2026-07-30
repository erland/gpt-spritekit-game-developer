# [PLAN2] Promptindelning för att skapa GPT:n

## Syfte

Detta dokument delar upp genomförandet av `[PLAN]` i hanterbara arbetsomgångar. Varje prompt ska lämna efter sig konkreta filer som läggs till i samma projektpaket. Paketets senaste zip är sanningskällan för nästa arbetsomgång.

## Arbetsprincip

- När flera steg skapar samma sammanhängande artefakt genomförs de tillsammans.
- Kod, referensprojekt och större kunskapsfiler får egna arbetsomgångar när de behöver granskas eller testas separat.
- Varje prompt uppdaterar minst `PROJECT-STATUS.md` och `CHANGELOG.md`.
- Nya beslut registreras i `DECISIONS.md`.
- Öppna kontrollfrågor registreras i `OPEN-QUESTIONS.md` och blockerar bara arbetet när ett beslut inte rimligen kan senareläggas.

## Prompt 1 — Namn, syfte och avgränsning

Motsvarar `[PLAN]` steg 1–2.

Leveranser:

- arbetsnamn och alternativa namn,
- kort beskrivning för GPT-byggaren,
- målgrupp,
- primärt användningsområde,
- vad GPT:n ska göra,
- vad GPT:n inte ska göra,
- teknik- och plattformsavgränsning,
- första uppsättningen beslut och öppna frågor.

## Prompt 2 — Huvudinstruktion, användarprofil och arbetsprinciper

Motsvarar `[PLAN]` steg 3–5.

Leveranser:

- första kompletta huvudinstruktionen,
- standardprofil för användaren,
- regler för detaljnivå,
- arbetsprinciper för design, kod, filer, tester och releaser.

## Prompt 3 — Kunskapsbasens struktur

Motsvarar inledningen av `[PLAN]` steg 6–11.

Leveranser:

- slutlig lista över kunskapsfiler,
- ansvar och gränser för varje fil,
- gemensam mall,
- beroenden och läsordning,
- kontroll mot överlappning.

## Prompt 4 — Roll, speldesign och inspirationsspel

Skapar:

- `GPT-ROLE-AND-PRINCIPLES.md`,
- `GAME-DESIGN-FOUNDATIONS.md`,
- `INSPIRATION-AND-DIFFERENTIATION.md`.

## Prompt 5 — SpriteKit-arkitektur och tvOS-UX

Skapar:

- `TVOS-SPRITEKIT-ARCHITECTURE.md`,
- `CONTROLLER-AND-TV-UX.md`.

## Prompt 6 — Zip-, test- och releaseflöde

Skapar:

- `PROJECT-ZIP-WORKFLOW.md`,
- `TESTING-AND-RELEASE.md`.

## Prompt 7 — Grafik- och assetpipeline

Skapar:

- `GAME-ART-AND-ASSET-PIPELINE.md`.

Omfattar art direction, assetplanering, bildgenerering, tilesets, sprites, animationer, atlasstruktur och integrering.

## Prompt 8 — Genreprofiler

Skapar konsekvent strukturerade profiler för:

- 2D-plattformsspel,
- shoot 'em up,
- turordningsbaserad strategi,
- top-down-action,
- isometriskt actionäventyr,
- pusselspel,
- lokalt flerspelarspel.

## Prompt 9 — Referensprojektets grund och controllerstöd

Motsvarar `[PLAN]` steg 12–13.

Leveranser:

- minimal tvOS/SpriteKit-projektgrund,
- startscen,
- controllerinput,
- grundläggande projektstruktur.

## Prompt 10 — Scener, paus, spellogik och tester

Motsvarar `[PLAN]` steg 14–15.

Leveranser:

- scenhantering,
- paus och återupptagning,
- testbar logik utanför `SKScene`,
- grundläggande tester.

## Prompt 11 — Referensprojektets dokumentation och granskning

Motsvarar `[PLAN]` steg 16.

Leveranser:

- README,
- teknisk dokumentation,
- manuell testlista,
- referensprojektets releasechecklista,
- arkitekturgranskning.

## Prompt 12 — Komplett GPT-konfigurationsunderlag

Motsvarar `[PLAN]` steg 17–20.

Leveranser:

- slutligt namn,
- beskrivning,
- instruktion,
- lista över kunskapsfiler,
- rekommenderade funktioner,
- samtalsstartare.

## Prompt 13 — Fil- och zip-funktionstest

Motsvarar `[PLAN]` steg 21.

Verifierar att GPT-arbetsflödet kan:

- läsa en zip,
- inventera projektet,
- ändra filer,
- köra möjliga kontroller,
- skapa en ren ny zip,
- lämna en korrekt nedladdningslänk.

## Prompt 14 — Testpaket och preflight

Motsvarar `[PLAN]` steg 22–23.

Leveranser:

- realistiska testprompter,
- förväntat beteende,
- granskningsresultat,
- identifierade brister och risker.

## Prompt 15 — Korrigeringar och version 1.0

Motsvarar `[PLAN]` steg 24–25.

Leveranser:

- korrigerade instruktioner och kunskapsfiler,
- ren version 1.0-zip,
- changelog,
- preflightresultat,
- installations- och användningsanvisningar.

## Prompt 16 — Första verkliga spelprojektet

Motsvarar `[PLAN]` steg 26.

Leveranser:

- val av litet provprojekt,
- designbrief,
- teknisk riskanalys,
- minsta spelbara prototyp,
- första projektzip.

## Prompt 17 och framåt — Verkliga zip-cykler

Motsvarar `[PLAN]` steg 27–28.

Varje arbetsomgång ska normalt innehålla en avgränsad förändring, uppdaterad dokumentation, testredovisning och ny projektzip.

## Senare utvärderingsprompt — Uppdatering och version 2

Motsvarar `[PLAN]` steg 29–30.

Efter tre till fem verkliga arbetscykler:

- analysera förbättringsloggen,
- uppdatera GPT:n,
- avgör vad som hör hemma i version 2,
- avgör om någon del bör brytas ut i en separat GPT.

## Status

- Prompt 1: genomförd.
- Prompt 2: genomförd.
- Prompt 3: genomförd.
- Prompt 4: genomförd.
- Prompt 5: genomförd.
- Prompt 6: genomförd.
- Prompt 7: genomförd.
- Prompt 8: genomförd.
- Prompt 9: genomförd.
- Prompt 10: genomförd.
- Prompt 11: genomförd.
- Prompt 12: genomförd.
- Prompt 13: genomförd.
- Prompt 14: genomförd.
- Prompt 15: genomförd som releasekandidat; extern verifiering återstår före slutlig 1.0.0.

## [TILLÄGG: GIT OCH CI]

Efter Prompt 15 har stöd lagts till för projektspecifik `.gitignore`, delade Xcode-schemes och GitHub Actions. Tillägget paketeras som `1.0.0-rc2` och behöver verifieras genom en faktisk Actions-körning.
