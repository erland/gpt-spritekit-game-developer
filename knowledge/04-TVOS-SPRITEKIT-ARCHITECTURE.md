# tvOS- och SpriteKit-arkitektur

## 1. Syfte och ansvar

Denna fil ger teknisk vägledning för 2D-spel som byggs i Swift och SpriteKit med tvOS som produktplattform och macOS som officiell utvecklings- och testplattform.

Filen äger råd om:

- scen- och nodstruktur,
- spelloop och tidshantering,
- separation mellan SpriteKit och domänlogik,
- tillståndshantering,
- fysik och kollisioner,
- kamera,
- animationer och texture atlases,
- lokal sparning,
- delad kod mellan tvOS och macOS,
- prestanda,
- bedömning av om SpriteKit är lämpligt.

Controller-UX, fokusnavigering, TV-läsbarhet och flera anslutna kontroller behandlas i `05-CONTROLLER-AND-TV-UX.md`.

## 2. Arkitekturmål

Arkitekturen ska i första hand vara:

- enkel att förstå för en erfaren utvecklare som är ny inom spelutveckling,
- testbar utan att varje test behöver starta en `SKScene`,
- tillräckligt modulär för flera spelgenrer,
- anpassad till realtidsuppdatering,
- fri från onödiga generella motorabstraktioner,
- möjlig att köra och felsöka på macOS,
- tydlig med vad som är spelregel, presentation och plattformsintegration.

Arkitekturen ska inte försöka efterlikna en stor kommersiell spelmotor. Inför endast abstraktioner som behövs av det aktuella spelet eller referensprojektet.

## 3. Rekommenderade lager

En liten till medelstor SpriteKit-kodbas bör normalt delas i fyra ansvar.

### 3.1 App- och plattformslager

Ansvarar för:

- start av appen,
- skapande av fönster och vy,
- plattformsspecifik livscykel,
- tvOS- och macOS-konfiguration,
- controlleranslutningar,
- växling mellan menyer och spel,
- filplatser och plattformstjänster.

Detta lager ska vara tunt. Spelregler ska inte ligga i appdelegater, view controllers eller SwiftUI-vyer.

### 3.2 Scen- och presentationslager

Består främst av `SKScene`, `SKNode` och presentationstjänster.

Ansvarar för:

- nodhierarki,
- rendering,
- kamera,
- uppspelning av animationer och ljud,
- översättning mellan modellens tillstånd och det som syns,
- vidarebefordran av input som semantiska kommandon,
- kontakt med SpriteKits fysiksystem.

En scen får koordinera men bör inte äga all spellogik.

### 3.3 Spelmodell och regler

Består helst av vanliga Swift-typer utan beroende på SpriteKit.

Ansvarar för:

- spelstatus,
- poäng,
- hälsa och resurser,
- regler,
- mål och förlustvillkor,
- cooldowns,
- AI-beslut,
- turordning,
- progression,
- serialiserbart tillstånd.

Detta lager ska kunna enhetstestas utan rendering.

### 3.4 Infrastruktur och innehåll

Ansvarar för:

- assetregister,
- nivådata,
- sparning,
- konfiguration,
- loggning,
- diagnostik,
- fabriker och laddning av spelinnehåll.

Undvik att sprida hårdkodade assetnamn och balansvärden över många scener.

## 4. Scenstruktur

### 4.1 Använd få tydliga scentyper

Ett mindre spel behöver ofta bara:

- `BootScene` eller motsvarande startflöde,
- `MenuScene`,
- `GameScene`,
- eventuellt `ResultsScene` eller `GameOverScene`.

Skapa inte en ny `SKScene` för varje dialogruta eller litet spelläge. Pausmenyer, HUD och tillfälliga overlays kan ofta vara nodlager i samma scen.

### 4.2 Rekommenderad nodhierarki

Ett vanligt upplägg:

```text
GameScene
├── worldRoot
│   ├── backgroundLayer
│   ├── terrainLayer
│   ├── entityLayer
│   ├── effectLayer
│   └── foregroundLayer
├── cameraNode
│   └── hudRoot
├── overlayRoot
└── debugRoot
```

