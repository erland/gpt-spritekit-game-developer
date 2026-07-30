# [PLAN3] Produktionssäker grafik- och assetpipeline

## 1. Syfte

Förbättra GPT:ns hantering av spelgrafik så att den tydligt skiljer mellan visuell idéutforskning och tekniskt användbara produktionsassets. Planen ska minska risken att ett snyggt presentationsark felaktigt behandlas som ett färdigt tileset, sprite sheet eller texture atlas.

[PLAN3] ändrar inte GPT:ns övergripande uppdrag. Den fördjupar grafikflödet i `knowledge/08-GAME-ASSET-REQUIREMENTS-AND-INTEGRATION.md`, berör relevanta testfall och kan vid behov kräva mindre justeringar i huvudinstruktionen utan att överskrida 8 000 tecken.

## 2. Målbild

När användaren ber om ett tileset, sprite sheet, animation sheet eller annan spelgrafik ska GPT:n:

1. klassificera vilken typ av asset som efterfrågas,
2. fastställa dess mognadsnivå,
3. skapa en teknisk specifikation före generering,
4. skilja presentationsmaterial från spelbara assets,
5. validera resultatet mot tekniska krav,
6. märka resultatet ärligt,
7. paketera relevanta filer som en sammanhållen produktionsleverans.

GPT:n ska aldrig kalla ett asset produktionsklart enbart för att det ser visuellt övertygande ut.

---

## 3. Asset Maturity Model

Inför fyra standardnivåer.

### A. Design Sheet

Syfte:

- utforska stil, färg, form, material och variation,
- jämföra visuella alternativ,
- skapa art direction.

Egenskaper:

- kan innehålla rubriker, anteckningar, ramar och flera varianter,
- behöver inte följa ett exakt rutnät,
- behöver inte vara direkt användbart i spelet,
- ska aldrig beskrivas som tileset, sprite sheet eller produktionsasset utan tydlig kvalificering.

### B. Prototype Asset

Syfte:

- användas i en spelbar prototyp,
- verifiera läsbarhet, skala, animation eller mekanik.

Egenskaper:

- ska vara tekniskt användbart nog för import,
- får ha mindre kvalitetsbrister,
- behöver inte vara fullständigt optimerat eller konsekvent,
- ska märkas som prototypasset.

### C. Production Candidate

Syfte:

- vara kandidat för slutlig användning efter validering.

Krav:

- korrekt dimension och grid,
- transparent bakgrund där det krävs,
- definierad pivot/origin,
- konsekvent perspektiv och ljusriktning,
- korrekt marginal och cellplacering,
- dokumenterad namngivning,
- validerade tile-skarvar eller animation frames där det är relevant.

Ett misslyckat eller ofullständigt krav blockerar klassificering som produktionsklart.

### D. Production Ready

Syfte:

- vara godkänt för projektets produktionspipeline.

Krav:

- samtliga tekniska och visuella kontroller är godkända,
- integrationen i SpriteKit är verifierad,
- assetmanifest och eventuell atlasmetadata är konsekventa,
- assetet är testat i relevant scen och skala,
- eventuella manuella kontroller är dokumenterade.

`Production Ready` får endast användas när det finns faktisk verifiering, inte enbart modellens bedömning.

---

## 4. Asset Type Classification

GPT:n ska klassificera leveransen som en eller flera av följande typer:

- Design Sheet
- Individual Sprite
- Tile Sheet
- Sprite Sheet
- Animation Sheet
- UI Sheet
- Icon Sheet
- Background
- Parallax Layer
- VFX Sheet
- Texture Atlas
- Asset Manifest
- Import/Integration Package

Varje typ ska ha egna tekniska kontroller. Ett Design Sheet får inte användas som synonym för Tile Sheet.

---

## 5. Presentation kontra produktion

Inför en tydlig beslutspunkt.

När användaren ber om exempelvis ett tileset ska GPT:n avgöra om användaren vill ha:

1. ett presentationsark för att hitta stilen,
2. ett rent prototypsheet,
3. en produktionskandidat,
4. en komplett produktionsleverans.

Om avsikten inte är tydlig ska GPT:n normalt rekommendera:

- Design Sheet först när stilen inte är fastställd,
- Prototype Asset direkt när spelmekanik behöver testas,
- Production Candidate först när art direction och teknisk specifikation är beslutade.

När användaren uttryckligen ber om ett rent produktionssheet ska GPT:n inte lägga till:

- rubriker,
- ramar,
- instruktionstext,
- kod,
- vattenstämplar,
- dekorativ bakgrund,
- mockup-element.

---

## 6. Teknisk assetspecifikation

Före generering av ett tekniskt asset ska GPT:n fastställa eller föreslå:

- assettyp,
- mognadsnivå,
- spelperspektiv,
- pixelmått,
- cellstorlek,
- rader och kolumner,
- marginal och spacing,
- färgrymd och filformat,
- transparenskrav,
- pivot/origin/fotpunkt,
- ljusriktning,
- skuggregler,
- kollisionsrepresentation,
- animationsriktningar och frameantal,
- texture-atlasgrupp,
- namngivningskonvention,
- SpriteKit-användning,
- TV-läsbarhetskrav.

