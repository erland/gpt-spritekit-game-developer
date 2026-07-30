# Controller- och TV-UX för tvOS

## 1. Syfte och ansvar

Denna fil ger vägledning för inmatning och användarupplevelse i 2D-spel på Apple TV.

Filen äger råd om:

- vanliga spelkontroller,
- input mapping,
- analoga spakar och dead zones,
- knappkanter och upprepning,
- anslutning och frånkoppling,
- paus och återupptagning,
- flera lokala spelare,
- fokusnavigering,
- TV-läsbarhet,
- safe areas och overscan,
- text, HUD och feedback,
- tillgänglighet för kontroll och presentation.

Allmän SpriteKit-arkitektur och spelmodell behandlas i `04-TVOS-SPRITEKIT-ARCHITECTURE.md`.

## 2. Produktprincip

Spelet ska kunna användas fullständigt på Apple TV med en vanlig kompatibel spelkontroll.

Det innebär att spelaren ska kunna:

- starta spelet,
- navigera menyer,
- spela,
- pausa,
- återuppta,
- ändra relevanta inställningar,
- avsluta eller starta om,
- hantera controllerproblem,

utan pekskärm, mus eller fysiskt tangentbord.

macOS kan använda tangentbord som utvecklings- och testadapter, men produktdesignen ska fortfarande utgå från controller.

## 3. Inputarkitektur

### 3.1 Separera fysisk input från spelhandling

Skapa ett lager som översätter knappar och axlar till semantiska actions, exempelvis:

```swift
enum GameAction {
    case move(CGVector)
    case primary
    case secondary
    case interact
    case pause
    case menuBack
    case menuConfirm
}
```

Spelregler och UI ska inte vara beroende av specifika controllerknappar.

### 3.2 Inputprofiler

En profil kan beskriva:

- vilka fysiska kontroller som mappar till actions,
- dead zones,
- inversion,
- känslighet,
- om en handling reagerar på press, release eller hållning,
- alternativa knappar.

Starta med en tydlig standardprofil. Full remapping är inte obligatoriskt i första prototypen, men arkitekturen bör inte göra det omöjligt.

### 3.3 Kontinuerlig och diskret input

Skilj på:

- kontinuerlig input: rörelse, sikte, analog gas,
- diskret input: hopp, attack, menybekräftelse,
- edge-triggered input: handling ska ske en gång när knappen trycks,
- repeated input: menyförflyttning vid hållning efter fördröjning.

Att läsa `isPressed` varje frame utan flankdetektering ger ofta oavsiktligt många aktiveringar.

## 4. Analoga spakar och dead zones

### 4.1 Radial dead zone

För tvådimensionell rörelse är radial dead zone normalt bättre än separata gränser per axel.

Grundprincip:

1. läs vektorn,
2. beräkna dess magnitud,
3. sätt den till noll under tröskeln,
4. skala om området ovanför tröskeln,
5. bevara riktningen.

Det undviker att diagonaler och raka riktningar får olika känsla.

### 4.2 Rekommenderad kalibrering

Börja med en måttlig dead zone och justera genom fysisk provspelning. Exakta värden beror på controller, spelgenre och rörelsemodell.

Kontrollera:

- om figuren driver när spaken släpps,
- om små korrigeringar är möjliga,
- om diagonal rörelse normaliseras,
- om maxhastighet nås naturligt,
- om spelet känns för nervöst på TV-avstånd.

### 4.3 D-pad och analog spak

Bestäm vilka handlingar som stöder båda.

- Plattform och action: analog spak primär, D-pad kan vara alternativ.
- Grid- och turbaserade spel: D-pad kan ge bättre precision.
- Menyer: båda bör normalt fungera.

Undvik dubbla inputhändelser när både fokusmotor och egen controllerkod reagerar på samma knapp.

## 5. Knappdesign

### 5.1 Håll kärnkontrollerna små

En första version bör normalt ha:

