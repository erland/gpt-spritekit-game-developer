# Manifest för kunskapsfiler

## Rekommenderade kärnfiler

Ladda upp följande 16 filer från `knowledge/`:

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

## Filer som inte ska laddas upp som kunskap

Följande filer styr projektbygget men ska inte normalt laddas upp i GPT:ns kunskapssektion:

- `PLAN.md`
- `PLAN2.md`
- `PROJECT-STATUS.md`
- `CHANGELOG.md`
- `DECISIONS.md`
- `OPEN-QUESTIONS.md`
- hela builder-zippen
- historiska releasezippar

De innehåller process- och versionsinformation snarare än stabil ämneskunskap.

## Referensprojektet

Referensprojektet ska behållas i builder-paketet och användas vid utveckling och test av GPT:n. Det behöver inte laddas upp permanent som GPT-kunskap i version 1.0 eftersom:

- de centrala arkitekturprinciperna redan finns i kunskapsfilerna,
- en uppladdad projektzip i en faktisk konversation ska vara sanningskällan,
- kodexempel riskerar att bli behandlade som mall även när ett projekt kräver annan struktur.

Vid behov kan utvalda referensprojektfiler senare samlas i en separat, fokuserad kunskapsfil efter preflight.

## Filbudget

Kärnuppsättningen använder 16 filer. Det lämnar utrymme för upp till fyra framtida specialfiler, exempelvis:

- mer avancerad isometrisk arkitektur,
- Game Center,
- tillgänglighet,
- prestandaprofilering,
- App Store- och distributionsflöde.

## Kontroll efter uppladdning

- Kontrollera att samtliga 16 filer syns.
- Kontrollera att inga historiska dubletter har laddats upp.
- Testa i Förhandsvisning att GPT:n använder rätt genreprofil.
- Testa att huvudinstruktionen har företräde framför kunskapsfilerna.
- Testa att GPT:n inte citerar eller återger stora delar av kunskapsfilerna i onödan.