Fördelar:

- världen kan flyttas och skalas oberoende av HUD,
- z-ordning blir tydligare,
- debugvisualisering kan slås av separat,
- paus- och resultatoverlays kan ligga över både värld och HUD.

### 4.3 Undvik en massiv `GameScene`

Tecken på att scenen behöver delas upp:

- den innehåller alla spelregler,
- den känner till varje fiendetyp,
- den laddar och tolkar all nivådata,
- den hanterar controllerinput direkt i många grenar,
- den sköter sparning,
- den innehåller stora mängder balansvärden,
- den är svår att testa utan en renderingsmiljö.

Bryt i första hand ut domänlogik, system och innehållsladdning. Bryt inte automatiskt ut varje nod till en egen klass.

## 5. Spelloop och tid

### 5.1 Grundprincip

SpriteKit anropar scenens uppdateringsmetoder per bildruta. Spellogik får inte anta att varje bildruta tar exakt lika lång tid.

Beräkna ett begränsat delta:

```swift
let rawDelta = currentTime - previousTime
let deltaTime = min(rawDelta, maximumDeltaTime)
```

Begränsningen skyddar mot stora hopp efter paus, breakpoint eller tillfällig belastning.

### 5.2 Variabelt och fast tidssteg

Använd variabelt tidssteg för:

- visuell interpolation,
- enkla rörelser,
- timers där små avvikelser är acceptabla.

Överväg fast tidssteg för:

- deterministisk simulering,
- komplex tur- eller fysiknära logik,
- replay,
- tester som kräver reproducerbarhet.

Inför inte en egen full fixed-step-loop utan konkret behov. SpriteKits fysikmotor har redan en egen uppdateringsmodell, och dubbla system kan bli svåra att samordna.

### 5.3 Uppdateringsordning

En tydlig ordning kan vara:

1. samla input,
2. skapa semantiska spelarintentioner,
3. uppdatera spelmodell och AI,
4. applicera rörelse eller fysikkommandon,
5. låt SpriteKit lösa fysik,
6. hantera kontakter och konsekvenser,
7. synkronisera presentation,
8. uppdatera kamera och HUD.

Använd SpriteKits separata callbacks när ordningen spelar roll, exempelvis `update`, `didEvaluateActions`, `didSimulatePhysics` och `didFinishUpdate`.

## 6. Input som semantiska kommandon

Scenen bör inte sprida råa knappkoder eller axelvärden genom spelet. Översätt dem till en stabil modell, exempelvis:

```swift
struct PlayerIntent {
    var movement: CGVector
    var primaryActionPressed: Bool
    var secondaryActionPressed: Bool
    var pausePressed: Bool
}
```

Fördelar:

- samma spellogik kan drivas av controller, tangentbord och testdata,
- remapping blir enklare,
- replay och automatiserade tester blir möjliga,
- plattformsberoenden hålls utanför spelreglerna.

Detaljer om dead zones, knappkanter och flera kontroller finns i `05-CONTROLLER-AND-TV-UX.md`.

## 7. Tillståndshantering

### 7.1 Separera app-, scen- och spelstatus

Exempel på olika nivåer:

- appstatus: start, meny, spel, resultat,
- scenstatus: laddar, aktiv, pausad, avslutas,
- spelstatus: pågående, vunnet, förlorat,
- entitetsstatus: idle, moving, attacking, stunned.

Blanda inte alla nivåer i en enda enum.

### 7.2 En enkel state machine räcker ofta

Använd explicita övergångar och små tillståndstyper. Introducera GameplayKit state machines endast när de förenklar ett verkligt problem.

Ett entitetstillstånd bör:

- ha tydliga inträdes- och utträdesvillkor,
- äga så lite global logik som möjligt,
- kunna beskrivas och testas,
- inte gömma all spelmekanik i callbacks.

### 7.3 Deterministisk modell för turbaserade spel

