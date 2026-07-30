# Instruktionskomprimering — 1.0.0-rc3

## Resultat

`config/FINAL-INSTRUCTIONS.md` har kortats från 10 635 till 7 707 Unicode-tecken.

- Gräns: 8 000 tecken
- Aktuell längd: 7 707 tecken
- Marginal: 293 tecken
- Knowledge-filer: 16 av 20

Teckenlängden mäts som antal Unicode-tecken i filinnehållet, motsvarande `len(text)` efter UTF-8-avkodning. Byteantalet är högre eftersom svenska tecken använder flera UTF-8-byte.

## Metod

Komprimeringen har gjorts genom att:

- ta bort upprepade procedurdetaljer ur huvudinstruktionen,
- behålla alla styrande prioriteringar, säkerhetsregler och obligatoriska beteenden,
- låta knowledge-filerna äga detaljerade checklistor och arbetsflöden,
- slå samman närliggande regler utan att ändra deras innebörd.

Ingen knowledge-fil behövde läggas till. De 16 befintliga filerna täcker redan det material som flyttats eller kondenserats.

## Täckningskontroll

| Område | Kvar i huvudinstruktionen | Detaljerad knowledge-fil |
|---|---|---|
| Roll och användarnivå | Ja | `01-GPT-ROLE-AND-PRINCIPLES.md` |
| Speldesign och scope | Ja | `02-GAME-DESIGN-FOUNDATIONS.md` + genreprofiler |
| Inspirationsspel | Ja | `03-INSPIRATION-AND-DIFFERENTIATION.md` |
| SpriteKit-arkitektur | Ja | `04-TVOS-SPRITEKIT-ARCHITECTURE.md` |
| Controller och TV-UX | Ja | `05-CONTROLLER-AND-TV-UX.md` |
| Zip-säkerhet och releaseflöde | Ja | `06-PROJECT-ZIP-WORKFLOW.md` |
| Testredovisning | Ja | `07-TESTING-AND-RELEASE.md` |
| Grafik och bildgenerering | Ja | `08-GAME-ART-AND-ASSET-PIPELINE.md` |
| Genrespecifika råd | Routingregel | `09`–`15-GENRE-*.md` |
| Git, `.gitignore` och CI | Ja | `16-VERSION-CONTROL-AND-CI.md` |

## Bedömning

Funktionaliteten har inte avsiktligt minskats. Huvudinstruktionen innehåller fortfarande de regler som måste styra GPT:n i varje konversation. Knowledge-filerna innehåller den detaljerade tillämpningen. Faktisk beteendeekvivalens ska slutligen kontrolleras med T01–T15 i GPT Preview.
