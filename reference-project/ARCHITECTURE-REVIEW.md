# Arkitekturgranskning — ReferenceGame

## Sammanfattning

Arkitekturen är lämplig som referens för en erfaren programvaruutvecklare som är ny inom SpriteKit. Den visar de viktigaste gränserna utan att introducera ett stort ramverk.

**Bedömning:** godkänd som referensprojekt, med dokumenterade begränsningar och kvarstående Xcode-verifiering.

## Styrkor

### Tydlig separation

- Fysisk input översätts till `PlayerIntent`.
- `GameWorld` och `GameSession` kan testas utan SpriteKit.
- `GameScene` fungerar huvudsakligen som adapter och presentation.
- Plattformsspecifika appstarter är separerade från delad kod.

### Rätt nivå av abstraktion

Projektet använder små protokoll och modeller där de ger konkret nytta. Det försöker inte skapa ett generellt entity-component-system, service locator eller egen spelmotor.

### tvOS först, macOS för iteration

Produktkraven styr controller- och TV-designen, medan tangentbord och XCTest på macOS gör utvecklingen snabbare.

### Explicit tid och paus

Rörelse är tidsbaserad och paus är domäntillstånd snarare än enbart `SKScene.isPaused`.

## Identifierade begränsningar

### En enda pausorsak

`GameSession` lagrar bara en pausorsak. Om appen blir inaktiv samtidigt som controllern är frånkopplad kan den senaste händelsen ersätta den tidigare orsaken. För referensprojektet är detta accepterat, men ett produktionsspel bör överväga en mängd aktiva pausorsaker eller en prioriterad tillståndsmodell.

### Automatisk återupptagning efter extern paus

När en controller återansluts eller appen blir aktiv återupptas en matchande extern paus automatiskt. Ett verkligt spel kan i stället kräva en bekräftelse från spelaren.

### Scenfabriken har bara en scen

`SceneCoordinator` demonstrerar en central skapandepunkt men innehåller ännu bara `.game`. Den ska inte byggas ut förrän ett projekt faktiskt behöver menyer, laddning eller resultatvyer.

### Inputpolling saknar konfigurerbar mapping

Kontrollerna är hårdkodade till vänster spak/D-pad, A, X och Menu. Det är lämpligt för ett minimalt exempel men inte ett fullständigt remapping-system.

### Ingen verklig SpriteKit-integrationstestning

XCTest täcker domänlogiken, inte scenens noder, actions eller GameController. Det är ett medvetet val; sådan kod kräver separat integrations- och manuell verifiering.

## Rekommendationer för framtida projekt

Inför endast följande när ett verkligt behov uppstår:

- flera samtidiga pausorsaker,
- dependency injection för fler system,
- datastrukturer för nivåer och assets,
- sparning och versionsmigrering,
- flera spelare och controllerassignment,
- profileringspunkter och object pooling,
- scenövergångar och laddning.

## Så ska GPT:n använda projektet

GPT:n ska använda projektet som exempel på principer, inte som mall som alltid kopieras oförändrad. Vid ett nytt projekt ska den:

1. inventera projektets verkliga behov,
2. återanvända relevanta gränser,
3. ta bort delar som inte behövs,
4. lägga till system först när kärnloopen kräver dem,
5. dokumentera avvikelser från referensarkitekturen.