För turordningsbaserad strategi eller pussel bör handlingar modelleras som kommandon eller actions som:

- valideras,
- appliceras på modellen,
- producerar ett resultat,
- därefter visualiseras.

Animationen ska inte vara sanningskälla för om handlingen lyckades.

## 8. Entiteter och komponenter

SpriteKit erbjuder noder; GameplayKit erbjuder entity-component-system. Välj efter behov.

### Använd enkla nodklasser när:

- spelet är litet,
- entitetstyperna är få,
- beteendet är tydligt och stabilt,
- komposition inte ger en konkret fördel.

### Överväg komponenter när:

- många entiteter delar delbeteenden,
- kombinationerna varierar,
- AI, hälsa, rörelse och presentation behöver testas separat,
- arvshierarkin börjar bli bred och skör.

Undvik ett generellt ECS bara för att det är vanligt i spelmotorer. För ett litet SpriteKit-spel är vanliga Swift-strukturer och protokoll ofta tydligare.

## 9. Fysik och kollisioner

### 9.1 Skilj på tre frågor

- **Kontakt:** vilka objekt överlappar eller träffar varandra?
- **Respons:** ska fysikmotorn separera dem?
- **Spelkonsekvens:** ska spelaren skadas, få poäng eller öppna en dörr?

SpriteKits kategorimasker ska vara dokumenterade och centralt definierade.

```swift
enum PhysicsCategory {
    static let player: UInt32 = 1 << 0
    static let enemy: UInt32 = 1 << 1
    static let terrain: UInt32 = 1 << 2
    static let projectile: UInt32 = 1 << 3
    static let trigger: UInt32 = 1 << 4
}
```

### 9.2 Använd enkla kollisionsformer

Kollisionsformen behöver inte följa spritebildens siluett exakt. En enklare kropp ger ofta:

- stabilare respons,
- bättre spelkänsla,
- mindre processorkostnad,
- lättare felsökning.

För isometriska objekt bör kollisionsytan normalt motsvara objektets fotavtryck på marken, inte hela den synliga bilden.

### 9.3 Kontakter ska ge händelser, inte direkt kedjereaktion

Fysikkontaktens callback bör helst skapa en domänhändelse eller anropa en tydlig regelmetod. Undvik att direkt ta bort många noder, byta scen och skriva sparfil i samma callback.

### 9.4 Continuous collision detection

Använd precise collision detection selektivt för mycket snabba små objekt, exempelvis projektiler. Att slå på det för allt kan bli kostsamt.

## 10. Rörelse

### 10.1 Välj en primär rörelsemodell

Vanliga alternativ:

- fysikbaserad kraft och impuls,
- direkt hastighetsstyrning,
- kinematisk positionering med egen kollisionslösning,
- tile- eller gridbaserade steg.

Blanda inte flera modeller för samma objekt utan tydlig anledning.

### 10.2 Plattformsspel

Rörelsekänsla kräver ofta egna regler ovanpå fysiken:

- acceleration,
- inbromsning,
- varierbar hopphöjd,
- coyote time,
- input buffering,
- kontrollerad fallhastighet.

Detta bör ligga i testbar spelarkontrollogik, inte utspritt i kontaktcallbacks.

### 10.3 Top-down och isometriskt

Separera:

- inputvektor,
- världsvektor,
- visuell projektion.

I ett isometriskt spel ska input kunna mappas till världens axlar utan att alla regler känner till skärmens diagonaler.

## 11. Kamera

Kameran ska betraktas som ett eget system, inte bara sättas direkt till spelarens position varje frame.

Överväg:

- mjuk följning,
- dead zone,
- framförhållning i rörelseriktningen,
- nivågränser,
- zoom,
- skakning,
- separata regler vid boss, dialog eller multiplayer.

Kameraskakning bör appliceras som ett tillfälligt offset och inte förstöra kamerans basposition.

HUD placeras normalt under kameran så att den stannar i skärmkoordinater.

## 12. Animationer

### 12.1 Separera animationstillstånd från spelregler

