# Testning och release

## Syfte

Denna fil beskriver hur GPT:n ska verifiera förändringar i ett tvOS/SpriteKit-projekt och hur resultatet ska redovisas inför release. Målet är hög trovärdighet: bara sådant som faktiskt har körts får beskrivas som testat, medan Xcode-, enhets- och spelkänslekontroller som återstår ska anges tydligt.

## När filen ska användas

Använd filen när GPT:n ska:

- planera tester för en ny funktion,
- ändra kod i ett befintligt projekt,
- granska projektets testbarhet,
- verifiera controller- och TV-beteende,
- förbereda en zip-release,
- skilja automatiserbar verifiering från fysisk provspelning,
- dokumentera kända begränsningar.

## Huvudansvar

Filen äger:

- testnivåer och teststrategi,
- enhetstestbar spellogik,
- integration mellan logik och SpriteKit,
- macOS-test som utvecklingsstöd,
- tvOS-simulator och Xcode-kontroller,
- fysisk Apple TV-testning,
- controller-testmatris,
- prestanda- och stabilitetskontroller,
- playtesting och game feel,
- ärlig testredovisning,
- releasechecklista och releasebeslut.

## Avgränsning

- Zipinventering och paketering ägs av `06-PROJECT-ZIP-WORKFLOW.md`.
- Arkitektur för testbar spellogik ägs i grunden av `04-TVOS-SPRITEKIT-ARCHITECTURE.md`.
- Controller- och TV-UX-krav ägs av `05-CONTROLLER-AND-TV-UX.md`.
- Balans, simulering och playtestingprinciper beskrivs även i `02-GAME-DESIGN-FOUNDATIONS.md`.

## Grundprinciper

### Testa på rätt nivå

Testa ren spellogik utan SpriteKit när möjligt. Använd SpriteKit- eller plattformsintegrationstest bara där beteendet faktiskt beror på noder, fysik, rendering, controller-API eller livscykel.

### Ett passerande test bevisar bara det testet

GPT:n ska inte dra bredare slutsatser än underlaget stödjer. Ett enhetstest av rörelsemodell bevisar inte att rörelsen känns bra med en fysisk kontroll på TV.

### Automatisering ersätter inte provspelning

Automatiska tester passar väl för:

- tillståndsövergångar,
- cooldowns,
- poäng,
- skada,
- resurser,
- spawnlogik,
- koordinatomvandling,
- sparformat,
- deterministiska regelsystem.

Faktisk provspelning krävs för bland annat:

- game feel,
- visuell läsbarhet,
- controllerrespons,
- svårighetskurva,
- animationstiming,
- ljudfeedback,
- TV-avstånd,
- fokusnavigering.

### Redovisa teststatus med exakta verb

Använd exempelvis:

- **Kört:** kommandot kördes och resultatet observerades.
- **Passerade:** testsviten rapporterade godkänt.
- **Granskat:** filer eller kod har inspekterats manuellt.
- **Inte kört:** miljö eller verktyg saknades.
- **Kräver manuell kontroll:** beteendet måste verifieras i Xcode, på Mac eller Apple TV.
- **Antagande:** slutsatsen bygger på arkitektur eller kodläsning, inte exekvering.

Undvik formuleringar som “allt fungerar” när fullständig verifiering saknas.

## Testpyramid för SpriteKit-projekt

### 1. Enhetstester för domän- och spellogik

Prioritera tester för kod som inte kräver `SKScene` eller `SKNode`.

Exempel:

- spelartillstånd,
- hälsa och skada,
- poäng och resurser,
- turordning,
- AI-beslut på abstrakt nivå,
- spawnregler,
- level progression,
- sparning och migrering,
- isometrisk tile-/screen-konvertering,
- inputmappning från semantiska actions.

Bra tester ska vara:

- deterministiska,
- snabba,
- isolerade,
- begripliga,
- oberoende av bildfrekvens och realtid där möjligt.

Använd injicerad klocka eller explicita tidsvärden i stället för verklig väntan.

