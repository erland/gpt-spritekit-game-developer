# ReferenceGame

Ett minimalt referensprojekt för 2D-spel med Swift, SpriteKit och tvOS.

## Syfte

Projektet visar en liten men användbar arkitektur för:

- tvOS som produktplattform,
- macOS som officiell utvecklings- och testplattform,
- delad SpriteKit-kod,
- semantisk controllerinput,
- analog top-down-rörelse,
- testbar spellogik utanför `SKScene`,
- explicit paus och app-livscykel,
- ärlig uppdelning mellan automatiska och manuella tester.

Projektet är en pedagogisk referens, inte en generell spelmotor eller produktionsfärdig mall.

## Targets

- `ReferenceGame-tvOS`
- `ReferenceGame-macOS`
- `ReferenceGameTests`

## Köra projektet

1. Öppna `ReferenceGame.xcodeproj` i Xcode.
2. Bygg och kör `ReferenceGame-macOS` för snabb iteration.
3. Kör `ReferenceGameTests`.
4. Bygg och kör `ReferenceGame-tvOS` i simulator.
5. Verifiera controller och TV-upplevelse på fysisk Apple TV innan en verklig release.

## Kontroller

### Spelkontroll

- vänster analog spak eller D-pad: rörelse,
- A: primär handling,
- X: sekundär handling,
- Menu: paus/fortsätt vid användarpaus.

### macOS-tangentbord

- WASD eller piltangenter: rörelse,
- mellanslag eller Return: primär handling,
- X: sekundär handling,
- Escape eller P: paus/fortsätt.

Tangentbordet är endast en utvecklingsadapter. Produktdesignen utgår från vanlig spelkontroll på Apple TV.

## Struktur

```text
Shared/
├── App/
├── Game/
├── GameLogic/
└── Input/
Platforms/
├── tvOS/
└── macOS/
Tests/
```

- `PlayerIntent` är gränsen mellan fysisk input och spelet.
- `GameWorld` och `GameSession` innehåller testbar logik.
- `GameScene` binder ihop input, modell och SpriteKit-presentation.
- `SceneCoordinator` är central skapandepunkt för scener.

## Dokumentation

- `TECHNICAL-DESIGN.md` — arkitektur och dataflöde.
- `ARCHITECTURE-REVIEW.md` — styrkor, begränsningar och rekommendationer.
- `MANUAL-TEST-PLAN.md` — macOS-, controller-, simulator- och Apple TV-testning.
- `RELEASE-CHECKLIST.md` — krav före paketering och release.
- `KNOWN-ISSUES.md` — öppna verifieringar och medvetna begränsningar.

## Verifieringsstatus

Filstruktur, projektfil och kod har kontrollerats strukturellt och manuellt i paketets skapandemiljö. Projektet har inte byggts med Xcode där. Xcode-byggning, XCTest, controllerprov och fysisk Apple TV-verifiering återstår enligt testplanen.

## Git och CI

- `.gitignore` ignorerar lokala Xcode-data, buildprodukter och signeringsmaterial.
- Delade schemes finns för macOS och tvOS.
- `.github/workflows/ci.yml` kör macOS-tester och bygger tvOS Simulator-targeten.
- Se `CI.md` för användning och begränsningar.
