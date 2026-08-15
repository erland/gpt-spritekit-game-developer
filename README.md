# SpriteKit Game Designer & Developer — GPT-byggprojekt

Detta paket används för att skapa en specialiserad GPT för speldesign och 2D-spelutveckling med Swift, SpriteKit och tvOS.

## Aktuell version

`1.0.0-rc12`

Detta är en releasekandidat. Allt som kan verifieras statiskt och genom lokalt fil-/zip-arbete är genomfört. GPT Preview samt Xcode-, controller- och fysisk Apple TV-verifiering återstår.

## Börja här

1. Läs `prompt-15/RELEASE-CANDIDATE-REPORT.md`.
2. Följ `prompt-15/INSTALLATION-AND-VALIDATION.md`.
3. Använd `config/BUILDER-CHECKLIST.md` när GPT:n skapas.
4. Registrera externa testresultat med `prompt-15/EXTERNAL-VERIFICATION-CHECKLIST.md`.

## Centrala filer

- `PLAN.md` — ursprunglig `[PLAN]`.
- `PLAN2.md` — genomförandet uppdelat i promptar.
- `PLAN3.md` — plan och status för produktionssäker grafik- och assetpipeline.
- `prompt-18/`–`prompt-24/` — genomföranderapporter för PLAN3, preflight, language consistency, and the T05B refinement.
- `DECISIONS.md` — fastställda beslut.
- `OPEN-QUESTIONS.md` — kontrollfrågor och beslut.
- `PROJECT-STATUS.md` — aktuell arbetsstatus.
- `CHANGELOG.md` — versionshistorik.
- `config/` — färdigt konfigurationsunderlag för GPT-byggaren.
- `knowledge/` — 16 kunskapsfiler.
- `reference-project/` — dokumenterat tvOS/macOS SpriteKit-referensprojekt.
- `prompt-14/` — testpaket och statisk preflight.
- `prompt-15/` — releasekandidat, installation och extern verifiering.

## Status

`[PLAN2 Prompt 15]` är genomförd i den utsträckning denna miljö tillåter. `[PLAN3 Prompt 1–4]` and the T05B refinement are implemented; external GPT Preview and Xcode verification remain.

## Git och CI

Kunskapsbasen och referensprojektet innehåller nu stöd för projektspecifik `.gitignore`, delade Xcode-schemes och GitHub Actions för macOS-tester och tvOS Simulator-build.

## Buildergränser

- Slutlig instruktion: 7 846 av 8 000 Unicode-tecken.
- Knowledge-filer: 16 av 20.
- Se `prompt-17/INSTRUCTION-COMPACTION-REPORT.md` för täckningskontroll.

## Language convention

Chat responses may follow the user's language, but technical project artifacts are written in English. User-facing game text may be localized to Swedish or another explicitly requested language.

## Graphics responsibility in rc12

This GPT plans, specifies, reviews, and integrates game assets. Polished sprite and tileset production is delegated to a separate Game Graphics Creator through a standardized Asset Request Package.

## Portable Chat-distribution och releases

Repositoryt kan bygga två distributionspaket från samma kanoniska GPT-underlag:

- `spritekit-developer-custom-gpt-vX.Y.Z.zip` för installation/arkivering av Custom GPT-konfigurationen.
- `spritekit-developer-chat-vX.Y.Z.zip` för användning i en vanlig ChatGPT-konversation. Bifoga paketet och be ChatGPT läsa `START-HERE.md` först.

Kör lokalt med `python3 scripts/build_distributions.py` och verifiera med `python3 scripts/validate_distributions.py`.

Vanliga push-, pull request- och manuella workflow-körningar använder `VERSION` som paketversion. När en GitHub Release publiceras används i stället release-taggen som versionskälla. En release med taggen `v1.1.0` producerar därför paket med `v1.1.0` i filnamn och intern versionsmetadata. Release-taggen måste följa `vMAJOR.MINOR.PATCH` (SemVer).