### 2. Komponent- och systemtester

Testa samverkan mellan några få system, exempelvis:

- input → rörelseavsikt → spelarmodell,
- skada → invulnerability → återgång,
- checkpoint → sparning → återställning,
- spawndefinition → fiendefabrik → aktiv fiendelista,
- pause state → simuleringsstopp.

Dessa tester bör fortfarande hållas fria från rendering där det går.

### 3. SpriteKit-integration

Använd integrationstest eller liten testscen för beteenden som beror på:

- nodhierarki,
- physics bodies,
- contact callbacks,
- texture atlases,
- actions,
- kamera,
- scenövergångar,
- z-position och rendering.

Integrationstester ska vara få och fokuserade. Om en funktion kräver stor scenmiljö för att testas är det ofta tecken på att logik bör extraheras.

### 4. Plattforms- och enhetstest

Verifiera:

- tvOS target,
- macOS testtarget eller testapp,
- olika controllerprofiler,
- controlleranslutning och frånkoppling,
- appens livscykel,
- paus och återupptagning,
- fokusnavigering,
- safe areas,
- prestanda på faktisk hårdvara.

## Rekommenderad verifieringsordning

1. Statisk projektgranskning.
2. Enhetstester.
3. Komponent- och systemtester.
4. Build för tillgängliga targets.
5. Körning på macOS som snabb utvecklingskontroll.
6. tvOS-simulator där relevant.
7. Fysisk Apple TV med fysisk controller.
8. Playtest av design och game feel.
9. Releasegranskning och zipverifiering.

Ordningen får anpassas, men fysisk enhetstestning får inte ersättas av simulator när beteendet beror på hårdvara, controller, prestanda eller TV-presentation.

## Statisk projektgranskning

Kontrollera:

- att nya filer ingår i rätt target,
- att imports och modulgränser är rimliga,
- att borttagna symboler inte refereras,
- att assetnamn matchar kod,
- att texture atlas-struktur är korrekt,
- att physics category bit masks är unika och avsiktliga,
- att tidsberoende kod inte är bildfrekvensberoende av misstag,
- att paustillstånd stoppar rätt system,
- att debugkod inte är aktiv i release,
- att sparformat inte ändrats utan migreringsstrategi.

## Build- och Xcode-kontroller

När Xcode-miljö är tillgänglig bör GPT:n eller användaren verifiera:

- att projektet öppnas utan saknade referenser,
- att valda schemes finns,
- att tvOS-target bygger,
- att macOS-utvecklingsmålet bygger om det ingår,
- att testschemat kan köras,
- att warnings granskas,
- att deployment target och SDK är rimliga,
- att code signing-frågor skiljs från kodfel.

Om build inte kan köras ska GPT:n beskriva exakt vilka kontroller som ändå utförts.

## macOS som officiell utvecklings- och testplattform

macOS-versionen ska användas för snabb iteration av delad spellogik och, när arkitekturen tillåter, SpriteKit-scener.

Mac-test är särskilt användbart för:

- snabb start och felsökning,
- test av tangentbord som utvecklingsinput,
- visuell kontroll av scener,
- deterministiska debuglägen,
- inspelning av loggar,
- automatiserade tester.

Mac-resultat ersätter inte tvOS-test för:

- focus engine,
- controllerprofiler,
- TV-läsbarhet,
- safe areas,
- appens tvOS-livscykel,
- faktisk Apple TV-prestanda.

## Controller-testmatris

Minsta manuella matris bör omfatta:

| Område | Kontroll |
|---|---|
| Start | Spelet kan startas och navigeras utan touch, mus eller tangentbord. |
| Rörelse | Analog input känns stabil nära centrum och vid full lutning. |
| Dead zone | Ingen oavsiktlig drift vid neutral spak. |
| Knappar | Tryck, hållning och release ger rätt semantik. |
| Paus | Paus fungerar och stoppar avsedda system. |
| Frånkoppling | Spelet reagerar begripligt när kontrollen kopplas från. |
| Återanslutning | Rätt spelare återfår kontroll eller får göra nytt val. |
| Menyer | Fokus är alltid synligt och kan inte fastna. |
| Flera kontroller | Spelartilldelning är stabil och tydlig där multiplayer används. |

