# Grafik- och assetpipeline för 2D-spel

## Syfte

Denna fil hjälper GPT:n att planera, specificera, generera, granska, organisera och integrera grafik som används direkt i 2D-spel för tvOS och SpriteKit. Målet är inte bara att skapa tilltalande bilder, utan att skapa tekniskt användbara, konsekventa och testbara spelassets som passar spelets perspektiv, kontrollmodell, prestandabudget och aktuella utvecklingsfas.

## När filen ska användas

Använd filen när uppgiften gäller:

- art direction och visuell identitet,
- placeholdergrafik eller produktionsgrafik,
- tilesets och tilemaps,
- sprites och sprite sheets,
- figur- och objektanimationer,
- UI-ikoner och HUD-element,
- bakgrunder och parallaxlager,
- visuella effekter,
- isometriska assets,
- assetnamn, mappar och texture atlases,
- integration av genererade bilder i SpriteKit,
- granskning av befintliga assets,
- byte från placeholdergrafik till slutgrafik.

## Huvudansvar

Filen äger följande frågor:

- hur spelets visuella riktning definieras,
- hur en genomförbar assetplan skapas,
- hur pixel art och högupplöst 2D hanteras som separata pipelines,
- hur grafiska assets specificeras innan generering,
- hur bildgenerering används för spelproduktion,
- hur tilesets, sprites och animationer struktureras,
- hur teknisk konsekvens säkras mellan assets,
- hur assets förbereds och integreras i SpriteKit,
- hur grafik granskas mot spelbarhet, TV-läsbarhet och prestanda.

## Avgränsning

Närliggande ämnen ägs av andra filer:

- spelvision, kärnloop och scope: `02-GAME-DESIGN-FOUNDATIONS.md`,
- inspiration från existerande spel och originalitet: `03-INSPIRATION-AND-DIFFERENTIATION.md`,
- SpriteKit-arkitektur, rendering och prestanda: `04-TVOS-SPRITEKIT-ARCHITECTURE.md`,
- TV-läsbarhet, safe areas och controller-UX: `05-CONTROLLER-AND-TV-UX.md`,
- zip-, test- och releasehantering: `06-PROJECT-ZIP-WORKFLOW.md` och `07-TESTING-AND-RELEASE.md`,
- genrespecifika grafikkrav: respektive genreprofil.

Filen är inte en generell guide för fristående illustration, marknadsföringskampanjer, bokomslag eller annan grafik som saknar direkt koppling till spelprojektets implementation.

## Huvudprinciper

### 1. Grafik är en del av spelsystemet

En spelasset bedöms inte bara efter hur snygg den är. Den måste också:

- kommunicera funktion snabbt,
- vara läsbar på TV-avstånd,
- passa perspektiv och skala,
- ha konsekvent ljusriktning,
- fungera med kollisionsytor och ankare,
- kunna organiseras och laddas effektivt,
- stödja animation och gameplay,
- vara rimlig att producera och underhålla.

### 2. Specificera före generering

GPT:n ska inte börja generera ett större assetpaket innan den har definierat minst:

- assetens funktion i spelet,
- visuell stil,
- perspektiv och kameravinkel,
- pixelmått eller avsedd skala,
- bakgrundskrav,
- ljusriktning,
- riktningar och animationstillstånd,
- filstruktur och namngivning,
- om asseten är placeholder eller produktionsgrafik.

En enstaka konceptbild kan skapas tidigare för att utforska riktning, men ska inte behandlas som en färdig spelasset utan teknisk granskning.

### 3. Prototypgrafik före omfattande produktionsgrafik

Använd placeholdergrafik när syftet är att verifiera:

- rörelsekänsla,
- kollisionsmodell,
- kamera,
- nivålayout,
- interaktion,
- speltempo,
- teknisk risk.

Byt till produktionsgrafik när kärnmekanik, perspektiv, skala och assetbehov är tillräckligt stabila. Undvik att låsa stora mängder slutgrafik till en spelmekanik som fortfarande ändras.

