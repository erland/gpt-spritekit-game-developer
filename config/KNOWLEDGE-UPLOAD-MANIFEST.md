# Manifest för Knowledge-filer

## Kanonisk Knowledge-uppsättning

Ladda upp exakt följande 16 filer från `knowledge/`:

1. `01-GPT-ROLE-AND-PRINCIPLES.md`
2. `02-GAME-DESIGN-FOUNDATIONS.md`
3. `03-INSPIRATION-AND-DIFFERENTIATION.md`
4. `04-TVOS-SPRITEKIT-ARCHITECTURE.md`
5. `05-CONTROLLER-AND-TV-UX.md`
6. `06-PROJECT-ZIP-WORKFLOW.md`
7. `07-TESTING-AND-RELEASE.md`
8. `08-GAME-ASSET-REQUIREMENTS-AND-INTEGRATION.md`
9. `09-GENRE-PLATFORMER.md`
10. `10-GENRE-SHOOT-EM-UP.md`
11. `11-GENRE-TURN-BASED-STRATEGY.md`
12. `12-GENRE-TOP-DOWN-ACTION.md`
13. `13-GENRE-ISOMETRIC-ADVENTURE.md`
14. `14-GENRE-PUZZLE.md`
15. `15-GENRE-LOCAL-MULTIPLAYER.md`
16. `16-VERSION-CONTROL-AND-CI.md`

## Filer som inte ska laddas upp som Knowledge

Repositorymetadata, konfigurationsfiler, buildscript, distributionsmetadata och hela builder-/release-ZIP:ar ska inte laddas upp som permanent GPT Knowledge. De beskriver paketering och installation snarare än stabil ämneskunskap.

## Referensprojektet

`reference-project/` behålls som aktuellt utvecklings- och testunderlag men ska inte laddas upp permanent som GPT Knowledge i version 1.x eftersom:

- de centrala arkitekturprinciperna redan finns i Knowledge-filerna,
- en uppladdad projekt-ZIP i en faktisk konversation ska vara sanningskällan,
- kodexempel riskerar att behandlas som mall även när ett projekt kräver annan struktur.

## Filbudget

Kärnuppsättningen använder 16 filer och lämnar utrymme för framtida fokuserade Knowledge-filer.

## Kontroll efter uppladdning

- Kontrollera att samtliga 16 filer syns.
- Kontrollera att inga historiska eller dubblerade filer har laddats upp.
- Testa i Förhandsvisning att GPT:n använder rätt genreprofil.
- Testa att huvudinstruktionen har företräde framför Knowledge-filerna.
- Testa att GPT:n inte citerar eller återger stora delar av Knowledge-filerna i onödan.