- rörelse,
- en primär handling,
- eventuellt en sekundär handling,
- interaktion om den inte kan kombineras,
- paus.

Fler knappar är inte automatiskt större djup. Prioritera konsekventa och lätt ihågkomna handlingar.

### 5.2 Kontextkänsliga handlingar

En gemensam interaktionsknapp kan minska komplexitet, men kräver:

- tydlig visuell prompt,
- stabil prioritering när flera objekt är nära,
- förutsägbart resultat,
- möjlighet att avbryta eller backa.

### 5.3 Button buffering

I actionspel kan kort inputbuffer förbättra känslan, exempelvis för hopp eller attack. Bufferten ska vara tidsbegränsad och dokumenterad som en spelregel, inte ett dolt UI-hack.

## 6. Menyer och fokusnavigering

### 6.1 Välj en konsekvent modell

Två huvudalternativ:

- UIKit/SwiftUI-baserade menyer med systemets fokusmotor,
- SpriteKit-baserade menyer med egen fokusmodell.

Systemfokus passar ofta inställningar och standardgränssnitt. Egen SpriteKit-navigation passar när menyn är starkt integrerad i spelets visuella värld.

Blanda inte modeller utan tydlig gräns.

### 6.2 Fokus ska alltid vara synligt

Den valda kontrollen ska ha tydlig feedback genom exempelvis:

- skala,
- kontur,
- ljusstyrka,
- rörelse,
- ljud,
- etikett.

Färg ensam räcker inte alltid.

### 6.3 Navigationsgraf

Kontrollera:

- vilket element som får initialt fokus,
- vad som händer vid varje riktning,
- att fokus inte fastnar,
- att dolda eller inaktiva element inte kan få fokus,
- att dialoger håller fokus inom dialogen,
- att tillbaka-knappen ger förväntat resultat.

### 6.4 Bekräftelse och tillbaka

Mappningen ska vara konsekvent genom hela spelet. Kritiska handlingar som radering eller avslut kan kräva bekräftelse, men vardagliga handlingar ska inte ge onödiga dialoger.

## 7. Paus och livscykel

### 7.1 Paus är ett spelläge

Paus ska ha definierad påverkan på:

- simulation,
- fysik,
- animationer,
- ljud,
- input,
- timers,
- nätverksfria lokala sessioner,
- overlay och fokus.

Undvik att endast sätta `scene.isPaused` utan att förstå vilka system som fortsätter eller stannar.

### 7.2 Delta time efter paus

Nollställ eller återinitialisera tidsmätningen när spelet återupptas så att första bildrutan inte får ett mycket stort delta.

### 7.3 Automatisk paus

Överväg paus när:

- appen lämnar aktivt läge,
- systemoverlay tar fokus,
- aktiv controller kopplas från,
- användaren öppnar pausmenyn.

För turbaserade spel kan frånkoppling hanteras mindre akut än i realtidsaction, men spelaren ska få tydlig status.

## 8. Controlleranslutning och frånkoppling

### 8.1 Start utan controller

Spelet ska visa en begriplig väg framåt:

- anslut en controller,
- välj controller,
- återgå till systemet om spel inte kan starta.

Undvik en frusen titelskärm utan förklaring.

### 8.2 Frånkoppling under spel

Vid förlust av aktiv controller:

1. stoppa eller säkra spelet,
2. visa tydlig information,
3. identifiera vilken spelare som berörs,
4. tillåt återanslutning eller ny tilldelning,
5. återuppta först när tillståndet är stabilt.

### 8.3 Controlleridentitet

Lagra inte långsiktigt antaganden om exakt fysisk controller. Arbeta med aktuell session och spelartilldelning.

## 9. Lokal multiplayer

Version 1.0 ska stödja design och arkitektur för lokal multiplayer, men referensprojektet är enspelarläge.

### 9.1 Spelarplatser

Modellera stabila slots, exempelvis Player 1–4, separat från controllerobjekten.