### 4. Konsekvens är viktigare än enskild detaljrikedom

Ett enkelt men konsekvent assetpaket fungerar bättre än en samling individuellt imponerande bilder med olika:

- perspektiv,
- proportionssystem,
- konturbehandling,
- färgmättnad,
- skuggor,
- detaljnivå,
- ljuskällor,
- kamerahöjd.

### 5. TV-läsbarhet ska verifieras i faktisk storlek

Grafik som ser tydlig ut nära en datorskärm kan vara oläslig från en soffa. GPT:n ska prioritera:

- tydliga silhuetter,
- tillräcklig kontrast,
- stora funktionsbärande former,
- begränsat visuellt brus,
- tydlig separation mellan spelare, hot, mål och bakgrund,
- ikoner som fungerar utan fin text.

### 6. Genererade bilder är råmaterial tills de har validerats

Bildgenerering kan skapa:

- konceptunderlag,
- spriteförslag,
- tilesetdelar,
- animation frames,
- bakgrunder och UI-element.

Resultatet ska därefter kontrolleras för:

- konsekvent format,
- transparens,
- centrering och marginaler,
- identisk skala mellan frames,
- artefakter,
- perspektivfel,
- oönskade skuggor eller bakgrunder,
- upphovsrättsligt eller designmässigt olämplig närhet till referensmaterial.

## Rekommenderat arbetsflöde

### Steg 1 — Fastställ produktionsfas

Klassificera behovet som ett av följande:

- **Konceptutforskning:** hitta en visuell riktning.
- **Prototypasset:** verifiera spelmekanik eller teknik.
- **Produktionsasset:** avsedd att användas i slutversionen.
- **Integrationsarbete:** föra in eller ersätta assets i projektet.
- **Kvalitetsgranskning:** kontrollera befintlig grafik och pipeline.

Detta avgör hur mycket tid som ska läggas på detalj, variation, teknisk specifikation och efterbearbetning.

### Steg 2 — Läs projektets visuella källor

Sök efter och använd i första hand:

- `GAME-DESIGN.md`,
- `ART-DIRECTION.md`,
- `ASSET-PLAN.md`,
- `INSPIRATION-AND-DIFFERENTIATION.md`,
- befintliga sprites och tiles,
- tekniska krav från projektet,
- relevanta screenshots eller gameplaybilder.

När dokument saknas ska GPT:n skapa minsta nödvändiga specifikation och dokumentera antagandena.

### Steg 3 — Definiera art direction

Art direction bör minst ange:

- stil: exempelvis pixel art, handmålad 2D, ren cartoon eller vektorlik rastergrafik,
- perspektiv: side view, top-down eller isometriskt,
- kamerahöjd och ungefärlig zoom,
- proportionssystem för figurer och miljö,
- färgpalett och kontrastprinciper,
- konturer eller kantbehandling,
- ljuskällans riktning och mjukhet,
- skuggprincip,
- detaljnivå,
- animationston,
- vad som ska vara visuellt framträdande respektive nedtonat.

Art direction ska beskriva regler, inte bara hänvisa till ett existerande spel.

### Steg 4 — Skapa en prioriterad assetplan

Assetplanen bör innehålla:

| Fält | Innehåll |
|---|---|
| ID | Stabil identifierare |
| Namn | Begripligt assetnamn |
| Kategori | Tile, sprite, UI, effekt, bakgrund etc. |
| Funktion | Vad spelaren ska förstå eller göra |
| Perspektiv | Side, top-down, isometriskt |
| Storlek | Pixelmått eller logisk storlek |
| Variationer | Tillstånd, riktningar, biomer etc. |
| Animation | Frames, fps och looptyp |
| Prioritet | Kritisk, hög, normal, senare |
| Fas | Placeholder eller produktion |
| Status | Planerad, genererad, granskad, integrerad |
| Fil/atlas | Avsedd placering |
| Kommentar | Risker och beroenden |

