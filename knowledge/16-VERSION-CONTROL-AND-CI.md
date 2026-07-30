# Versionshantering och CI för SpriteKit/tvOS

## Syfte

Denna fil beskriver hur GPT:n ska hjälpa till med `.gitignore`, Git-repositoryhygien och GitHub Actions för Swift-, SpriteKit-, macOS- och tvOS-projekt. Målet är reproducerbara byggen och tester utan att lägga in signeringshemligheter, lokala Xcode-data eller genererade filer i Git.

## När filen ska användas

Använd filen när användaren vill:

- initiera eller städa ett Git-repository,
- skapa eller granska `.gitignore`,
- lägga till GitHub Actions,
- bygga macOS- eller tvOS-targets i CI,
- köra XCTest automatiskt,
- validera projektstruktur, assets eller dokumentation,
- skapa release- eller distributionsflöden.

## Grundprinciper

1. Inventera projektet innan filer genereras.
2. Anpassa `.gitignore` efter faktisk projektstruktur och använda verktyg.
3. Kontrollera targets, schemes, workspace/project, deployment targets och beroenden innan workflow skrivs.
4. Använd minsta nödvändiga GitHub Actions-behörigheter.
5. Håll hemligheter utanför repositoryt och loggarna.
6. Skilj bygg/test från signering, arkivering och distribution.
7. Påstå inte att ett workflow fungerar förrän det har körts i GitHub Actions eller motsvarande miljö.

## `.gitignore`

En lämplig `.gitignore` för ett Xcode/SpriteKit-projekt bör normalt ignorera:

- `.DS_Store`,
- `DerivedData/`,
- `build/`,
- `*.xcuserstate`,
- `xcuserdata/`,
- användarspecifika Xcode-workspaces,
- Swift Package Manager-buildcache som `.build/`,
- lokala loggar och temporära filer,
- `.env` och lokala hemlighetsfiler,
- exporterade arkiv och signeringsmaterial.

Ignorera inte automatiskt:

- `project.pbxproj`,
- delade schemes under `xcshareddata/xcschemes`,
- `Package.resolved` när projektet vill låsa beroendeversioner,
- källassets,
- projektets scripts och workflowfiler,
- dokumentation som behövs för att återskapa projektet.

GPT:n ska granska befintlig `.gitignore` och slå samman ändringar utan att radera projektspecifika regler.

## Delade schemes

GitHub Actions och andra rena CI-miljöer behöver schemes som är tillgängliga efter checkout. När `xcodebuild` använder `-scheme` ska GPT:n kontrollera att schemat är delat och finns under:

`<Project>.xcodeproj/xcshareddata/xcschemes/`

eller motsvarande workspace-struktur.

Om ett scheme saknas ska GPT:n antingen:

- skapa ett delat scheme som matchar befintliga targets, eller
- använda ett dokumenterat target-baserat buildkommando där scheme inte behövs.

Testning med `xcodebuild test` bör normalt använda ett delat scheme.

## GitHub Actions: lämplig grundnivå

Ett normalt CI-workflow för detta slags projekt kan innehålla:

1. checkout,
2. utskrift av vald Xcode-version,
3. `xcodebuild -list` för diagnostik,
4. macOS-build och XCTest för delad logik,
5. tvOS Simulator-build utan signering,
6. valfria statiska projektkontroller,
7. uppladdning av testresultat eller loggar vid fel.

Använd normalt en GitHub-hostad macOS-runner och `CODE_SIGNING_ALLOWED=NO` för simulator- och CI-byggen som inte ska distribueras.

Använd `macos-latest` när projektet inte kräver en fast Xcode-version. Om reproducerbarhet eller SDK-kompatibilitet kräver en bestämd Xcode-version ska runner/Xcode-valet uttryckligen låsas och dokumenteras. Kontrollera alltid aktuell runner-image innan en version låses.

## Exempel på xcodebuild-strategi

### macOS-tester

```bash
xcodebuild test \
  -project ReferenceGame.xcodeproj \
  -scheme ReferenceGame-macOS \
  -destination 'platform=macOS' \
  CODE_SIGNING_ALLOWED=NO
```

### tvOS Simulator-build

```bash
xcodebuild build \
  -project ReferenceGame.xcodeproj \
  -scheme ReferenceGame-tvOS \
  -destination 'generic/platform=tvOS Simulator' \
  CODE_SIGNING_ALLOWED=NO
```

Kommandona ska anpassas efter workspace, schemes, konfiguration och projektets faktiska namn.

## Signering och distribution

Vanliga build- och testflöden ska helst inte kräva Apple-certifikat. För arkivering, fysisk enhet eller distribution kan följande behövas:

- Apple Developer-konto,
- distributions- eller utvecklarcertifikat,
- provisioning profiles,
- App Store Connect-uppgifter,
- secrets i GitHub,
- tillfällig keychain på runnern.

GPT:n ska aldrig lägga certifikat, privata nycklar, lösenord, provisioning profiles eller API-nycklar direkt i repositoryt. När signering efterfrågas ska GPT:n beskriva secrets, åtkomstbegränsning, städning och GitHub Environments där det är relevant.

## Pull request- och branchkontroller

Ett grundworkflow bör normalt köras på:

- `pull_request`,
- push till primär branch,
- manuell `workflow_dispatch` när felsökning eller explicit körning är användbar.

Använd concurrency för att avbryta äldre körningar på samma branch när det minskar onödig macOS-runneranvändning.

## Ytterligare lämpliga kontroller

Lägg bara till kontroller som projektet faktiskt använder, till exempel:

- SwiftFormat eller SwiftLint,
- validering av JSON/YAML,
- kontroll av saknade assets,
- kontroll av filnamn och skiftläge,
- dokumentationslänkar,
- test coverage,
- schemavalidering,
- kontroll att genererade filer är aktuella.

Inför inte nya format- eller lintverktyg enbart för CI utan att användaren accepterar beroendet och dess regler.

## Kostnad och robusthet

macOS-runners är en begränsad resurs jämfört med enklare Linux-jobb. GPT:n bör:

- hålla workflowt fokuserat,
- undvika onödiga matriser,
- använda path filters när ändringar inte kan påverka bygget,
- använda dependency caching endast när den är säker och ger verklig nytta,
- sätta rimlig timeout,
- undvika att köra samma build flera gånger utan skäl.

## Självhostad Mac

En självhostad Mac kan vara lämplig när användaren behöver:

- en specifik Xcode-installation,
- fysisk Apple TV eller controller i automatiserade tester,
- lokala SDK:er eller verktyg,
- lägre kostnad vid många körningar.

GPT:n ska samtidigt varna för säkerhetsriskerna med självhostade runners, särskilt för pull requests från okända forks, och rekommendera isolering samt begränsad åtkomst.

## Leveranskrav

När GPT:n lägger till versionshanterings- eller CI-stöd ska den redovisa:

- skapade och ändrade filer,
- vilka triggers som används,
- vilka targets/schemes som byggs,
- om signering är avstängd eller konfigurerad,
- vilka tester som körs,
- vad som återstår att verifiera i GitHub,
- eventuella secrets användaren måste skapa,
- hur workflowt kan köras manuellt.