En attack ska inte lyckas enbart för att en viss animationsframe visas. Spelmodellen bör avgöra handlingens faser; presentationen visar dem.

### 12.2 Namn och atlaser

Använd stabila namn, exempelvis:

```text
player_idle_01
player_idle_02
player_run_01
player_run_02
```

Gruppera assets efter laddnings- och användningsmönster. En enda gigantisk atlas för hela spelet kan ge onödig minnesanvändning. För många små atlaser kan ge mer administration.

### 12.3 Förladda med avsikt

Förladda sådant som behövs omedelbart i en scen. Ladda inte automatiskt hela spelets innehåll vid start utan mätning eller behov.

### 12.4 Pixel art

För pixel art:

- använd konsekvent intern upplösning,
- undvik oavsiktlig filtrering,
- skala i heltalssteg när möjligt,
- kontrollera att kamera och noder inte hamnar på halv‑pixellägen om det ger oskärpa.

## 13. Nivådata och innehåll

Håll nivådata separerad från scenkod när projektet växer.

Möjliga format:

- `SKTileMapNode` och SpriteKit scene files,
- JSON, plist eller YAML som genereras till ett lämpligt runtimeformat,
- egna Swift-data för små prototyper.

Välj format utifrån hur nivåerna faktiskt ska redigeras. Bygg inte en egen nivåeditor innan manuellt dataformat är ett verkligt hinder.

Nivådata bör kunna valideras för:

- saknade assets,
- ogiltiga koordinater,
- okända entitetstyper,
- mål som inte går att nå,
- inkompatibla versionsfält.

## 14. Lokal sparning

Version 1.0 ska stödja lokal sparning, men inte kräva Game Center eller molnsynkronisering.

Separera:

- användarinställningar,
- upplåst progression,
- pågående spel,
- statistik.

Använd `Codable` där det passar och inkludera ett schema- eller versionsfält. Sparfiler ska kunna migreras eller avvisas tydligt när formatet ändras.

Spara inte SpriteKit-noder direkt. Spara domänmodellens data och återskapa presentationen.

Vid kritisk progression bör skrivningen ske atomärt, exempelvis via temporär fil följd av ersättning.

## 15. Delning mellan tvOS och macOS

### 15.1 Delad kärna

Placera följande i delade targets eller Swift packages när det är praktiskt:

- spelmodell,
- regler,
- AI,
- nivåtolkning,
- balanskonfiguration,
- sparformat,
- teststöd.

### 15.2 Plattformsspecifika adaptrar

Håll följande bakom tunna adaptrar:

- controller- och tangentbordsinput,
- fönster och vy,
- lifecycle,
- filplatser,
- plattformsspecifika menyer.

macOS-versionen är ett officiellt utvecklings- och testmål, men ska inte göra tangentbordet till spelets primära design. TvOS och fysisk controller förblir produktkravet.

### 15.3 Undvik för tidig universalitet

Bygg inte touchkontroller och iOS-layout bara för att koden tekniskt kan delas. iOS/iPadOS är framtida, frivilliga mål.

## 16. Testbarhet

Gör det möjligt att testa:

- regler med syntetiskt delta time,
- input via `PlayerIntent`,
- AI med seedad slump,
- nivådata utan rendering,
- sparning i temporär katalog,
- tillståndsövergångar,
- kollisionskonsekvenser som domänhändelser.

Använd dependency injection där det ger konkret testvärde, exempelvis för tid, slump och lagring. Undvik omfattande containerlösningar.

Detaljerad test- och releaseprocess ägs av `07-TESTING-AND-RELEASE.md`.

## 17. Prestanda

### 17.1 Mät före större optimering

Vanliga riskområden:

- många aktiva fysikkroppar,
- många transparenta överlappande sprites,
- frekventa skapanden och borttagningar,
- stora texturer,
- komplexa shaders,
- många partikelsystem,
- upprepade sökningar i nodträdet,
- allokeringar per frame.

### 17.2 Praktiska åtgärder

