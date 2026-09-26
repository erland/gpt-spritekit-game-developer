# OpenAI Plugin – compatibility assessment

Projekt: **SpriteKit Game Designer & Developer**  
GPT Byggaren: **1.5.0**

## Slutsats

OpenAI Plugin bedöms som **reduced candidate**, med **skills-first** arkitektur, och lämnas **not active** i denna migrering.

Designprinciper, SpriteKit/tvOS-riktlinjer, controller/TV-UX, assetkrav, testtransparens och Git/CI lämpar sig väl för skills. Full produktparity kräver däremot också faktisk hantering av projektträd, Swift/Xcode-filer, validering, build/test där miljön tillåter samt deterministisk zip-/releasepaketering.

## Parity-bedömning

| Område | Bedömning |
|---|---|
| Behavior | equivalent candidate |
| Capability | reduced |
| Artifact | reduced |
| Workspace/state | reduced |
| Tool | reduced |

## Skills-first upplägg

En framtida Plugin v1 bör minst ha skills för:
- game design och riskprototyping,
- SpriteKit/tvOS-arkitektur,
- controller- och TV-UX,
- project-zip workflow och zip-säkerhet,
- asset requirements/review/integration,
- testing and release,
- version control och CI,
- genreprofiler,
- inspirationsanalys och differentiering.

## Kritiska regler som måste bevaras

- senaste kompletta projektzip som sanningskälla,
- zip-slip/path traversal-kontroll,
- arbete i separat mapp och aldrig ändra originalarkivet,
- Swift/SpriteKit/tvOS som primär profil,
- controller/TV-UX utan dolt beroende av touch/mus/tangentbord,
- liten riskprototyp före större motor-/arkitekturbyte,
- asset-specifikation och teknisk verifiering,
- tydlig skillnad mellan faktiskt körda tester, statiska kontroller och manuell granskning,
- faktisk Actions-körning innan CI sägs vara verifierad,
- 16/16 Knowledge-filer eller verifierat equivalent representation.

## Fil-, build- och testbegränsning

Full parity kräver att plugin-runtime eller anslutna verktyg faktiskt kan:
1. läsa komplett projektträd eller zip,
2. säkert extrahera och inventera projektet,
3. ändra Swift/Xcode-projektfiler och dokumentation,
4. köra relevanta statiska kontroller,
5. köra Xcode/tvOS build/test när miljön finns,
6. uppdatera release-/test-/CI-dokumentation,
7. paketera en ny komplett verifierad zip deterministiskt.

Utan detta ska pluginen betraktas som design-, analys- och rådgivningskapabel, men inte som fullvärdig ersättare för Chat/Custom GPT-flödet.

## Aktiveringsbeslut

- status: `assessed_not_active`
- compatibility: `reduced`
- architecture: `skills_first`
- activation: `not_active`
- blocker: `deterministic_project_edit_xcode_test_and_zip_parity_not_implemented`

Ingen Plugin-distribution byggs eller publiceras i denna migrering.

## Aktiveringsregel

Plugin får aktiveras först när:
1. skills-strukturen är implementerad,
2. canonical instruktion och 16/16 Knowledge representeras deterministiskt,
3. zip-säkerhet och projektinventering verifieras,
4. SpriteKit/tvOS/controller-regler regressionstestas,
5. asset- och testtransparensregler verifieras,
6. faktisk filändring och releasepaketering verifieras,
7. Xcode/tvOS build/test verifieras när sådan parity påstås,
8. plugin-distributionen byggs och valideras i CI.

Ingen canonical produktregel ändras av denna bedömning.
