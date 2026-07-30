# Manuell testplan — ReferenceGame

## Förutsättningar

- Mac med en aktuell Xcode-version som stöder projektets valda tvOS- och macOS-SDK.
- En kompatibel spelkontroll.
- Apple TV-simulator och helst en fysisk Apple TV.

Dokumentera Xcode-version, macOS-version, tvOS-version, controller och testdatum.

## 1. Projekt och byggning

- [ ] Öppna `ReferenceGame.xcodeproj` utan reparationsdialoger.
- [ ] Välj `ReferenceGame-macOS` och bygg utan fel.
- [ ] Välj `ReferenceGame-tvOS` och bygg utan fel.
- [ ] Kontrollera att inga oväntade varningar finns.
- [ ] Kör `ReferenceGameTests` och verifiera att alla tester passerar.

## 2. macOS — tangentbord

- [ ] WASD och piltangenter flyttar spelaren.
- [ ] Diagonal rörelse är inte snabbare än rak rörelse.
- [ ] Spelaren stannar vid arenans gränser.
- [ ] Space/Return visar primär handling en gång per knapptryck.
- [ ] X visar sekundär handling en gång per knapptryck.
- [ ] P/Escape pausar och återupptar.
- [ ] Spelaren rör sig inte medan spelet är pausat.

## 3. macOS — controller

- [ ] Ansluten controller visas med rimligt namn eller generell status.
- [ ] Vänster spak och D-pad flyttar spelaren.
- [ ] Små spakrörelser inom dead zone orsakar ingen rörelse.
- [ ] A och X ger en diskret handling per knapptryck.
- [ ] Menu pausar och återupptar användarpaus.
- [ ] Tangentbord och controller kan användas utan att rörelsevektorn överstiger normal hastighet.

## 4. Controllerfrånkoppling

- [ ] Koppla från controllern under spel.
- [ ] Spelet pausas och visar korrekt meddelande.
- [ ] Ingen rörelse sker medan controllern är frånkopplad.
- [ ] Återanslut controllern.
- [ ] Spelet återupptas enligt nuvarande referensbeteende.
- [ ] Input fungerar efter återanslutning.

## 5. Appens livscykel

- [ ] Gör appen inaktiv eller flytta den till bakgrunden.
- [ ] Spelet pausas.
- [ ] Återgå till appen.
- [ ] Spelet återupptas enligt nuvarande referensbeteende.
- [ ] Inget stort positionshopp sker efter återkomst.

## 6. tvOS-simulator

- [ ] Scenen fyller skärmen korrekt.
- [ ] Text och pausoverlay är läsbara på normal TV-storlek.
- [ ] Controllerinput fungerar.
- [ ] Menu-hanteringen ger avsett spelbeteende och krockar inte oväntat med systemnavigation.
- [ ] Pausoverlay ligger över spelvärlden.

## 7. Fysisk Apple TV

- [ ] Installera och starta appen på fysisk Apple TV.
- [ ] Kontrollera bildfrekvens och jämn rörelse.
- [ ] Kontrollera läsbarhet från normalt soffavstånd.
- [ ] Testa controlleranslutning före och efter appstart.
- [ ] Testa frånkoppling och återanslutning.
- [ ] Testa att lämna appen och återgå.
- [ ] Kontrollera att inga kanter eller texter kapas av TV-inställningar.

## 8. Resultatredovisning

För varje fel dokumenteras:

- plattform och enhet,
- versionsnummer,
- reproduktionssteg,
- förväntat resultat,
- faktiskt resultat,
- skärmbild eller logg när det hjälper,
- allvarlighetsgrad.
