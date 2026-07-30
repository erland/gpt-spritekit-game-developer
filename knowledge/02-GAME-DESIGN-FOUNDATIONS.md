# Grundprinciper för speldesign

## Syfte

Denna fil ger genreoberoende stöd för att gå från spelidé till testbar kärnupplevelse. Fokus ligger på praktiska designbeslut, scope, prototyper, balans och playtesting.

## När filen ska användas

Använd filen när GPT:n:

- analyserar en ny spelidé,
- hjälper till att formulera kärnloop och mål,
- avgör vad som ska ingå i första prototypen,
- granskar progression, svårighetskurva eller feedback,
- avgör om en fråga kan simuleras eller måste provspelas,
- behöver minska scope utan att förlora kärnupplevelsen.

## Huvudansvar

Filen äger:

- spelarupplevelse,
- kärnloop,
- mål och feedback,
- progression,
- svårighetskurva,
- onboarding,
- scope,
- prototyper och vertical slices,
- playtesting,
- genreoberoende balans,
- skillnaden mellan mätbara system och spelkänsla.

## Avgränsning

- Detaljerade genreprofiler finns i `genres/`.
- Referensspel och originalitet ägs av `03-INSPIRATION-AND-DIFFERENTIATION.md`.
- Implementation i SpriteKit ägs av `04-TVOS-SPRITEKIT-ARCHITECTURE.md`.
- Grafikpipeline ägs av `08-GAME-ASSET-REQUIREMENTS-AND-INTEGRATION.md`.
- Release- och testprocedurer ägs av `07-TESTING-AND-RELEASE.md`.

## Från idé till spelbar kärna

En spelidé är inte tillräckligt definierad förrän det går att svara på:

1. Vad gör spelaren oftast?
2. Varför gör spelaren det?
3. Vilka beslut eller färdigheter gör aktiviteten intressant?
4. Hur får spelaren återkoppling?
5. Vad förändras över tid?
6. Vad innebär framgång och misslyckande?

### Kärnupplevelse

Kärnupplevelsen beskriver vad spelet ska få spelaren att känna eller bemästra, exempelvis:

- precision och rytm,
- taktisk kontroll,
- upptäckarglädje,
- press under begränsad tid,
- problemlösning,
- riskfylld improvisation,
- samarbete och kommunikation.

Kärnupplevelsen ska styra mekanik, tempo, feedback och scope.

### Kärnloop

Kärnloopen är den återkommande cykeln av handling, feedback och nytt beslut.

Exempel:

- **Shoot 'em up:** undvik → skjut → samla → förbättra position → möt svårare våg.
- **Plattformsspel:** observera → rörelse/hopp → landa eller misslyckas → justera timing → fortsätt.
- **Strategi:** analysera läge → välj handling → se konsekvens → omvärdera resurser och position.

En användbar kärnloop ska kunna beskrivas utan berättelse eller innehållslista.

## Designanalys för nya idéer

När en idé introduceras ska GPT:n vid behov analysera:

1. huvudgenre och sekundärgenre,
2. önskad spelarupplevelse,
3. kärnloop,
4. central designrisk,
5. central teknisk risk,
6. minsta spelbara prototyp,
7. system som bör vänta,
8. vad som kan simuleras,
9. vad som kräver provspelning,
10. hur tvOS och controller påverkar designen.

## Mål, regler och feedback

### Tydliga mål

Spelaren ska förstå:

- vad som ska göras nu,
- varför det spelar roll,
- hur framsteg märks,
- vad som orsakar misslyckande,
- vad nästa meningsfulla val är.

Målet kan vara explicit eller upptäckas genom spel, men brist på avsikt är inte samma sak som mysterium.

### Feedback

Varje viktig handling bör ge relevant återkoppling genom en eller flera kanaler:

- visuell förändring,
- animation,
- ljud,
- controller vibration där lämpligt,
- UI,
- förändrat spelvärde,
- förändrat motståndarbeteende.

Feedback ska vara läsbar på TV-avstånd och skilja viktig information från dekor.

### Konsekvens och förutsägbarhet

Spelaren behöver kunna bygga en mental modell. Regler får vara komplexa, men de bör vara konsekventa. Otydlig slump, dolda undantag och inkonsekvent kollisionsbeteende skapar frustration snarare än utmaning.

