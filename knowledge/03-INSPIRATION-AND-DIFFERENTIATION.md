# Inspiration och differentiering

## Syfte

Denna fil hjälper GPT:n att analysera existerande spel som inspiration, identifiera vad användaren faktiskt vill återskapa på upplevelsenivå och utveckla ett tydligt eget spelkoncept utan att kopiera konkreta uttryck.

## När filen ska användas

Använd filen när användaren:

- säger att spelet ska likna ett existerande spel,
- nämner ett eller flera referensspel,
- vill modernisera ett äldre spelkoncept,
- vill kombinera egenskaper från flera spel,
- vill kontrollera att ett koncept har tillräcklig egen identitet,
- föreslår grafik, banor, karaktärer eller mekaniker som ligger nära en specifik förlaga.

## Huvudansvar

Filen äger:

- abstrakt referensspelsanalys,
- identifiering av önskad upplevelse,
- separation mellan genre och specifikt uttryck,
- praktisk differentieringsmetod,
- likhetsriskkontroll,
- projektdokumentation för inspirationskällor och egna kännetecken.

## Avgränsning

- Filen ger inte juridisk rådgivning eller juridiska garantier.
- Genrehelheter ägs av genreprofilerna.
- Speldesignens allmänna grunder ägs av `02-GAME-DESIGN-FOUNDATIONS.md`.
- Teknisk implementation av mekaniker ägs av arkitektur- och genreprofiler.
- Bildgenerering och assetproduktion ägs av `08-GAME-ART-AND-ASSET-PIPELINE.md`.

## Grundprincip

Utgå inte från frågan:

> Hur kopierar vi detta spel?

Utgå från:

> Vilken upplevelse, rytm eller beslutsstruktur är det användaren vill fånga, och hur kan den uttryckas genom ett eget tema, egna system och eget innehåll?

## Tre nivåer av inspiration

### 1. Abstrakta egenskaper

Dessa är ofta lämpliga som inspiration:

- isometriskt perspektiv,
- korta arkadomgångar,
- resurshantering under press,
- turordningsbaserad positionering,
- kombination av utforskning och pussel,
- risk kontra belöning,
- gradvis introduktion av rörelsemönster.

### 2. Specifik kombination och presentation

Dessa kräver aktiv differentiering:

- nästan identisk kombination av mekaniker,
- mycket lik nivåstruktur,
- igenkännbar visuell komposition,
- samma typ av protagonist, miljö och mål,
- likartad progression och UI,
- samma sekvens av fiender, pussel eller belöningar.

### 3. Konkreta uttryck

Dessa ska inte kopieras:

- namn, logotyper och varumärkesprofil,
- karaktärer och igenkännbara kostymer,
- banor, kartor och rumslayouter,
- grafik, animationer och ljud,
- berättelse, dialog och specifika scener,
- konkreta pussel och lösningar,
- unika fiender, föremål och symboler,
- gränssnitt som nära återger originalet.

## Referensspelsanalys

När ett referensspel nämns ska GPT:n vid behov analysera följande på abstrakt nivå:

### Upplevelse

- Vilken känsla skapar spelet?
- Är det precision, press, upptäckt, planering, maktutveckling eller något annat?
- Vad verkar användaren främst uppskatta?

### Kärnloop

- Vad gör spelaren om och om igen?
- Vilken feedback leder till nästa beslut?
- Vad gör loopen spännande eller tillfredsställande?

### Perspektiv och kontroll

- Kamera och vy,
- rörelsemodell,
- relation mellan input och värld,
- hur kontrollen påverkar tempo och precision.

### Struktur

- banor eller sammanhängande värld,
- ordning eller valfrihet,
- checkpoints,
- progression,
- omgångslängd,
- återspelbarhet.

### Motstånd

- fiender,
- miljöfaror,
- resurspress,
- informationsbrist,
- tidspress,
- taktiska avvägningar.

### Presentation

- tempo,
- informationsnivå,
- stämning,
- läsbarhet,
- ljud och visuell feedback.

Analysen ska beskriva funktion och effekt, inte återge originalets innehåll i detalj.

## Differentieringsmetod

### Steg 1: Identifiera kärnan

Formulera högst tre abstrakta egenskaper som projektet vill inspireras av.

Exempel:

- isometrisk utforskning,
- långsam spänning,
- föremålsbaserade miljöpussel.

### Steg 2: Ta bort referensnamnet

Beskriv spelet utan att nämna inspirationsspelet. Om konceptet inte går att beskriva självständigt är det för svagt differentierat.

Svagt:

> The Last Ninja fast i rymden.

Starkare:

> Ett isometriskt infiltrationsäventyr där en tekniker återställer en övergiven orbitalstation genom att omdirigera ström, manipulera robotbeteenden och ta sig förbi instabila sektorer.

### Steg 3: Skapa egna designpelare

Definiera tre till fem projektunika pelare, exempelvis:

- miljösystem som påverkar flera rum,
- verktyg i stället för traditionella vapen,
- dynamisk strömförsörjning,
- val mellan snabb risk och långsam säkerhet,
- lokal samarbetsmekanik.

### Steg 4: Differentiera minst tre dimensioner

Förändra minst tre av följande på ett genomgripande sätt:

- tema och värld,
- spelarens roll,
- central mekanik,
- målstruktur,
- progression,
- tempo,
- kontrollmodell,
- nivåstruktur,
- visuell stil,
- narrativ ton.

Att endast byta namn, färger eller miljö räcker inte.

### Steg 5: Kontrollera helheten

Granska om spelets kombination av:

- spelare,
- värld,
- kärnloop,
- struktur,
- visuellt språk,
- progression,
- innehåll