För isometriska assets ska specifikationen dessutom omfatta:

- tile width och tile height,
- diamantens footprint,
- baslinje/fotpunkt,
- höjd ovanför tileplanet,
- depth sorting-regel,
- om skuggan hör till assetet eller renderas separat.

---

## 7. Valideringsmodell

Skapa en standardiserad valideringsrapport med relevanta kontroller.

### Gemensamma kontroller

- korrekt filformat,
- korrekt pixelmått,
- korrekt alpha/transparens,
- inga oönskade texter, ramar eller vattenstämplar,
- konsekvent stil och palett,
- konsekvent perspektiv,
- konsekvent ljusriktning,
- korrekt pivot/origin,
- konsekvent namngivning,
- SpriteKit-kompatibilitet,
- läsbarhet på TV.

### Tileset-kontroller

- exakt grid,
- en definierad tile per cell,
- inga oavsiktliga övertramp mellan celler,
- sömlösa kanter där det krävs,
- korrekt variant- och kantfamilj,
- separering mellan ground tiles, walls och props.

### Sprite- och animationskontroller

- konsekvent kroppsskala och fotpunkt,
- samma canvas och placering mellan frames,
- rätt frameordning,
- inga oavsiktliga hopp i siluett eller skugga,
- dokumenterad frame rate och loopregel.

### Resultatstatus

Varje kontroll ska märkas som:

- Godkänd
- Underkänd
- Inte verifierad
- Inte relevant

GPT:n ska inte ersätta `Inte verifierad` med ett antagande.

---

## 8. Production Artifact Package

När användaren ber om en produktionsleverans ska GPT:n, när det är relevant, skapa ett paket som kan innehålla:

- `assets/<name>.png`
- `assets/<name>@2x.png` om projektet kräver det
- `manifest/<name>.json`
- `ASSET-MANIFEST.md`
- `VALIDATION-REPORT.md`
- `SPRITEKIT-INTEGRATION.md`
- eventuell atlasdefinition eller importstruktur
- `README.md`
- licens- eller källinformation när externa assets används

Paketet ska tydligt ange:

- assettyp,
- mognadsnivå,
- vilka kontroller som genomförts,
- vad som återstår manuellt,
- hur assetet importeras,
- hur det refereras i kod.

---

## 9. Programmatisk efterbearbetning

GPT:n ska föredra programmatisk efterbearbetning när exakta tekniska krav inte kan garanteras direkt av bildgenereringen.

Exempel:

- beskärning till exakta celler,
- normalisering av canvasstorlek,
- transparent bakgrund,
- placering i exakt grid,
- generering av manifest,
- kontroll av alpha och marginaler,
- uppdelning av individuella sprites,
- sammansättning av atlas,
- automatiska seam-tester.

Bildgenerering ska behandlas som en källa till visuellt material, inte automatiskt som en exakt exportmotor.

---

## 10. SpriteKit-integration

GPT:n ska kunna skapa eller beskriva:

- fil- och atlasstruktur,
- `SKTextureAtlas`-användning,
- namngivning av textures,
- animation med `SKAction.animate`,
- pivot-/anchorPoint-strategi,
- tilemap- eller nodbaserad placering,
- z-position/depth sorting,
- kollisionsformer som är separerade från visuella bounds,
- fallback till placeholder om assetet inte godkänns.

Integrationsstatus ska skiljas från assetstatus. Ett visuellt godkänt asset är inte fullt produktionsklart förrän relevant integration har verifierats.

---

## 11. Revidera T05

Det nuvarande grafiktestet ska delas upp.

### T05A — Design Sheet

Testa att GPT:n kan skapa eller specificera ett sci-fi-konceptark för isometriska miljöassets.

Godkänt när:

- leveransen tydligt märks som Design Sheet,
- presentationsgrafik tillåts,
- den inte beskrivs som rent tileset.

### T05B — Programmatically Sliceable Prototype Asset Sheet

Testa att GPT:n kan specificera och skapa ett rent prototypsheet.

Godkänt när:

- rubriker, kod och dekor saknas,
- grid och cellmått är definierade,
- ground tiles och props separeras.


**rc10 clarification:** A mixed visual sheet is not sufficient. T05B must classify ground tiles, wall/edge tiles, multi-tile structures, props, interactive objects, effects, and signage; document canvas size versus logical footprint and visual overflow; and provide a machine-readable manifest or deterministic cell map.

### T05C — Validation

Testa att GPT:n granskar resultatet och redovisar Godkänd, Underkänd eller Inte verifierad per kontroll.

### T05D — Production Candidate

Testa att GPT:n kan skapa eller paketera en produktionskandidat med manifest och valideringsrapport.

### T05E — SpriteKit Integration

