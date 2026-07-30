# Testpaket — [PLAN2 Prompt 14]

## Syfte

Testpaketet används i GPT-byggarens Preview och vid senare regressionstest. Varje fall bedöms mot förväntade beteenden, inte mot en ordagrann idealsvarsmall.

## Bedömningsskala

- **Godkänd:** alla kritiska förväntningar uppfylls och inga allvarliga fel uppstår.
- **Godkänd med anmärkning:** kärnbeteendet är korrekt men svaret är för långt, otydligt eller missar en mindre punkt.
- **Underkänd:** en kritisk regel bryts, exempelvis fabricerad testning, felaktig zip-hantering eller direkt kopieringshjälp.

## Testfall

### T01 — Speldesign

> Jag vill skapa ett enkelt shoot 'em up för Apple TV. Hjälp mig hitta minsta spelbara prototyp.

**Förväntat beteende:**

- identifierar genre och kärnupplevelse
- föreslår liten prototyp
- prioriterar game feel och läsbarhet
- bedömer SpriteKit som rimligt
- undviker onödigt stor scope

**Prioritet:** critical

### T02 — Inspirationsspel

> Jag vill göra något som The Last Ninja, fast modernt.

**Förväntat beteende:**

- analyserar abstrakta egenskaper
- frågar eller härleder vad användaren uppskattar
- föreslår tydlig differentiering
- kopierar inte banor, figurer, namn eller pussel
- formulerar en självständig pitch

**Prioritet:** critical

### T03 — Teknikgrind

> Jag vill göra ett fritt 3D-spel med roterbar kamera och stora sammanhängande miljöer i SpriteKit.

**Förväntat beteende:**

- varnar tydligt för teknikvalet
- skiljer möjligt från praktiskt lämpligt
- föreslår riskprototyp, minskat scope eller annan motor
- byter inte motor utan motivering

**Prioritet:** critical

### T04 — Zip-arbetsflöde

> Här är senaste projektzippen. Lägg till paus och ge mig en uppdaterad zip.

**Förväntat beteende:**

- inventerar zippen först
- använder senaste zip som sanningskälla
- gör minsta rimliga ändring
- redovisar faktiskt utförda tester
- skapar ren ny zip

**Prioritet:** critical

### T05A — Identifiera assetbehov

**Prompt:** Analysera spelidén och identifiera minsta grafikmängd för nästa spelbara prototyp.

**Godkänt:** GPT:n kopplar assets till gameplay, prioriterar, föreslår placeholders och börjar inte producera polerad grafik.

### T05B — Asset Request Package

**Prompt:** Skapa ett överlämningspaket till en separat Game Graphics Creator för isometriska tiles och props.

**Godkänt:** Paketet innehåller brief, maskinläsbar spec, style guide och validation criteria. Det definierar canvas, footprint, anchor, overflow, atlas, lokalisering och separata sheets där slicingkraven skiljer sig. Huvudleveransen är specifikation, inte genererad bild.

### T05C — Granska Asset Delivery Package

**Prompt:** Jämför levererade grafikfiler och manifest med ursprunglig request package och skapa en revisionslista.

**Godkänt:** GPT:n verifierar mätbara krav, skiljer visuell bedömning från teknisk kontroll, använder Passed/Failed/Not verified/Not applicable och blockerar Production Ready vid obligatoriska brister.

### T05D — Deterministiska placeholders

**Prompt:** Skapa placeholders för att testa isometrisk rörelse, kollision och kamera före slutgrafik.

**Godkänt:** Placeholderfilerna är enkla, märkta och kompatibla med framtida dimensioner, footprint, anchor och naming.

### T05E — SpriteKit-integration

**Prompt:** Integrera godkända runtime-assets och manifest i projektet.

**Godkänt:** GPT:n hanterar atlaser, target membership, texture identifiers, anchors, collision, depth sorting, animation, filtering och ärlig testredovisning.

### T06 — Plattformsspel

> Hoppet känns oprecist. Vad ska jag mäta och ändra?

**Förväntat beteende:**

- fokuserar på acceleration, gravitation, jump velocity, coyote time och input buffer
- föreslår mätbara parametrar
- skiljer kodtest från playtest
- undviker generell nybörjarförklaring

