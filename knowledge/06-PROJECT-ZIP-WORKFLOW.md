# Projekt- och zip-arbetsflöde

## Syfte

Denna fil beskriver hur GPT:n ska arbeta säkert och reproducerbart med uppladdade spelprojekt, särskilt när användaren lämnar in en zip och förväntar sig en uppdaterad zip tillbaka. Målet är att bevara projektets faktiska struktur, göra avgränsade ändringar, dokumentera resultatet och leverera en ren release utan att låtsas att saknade filer eller tester finns.

## När filen ska användas

Använd denna fil när GPT:n ska:

- ta emot ett befintligt projekt som zip,
- analysera ett projekts struktur och status,
- göra kod-, dokumentations- eller assetändringar,
- städa ett projekt inför leverans,
- skapa en ny versionszip,
- fortsätta ett projekt över flera arbetscykler,
- bedöma om en uppladdning är komplett nog för den begärda ändringen.

## Huvudansvar

Filen äger:

- inventering av projektfiler,
- val av sanningskälla,
- säkert arbetsområde,
- förändringsdisciplin,
- versions- och filnamnshantering,
- städning av releasepaket,
- leverans av ny zip,
- hantering av saknade eller motstridiga filer,
- kontinuitet mellan zip-baserade arbetsomgångar.

## Avgränsning

- Teststrategi och releasekvalitet ägs av `07-TESTING-AND-RELEASE.md`.
- SpriteKit-arkitektur ägs av `04-TVOS-SPRITEKIT-ARCHITECTURE.md`.
- Controller- och TV-UX ägs av `05-CONTROLLER-AND-TV-UX.md`.
- Speldesignbeslut ägs av `02-GAME-DESIGN-FOUNDATIONS.md` och projektets `GAME-DESIGN.md`.
- Grafikpipeline ägs av `08-GAME-ART-AND-ASSET-PIPELINE.md`.

## Grundprinciper

### Senaste kompletta zip är sanningskällan

Utgå från den senast uppladdade kompletta projektzippen. Tidigare chattbeskrivningar, äldre releaser och minnesbilder får inte ersätta faktisk filstruktur.

När flera zippar finns ska GPT:n:

1. identifiera den senaste relevanta versionen,
2. kontrollera versionsnummer och innehåll,
3. undvika att blanda filer från olika releaser utan uttryckligt skäl,
4. dokumentera om en äldre fil används som stöd.

### Arbeta alltid i en kopia

Originalzippen ska lämnas orörd. Packa upp till ett separat arbetsområde och skapa releasezippen från det arbetsområdet.

### Inventera före ändring

Ingen fil ska ändras innan GPT:n har identifierat:

- rotmapp,
- Xcode-projekt eller workspace,
- källkod,
- targets,
- tester,
- assets och texture atlases,
- dokumentation,
- build- och releasefiler,
- versionsinformation,
- uppenbara historiska eller temporära filer.

### Gör minsta rimliga förändring

Bevara:

- befintlig arkitektur,
- filnamn,
- målstruktur,
- kodstil,
- dokumentationsformat,
- användbara scripts och tester.

Större refaktorering ska endast göras när den krävs för uppgiften eller tydligt minskar en konkret risk.

### Skilj projektkälla från genererat material

Identifiera vad som är:

- redigerbar källkod,
- genererad build-output,
- exporterade PDF:er eller bilder,
- cache,
- historiska releaser,
- externa beroenden.

Ändra källan, inte bara en genererad kopia, när projektet har en etablerad genereringspipeline.

## Standardiserat arbetsflöde

### 1. Bekräfta arbetsunderlaget

Kontrollera:

- zipfilens namn och storlek,
- att den går att packa upp,
- om den innehåller en gemensam rotmapp,
- om projektet ser komplett ut,
- om användarens begäran matchar innehållet.

Om zippen är skadad eller saknar kritiska filer ska GPT:n säga exakt vad som saknas och göra allt som fortfarande är möjligt utan att fabricera innehåll.

### 2. Skapa projektinventering

Inventeringen bör minst ange:

- projektets namn,
- aktuell version om den finns,
- plattform och targets,
- huvudsaklig teknik,
- viktiga mappar,
- teststruktur,
- assetstruktur,
- centrala projektdokument,
- bygginstruktioner,
- identifierade risker eller oklarheter.

För större projekt kan inventeringen sparas i `PROJECT-INVENTORY.md` eller sammanfattas i `PROJECT-STATUS.md`.

### 3. Fastställ ändringsomfattning

Översätt användarens önskemål till en konkret förändringslista:

- filer som sannolikt ändras,
- nya filer som behövs,
- beteende som ska bevaras,
- tester som bör påverkas,
- dokumentation som måste uppdateras,
- manuella kontroller som krävs efteråt.

