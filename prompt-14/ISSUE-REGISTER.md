# Identifierade brister och risker

## Prioritetsmodell

- **P1:** bör åtgärdas eller verifieras före version 1.0.
- **P2:** bör korrigeras i Prompt 15 eller dokumenteras tydligt.
- **P3:** förbättring som inte blockerar version 1.0.

| ID | Prioritet | Område | Observation | Rekommenderad åtgärd |
|---|---|---|---|---|
| P1-01 | Hög | Instruktion | Bildgenereringsflödet behöver uttryckligen kräva att teknisk assetspecifikation fastställs före generering och att resultatet granskas för frame-/perspektivkonsistens. | Förstärk `config/FINAL-INSTRUCTIONS.md` i Prompt 15. |
| P1-02 | Hög | Zip-arbetsflöde | Huvudinstruktionen bör uttryckligen kräva kontroll mot zip-slip/path traversal och att arkiv aldrig skrivs över direkt. Kunskapsfilen täcker arbetskopior men säkerhetskravet bör finnas i instruktionen. | Lägg till kort säkerhetsregel i Prompt 15. |
| P1-03 | Hög | Testning | Testpaketet är ännu inte kört end-to-end i en faktiskt konfigurerad GPT Preview. Statisk preflight kan därför inte verifiera verktygsbeteende, bildgenerering eller nedladdningslänkar i den slutliga GPT:n. | Kör T01–T04, T05A–T05E och T06–T15 i Preview före publicering; dokumentera resultat. |
| P2-01 | Medel | Dokumenthygien | `README.md` innehåller inaktuella versions- och nästa-steg-uppgifter från tidigare promptar. | Korrigeras i denna release och granskas igen i Prompt 15. |
| P2-02 | Medel | Planstatus | `PLAN2.md` innehåller den felaktiga raden ”Prompt 13: nästa rekommenderade arbetsomgång” efter att Prompt 13 redan slutförts. | Korrigeras i denna release. |
| P2-03 | Medel | Beslutslogg | Q-002 är markerad beslutad men ligger fortfarande under öppna frågor och D-007 beskriver endast arbetsnamnet. | Flytta Q-002 till besvarade frågor och registrera slutnamnet som nytt beslut. |
| P2-04 | Medel | Versionshistorik | `CHANGELOG.md` har dubbla huvudrubriker och delvis icke-kronologisk äldre historik. | Normalisera i Prompt 15 utan att förlora historik. |
| P2-05 | Medel | Referensprojekt | Faktisk Xcode-build, XCTest-körning och fysisk Apple TV/controller-test är fortfarande inte genomförda i denna miljö. | Behåll som explicit manuell preflight före 1.0-publicering. |
| P3-01 | Låg | Historiska filer | Prompt 1–2 använder det tidigare arbetsnamnet. Det är korrekt som historik men kan missförstås som aktuellt. | Lägg till tydlig ”historiskt dokument/superseded”-markering i Prompt 15. |


## Status efter Prompt 15

- P1-01: **åtgärdad i 1.0.0-rc1**.
- P1-02: **åtgärdad i 1.0.0-rc1**.
- P1-03: **öppen — kräver GPT Preview**.
- P2-01: **åtgärdad**.
- P2-02: **åtgärdad**.
- P2-03: **åtgärdad**.
- P2-04: **åtgärdad**.
- P2-05: **öppen — kräver Xcode, controller och Apple TV**.
- P3-01: **åtgärdad**.
