# Installation och validering

## Skapa GPT:n

1. Öppna GPT-byggaren.
2. Följ `config/BUILDER-CHECKLIST.md`.
3. Använd namn, beskrivning och instruktion från `config/GPT-CONFIGURATION.md` och `config/FINAL-INSTRUCTIONS.md`.
4. Aktivera funktionerna i `config/CAPABILITIES.md`.
5. Ladda upp exakt de 15 filer som anges i `config/KNOWLEDGE-UPLOAD-MANIFEST.md`.
6. Lägg in samtalsstartarna från `config/CONVERSATION-STARTERS.md`.
7. Håll GPT:n privat under verifieringen.

## Preview-test

Kör testfallen T01–T04, T05A–T05E och T06–T15 i `prompt-14/TEST-PACK.md`. Registrera faktiskt utfall i en kopia av `prompt-14/TEST-EXECUTION-RESULTS.md`. Markera inte ett test godkänt utifrån enbart förväntat beteende.

## Referensprojekt

1. Öppna Xcode-projektet under `reference-project/`.
2. Följ `reference-project/MANUAL-TEST-PLAN.md`.
3. Slutför `reference-project/RELEASE-CHECKLIST.md`.
4. Dokumentera avvikelser i `reference-project/KNOWN-ISSUES.md`.

## Godkännande för 1.0.0

Version 1.0.0 kan skapas när Preview-testpaketet är godkänt eller accepterat med dokumenterade avvikelser, båda Xcode-targets bygger, XCTest är godkänt och grundflödet är provat på Apple TV med controller.