Undvik att lägga till orelaterade förbättringar i samma release.

### 4. Kontrollera projektets egna regler

Läs i första hand:

- `README.md`,
- `PROJECT-STATUS.md`,
- `TECHNICAL-DESIGN.md`,
- `GAME-DESIGN.md`,
- `CONTRIBUTING.md`,
- build-scripts,
- testinstruktioner,
- versions- och releasefiler.

Projektets egna dokument gäller framför generella standardmönster när de är aktuella och konsekventa.

### 5. Genomför ändringen

Under ändringen ska GPT:n:

- hålla diffen fokuserad,
- undvika onödig formattering av orörda filer,
- återanvända befintliga abstraktioner när de är rimliga,
- uppdatera testbar logik samtidigt som produktionkod,
- undvika att lägga in hemligheter, certifikat eller lokala absoluta sökvägar,
- dokumentera nya antaganden.

### 6. Granska ändringen

Kontrollera minst:

- att alla referenser pekar på existerande filer,
- att filnamn och skiftläge är konsekventa,
- att projektfilen inkluderar nya källfiler och assets där detta krävs,
- att inga temporära debug-lösningar har lämnats kvar,
- att borttagna filer inte längre refereras,
- att dokumentation och versionsstatus stämmer.

### 7. Kör möjliga kontroller

Följ `07-TESTING-AND-RELEASE.md` och dokumentera:

- faktiskt körda tester,
- resultat,
- sådant som inte kunde köras,
- manuella tester som återstår i Xcode, på macOS eller Apple TV.

### 8. Uppdatera projektdokumentation

Beroende på projektet bör följande uppdateras:

- `PROJECT-STATUS.md`,
- `CHANGELOG.md`,
- `README.md`,
- `KNOWN-ISSUES.md`,
- design- eller teknikdokument,
- assetplan,
- releasechecklista.

Dokumentationen ska beskriva faktisk status, inte avsedd framtida status.

### 9. Städa releaseinnehållet

Ta normalt bort:

- `.git/`,
- `.DS_Store`,
- Derived Data,
- `xcuserdata`, om det inte finns ett dokumenterat skäl att behålla det,
- build-mappar,
- temporära filer,
- cachefiler,
- editorbackupfiler,
- onödiga loggar,
- historiska releasezippar,
- duplicerade exporter,
- lokala signeringsdata,
- hemligheter och tokens.

Ta inte bort filer bara för att de ser oanvända ut. Kontrollera först referenser, dokumentation och genereringsflöden.

### 10. Versionssätt leveransen

Följ projektets befintliga versionsmodell. Om ingen modell finns, använd en enkel semantisk eller prototypbaserad versionering och dokumentera den.

Exempel:

- `0.6.0` för ny planerad funktion,
- `0.6.1` för korrigering utan ändrad funktionell omfattning,
- `v0_6` endast om projektet redan använder sådan namngivning.

Filnamnet på zippen ska vara tydligt och unikt, exempelvis:

`project-name-v0.6.0.zip`

### 11. Skapa och verifiera zippen

Efter paketering ska GPT:n:

- lista zip-innehållet,
- verifiera att rotstrukturen är korrekt,
- kontrollera att centrala filer finns,
- kontrollera att onödiga build- och cachefiler saknas,
- vid möjlighet provpacka upp zippen i en separat kontrollmapp.

### 12. Leverera med ändringssammanfattning

Leveransen ska ange:

- vad som ändrats,
- vilka filer eller områden som berörts,
- vilka tester som körts,
- vilka tester som återstår,
- kända begränsningar,
- versionsnummer,
- nedladdningslänk till exakt skapad zip.

## Hantering av ofullständiga projekt

### Kritiska filer saknas

Exempel:

- `.xcodeproj` eller `.xcworkspace` saknas,
- projektfilen refererar till filer som inte finns,
- assets saknas,
- centrala källfiler är tomma,
- zippen innehåller bara build-output.

GPT:n ska då:

1. dokumentera det konkreta problemet,
2. inte påstå att projektet kan byggas,
3. genomföra säkra dokument- eller kodändringar om möjligt,
4. undvika att skapa en missvisande komplett release,
5. markera vilka filer som behövs för full verifiering.

### Motstridiga versioner

När versionsnummer i zipnamn, changelog och projektfiler skiljer sig ska GPT:n:

- inte gissa tyst,
- identifiera vilken källa som verkar mest aktuell,
- dokumentera avvikelsen,
- normalisera bara om det är en del av uppgiften eller uppenbart säkert.

### Flera parallella spår

Om projektet innehåller flera exporter, alternativa implementationer eller historiska mappar ska GPT:n först avgöra vilket spår som är aktivt. Bevis kan vara:

- README,
- build-scripts,
- aktuell projektfil,
- senast ändrade källor,
- releaseinstruktioner.

Radera inte alternativa spår utan tydligt beslut.

## Kontinuitet mellan arbetsomgångar

Varje release bör lämna projektet i ett tillstånd där nästa arbetsomgång kan starta enbart från zippen.

Det innebär att zippen bör innehålla:

- aktuell källkod,
- aktuella assets,
- aktuell dokumentation,
- versionsinformation,
- relevanta tester,
- bygg- och körinstruktioner,
- kända problem och nästa steg.

Chatthistorik ska inte vara nödvändig för att förstå projektets aktuella status.

## Vanliga misstag

- Att utgå från en äldre zip eftersom den är bekant.
- Att ändra exporterad output men inte källan.
- Att skriva om stora delar av projektet för en liten funktion.
- Att skapa en zip utan att kontrollera dess innehåll.
- Att lämna med Derived Data eller historiska releaser.
- Att hävda att Xcode-build eller Apple TV-test har körts när de inte har körts.
- Att skapa länkar till filer som inte faktiskt finns i arbetsmiljön.
- Att ta bort filer som verkar gamla men fortfarande används av buildprocessen.
- Att glömma att lägga till nya filer i Xcode-target eller asset catalog.

## Checklistor

### Före ändring

- [ ] Senaste relevanta zip har identifierats.
- [ ] Zippen går att packa upp.
- [ ] Projektets rot och huvudsakliga targets är identifierade.
- [ ] Dokumentation och versionsstatus är lästa.
- [ ] Ändringsomfattningen är avgränsad.
- [ ] Kritiska saknade filer är dokumenterade.

### Före paketering

- [ ] Begärd ändring är genomförd.
- [ ] Referenser och filnamn är kontrollerade.
- [ ] Relevanta tester eller kontroller är körda.
- [ ] Testbegränsningar är dokumenterade.
- [ ] Status och changelog är uppdaterade.
- [ ] Temporära och lokala filer är borttagna.
- [ ] Inga hemligheter eller signeringsdata ingår.

### Efter paketering

- [ ] Zippen går att lista och packa upp.
- [ ] Rätt rotmapp finns.
- [ ] Centrala projektfiler finns.
- [ ] Onödiga build- och cachefiler saknas.
- [ ] Versionsnamnet är konsekvent.
- [ ] Exakt zipfil länkas i svaret.

## Projektdokumentation

GPT:n ska vid behov skapa eller uppdatera:

- `PROJECT-STATUS.md`,
- `CHANGELOG.md`,
- `PROJECT-INVENTORY.md`,
- `KNOWN-ISSUES.md`,
- `RELEASE-CHECKLIST.md`,
- `README.md`.

## Grafik- och assetpaket i projektzippen

När ett Production Artifact Package ingår i leveransen ska zippen bevara dess struktur för output, manifest, integration och validering. Kontrollera särskilt att:

- presentationsmaterial inte blandas med runtime-output,
- källmaterial inte av misstag används av spelets targets,
- manifest refererar till filer som faktiskt finns,
- valideringsrapporten följer med,
- temporära mellanbilder och oanvända genereringsresultat inte följer med utan syfte,
- licens- eller källinformation bevaras när den är relevant.

## Hänvisningar

- `07-TESTING-AND-RELEASE.md` — verifiering, provspelning och releasekvalitet.
- `04-TVOS-SPRITEKIT-ARCHITECTURE.md` — teknisk struktur och SpriteKit-mönster.
- `05-CONTROLLER-AND-TV-UX.md` — controller- och TV-relaterade manuella kontroller.
- `01-GPT-ROLE-AND-PRINCIPLES.md` — övergripande arbets- och kvalitetsprinciper.

## Git- och CI-filer i projektzippen

`.gitignore`, `.github/workflows/`, delade Xcode-schemes och andra reproducerbara CI-filer är projektkällor och ska normalt bevaras i releasezippen. Själva `.git/`-mappen ska däremot normalt tas bort.

Vid projektinventering ska GPT:n kontrollera om:

- en befintlig `.gitignore` behöver kompletteras,
- workflowfiler refererar rätt project/workspace och schemes,
- delade schemes faktiskt följer med projektet,
- workflowt innehåller hårdkodade hemligheter eller lokala sökvägar,
- CI-kommandon fortfarande matchar targets och deployment targets.

Se `16-VERSION-CONTROL-AND-CI.md` för detaljer.

## Language consistency during project changes

When creating or updating files, keep source code, comments, tests and technical project documentation in English even when the request and chat response are in another language. Preserve user-facing localized game strings as content, preferably through the project's localization mechanism. Report existing mixed-language technical material as a consistency issue rather than silently translating large parts outside the requested scope.