Testa med de controllerprofiler projektet faktiskt avser stödja. Dokumentera modeller och profiler när hårdvaruspecifika fel uppstår.

## TV- och presentationskontroller

Testa från normalt soffavstånd:

- textstorlek,
- kontrast,
- fokusindikering,
- HUD-läsbarhet,
- visuella effekter,
- kritisk feedback,
- safe areas,
- bildkanter,
- mörka och ljusa scener,
- färgberoende information.

En skärmdump på dator ersätter inte kontroll på TV eftersom visningsavstånd och bildbehandling skiljer sig.

## Prestanda och stabilitet

### Mät i representativa scener

Mät inte bara en tom startscen. Använd en scen med realistiskt antal:

- sprites,
- projektiler,
- partiklar,
- physics bodies,
- animationer,
- ljud,
- UI-element.

### Kontrollera

- stabil frame pacing,
- toppar i frame time,
- minnesökning över tid,
- återkommande allokeringar i update-loop,
- texture atlas-laddning,
- nodantal,
- fysikkontakter,
- scenbyten,
- paus/återupptagning,
- långvarig körning.

### Riskprototyper

Skapa separat belastningsprototyp när projektet beror på:

- många projektiler,
- stort antal rörliga noder,
- avancerad depth sorting,
- många samtidiga animationer,
- stora tile maps,
- dynamisk assetstreaming.

## Playtesting

### Designfrågor

Ett playtest ska ha ett tydligt syfte. Exempel:

- Förstår spelaren målet utan förklaring?
- Känns rörelsen exakt nog?
- Är risk och belöning läsbara?
- Finns dominerande strategi?
- Är misslyckanden begripliga?
- Är tempot lämpligt?
- Är kontrollmappningen naturlig?

### Observera före intervju

Notera:

- var spelaren tvekar,
- vad spelaren missar,
- vilka handlingar upprepas,
- när frustration eller tristess uppstår,
- om spelaren använder avsedda mekaniker.

Fråga därefter efter upplevelsen. Undvik att förklara designavsikten innan testpersonen försökt själv.

### Separera feltyper

Klassificera fynd som:

- tekniskt fel,
- UX-problem,
- game feel-problem,
- balansproblem,
- onboardingproblem,
- innehållsbrist,
- visuell läsbarhet.

Det gör det lättare att välja rätt åtgärd.

## Releasekriterier

En releasekandidat bör minst ha:

- avgränsad och dokumenterad funktion,
- inga kända blockerande fel för avsett användningsfall,
- passerande tillgängliga automatiska tester,
- genomförd statisk granskning,
- dokumenterade manuella kontroller,
- uppdaterad status och changelog,
- inga hemligheter eller lokala buildartefakter,
- verifierad zipstruktur.

För en spelbar tvOS-release bör dessutom följande vara verifierat på fysisk Apple TV när möjligt:

- start,
- controllerinput,
- paus,
- frånkoppling/återanslutning,
- TV-läsbarhet,
- representativ prestanda,
- avslut och återstart,
- lokal sparning om den ingår.

## Releasebeslut

Använd tydliga statusnivåer:

### Godkänd för intern utveckling

- Projektet kan byggas eller granskas vidare.
- Vissa manuella tester kan återstå.
- Kända begränsningar är dokumenterade.

### Godkänd för intern provspelning

- Kärnflödet fungerar.
- Controller och scenflöde har testats i relevant miljö.
- Inga kända blockerande fel hindrar testmålet.

### Releasekandidat

- Planerade funktioner är färdiga.
- Testmatris och releasechecklista är genomförda.
- Kvarstående risker är accepterade och dokumenterade.

### Inte releaseklar

- Kritisk build, dataförlust, input, prestanda eller progression är obekräftad eller felaktig.
- Nödvändiga projektfiler saknas.
- Testredovisningen är otillräcklig.

