# Teknisk design — ReferenceGame

## Syfte

ReferenceGame är ett minimalt, pedagogiskt referensprojekt för 2D-spel med Swift, SpriteKit och tvOS. Det visar en återanvändbar grund utan att försöka vara en generell spelmotor.

## Plattformar

- **tvOS** är produktplattform.
- **macOS** är officiell utvecklings- och testplattform.
- iOS och iPadOS ingår inte i referensprojektet.

Båda appmålen använder samma filer under `Shared/`. Plattformsspecifik kod hålls under `Platforms/`.

## Lager

### App och livscykel

`GameContainerView` skapar scenen, visar den med `SpriteView` och vidarebefordrar appens `scenePhase` till spelet.

### Scenkoordinering

`SceneCoordinator` är den centrala skapandepunkten för scener. Den äger det delade inputobjektet och skapar `GameScene`.

### Presentation

`GameScene` ansvarar för SpriteKit-noder, frame-uppdatering, visuell synkronisering och återkoppling. Scenen läser semantisk input och uppdaterar den rena spelmodellen.

`PauseOverlayNode` visar orsaken till paus på ett TV-läsbart sätt.

### Spellogik

`GameWorld` innehåller spelvärldens testbara tillstånd och rörelselogik. Den beror på `CoreGraphics`, men inte på SpriteKit.

`GameSession` modellerar om spelet pågår eller är pausat och varför.

### Input

`InputSource` exponerar en semantisk `PlayerIntent` i stället för råa knappar.

- `ControllerInputSource` läser GameController.
- `KeyboardInputSource` ger snabb utvecklingsinput på macOS.
- `CombinedInputSource` slår samman källorna och normaliserar rörelsevektorn.

## Uppdateringsflöde

Varje frame gör `GameScene` följande:

1. beräknar och begränsar `deltaTime`,
2. läser aktuell `PlayerIntent`,
3. upptäcker controlleranslutning eller frånkoppling,
4. hanterar pausintention,
5. uppdaterar `GameWorld` om sessionen inte är pausad,
6. synkroniserar SpriteKit-presentationen med modellen.

`deltaTime` begränsas till `1/15` sekund för att undvika stora hopp efter avbrott.

## Pausmodell

`GameSessionState` har två lägen:

- `playing`,
- `paused(PauseReason)`.

Stödda orsaker är:

- användaren begär paus,
- controller har kopplats från,
- appen är inaktiv.

Användaren kan endast växla bort en användarbegärd paus. Externa pausorsaker återupptas genom motsvarande extern händelse.

## Teststrategi

Tester körs mot macOS-targeten och fokuserar på kod utan SpriteKit-beroende:

- rörelse utifrån intent, hastighet och tid,
- begränsning till spelvärldens gränser,
- ingen rörelse vid nolltid,
- användarpaus,
- externa pausorsaker,
- återupptagning efter extern paus.

Controller, SpriteKit-rendering, app-livscykel och fysisk Apple TV kräver integrations- och manuella tester.

## Avsiktliga begränsningar

Referensprojektet innehåller inte:

- laddnings- eller menyscen,
- sparning,
- ljud,
- fysikvärld,
- tilemap,
- flera spelare,
- nätverk,
- assetpipeline,
- produktionsfärdig felhantering.

Dessa delar ska läggas till när ett verkligt projekt behöver dem, inte byggas in i referensgrunden på förhand.