## Progression

Progression kan vara:

- **mekanisk:** nya förmågor eller system,
- **kompetensbaserad:** spelaren blir bättre,
- **innehållsbaserad:** nya områden, fiender eller pussel,
- **numerisk:** starkare statistik eller resurser,
- **narrativ:** ny information eller nya mål.

Fråga alltid vilken progression som förstärker kärnupplevelsen. Lägg inte till progression enbart för att förlänga spelet.

### Undvik snöbollseffekter

I strategi- och resursspel bör tidiga fördelar inte automatiskt göra senare beslut irrelevanta. Testa:

- om den ledande spelaren får både mer resurser och bättre position,
- om en dålig tidig tur kan återhämtas,
- om alternativa strategier förblir möjliga,
- om spelet borde avslutas tidigare när utgången redan är avgjord.

## Svårighetskurva

Svårighet kan skapas genom:

- högre krav på precision,
- mindre tid,
- fler samtidiga hot,
- mer komplex information,
- hårdare resursbegränsning,
- fler kombinationer av redan introducerade regler.

Öka inte alla dimensioner samtidigt. Introducera, träna, kombinera och variera.

En vanlig struktur:

1. introducera ett element säkert,
2. låt spelaren demonstrera förståelse,
3. kombinera med tidigare element,
4. skapa variation eller press,
5. ge återhämtning före nästa topp.

## Onboarding

Onboarding ska lära genom handling när möjligt.

Bra onboarding:

- introducerar ett koncept i taget,
- använder faktisk spelkontroll,
- ger direkt feedback,
- låter spelaren prova utan stor bestraffning,
- återanvänder senare samma koncept i svårare form.

Undvik långa texttutorials för mekaniker som kan läras genom en säker testsituation.

## Scope

### Scope-triangeln

Varje projekt balanserar ungefär:

- mängd innehåll,
- kvalitet/polish,
- systemkomplexitet.

För en ensam utvecklare måste minst en dimension hållas låg.

### Prioriteringsordning

1. kärnkontroll och återkoppling,
2. central mekanik,
3. vinst/förlust eller tydligt mål,
4. ett representativt område eller scenario,
5. grundläggande fiende, hinder eller beslutsmotstånd,
6. därefter innehåll och polish.

### Vad som normalt ska vänta

- många spelbara karaktärer,
- omfattande berättelse,
- stora mängder slutgrafik,
- avancerade meta-system,
- flera spellägen,
- omfattande onlinefunktioner,
- generell editor eller motorplattform.

## Prototyper

### Riskprototyp

En riskprototyp besvarar en specifik fråga och får gärna vara ful eller tillfällig.

Exempel:

- känns analog rörelse bra med controller?
- klarar SpriteKit mängden projektiler?
- fungerar isometrisk djupsortering med höga objekt?
- ger strategisystemet meningsfulla val?

Prototypen ska ha ett definierat beslutskriterium innan den byggs.

### Minsta spelbara prototyp

Den minsta spelbara prototypen ska innehålla:

- en kontrollerbar spelare eller beslutspunkt,
- ett tydligt mål,
- en central mekanik,
- feedback,
- möjlighet till framgång eller misslyckande,
- tillräckligt motstånd för att testa kärnupplevelsen.

### Vertical slice

En vertical slice är ett litet men representativt utsnitt med mer realistisk presentation och produktionsstruktur. Den kommer efter att riskprototyperna har besvarat de största frågorna.

## Balans

Balans betyder inte att alla alternativ är identiska. Bra balans innebär att:

- flera val är rimliga i olika situationer,
- risk motsvaras av möjlig belöning,
- dominerande strategier inte gör andra val meningslösa,
- spelaren förstår varför ett resultat uppstod,
- slump skapar variation utan att utplåna beslut.

### Balansmetoder

- analytiska tabeller,
- simulationskörningar,
- botstrategier,
- känslighetsanalys,
- telemetri,
- riktad playtesting,
- jämförelse av extrema strategier.

Simulering kan visa att ett system är snedfördelat. Den kan inte ensam visa att systemet är roligt, tydligt eller känns rätt.

## Simulering kontra provspelning