## Standardformat för testredovisning

Använd följande struktur i leveransen:

### Automatiska kontroller

- Kommando eller testsvit.
- Resultat.
- Antal tester om tillgängligt.

### Manuellt granskat

- Kodområden.
- Filreferenser.
- Projektstruktur.

### Inte möjligt att köra här

- Xcode-build.
- tvOS-simulator.
- fysisk Apple TV.
- specifik controller.

### Rekommenderad manuell verifiering

1. Konkret teststeg.
2. Förväntat resultat.
3. Relevant risk som testet täcker.

### Kända begränsningar

- Faktiska kvarstående problem eller osäkerheter.

## Vanliga misstag

- Att bara testa happy path.
- Att låta `SKScene` innehålla all logik och därmed göra tester svåra.
- Att använda verklig tid och väntan i enhetstester.
- Att kalla simulatorprov för fysisk Apple TV-testning.
- Att bedöma game feel enbart från kod.
- Att ignorera controllerfrånkoppling.
- Att mäta prestanda i en tom scen.
- Att leverera utan att redovisa vilka tester som inte körts.
- Att markera en release som klar trots motstridig versionsinformation.

## Checklistor

### Före implementation

- [ ] Funktionen har tydliga acceptanskriterier.
- [ ] Testbar logik kan separeras från SpriteKit där det är rimligt.
- [ ] Nödvändiga controller- och TV-fall är identifierade.
- [ ] Designfrågor som kräver playtest är markerade.

### Efter implementation

- [ ] Enhetstester är tillagda eller uppdaterade.
- [ ] Integrationer och filreferenser är granskade.
- [ ] Build har körts där miljö finns.
- [ ] Warnings är granskade.
- [ ] Manuell controller- och TV-testlista finns.
- [ ] Prestandarisker är testade eller dokumenterade.
- [ ] Testredovisningen skiljer kört, granskat och ej kört.

### Före release

- [ ] Ändringsomfattningen är uppfylld.
- [ ] Kritiska tester passerar.
- [ ] Kända begränsningar är dokumenterade.
- [ ] Status och changelog är aktuella.
- [ ] Releasezippen är verifierad enligt `06-PROJECT-ZIP-WORKFLOW.md`.
- [ ] Fysisk Apple TV-testning är genomförd eller tydligt markerad som återstående.

## Projektdokumentation

GPT:n ska vid behov skapa eller uppdatera:

- `TEST-PLAN.md`,
- `RELEASE-CHECKLIST.md`,
- `PLAYTEST-NOTES.md`,
- `KNOWN-ISSUES.md`,
- `PROJECT-STATUS.md`,
- `CHANGELOG.md`.

## Hänvisningar

- `06-PROJECT-ZIP-WORKFLOW.md` — inventering, städning och paketering.
- `04-TVOS-SPRITEKIT-ARCHITECTURE.md` — testbar arkitektur, spelloop och systemgränser.
- `05-CONTROLLER-AND-TV-UX.md` — krav för controller, fokus och TV-läsbarhet.
- `02-GAME-DESIGN-FOUNDATIONS.md` — balans, simulering och playtesting.

## Continuous Integration

När projektet använder GitHub Actions ska CI normalt verifiera samma reproducerbara kärna som kan köras utan fysisk hårdvara:

- projekt- och schemeinventering med `xcodebuild -list`,
- macOS-build och XCTest för delad/testbar spellogik,
- tvOS Simulator-build utan code signing,
- projektspecifika statiska kontroller som redan ingår i projektet.

CI ersätter inte fysisk Apple TV, controllerprovning, fokusnavigering, prestanda på målhårdvara eller playtesting. Se `16-VERSION-CONTROL-AND-CI.md` för workflowdesign, GitHub-behörigheter, secrets och runnerstrategi.

När ett workflow levereras ska teststatus skilja mellan strukturellt validerad YAML, lokalt körda `xcodebuild`-kommandon och faktiskt godkänd GitHub Actions-körning.