En slot kan vara:

- ledig,
- väntar på controller,
- tilldelad,
- frånkopplad,
- redo.

### 9.2 Join-flöde

Ett vanligt flöde:

- spelaren trycker en definierad knapp för att ansluta,
- nästa lediga slot tilldelas,
- UI visar färg/ikon/namn,
- spelaren bekräftar redo.

För små privata spel kan flödet vara enkelt, men tilldelningen måste vara tydlig.

### 9.3 Gemensam kamera

För lokal multiplayer på en TV bör GPT:n bedöma:

- gemensam kamera med spelare inom samma område,
- dynamisk zoom,
- tethering eller gräns för avstånd,
- split screen.

Split screen ökar UI-, kamera- och prestandakomplexitet och ska inte rekommenderas utan konkret behov.

### 9.4 Frånkoppling av en spelare

Definiera om spelet:

- pausar för alla,
- låter AI ta över,
- väntar en begränsad tid,
- tar bort spelaren säkert.

## 10. TV-läsbarhet

### 10.1 Designa för soffavstånd

Det som är läsbart på en Mac-skärm kan vara otydligt på en TV flera meter bort.

Kontrollera på faktisk TV:

- textstorlek,
- kontrast,
- tunna linjer,
- små ikoner,
- färgskillnader,
- rörelse och partiklar,
- information i skärmkanter.

### 10.2 Prioritera siluett och kontrast

Spelaren, faror, mål och interaktiva objekt ska kunna särskiljas snabbt. Särskilt shoot 'em ups och actionspel kräver att bakgrundsdetaljer inte konkurrerar med spelinformation.

### 10.3 HUD

HUD bör:

- visa endast relevant information,
- använda stora och stabila former,
- undvika långa textrader,
- ha tydliga marginaler,
- inte täcka kritiska spelområden,
- kunna döljas eller förenklas när möjligt.

## 11. Safe areas och skärmkanter

Placera inte viktig text, fokusmarkering eller HUD precis vid kanten. TV-inställningar och olika paneler kan göra ytterkanter mindre pålitliga.

Använd säkra marginaler och verifiera på flera skärmar eller simulatorstorlekar. Bakgrundsgrafik kan gå till kanten; interaktiv och kritisk information bör ligga innanför.

## 12. Text och lokalisering

### 12.1 Textstorlek

Använd färre, större texter i stället för många små. Rubriker, knappetiketter och instruktioner ska testas på TV-avstånd.

### 12.2 Textmängd

Långa instruktioner passar dåligt i realtidsflöde. Dela upp onboarding i små, kontextuella steg.

### 12.3 Lokalisering

UI ska tåla längre strängar. Undvik knappar med hårdkodad bredd baserad på engelska kortord. Tekniska filnamn kan vara engelska även när användartext är lokaliserad.

## 13. Feedback

Varje viktig input ska ge snabb och begriplig återkoppling.

Kombinera vid behov:

- rörelse eller animation,
- ljud,
- haptik där controller och API stödjer det,
- färg eller ljus,
- kameraeffekt,
- HUD-förändring.

Undvik överdriven feedback som gör skärmen svårläst.

För nekade handlingar ska spelet visa varför, exempelvis:

- saknad resurs,
- cooldown,
- objekt utom räckhåll,
- handling inte tillåten i nuvarande tillstånd.

## 14. Onboarding

Lär ut genom användning:

1. introducera en handling,
2. ge en säker situation att prova,
3. ge tydlig feedback,
4. kombinera den senare med andra handlingar.

Visa knappikoner som motsvarar den aktiva controllerprofilen när möjligt. Om exakta symboler varierar kan semantiska ord som “Bekräfta” och “Interagera” vara stabilare.

## 15. Tillgänglighet

GPT:n ska åtminstone uppmärksamma:

