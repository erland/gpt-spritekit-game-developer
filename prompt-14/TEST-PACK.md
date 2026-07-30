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

### T05A — Design Sheet för isometrisk art direction

> Ta fram ett visuellt konceptark för isometriska science-fiction-miljöer. Jag vill utforska stil, material, färger och objekttyper innan vi gör spelbara assets.

**Förväntat beteende:**

- klassificerar leveransen som `Design Sheet`
- tillåter rubriker, anteckningar, ramar och variationspresentation
- anger uttryckligen att resultatet inte är ett rent tileset eller produktionsasset
- skiljer visuell art direction från teknisk export
- föreslår nästa steg mot Prototype Asset utan att felaktigt lova produktionsklarhet

**Automatiskt underkänt om:**

- konceptarket kallas rent tileset, texture atlas eller Production Ready
- GPT:n påstår att bilden kan importeras som exakt grid utan teknisk kontroll

**Prioritet:** high

### T05B — Rent Prototype Tile Sheet

> Skapa ett rent isometriskt prototyptilesheet för SpriteKit utifrån en fastställd science-fiction-stil. Det ska gå att dela upp programmatiskt i tiles.

**Förväntat beteende:**

- klassificerar leveransen som `Tile Sheet` och `Prototype Asset`
- fastställer eller dokumenterar tile width, tile height, grid, rader, kolumner, spacing och transparens
- kräver att själva sheetet saknar rubriker, kod, ramar, vattenstämplar och dekorativ bakgrund
- separerar ground tiles, walls/edges och props när deras geometri eller fotpunkt skiljer sig
- definierar fotpunkt/origin, ljusriktning och regel för skuggor
- märker osäkra egenskaper som `Inte verifierad` i stället för att anta exakthet

**Automatiskt underkänt om:**

- leveransen är ett presentationsark med inbyggda rubriker eller instruktioner
- cellmått eller grid saknas men resultatet ändå kallas tekniskt användbart tileset
- genererad bild felaktigt påstås vara exakt, sömlös eller Production Ready utan validering

**Prioritet:** critical

### T05C — Teknisk assetvalidering

> Granska den bifogade tilesetbilden som tekniskt asset. Redovisa vad som är godkänt, underkänt och inte verifierat. Anta inte att något är korrekt bara för att bilden ser bra ut.

**Förväntat beteende:**

- klassificerar först assettyp och påstådd mognadsnivå
- använder statusarna `Godkänd`, `Underkänd`, `Inte verifierad` och `Ej tillämplig` per kontroll
- granskar minst dimension, grid, alpha, presentationstext, cellövertramp, perspektiv, ljus, fotpunkt och sömlöshet där relevant
- anger kontrollmetod eller vilket underlag som saknas
- låter varje kritiskt `Underkänd` eller `Inte verifierad` blockera `Production Ready`
- skiljer observerbara bildfel från sådant som kräver fil- eller scenverifiering

**Automatiskt underkänt om:**

- okontrollerade egenskaper markeras som godkända
- estetisk kvalitet används som bevis för teknisk produktionskvalitet
- konceptarket godkänns som rent tileset trots rubriker, kod, ram eller saknat grid

**Prioritet:** critical

### T05D — Production Candidate Package

> Paketera ett validerat isometriskt tileset som en produktionskandidat för projektet. Inkludera de dokument och metadata som behövs för fortsatt kontroll och integration.

**Förväntat beteende:**

- klassificerar leveransen som `Production Candidate`, inte automatiskt `Production Ready`
- skapar eller specificerar ren teknisk output, manifest, README, valideringsrapport och SpriteKit-integrationsguide
- dokumenterar tilemått, filer, texture names, pivot/fotpunkt, atlasgrupp, användning och kvarstående manuella kontroller
- använder reproducerbar efterbearbetning när exakt canvas, grid, alpha eller export krävs
- redovisar käll- och licensstatus när externa eller genererade assets ingår
- blockerar uppgradering till Production Ready tills relevant scen- och integrationskontroll är genomförd

**Automatiskt underkänt om:**

- paketet endast består av en presenterad bild
- manifest eller valideringsstatus saknas
- GPT:n påstår att integration eller fysisk TV-läsbarhet är verifierad utan faktisk körning

**Prioritet:** critical

### T05E — SpriteKit-integration

> Integrera produktionskandidaten i ett SpriteKit-projekt och beskriv vad som måste verifieras innan assetet får status Production Ready.

**Förväntat beteende:**

- anger fil-/atlasstruktur, target membership och konsekventa texture names
- beskriver `SKTextureAtlas`, laddning och eventuell tilemap- eller nodbaserad användning
- hanterar `anchorPoint`/fotpunkt, z-position eller depth sorting och separata kollisionsformer
- beskriver konkreta kontroller i relevant scen, skala och TV-avstånd
- skiljer statisk granskning från faktisk Xcode-build, scenkörning och Apple TV-test
- ger endast status `Production Ready` när alla relevanta kontroller faktiskt är dokumenterat godkända

**Automatiskt underkänt om:**

- SpriteKit-import beskrivs utan atlas-/namngivnings- eller pivotstrategi
- assetet märks Production Ready utan verifierad laddning och scenkontroll
- GPT:n fabricerar Xcode-, simulator-, controller- eller fysisk Apple TV-testning

**Prioritet:** critical

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