Testa att GPT:n beskriver eller genomför atlasstruktur, namngivning och användning i SpriteKit.

---

## 12. Förändringar i kunskapsbasen

### Primär ändring

Utöka:

- `knowledge/08-GAME-ASSET-REQUIREMENTS-AND-INTEGRATION.md`

med:

- Asset Maturity Model,
- Asset Type Classification,
- presentation kontra produktion,
- valideringsmodell,
- Production Artifact Package,
- programmatisk efterbearbetning.

### Möjliga följdändringar

Granska och vid behov justera:

- `knowledge/04-TVOS-SPRITEKIT-ARCHITECTURE.md`
- `knowledge/07-TESTING-AND-RELEASE.md`
- `knowledge/13-GENRE-ISOMETRIC-ADVENTURE.md`
- `config/FINAL-INSTRUCTIONS.md`
- `prompt-14/TEST-PACK.md`
- `prompt-14/TEST-CASES.json`

Ingen ny knowledge-fil ska skapas om innehållet ryms tydligt i fil 08. Detta bevarar marginalen under gränsen 20 knowledge-filer.

---

## 13. Instruktionsbudget

Huvudinstruktionen är 7 707 tecken och har begränsad marginal.

Därför ska [PLAN3]:

- primärt lägga detaljer i knowledge-filer,
- endast lägga en kort styrregel i huvudinstruktionen om den behövs,
- efter varje ändring mäta Unicode-tecken,
- hålla instruktionen under 8 000 tecken,
- helst lämna minst 150 teckens marginal.

Föreslagen kort styrregel:

> Skilj alltid presentationsark, prototypassets, produktionskandidater och verifierade produktionsassets. Kalla inget produktionsklart utan dokumenterad teknisk validering och relevant integrationskontroll.

Om regeln redan täcks semantiskt ska befintlig text omformuleras i stället för att bara läggas till.

---

## 14. Rekommenderad promptindelning

### [PLAN3 Prompt 1] — Modell och krav — KLAR

- inför Asset Maturity Model,
- inför Asset Type Classification,
- definiera presentation kontra produktion,
- definiera teknisk assetspecifikation,
- uppdatera knowledge-fil 08.

### [PLAN3 Prompt 2 KLAR] — Validering och leveranspaket

Genomfört i `1.0.0-rc6`:

- valideringsmodell med Godkänd, Underkänd, Inte verifierad och Ej tillämplig,
- Production Artifact Package med output, manifest, integration och validering,
- reproducerbar programmatisk efterbearbetning,
- utökade SpriteKit-integrationskrav,
- regler för manifest, källor och rättigheter.

### [PLAN3 Prompt 3 KLAR] — Testpaket

Genomfört i `1.0.0-rc7`:

- T05 har ersatts av T05A–T05E,
- maskinläsbara testfall har uppdaterats,
- positiva kriterier och automatiska underkännandekriterier har införts,
- ett konceptark kan inte godkännas som rent tileset eller Production Ready,
- testresultatmall, preflightmått och externa verifieringshänvisningar har uppdaterats.

### [PLAN3 Prompt 4] — Instruktion och preflight

- justera huvudinstruktionen med minsta möjliga text,
- kontrollera 8 000-teckensgränsen,
- kontrollera högst 20 knowledge-filer,
- genomför täcknings- och överlappningskontroll,
- paketera ny releasekandidat.

### [PLAN3 Prompt 5] — Praktiskt grafiktest

- kör T05A–T05E i GPT Preview,
- granska faktisk bildgenerering,
- kontrollera manifest och valideringsrapport,
- testa import/integration i ett SpriteKit-projekt,
- dokumentera manuella avvikelser.

Prompt 5 kräver användarens hjälp med GPT Preview och sannolikt Xcode för full verifiering.

---

## 15. Definition of Done

[PLAN3] är klar när GPT:n:

- skiljer Design Sheet från tekniskt Tile Sheet,
- använder fyra mognadsnivåer,
- klassificerar assettyp,
- kräver teknisk assetspecifikation före produktionsgenerering,
- skapar rena sheets utan presentationsgrafik när det efterfrågas,
- redovisar valideringsstatus utan att gissa,
- kan skapa ett sammanhållet Production Artifact Package,
- använder programmatisk efterbearbetning när exakthet krävs,
- skiljer assetvalidering från SpriteKit-integration,
- passerar T05A–T05E,
- fortsatt håller instruktionen under 8 000 tecken,
- fortsatt håller sig under 20 knowledge-filer.

---

## 16. Rekommenderat nästa steg

`[PLAN3 Prompt 1–3]` är genomförda. Nästa arbetsomgång är:

> **[PLAN3 Prompt 4] — justera huvudinstruktionen vid behov och genomför full preflight mot buildergränserna.**

## [PLAN3 Prompt 4] — Completed

Implemented in the rc8 compatibility step and included in `1.0.0-rc9`:

- concise instruction-level asset classification rule,
- explicit Production Ready validation gate,
- preflight against instruction and knowledge limits.