### Lämpligt att simulera

- sannolikheter,
- resursflöden,
- genomsnittlig skada,
- vapeneffektivitet,
- enhetsbalans,
- turantal,
- progressionstakt,
- frekvens av specifika händelser,
- strategiers ungefärliga vinstfrekvens.

### Kräver faktisk provspelning

- rörelsekänsla,
- hoppkänsla,
- kontrollrespons,
- läsbarhet,
- spänning,
- tempo,
- intuitivitet,
- frustration kontra rättvis utmaning,
- om en spelare förstår feedbacken.

## Playtesting

### Testa en fråga åt gången

Varje testomgång bör ha ett huvudsyfte, exempelvis:

- Förstår spelaren målet utan förklaring?
- Känns analog rörelse för trög?
- Är riskbelöningen i power-ups tydlig?
- Finns ett dominerande öppningsdrag?

### Observera före förklaring

Undvik att hjälpa spelaren direkt. Notera:

- var spelaren tvekar,
- vilka regler som glöms,
- var feedback misstolkas,
- vilka strategier som uppstår spontant,
- när koncentrationen eller intresset sjunker.

### Skilj problem från lösning

När en spelare säger ”lägg till en karta” kan grundproblemet vara orientering, inte avsaknad av kartfunktion. Dokumentera först problemet, sedan möjliga lösningar.

## Rekommenderat arbetsflöde

1. Formulera kärnupplevelsen i en mening.
2. Beskriv kärnloopen.
3. Identifiera största designrisken.
4. Definiera en riskprototyp eller minsta spelbar prototyp.
5. Ange tydliga beslutskriterier.
6. Implementera med placeholdergrafik.
7. Testa eller simulera rätt typ av fråga.
8. Dokumentera observationer.
9. Justera en eller få variabler åt gången.
10. Skapa vertical slice först när kärnan håller.

## Kontrollfrågor

- Vad ska spelaren känna eller bemästra?
- Vad gör spelaren om och om igen?
- Vad är det mest intressanta beslutet?
- Vad är den största risken för att spelet inte blir roligt?
- Vilken minsta prototyp kan falsifiera idén?
- Vad kan tas bort utan att kärnupplevelsen försvinner?
- Vad måste provspelas och vad kan simuleras?
- Hur lång ska en omgång eller bana vara?
- Hur påverkar TV-avstånd och controller designen?

## Checklistor

### Före prototyp

- Kärnupplevelsen är formulerad.
- Kärnloopen är beskriven.
- Största designrisken är identifierad.
- Prototypens beslutskriterium är tydligt.
- Scope är tillräckligt litet.
- Placeholdergrafik accepteras.

### Efter prototyp

- Frågan som prototypen byggdes för är besvarad eller tydligare.
- Testresultat skiljs från antaganden.
- Observationer är dokumenterade.
- Nästa beslut är tydligt.
- Prototypkod som inte ska vidare används inte slentrianmässigt som produktionsarkitektur.

## Vanliga misstag

- Börja med berättelse och innehåll innan kärnmekaniken fungerar.
- Testa många variabler samtidigt.
- Tolka en enskild spelares lösningsförslag som själva problemet.
- Använda simulering som ersättning för spelkänsla.
- Lägga till fler system för att rädda en svag kärnloop.
- Göra prototypen så polerad att den blir dyr att kasta bort.
- Förväxla svårighet med otydlighet.

## Projektdokumentation

Relevanta dokument:

- `GAME-DESIGN.md` — vision, kärnloop, regler, mål och scope.
- `PLAYTEST-NOTES.md` — testfrågor, observationer och beslut.
- `BALANCE-NOTES.md` — parametrar, simuleringar och balanshypoteser.
- `PROJECT-STATUS.md` — aktuell fas och nästa beslut.
- `DECISIONS.md` — fattade designbeslut och motiv.

## Hänvisningar

- `03-INSPIRATION-AND-DIFFERENTIATION.md` — arbete med referensspel.
- `genres/` — genreberoende risker och utvecklingsordning.
- `04-TVOS-SPRITEKIT-ARCHITECTURE.md` — teknisk implementering.
- `07-TESTING-AND-RELEASE.md` — verifiering och release.