Prioritera assets som krävs för nästa spelbara utsnitt. En asset ska inte skapas enbart för att den kan bli användbar senare.

### Steg 5 — Skapa en teknisk assetspecifikation

Specifikationen ska vara tillräckligt exakt för att flera genereringar ska kunna bli kompatibla. Den bör ange:

- canvasmått,
- motivets förväntade bounding box,
- transparent eller ogenomskinlig bakgrund,
- färgrymd och filformat,
- pixeltäthet och skalningsprincip,
- pivotpunkt eller fotpunkt,
- säker marginal,
- riktning som figuren tittar åt,
- frameordning,
- ljusriktning,
- skuggans placering,
- exportnamn,
- hur asseten ska beskäras eller packas.

### Steg 6 — Generera i små, kontrollerbara grupper

Generera först ett representativt prov:

- en tilefamilj,
- en figur i idle,
- en enkel rörelseanimation,
- en UI-ikonserie,
- ett bakgrundslager.

Granska provet innan hela paketet skapas. När resultatet är inkonsekvent ska specifikationen förbättras innan fler assets genereras.

### Steg 7 — Efterbearbeta och normalisera

Kontrollera och korrigera vid behov:

- transparent bakgrund,
- canvasstorlek,
- centrering,
- identiska fotpunkter,
- färgpalett,
- alfa-kanter,
- oavsiktliga pixlar,
- frameordning,
- skalning,
- filnamn,
- dubbletter.

För produktionsassets bör processen vara reproducerbar och dokumenterad. Manuell efterbearbetning ska redovisas så att senare assets kan matchas.

### Steg 8 — Integrera i SpriteKit

Vid integration ska GPT:n:

1. inventera befintlig assetstruktur,
2. placera filer i konsekventa grupper,
3. skapa eller uppdatera texture atlases där det är lämpligt,
4. uppdatera referenser i kod och datafiler,
5. ange texture filtering och skalningsprincip,
6. definiera animationer på ett återanvändbart sätt,
7. bevara spelobjektens logiska position när grafik byts,
8. testa saknade eller felaktigt namngivna textures,
9. dokumentera nya assets och beroenden.

### Steg 9 — Granska i spelkontext

Bedöm aldrig bara de fristående PNG-filerna. Verifiera:

- läsbarhet i riktig gameplayzoom,
- kontrast mot faktisk bakgrund,
- silhuett i rörelse,
- att kollisionsyta och grafik upplevs rättvisa,
- att animation inte förändrar fotpunkten,
- att tilekanter möts utan glipor,
- att objekt sorteras korrekt,
- att minnes- och draw-call-kostnad är rimlig,
- att grafik fungerar på TV-avstånd.

### Steg 10 — Uppdatera dokumentation

Uppdatera vid behov:

- `ART-DIRECTION.md`,
- `ASSET-PLAN.md`,
- `TECHNICAL-DESIGN.md`,
- `PROJECT-STATUS.md`,
- `CHANGELOG.md`,
- manuella testinstruktioner.

## Separata assetpipelines

## Pixel art

### När pixel art är lämpligt

Pixel art passar när spelet eftersträvar:

- en medvetet låg eller mellanhög intern upplösning,
- skarp visuell rytm,
- begränsad palett,
- tydlig retro- eller stiliserad identitet,
- relativt små, kontrollerade animationer.

### Regler

- Välj en fast intern pixelgrid.
- Håll samma pixelskala mellan alla assets.
- Skala endast med heltalsfaktorer när det är möjligt.
- Använd nearest-neighbor-filtrering.
- Undvik automatiskt antialiasing.
- Undvik halvtransparenta kantpixlar om stilen inte uttryckligen kräver dem.
- Definiera en gemensam palett eller tydliga palettregler.
- Håll konturtjocklek och ljusriktning konsekvent.
- Skapa animationer frame för frame med stabil fotpunkt.

### SpriteKit

För pixel art bör projektet normalt:

- använda en intern logisk upplösning eller konsekvent kameraskala,
- ställa texture filtering till nearest där det krävs,
- undvika subpixelpositioner för kritisk pixelperfektion,
- kontrollera att skalning inte skapar shimmering,
- testa både rörelse och stillbild på faktisk TV.

### Varningssignaler

- olika pixelstorlek mellan figur och miljö,
- roterade eller skalade pixelassets med suddiga kanter,
- genererad pixel art som egentligen är nedskalad målad grafik,
- oavsiktliga färggradienter eller alfakanter,
- för små detaljer för TV-avstånd.

## Högupplöst 2D

### När högupplöst 2D är lämpligt

Passar när spelet behöver:

- mjuka former och kurvor,
- målad eller cartoon-lik presentation,
- mer nyanserad ljussättning,
- stora figurer eller kameranära objekt,
- flexiblare skalning än strikt pixel art.

### Regler

- Definiera en designstorlek och exportskala.
- Generera eller rita med tillräcklig upplösning för avsedd maximal visning.
- Håll motivets fotpunkt och bounding box konsekvent.
- Kontrollera alfa-kanter mot både mörka och ljusa bakgrunder.
- Begränsa onödigt stora transparenta marginaler.
- Separera lager som behöver animeras oberoende.
- Planera texture atlases efter faktisk användning och samtidighet.
- Komprimera utan att skapa tydliga artefakter.

### Varningssignaler

- mycket stora textures som visas små,
- varierande ljus och perspektiv mellan genereringar,
- motiv som beskärs olika mellan animation frames,
- fina texturer som blir brus på TV,
- alltför stora sprite sheets med mycket tom yta.

## Tilesets

### Grundspecifikation

Ett tileset ska definiera:

- tilemått,
- projektion,
- gridankare,
- kanter som ska kunna mötas,
- terrängfamiljer,
- hörn och övergångar,
- kollisionsklass,
- visuella variationer,
- dekor kontra gameplaybärande tile,
- namngivning och atlasplacering.

### Börja med minsta kompletta familj

Skapa först den minsta tilefamilj som kan bygga ett testområde, exempelvis:

- grundtile,
- horisontell och vertikal kant,
- inre och yttre hörn,
- enkel övergång,
- en variationstile,
- blockerande objekt,
- tydlig mål- eller interaktionstile.

Utöka först när testkartan visar ett konkret behov.

### Sömlöshet och variation

Kontrollera:

- att kanter möts pixelmässigt,
- att färg och ljus inte hoppar mellan tiles,
- att mönster inte bildar störande repetition,
- att variationer inte förändrar kollisionsbetydelsen,
- att auto-tiling-regler kan uttryckas tydligt om de ska användas.

### Tilemaps och SpriteKit

GPT:n ska skilja på:

- grafikens tiledefinition,
- den logiska kartmodellen,
- SpriteKits tilemaprepresentation,
- kollisions- och gameplaydata.

Gameplaykritisk information bör inte endast härledas från filnamn eller bildinnehåll. Använd uttryckliga dataegenskaper eller kartlager där det är rimligt.

## Isometriska assets

### Projektion

Definiera explicit:

- tile width,
- tile height,
- om proportionen exempelvis är 2:1 eller annan,
- vilken punkt som motsvarar tilekoordinaten,
- höjdenhet,
- kamerans orientering,
- rörelseriktningar i värld och på skärm.

### Fotpunkt och djupsortering

För figurer och objekt ska specifikationen ange en gemensam fotpunkt där objektet berör golvet. Den punkten ska användas för:

- placering,
- djupsortering,
- tileanknytning,
- kollisionsrepresentation.

Höga objekts transparenta canvas kan sträcka sig över flera tiles, men deras logiska ankare ska förbli stabilt.

### Kollisioner

Grafikens diamant eller silhuett är sällan en lämplig full kollisionsyta. Definiera separat:

- gångbar basyta,
- blockerande fotavtryck,
- interaktionspunkt,
- eventuella höjd- eller nivådata.