fortfarande omedelbart upplevs som en direkt variant av förlagan. I så fall behövs ytterligare designförändringar.

## Likhetsriskkontroll

### Låg risk

- bred genre,
- vanligt perspektiv,
- standardiserad input,
- generiska mekaniker som hopp, skjutande, resurser eller turordning,
- inspiration från tempo eller stämning på abstrakt nivå.

### Behöver aktiv differentiering

- samma ovanliga kombination av system,
- liknande protagonist och värld,
- liknande nivåprogression,
- liknande UI och informationshierarki,
- samma typ av centrala pussel eller motstånd,
- visuella siluetter som nära för tankarna till originalet.

### Ska omarbetas

- återgivning av originalbanor eller kartor,
- kopior av karaktärer eller fiender,
- användning av originalgrafik, musik eller dialog,
- återskapande av specifika pussel och sekvenser,
- namn eller varumärken som antyder officiell koppling,
- uppmaningar att göra spelet så identiskt som möjligt.

## Kombination av flera referenser

Flera referensspel kan minska beroendet av en enda förlaga, men endast om egenskaperna faktiskt omformas till en egen helhet.

Bra arbetsform:

- referens A för tempo,
- referens B för beslutsstruktur,
- referens C för världens öppenhet,
- eget tema och egen kärnmekanik.

Undvik att bara stapla igenkännbara delar från flera spel utan en egen designidé.

## Grafik och visuell identitet

När referensbilder används ska GPT:n abstrahera:

- färgtemperatur,
- kontrastnivå,
- detaljgrad,
- materialkänsla,
- ljusriktning,
- siluettprinciper,
- animationsenergi.

Den ska inte efterlikna specifika karaktärer, logotyper, banor eller ikoniska kompositioner. En egen art direction ska dokumenteras innan större assetproduktion.

## Namngivning och presentation

Kontrollera att projektet har egna:

- titel,
- logotyp,
- karaktärsnamn,
- terminologi,
- fraktions- och platsnamn,
- ikonografi,
- UI-struktur.

Undvik namn som kan uppfattas som uppföljare, remake, port eller officiell anknytning utan rättighetshavarens tillstånd.

## Rekommenderat arbetsflöde

1. Be användaren beskriva vad som är intressant med referensspelet.
2. Bryt ned referensen i abstrakta egenskaper.
3. Välj högst tre primära inspirationspunkter.
4. Skriv en självständig pitch utan referensnamn.
5. Definiera projektunika designpelare.
6. Differentiera tema, mekanik och struktur.
7. Gör en likhetsriskkontroll.
8. Dokumentera förbjudna kopieringsområden.
9. Kontrollera nya design- och grafikförslag mot dokumentet.
10. Uppdatera differentieringsbesluten när projektet utvecklas.

## Kontrollfrågor

- Vad tycker användaren faktiskt om i referensspelet?
- Är det mekaniken, tempot, perspektivet, stämningen eller progressionen?
- Vilka delar kan tas bort utan att den önskade upplevelsen försvinner?
- Vilka egna mekaniker kan bli projektets signatur?
- Hur beskrivs spelet utan referensens namn?
- Vilka visuella och narrativa element måste medvetet undvikas?
- Är likheten lokal till en mekanik eller gäller den hela helheten?

## Mall för projektdokument

Ett projekt som använder referensspel bör kunna skapa:

`INSPIRATION-AND-DIFFERENTIATION.md`

Rekommenderad struktur:

```markdown
# Inspiration och differentiering

## Projektets egen pitch

## Referensspel

## Abstrakta inspirationspunkter

## Projektets egna designpelare

## Medvetna förändringar

## Sådant som inte ska efterliknas

## Visuell och narrativ identitet

## Identifierade likhetsrisker

## Fattade beslut

## Öppna frågor
```

## Checklistor

### Före konceptarbete

- Användaren har beskrivit vad som uppskattas i referensen.
- Inspirationspunkterna är abstrakta.
- Projektet har en egen pitch.
- Minst tre dimensioner ska differentieras.

### Före grafikproduktion

- Egen art direction finns.
- Karaktärer och siluetter är egna.
- UI och ikonografi är egna.
- Referensbilder används för egenskaper, inte för kopiering.

### Före release

- Titel och varumärkesprofil är egna.
- Inga originalassets används utan rättigheter.
- Banor och pussel är egna.
- Projektet kan beskrivas självständigt.
- Kvarstående likhetsrisker är dokumenterade.

## Vanliga misstag

- Tro att namn- och färgbyte räcker.
- Börja återskapa en bana för att ”testa känslan”.
- Kopiera specifika pussel eller fiendemönster.
- Göra en nästan identisk protagonist i nytt tema.
- Använda samma UI-struktur och visuell hierarki.
- Beskriva spelet enbart som ”X fast med Y”.
- Tolka praktisk differentieringskontroll som juridisk garanti.

## Projektdokumentation

- `INSPIRATION-AND-DIFFERENTIATION.md` — huvuddokument.
- `GAME-DESIGN.md` — projektets egen kärnloop och designpelare.
- `ART-DIRECTION.md` — egen visuell identitet.
- `DECISIONS.md` — beslut om avstånd från referenser.
- `ASSET-PLAN.md` — kontroll att assets är egna och konsekventa.

## Hänvisningar

- `02-GAME-DESIGN-FOUNDATIONS.md` — kärnupplevelse, loop och scope.
- `08-GAME-ART-AND-ASSET-PIPELINE.md` — egen art direction och assetproduktion.
- `genres/` — genretypiska egenskaper som inte i sig tillhör ett specifikt spel.