**Prioritet:** high

### T07 — Turordningsstrategi

> Hur balanserar jag två enhetstyper i ett turordningsspel?

**Förväntat beteende:**

- identifierar roller och beslutsutrymme
- föreslår modell eller simulering
- varnar för enbart DPS-jämförelse
- inkluderar kartposition, ekonomi och handlingsvärde

**Prioritet:** high

### T08 — Controller/tvOS

> Spelet fungerar med tangentbord på Mac. Vad måste verifieras innan Apple TV-test?

**Förväntat beteende:**

- controlleranslutning och frånkoppling
- dead zones och flankdetektering
- paus och återupptagning
- fokusnavigering där relevant
- TV-läsbarhet och safe areas

**Prioritet:** critical

### T09 — Kommunikationsnivå

> Implementera en state machine för animationer. Hoppa över grundläggande Swift-förklaringar.

**Förväntat beteende:**

- svarar tekniskt och direkt
- förklarar spelarkitekturella konsekvenser
- undviker grundläggande språklektion
- behåller testbarhet

**Prioritet:** medium

### T10 — Testredovisning

> Är det säkert att projektet bygger på fysisk Apple TV?

**Förväntat beteende:**

- påstår inte att det är byggt utan bevis
- skiljer strukturell granskning från Xcode-build
- ger konkret manuell verifiering
- redovisar osäkerhet

**Prioritet:** critical

### T11 — Lokal multiplayer

> Lägg till stöd för två lokala spelare i referensarkitekturen.

**Förväntat beteende:**

- modell för spelartilldelning och flera controllers
- hanterar frånkoppling per spelare
- diskuterar gemensam/delad kamera
- överkomplicerar inte grundprojektet

**Prioritet:** high

### T12 — Scopekontroll

> Jag vill börja med 12 världar, 40 fiender och full produktionsgrafik.

**Förväntat beteende:**

- föreslår vertical slice
- identifierar största risk
- prioriterar placeholdergrafik
- ger konkret minskad scope

**Prioritet:** critical

### T13 — Bildgenerering

> Generera en åttaframars gånganimation med transparent bakgrund.

**Förväntat beteende:**

- specificerar konsekvent siluett, riktning, canvas och footpoint
- varnar för frame-to-frame drift
- föreslår kvalitetskontroll och atlaslayout
- integrerar med assetplan

**Prioritet:** high

### T14 — Aktuell dokumentation

> Vilket tvOS- eller SpriteKit-API bör jag använda för controllerinput idag?

**Förväntat beteende:**

- använder webbsökning när aktualitet spelar roll
- prioriterar officiell Apple-dokumentation
- skiljer aktuella fakta från arkitekturråd

**Prioritet:** high

### T15 — Saknad projektfil

> Fortsätt ändra mitt projekt från förra chatten, men jag laddar inte upp zippen.

**Förväntat beteende:**

- låtsas inte ha projektet
- begär senaste zip när filerna krävs
- kan ge generell vägledning utan att rekonstruera projektet

**Prioritet:** critical

## Körning

1. Konfigurera GPT:n enligt `config/BUILDER-CHECKLIST.md`.
2. Kör varje testfall i en ny Preview-konversation när tidigare kontext skulle påverka resultatet.
3. Dokumentera utfall i `TEST-EXECUTION-RESULTS.md`.
4. Kör om kritiska fall efter varje ändring i instruktion eller kunskapsbas.

## Viktig begränsning

Detta paket definierar och granskar testerna. En faktisk end-to-end-körning i den färdigkonfigurerade GPT:n måste göras i GPT-byggarens Preview och kan inte bevisas enbart genom statisk filgranskning.

## T20 — Language consistency and localization

**Prompt:**

> Lägg till en svensk inställningsmeny i SpriteKit-projektet och dokumentera ändringen. Svara gärna på svenska.

**Pass criteria:**

- The chat response may be Swedish.
- New source code, identifiers, comments, tests and technical documentation are English.
- Visible menu copy may be Swedish and is kept localizable.
- Technical language and localized game content are not mixed.

**Automatic failure:**

- New Swedish identifiers, code comments or technical documentation.
- Refusal to create Swedish game text.
- Hard-coded localized text inside gameplay logic when a localization boundary is expected.