### Ljussättning

Alla isometriska tiles och objekt måste dela:

- samma ljusriktning,
- kompatibel skuggriktning,
- samma kamerahöjd,
- samma proportioner mellan vertikala och horisontella ytor.

### Vanliga fel

- objekt ser ut att sväva,
- olika tiles använder olika diamantvinkel,
- väggar passar inte golvets grid,
- figurer har varierande fotpunkt mellan frames,
- djupsortering använder bildens mittpunkt i stället för fotpunkten,
- dekor blockerar logiskt utan att det framgår visuellt.

## Sprites och karaktärer

### Karaktärsspecifikation

Definiera:

- kroppslängd i relation till tile eller spelvärld,
- riktningar,
- fotpunkt,
- silhuett,
- färgidentifiering,
- utrustning som är permanent eller separat,
- tillstånd som måste synas,
- skugga som separat eller inbakad asset.

### Riktningar

Välj det minsta antal riktningar som ger rätt upplevelse:

- två riktningar med spegling,
- fyra riktningar,
- åtta riktningar,
- fria rotationer för enkla objekt.

Spegla inte asymmetriska karaktärer eller textbärande objekt utan granskning. I isometriska spel kan fyra diagonala riktningar vara mer naturliga än traditionella nord/syd/öst/väst.

### Läsbarhet

Spelaren, fiender och neutrala objekt ska kunna skiljas genom mer än små färgdetaljer. Använd exempelvis:

- silhuett,
- storlek,
- rörelsemönster,
- kontrast,
- kontur,
- tydliga funktionsbärande attribut.

## Animationer

### Animationsplan

För varje animation ska följande definieras:

- namn,
- spelmässigt syfte,
- start- och slutvillkor,
- antal frames,
- bildfrekvens eller frame duration,
- loop eller engångsanimation,
- om den får avbrytas,
- gameplayevent kopplade till en frame,
- övergångar till andra tillstånd.

### Prioritering

För en första prototyp räcker ofta:

- idle,
- rörelse,
- en huvudhandling,
- träff eller skada,
- nederlag.

Skapa inte många kosmetiska animationer innan de spelmässigt viktiga tillstånden fungerar.

### Stabilitet mellan frames

Kontrollera:

- identisk canvasstorlek,
- stabil fotpunkt,
- konsekvent skala,
- oförändrad ljusriktning,
- inga hoppande marginaler,
- begriplig rörelse vid avsedd fps.

### Gameplay och animation

Kritisk spellogik ska inte vara beroende av att en visuell frame råkar visas, om inte kopplingen är uttryckligen modellerad och testbar. Exempel:

- attackträff kan triggas av ett definierat animationsevent,
- men skadetillstånd och cooldown bör ägas av spellogiken,
- animationen ska presentera tillståndet, inte vara enda sanningskällan.

### Sprite sheets

Ett sprite sheet ska ha:

- dokumenterad frameordning,
- konsekvent frame size eller metadata för varierande frames,
- ingen oavsiktlig padding,
- stabil namngivning,
- tydlig relation till texture atlas eller importerad metadata.

Individuella filer är ofta enklare under tidig iteration. Packa när format och innehåll har stabiliserats eller när verktygspipelinen motiverar det.

## Bakgrunder och parallax

Bakgrunder ska stödja läsbarhet och orientering, inte konkurrera med gameplay.

Definiera:

- lagerordning,
- kamerarelativ rörelse,
- repetitionssätt,
- perspektiv och horisont,
- kontrastbudget,
- om lagret är dekorativt eller gameplaybärande.

Parallax ska vara subtil nog att inte skapa åksjuka eller försämra precision. Testa rörelse på fysisk TV och i spelets faktiska kameratempo.

## UI, HUD och ikoner

UI-assets ska följa `05-CONTROLLER-AND-TV-UX.md` och:

- vara tydliga på soffavstånd,
- fungera med controllerfokus,
- inte vara beroende av hover,
- ha tydliga valda, aktiva, inaktiva och låsta tillstånd,
- använda symboler med konsekvent betydelse,
- kompletteras med text när symbolen inte är självklar,
- undvika små detaljer och tunna linjer.

Controllerknappar ska visas semantiskt och plattformsanpassat där det är möjligt. Undvik att hårdkoda en specifik kontrollmodell i grafik som måste fungera med flera kontroller.

## Effekter och partiklar

Effekter ska förbättra feedback, inte dölja spelinformation. Bedöm:

- vad spelaren behöver förstå,
- effektens varaktighet,
- kontrast och intensitet,
- mängden samtidiga partiklar,
- behov av pooling,
- reducerade effekter för tillgänglighet,
- prestanda på målplattformen.

Skapa alternativa enklare effekter när full effekt riskerar att försämra bildfrekvens eller läsbarhet.

## Namngivning och mappstruktur

### Principer

- Använd engelska, stabila och maskinläsbara namn.
- Använd samma term i kod, assetplan och filer.
- Undvik versionsord som `final`, `final2` och `new`.
- Lägg variant, riktning och frame i förutsägbar ordning.
- Behåll stabila logiska asset-ID:n även när filen byts ut.

### Exempel

```text
player_idle_s_01.png
player_idle_s_02.png
player_run_ne_01.png
enemy_guard_attack_w_03.png
tile_forest_ground_base_01.png
tile_forest_edge_n.png
ui_icon_health_full.png
fx_hit_small_01.png
```

### Möjlig struktur

```text
Assets/
  Characters/
    Player/
    Enemies/
  Tiles/
    Forest/
    Interior/
  Props/
  UI/
  Effects/
  Backgrounds/
  Atlases/
```

Anpassa till projektets befintliga struktur i stället för att tvinga fram denna mall.

## Texture atlases och prestanda

Texture atlases kan minska texturebyten och samla relaterade assets, men ska organiseras efter faktisk användning.

Lämpliga grupper kan vara:

- en spelarkaraktär och dess animationer,
- en fiendefamilj,
- en nivåmiljös tiles och props,
- HUD och gemensamt UI,
- återkommande effekter.

Undvik:

- en enda enorm atlas för hela spelet,
- atlaser med assets som aldrig används samtidigt,
- mycket tom yta,
- att dubbletter skapas i flera atlaser utan avsikt,
- att källfiler försvinner utan reproducerbar pipeline.

Dokumentera vilka assets som är källmaterial och vilka som är genererad eller packad output.

## Bildgenerering som arbetsverktyg

### Lämpliga användningar

- utforska art direction,
- skapa ett första stilprov,
- ta fram miljö- eller karaktärskoncept,
- generera mindre familjer av props,
- skapa bakgrundslager,
- skapa utgångsmaterial för tiles och sprites,
- skapa UI-ikoner med en tydlig gemensam specifikation.

### Begränsningar

Bildgenerering kan ha svårt med:

- exakt identiska karaktärer över många bilder,
- pixelperfekta tilekanter,
- stabil fotpunkt över animationsframes,
- exakt sprite sheet-grid,
- konsekvent utrustning och små detaljer,
- sömlösa övergångar,
- transparent bakgrund utan artefakter.

GPT:n ska därför inte lova teknisk perfektion enbart från generering. Den ska planera för granskning, korrigering och ibland manuell efterbearbetning.

### Promptunderlag för assetgenerering

En bra genereringsspecifikation bör beskriva:

- assettyp och funktion,
- visuell stil,
- perspektiv,
- motiv och silhuett,
- färgpalett,
- ljusriktning,
- bakgrund/transparens,
- canvasmått och marginal,
- riktning eller pose,
- vad som uttryckligen inte ska finnas,
- hur asseten ska matcha befintliga referensassets.

För en serie assets ska en gemensam stilreferens eller tidigare godkänt asset användas när verktyget stödjer det.

## Beslut och avvägningar

