# Claude Projects och OpenCode – runtime compatibility

Projekt: **SpriteKit Game Designer & Developer**  
GPT Byggaren: **1.5.0**

## Slutsats

Claude Projects och OpenCode bedöms olika.

- **OpenCode** bedöms som **equivalent candidate** för kärnflödet eftersom workspace-/fil-/kodorienteringen kan matcha projektinventering, Swift-redigering, statiska kontroller, dokumentation och paketering.
- **Claude Projects** bedöms som **reduced candidate** eftersom instruktioner, Knowledge, designanalys och dokumentation kan mappas väl, men full parity för deterministisk projektfilredigering, Xcode/tvOS-build/test och zip-/releasehantering inte kan tas för given.

Båda lämnas **not active** tills faktiska distributioner/adapterspecifikationer och regressionstester finns.

## Parity-bedömning

| Område | Claude Projects | OpenCode |
|---|---|---|
| Behavior | equivalent candidate | equivalent candidate |
| Capability | reduced | equivalent candidate |
| Artifact | reduced | equivalent candidate |
| Workspace/state | reduced | equivalent candidate |
| Tool | reduced | equivalent candidate |

## Kritiska regler som måste bevaras

Varje runtime måste så långt den aktiveras bevara:
- senaste kompletta projektzip som sanningskälla,
- säker zip-slip/path traversal-kontroll,
- arbete i separat mapp och aldrig ändra originalarkivet,
- Swift/SpriteKit/tvOS som primär teknisk profil,
- controller- och TV-UX-krav,
- liten riskprototyp före större motor-/arkitekturbyte,
- asset-specifikation, granskning och integration,
- tydlig skillnad mellan faktiskt körda tester, statiska kontroller och manuell granskning,
- Git/CI-principer och faktisk workflow-verifiering,
- 16/16 Knowledge-filer eller verifierat equivalent representation.

## Claude Projects

Styrkor:
- kan bära instruktioner, Knowledge, designprinciper och projektdokumentation,
- kan analysera Swift/SpriteKit-arkitektur och tvOS/controller-frågor.

Begränsning:
- full parity för att faktiskt redigera ett komplett projektträd, köra Xcode/tvOS build/test, validera releaseinnehåll och paketera en ny verifierad zip kan inte tas för given.

Beslut:
- compatibility: `reduced`
- activation: `not_active`
- blocker: `deterministic_project_edit_xcode_test_and_zip_parity_not_guaranteed`

## OpenCode

Workspace-, fil- och kodorienteringen matchar kärnflödet väl:
- inventera projekt,
- redigera Swift/Xcode-projektfiler och dokumentation,
- köra statiska kontroller och kommandon där miljön tillåter,
- uppdatera Git/CI-filer,
- paketera projekt och releaser.

Xcode/tvOS-testparity beror fortsatt på faktisk macOS/Xcode-miljö och ska aldrig antas utan körning.

Beslut:
- compatibility: `equivalent`
- activation: `not_active`
- blocker: `distribution_and_regression_not_implemented`

## Aktiveringsregel

En runtime får aktiveras först när:
1. canonical instruktion paketeras deterministiskt,
2. 16/16 Knowledge-filer eller verifierat equivalent representation ingår,
3. projekt-zip-inventering och zip-säkerhet verifieras,
4. filredigering och releasepaketering regressionstestas,
5. SpriteKit/tvOS/controller-regler verifieras,
6. testtransparens verifieras,
7. faktisk Xcode/tvOS-build/test används när sådan parity påstås,
8. distributionen byggs och valideras i CI.

Ingen canonical produktregel ändras av denna bedömning.
