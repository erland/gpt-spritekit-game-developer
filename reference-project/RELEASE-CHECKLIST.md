# Releasechecklista — ReferenceGame

## Källkod och struktur

- [ ] Delad kod ligger under `Shared/`.
- [ ] Plattformsspecifik kod ligger under `Platforms/`.
- [ ] Domänlogik har inget SpriteKit-beroende utan avsiktligt skäl.
- [ ] Fysisk input läcker inte in i spellogiken.
- [ ] Projektfilen refererar till samtliga nödvändiga filer.
- [ ] Inga temporära, lokala eller genererade buildfiler ingår.

## Funktion

- [ ] macOS-targeten bygger och startar.
- [ ] tvOS-targeten bygger och startar.
- [ ] Tester passerar.
- [ ] Rörelse, handlingar och gränser fungerar.
- [ ] Användarpaus fungerar.
- [ ] Controllerfrånkoppling hanteras.
- [ ] Appens inaktivitet hanteras.

## TV och controller

- [ ] All nödvändig funktion kan användas med vanlig spelkontroll.
- [ ] Text är läsbar på TV-avstånd.
- [ ] Viktigt innehåll ligger inom säkra visuella marginaler.
- [ ] Fokus eller systemnavigation stör inte spelets kontrollflöde.
- [ ] Minst en fysisk controller har testats.
- [ ] Fysisk Apple TV har testats inför en verklig produktrelease.

## Dokumentation

- [ ] `README.md` motsvarar aktuell implementation.
- [ ] `TECHNICAL-DESIGN.md` beskriver arkitekturen.
- [ ] `ARCHITECTURE-REVIEW.md` har aktuella begränsningar.
- [ ] `MANUAL-TEST-PLAN.md` har genomförts eller öppna punkter redovisats.
- [ ] `KNOWN-ISSUES.md` är uppdaterad.

## Testredovisning

- [ ] Det framgår vilka tester som faktiskt har körts.
- [ ] Manuella kontroller är separerade från automatiska tester.
- [ ] Ej genomförbar verifiering är uttryckligen markerad.
- [ ] Kända begränsningar och risker är dokumenterade.

## Paketering

- [ ] Zippen har ett tydligt versionsnummer.
- [ ] Zippen kan listas och packas upp utan fel.
- [ ] Rotmappen har ett stabilt namn.
- [ ] `.git`, DerivedData, buildprodukter, cache och systemfiler saknas.
- [ ] Changelog och projektstatus är uppdaterade.