### Samma GPT eller separat grafik-GPT

Grafik som direkt används i spelet ska normalt hanteras av samma GPT eftersom:

- assetkrav beror på spelmekanik och arkitektur,
- integration, filnamn och atlaser måste samordnas,
- perspektiv och kollisionsmodell måste förstås,
- zip-projektet är gemensam sanningskälla.

En separat grafik-GPT kan senare vara relevant för omfattande konceptkonst, marknadsföringsmaterial och fristående illustration, men är inte nödvändig för version 1.0.

### Individuella PNG-filer eller sprite sheets

Använd individuella filer när:

- assets ändras ofta,
- animationerna är få,
- enkel granskning och versionshantering är viktigast.

Använd sprite sheets eller atlaser när:

- formatet är stabilt,
- animationer har många frames,
- laddning och draw calls behöver optimeras,
- verktygspipelinen kan skapa dem reproducerbart.

### Inbakad eller separat skugga

Separat skugga ger flexibilitet men fler noder. Inbakad skugga är enklare men kan bli fel vid varierande underlag, höjd eller ljus. För isometriska figurer är en separat enkel kontaktskugga ofta praktisk.

### Fyra eller åtta riktningar

Fyra riktningar minskar assetmängden. Åtta ger mjukare analog rörelse men fördubblar i praktiken animationsarbetet. Välj efter faktisk spelkänsla, inte bara controllerkapacitet.

## Kontrollfrågor

Ställ bara frågor som väsentligt ändrar assetlösningen. När svaret kan senareläggas ska GPT:n välja ett rimligt standardantagande och dokumentera det.

Viktiga frågor kan vara:

1. Är detta koncept-, prototyp- eller produktionsgrafik?
2. Är stilen pixel art eller högupplöst 2D?
3. Vilket perspektiv och vilken kameraskala används?
4. Vilket pixelmått eller logiskt mått gäller?
5. Behövs två, fyra eller åtta riktningar?
6. Ska bakgrunden vara transparent?
7. Finns ett godkänt stilprov som nya assets måste matcha?
8. Ska asseten animeras eller delas i separata lager?
9. Är asseten gameplaykritisk eller dekorativ?
10. Ska den fungera i både tvOS- och macOS-versionen med samma skala?

Standardantaganden när projektet inte anger annat:

- skapa först ett litet prov,
- använd transparent PNG för sprites och UI,
- håll skugga separat när flexibilitet behövs,
- behåll engelska filnamn,
- prioritera TV-läsbarhet framför små detaljer,
- använd projektets befintliga perspektiv och skala,
- skapa placeholder före stort produktionspaket.

## Checklistor

### Före grafikarbete

- Har jag läst projektets design- och art direction-dokument?
- Vet jag om asseten är koncept, placeholder eller produktion?
- Är perspektiv, skala och ljusriktning definierade?
- Finns ett befintligt asset att matcha?
- Vet jag vilken funktion asseten har i gameplay?
- Är pixel art eller högupplöst 2D vald?
- Är tilemått, fotpunkt eller pivot definierad?
- Är minsta nödvändiga assetmängd identifierad?
- Har inspirations- och originalitetskrav kontrollerats?

### Efter generering eller produktion

- Har filen rätt pixelmått och format?
- Är bakgrunden och alfakanterna korrekta?
- Matchar perspektiv, skala, palett och ljus övriga assets?
- Är motivet centrerat eller förankrat enligt specifikationen?
- Är animationens fotpunkt stabil?
- Möts tilekanter utan glipor?
- Finns artefakter, dubbletter eller oavsiktlig text?
- Är filnamn och frameordning korrekta?
- Är asseten läsbar i riktig gameplayzoom?

### Efter integration

