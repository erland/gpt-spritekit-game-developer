# GPT Byggaren 1.5.0 – migreringsplan

Projekt: **SpriteKit Game Designer & Developer**

## Preserve-first baseline

Migreringen ska bevara:
- version **1.0.0**
- exakt **16 Knowledge-filer** enligt manifestet
- slutlig instruktion byte-identiskt som canonical beteendekälla
- instruktion inom GPT Builder-gränsen
- projekt-zip som sanningskälla för faktiskt projektinnehåll
- säkerhetsgranskning av zip/path traversal och arbete i separat mapp
- Swift, SpriteKit och tvOS som primär teknisk profil
- macOS som utvecklings- och testplattform
- controller- och TV-UX som förstaklasskrav
- liten spelbar riskprototyp före onödig arkitektur eller innehåll
- tydlig separation mellan spelbarhet, teknik, design och innehåll
- asset-specifikation, granskning och integration utan att felaktigt lova produktionsgrafik
- ärlig redovisning av faktiskt körda tester kontra statiska/manuella kontroller
- Git/CI-principer, delade schemes och tvOS simulatorbuild
- befintligt referensprojekt som utvecklings-/testunderlag, inte permanent Knowledge
- befintliga Chat- och Custom GPT-distributioner

## Steg

1. Etablera canonical instruktion och projektkontrakt.
2. Normalisera capability-, artifact-, workspace/state- och tool-kontrakt.
3. Normalisera Chat och Custom GPT till samma canonical källa.
4. Bedöm Claude Projects och OpenCode.
5. Bedöm OpenAI Plugin.
6. Generalisera build, parity, CI och release via runtime-registry.
7. Slutlig readiness, dokumentationssynk och 7/7-gate.

## Aktivering av nya runtimes

En runtime får bara aktiveras om den kan bevara projekt-zip-flödet, säker filhantering, faktisk filredigering/paketering, SpriteKit/tvOS-utveckling, test/redovisning och release/CI utan kritisk degradering.
