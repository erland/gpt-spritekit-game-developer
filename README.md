# SpriteKit Game Designer & Developer — GPT-byggprojekt

Detta paket används för att skapa en specialiserad GPT för speldesign och 2D-spelutveckling med Swift, SpriteKit och tvOS.

## Aktuell version

`1.0.0-rc1`

Detta är en releasekandidat. Allt som kan verifieras statiskt och genom lokalt fil-/zip-arbete är genomfört. GPT Preview samt Xcode-, controller- och fysisk Apple TV-verifiering återstår.

## Börja här

1. Läs `prompt-15/RELEASE-CANDIDATE-REPORT.md`.
2. Följ `prompt-15/INSTALLATION-AND-VALIDATION.md`.
3. Använd `config/BUILDER-CHECKLIST.md` när GPT:n skapas.
4. Registrera externa testresultat med `prompt-15/EXTERNAL-VERIFICATION-CHECKLIST.md`.

## Centrala filer

- `PLAN.md` — ursprunglig `[PLAN]`.
- `PLAN2.md` — genomförandet uppdelat i promptar.
- `DECISIONS.md` — fastställda beslut.
- `OPEN-QUESTIONS.md` — kontrollfrågor och beslut.
- `PROJECT-STATUS.md` — aktuell arbetsstatus.
- `CHANGELOG.md` — versionshistorik.
- `config/` — färdigt konfigurationsunderlag för GPT-byggaren.
- `knowledge/` — 15 kunskapsfiler.
- `reference-project/` — dokumenterat tvOS/macOS SpriteKit-referensprojekt.
- `prompt-14/` — testpaket och statisk preflight.
- `prompt-15/` — releasekandidat, installation och extern verifiering.

## Status

`[PLAN2 Prompt 15]` är genomförd i den utsträckning denna miljö tillåter. Nästa steg är extern verifiering och därefter antingen slutlig `1.0.0` eller en korrigerad `1.0.0-rc3`.

## Git och CI

Kunskapsbasen och referensprojektet innehåller nu stöd för projektspecifik `.gitignore`, delade Xcode-schemes och GitHub Actions för macOS-tester och tvOS Simulator-build.

## Buildergränser

- Slutlig instruktion: 7 707 av 8 000 tecken.
- Knowledge-filer: 16 av 20.
- Se `prompt-17/INSTRUCTION-COMPACTION-REPORT.md` för täckningskontroll.