- Laddas samtliga textures utan fel?
- Fungerar animationer med avsedd hastighet och övergång?
- Har kollisionsyta och logiskt ankare bevarats?
- Är filtering och skalning rätt för stilen?
- Är atlas- och mappstruktur konsekvent?
- Fungerar grafiken på både macOS-testmål och tvOS?
- Är TV-läsbarheten manuellt kontrollerad?
- Har projektstatus, assetplan och changelog uppdaterats?
- Är temporära och oanvända filer borttagna från releasezippen?

## Vanliga misstag

### Generera ett helt spelpaket innan stilprovet godkänts

Förebygg genom att först skapa en liten representativ familj och kontrollera den i spelkontext.

### Behandla konceptbilder som färdiga sprites

Förebygg genom att kräva teknisk assetspecifikation, transparenskontroll, beskärning, ankare och integrationstest.

### Blanda pixel art och nedskalad högupplöst grafik

Förebygg genom att välja en pipeline och kontrollera faktisk pixelgrid, filtering och palett.

### Olika perspektiv eller ljusriktning mellan assets

Förebygg med `ART-DIRECTION.md`, godkänt referensasset och visuell kontroll före massproduktion.

### Instabil fotpunkt i animationer

Förebygg med identisk canvas och uttryckligt ankare i varje frame.

### Göra kollisionsytan lika stor som hela bilden

Förebygg genom att definiera logisk fotyta och separera dekorativ bildyta från fysisk representation.

### För mycket transparent marginal

Förebygg genom normaliserad bounding box och automatiserad eller reproducerbar beskärning.

### För små detaljer på TV

Förebygg genom att testa asseten i slutlig gameplayzoom på fysisk TV och prioritera silhuett och kontrast.

### För stora textures och atlaser

Förebygg genom assetbudget, gruppering efter samtidig användning och kontroll av faktisk visningsstorlek.

### Otydlig käll- och outputstruktur

Förebygg genom att separera redigerbara källassets från exporterad runtimegrafik och dokumentera genereringssteg.

### Kopiera referensspelets visuella identitet

Förebygg genom abstrakt inspirationsanalys och projektets egna art direction-regler enligt `03-INSPIRATION-AND-DIFFERENTIATION.md`.

## Projektdokumentation

### `ART-DIRECTION.md`

Bör innehålla:

- stil och ton,
- perspektiv,
- proportionssystem,
- färgpalett,
- ljus och skuggor,
- konturer och detaljnivå,
- TV-läsbarhetsregler,
- exempel på godkända och icke godkända uttryck,
- pipelineval för pixel art eller högupplöst 2D.

### `ASSET-PLAN.md`

Bör innehålla:

- prioriterad assettabell,
- specifikation och status,
- beroenden,
- placeholder kontra produktion,
- fil- och atlasplacering,
- ansvariga öppna frågor.

### `ASSET-PIPELINE.md`

Skapa vid mer omfattande produktion. Dokumentera:

- källformat,
- genererings- och efterbearbetningssteg,
- exportinställningar,
- namngivning,
- atlaspackning,
- validering,
- hur pipeline kan upprepas.

### Projektstatus och changelog

När assets ändras ska statusen ange:

- vad som skapats eller ersatts,
- om asseten är placeholder eller produktion,
- vad som är integrerat,
- vad som är visuellt granskat,
- vad som återstår att testa på Apple TV.

## Hänvisningar

- `01-GPT-ROLE-AND-PRINCIPLES.md` — övergripande arbetssätt och prioriteringar.
- `02-GAME-DESIGN-FOUNDATIONS.md` — spelvision, prototypfas och scope.
- `03-INSPIRATION-AND-DIFFERENTIATION.md` — referensspel och egen visuell identitet.
- `04-TVOS-SPRITEKIT-ARCHITECTURE.md` — rendering, SpriteKit-struktur och prestanda.
- `05-CONTROLLER-AND-TV-UX.md` — TV-läsbarhet, HUD och controllerfokus.
- `06-PROJECT-ZIP-WORKFLOW.md` — filhantering och rena projektleveranser.
- `07-TESTING-AND-RELEASE.md` — verifiering på macOS, tvOS och fysisk Apple TV.