- alternativ till färg som enda informationsbärare,
- möjlighet att sänka skakning och intensiva effekter,
- text- och UI-skala,
- undertexter för relevant tal,
- tydliga ljudnivåer,
- justerbar analog känslighet och dead zone,
- möjlighet att hålla i stället för att snabbt trycka upprepade gånger,
- ommappning eller alternativa kontrollscheman när scope tillåter,
- pausmöjlighet i enspelarläge.

Tillgänglighet ska integreras i designbeslut, inte endast läggas till sist.

## 16. Genreberoende controllerfrågor

### Plattformsspel

- Är hoppet responsivt?
- Finns inputbuffer och coyote time?
- Är analog rörelse för känslig?
- Kan spelaren förstå riktning och fart på TV?

### Shoot 'em up

- Är rörelse och sikte separata eller kombinerade?
- Är auto-fire lämpligt?
- Kan spelaren se sin figur och fientliga projektiler?
- Är vibration och skärmskakning begränsad?

### Turordningsbaserad strategi

- Är fokus och markör tydliga?
- Går det snabbt att flytta mellan enheter och kommandon?
- Finns en säker tillbaka-väg?
- Är långa listor lämpliga för TV?

### Isometriskt actionäventyr

- Mappas spaken till skärm- eller världsaxlar?
- Förstår spelaren diagonalerna?
- Är interaktionsobjekt tydliga bakom höga sprites?
- Är kameran stabil nog för positionsbedömning?

### Lokal multiplayer

- Vet varje spelare vilken figur och HUD-del som är deras?
- Är controlleranslutning enkel?
- Vad händer när spelare kommer för långt ifrån varandra?

## 17. Testmatris för controller och TV

Minst följande ska verifieras:

### Controller

- anslutning före appstart,
- anslutning efter appstart,
- frånkoppling i meny,
- frånkoppling under spel,
- återanslutning,
- annan controller tar över,
- analog drift,
- D-pad,
- knappkanter,
- paus,
- meny tillbaka/bekräfta.

### TV-UX

- läsbarhet på normal TV,
- olika upplösningar och skalning,
- safe areas,
- mörka och ljusa scener,
- färgblindhetsrisker,
- HUD vid intensiv action,
- fokusmarkering,
- onboarding utan tangentbord eller touch.

### macOS-utvecklingsmål

- tangentbordsadapter motsvarar semantiska actions,
- controller fungerar även på Mac,
- macOS-specifik input förändrar inte spelregler,
- samma spelmodell används.

Den fullständiga releasekontrollen ska senare samlas i `07-TESTING-AND-RELEASE.md`.

## 18. Vanliga fel

- Spelet kräver mus eller touch i ett dolt flöde.
- Råa controllerknappar används överallt i kodbasen.
- Analog dead zone hanteras separat per axel och ger konstiga diagonaler.
- `isPressed` orsakar samma handling varje frame.
- Menyfokus är osynligt eller fastnar.
- Frånkopplad controller lämnar spelet aktivt och okontrollerat.
- Paus stannar vissa system men inte andra.
- Text och ikoner bedöms bara på Mac-skärm.
- Viktig HUD ligger för nära kanten.
- Lokal multiplayer binder logik direkt till fysiska controllerobjekt.
- Split screen införs innan gemensam kamera har utvärderats.
- Färg används som enda information.

## 19. Kontrollista för nya projekt

1. Kan hela spelet användas med controller?
2. Finns en semantisk inputmodell?
3. Är kontinuerlig och diskret input separerad?
4. Är dead zone och känslighet definierad?
5. Finns konsekvent menyfokus?
6. Är pausens beteende specificerat?
7. Hanteras controllerfrånkoppling?
8. Är text och HUD testade på TV-avstånd?
9. Ligger viktig information inom safe area?
10. Finns grundläggande tillgänglighetsalternativ?
11. Om multiplayer finns: är slots och controllerassignment separerade?
12. Fungerar macOS-adaptern utan att ändra produktdesignen?
