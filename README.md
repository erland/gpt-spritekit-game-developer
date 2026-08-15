# SpriteKit Game Designer & Developer — GPT-byggprojekt

Detta repository är den kanoniska källan för en specialiserad GPT för speldesign och 2D-spelutveckling med Swift, SpriteKit och tvOS.

Git-historiken och GitHub Releases används för versionshistorik. Repositoryt innehåller därför endast aktuella konfigurations-, kunskaps-, referens- och distributionsfiler.

## Aktuell distribution

Fallback-versionen för vanliga preview-byggen finns i `VERSION`. Vid publicerad GitHub Release används release-taggen i formatet `vMAJOR.MINOR.PATCH` som versionskälla.

## Börja här

1. Läs `config/GPT-CONFIGURATION.md`.
2. Följ `config/BUILDER-CHECKLIST.md` när Custom GPT:n skapas eller uppdateras.
3. Använd `config/FINAL-INSTRUCTIONS.md` som GPT Instructions.
4. Använd `config/CONVERSATION-STARTERS.md` som conversation starters.
5. Ladda upp exakt de 16 filer som anges i `config/KNOWLEDGE-UPLOAD-MANIFEST.md` som Knowledge.

## Centrala filer

- `config/` — aktuell konfiguration för GPT Builder.
- `knowledge/` — de 16 kanoniska Knowledge-filerna.
- `reference-project/` — aktuellt tvOS/macOS SpriteKit-referensprojekt för utveckling och test; det laddas inte upp permanent som GPT Knowledge.
- `portable/START-HERE.md` — startinstruktion för den portabla Chat-distributionen.
- `scripts/` — deterministisk build och validering av distributionspaketen.
- `.github/workflows/build-distributions.yml` — bygger preview-artifacts och release-assets.

## Git och CI

Kunskapsbasen och referensprojektet innehåller stöd för projektspecifik `.gitignore`, delade Xcode-schemes och GitHub Actions för macOS-tester och tvOS Simulator-build.

## Buildergränser

- Slutlig instruktion ligger under GPT Builders gräns på 8 000 Unicode-tecken.
- Knowledge-uppsättningen består av 16 filer.
- `config/KNOWLEDGE-UPLOAD-MANIFEST.md` är sanningskälla för vilka filer som ska laddas upp.

## Språk

Chattsvar kan följa användarens språk. Tekniska projektartefakter skrivs på engelska. Användarsynlig speltext kan lokaliseras till svenska eller annat uttryckligen önskat språk.

## Grafikansvar

GPT:n planerar, specificerar, granskar och integrerar spelassets. Polerad sprite- och tileset-produktion delegeras normalt till en separat grafikskapare via ett standardiserat Asset Request Package.

## Portable Chat-distribution och releases

Repositoryt bygger två distributionspaket från samma kanoniska GPT-underlag:

- `spritekit-developer-custom-gpt-vX.Y.Z.zip` för installation och arkivering av Custom GPT-konfigurationen.
- `spritekit-developer-chat-vX.Y.Z.zip` för användning i en vanlig ChatGPT-konversation. Bifoga paketet och be ChatGPT läsa `START-HERE.md` först.

Kör lokalt:

```bash
python3 scripts/build_distributions.py
python3 scripts/validate_distributions.py
```

Vanliga push-, pull request- och manuella workflow-körningar använder `VERSION` som paketversion. När en GitHub Release publiceras används i stället release-taggen som versionskälla. En release med taggen `v1.1.0` producerar därför paket med `v1.1.0` i filnamn och intern versionsmetadata. Release-taggen måste följa `vMAJOR.MINOR.PATCH` (SemVer).