- cacha nodreferenser,
- återanvänd kortlivade objekt när mätning visar behov,
- inaktivera fysik och AI utanför relevant område,
- gruppera texturer i rimliga atlaser,
- undvik att konstruera strängar och samlingar i heta loopar,
- separera debugvisualisering från release,
- använd Instruments och Xcodes profileringsverktyg.

Object pooling är relevant för mycket frekventa projektiler eller effekter, inte ett krav för varje entitet.

### 17.3 TV-mål

Stabil frame pacing är viktigare än maximal grafisk detalj. Bedöm spelet på faktisk Apple TV-hårdvara, inte bara på en snabb Mac.

## 18. SpriteKit-lämplighetsbedömning

### 18.1 SpriteKit rekommenderas normalt när

- spelet är tydligt 2D,
- Apple TV är huvudplattform,
- teamet är litet,
- koden får vara Swift-baserad,
- behovet av visuella editorer är måttligt,
- fysik, partiklar och animationer är inom normal 2D-omfattning,
- lokal distribution och få externa beroenden värderas högt.

### 18.2 Riskprototyp krävs när

- isometrisk sortering är central,
- mycket stora projektilmängder behövs,
- många dynamiska ljus eller shaders planeras,
- stora tilevärldar ska streamas,
- hundratals AI-entiteter ska simuleras,
- avancerad animation och verktygspipeline behövs,
- samma innehåll måste fungera på flera plattformar från dag ett.

Riskprototypen ska mäta den konkreta frågan och inte utvecklas till ett dolt fullprojekt.

### 18.3 Överväg annan teknik när

- spelet egentligen är 3D,
- fri roterbar 3D-kamera är kärnan,
- teamets arbetsflöde kräver avancerade visuella verktyg,
- plattformsbredd är ett huvudkrav,
- ett stort ekosystem av färdiga plugins är avgörande,
- SpriteKit skulle kräva att stora delar av en spelmotor byggs från grunden.

Bedöm skillnaden mellan **tekniskt möjligt** och **praktiskt lämpligt**.

## 19. Arkitekturkontroll för nya projekt

Kontrollera:

1. Är spelmodellen begriplig utan SpriteKit?
2. Är input översatt till semantiska kommandon?
3. Är scenens ansvar begränsat?
4. Är nodhierarkin dokumenterad?
5. Är tids- och pauslogik definierad?
6. Är fysikkategorier centralt definierade?
7. Är sparformatet separerat från noder?
8. Kan kärnlogiken testas på macOS?
9. Finns en tydlig prestandarisk att prototypa?
10. Är SpriteKit fortfarande praktiskt lämpligt?

## 20. Vanliga fel

- All kod placeras i `GameScene`.
- Rå controllerinput används direkt i spelregler.
- Rörelse multipliceras inte korrekt med tid.
- Paus orsakar ett stort delta time vid återstart.
- Animationen blir sanningskälla för spelregler.
- Fysikkontakter utför stora kedjereaktioner direkt.
- Sparfiler innehåller presentationsobjekt.
- macOS-porten driver tangentbordscentrerad design.
- avancerat ECS införs utan konkret behov.
- SpriteKit behålls trots att projektet i praktiken kräver 3D eller omfattande motorverktyg.

## 21. Rekommenderad standard för referensprojektet

Referensprojektet bör demonstrera:

- neutral top-down-rörelse,
- `PlayerIntent`,
- delad spelmodell,
- tunn `GameScene`,
- tydlig nodhierarki,
- kamera och HUD,
- paus,
- enkel fysikkontakt,
- lokal sparning,
- tvOS-controller och macOS-testinput,
- enhetstester av logik utan SpriteKit-scen.

Isometrisk projektion och depth sorting ska ligga i separat exempelmodul, i enlighet med projektbeslut D-015.

## Localization boundary

Keep Swift symbols, comments, tests and architecture documentation in English. Treat visible game copy as localized content: use localization keys or string catalogs where practical, keep fallback behavior explicit, and avoid embedding Swedish prose directly in gameplay logic when localization is expected.
