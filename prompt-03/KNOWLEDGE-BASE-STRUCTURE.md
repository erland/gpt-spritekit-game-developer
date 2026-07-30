# Kunskapsbasens struktur

## 1. Syfte

Kunskapsbasen ska ge GPT:n återanvändbar och lättgranskad referenskunskap utan att duplicera huvudinstruktionens beteenderegler. Den ska hjälpa GPT:n att fatta konsekventa beslut om speldesign, SpriteKit, tvOS, grafik, projektfiler, tester och releaser.

Kunskapsbasen ska vara:

- modulär,
- kortfattad men praktiskt användbar,
- konsekvent strukturerad,
- tydlig med filansvar,
- enkel att uppdatera,
- lämplig för både nya projekt och zip-baserat underhåll.

## 2. Informationshierarki

Information ska placeras enligt följande ordning:

1. **Huvudinstruktionen** styr beteende, prioriteringar och obligatoriska arbetsregler.
2. **Kunskapsfilerna** ger fördjupning, checklistor, teknikmönster och genrevägledning.
3. **Projektets egna dokument** är sanningskälla för det aktuella spelet.
4. **Aktuell projektzip** är sanningskälla för faktisk kod, assets och filstruktur.
5. **Aktuell officiell dokumentation** används när API:er, plattformsregler eller verktyg kan ha förändrats.

Vid konflikt gäller den mer projektspecifika och aktuella källan, så länge den inte bryter mot huvudinstruktionens säkerhets- och arbetsregler.

## 3. Slutlig filstruktur för version 1.0

```text
knowledge/
├── 00-INDEX.md
├── 01-GPT-ROLE-AND-PRINCIPLES.md
├── 02-GAME-DESIGN-FOUNDATIONS.md
├── 03-INSPIRATION-AND-DIFFERENTIATION.md
├── 04-TVOS-SPRITEKIT-ARCHITECTURE.md
├── 05-CONTROLLER-AND-TV-UX.md
├── 06-PROJECT-ZIP-WORKFLOW.md
├── 07-TESTING-AND-RELEASE.md
├── 08-GAME-ART-AND-ASSET-PIPELINE.md
└── genres/
    ├── 00-GENRE-INDEX.md
    ├── GENRE-PLATFORMER.md
    ├── GENRE-SHOOT-EM-UP.md
    ├── GENRE-TURN-BASED-STRATEGY.md
    ├── GENRE-TOP-DOWN-ACTION.md
    ├── GENRE-ISOMETRIC-ADVENTURE.md
    ├── GENRE-PUZZLE.md
    └── GENRE-LOCAL-MULTIPLAYER.md
```

Referensprojektet placeras separat och ska inte laddas upp som flera lösa kunskapsfiler om det gör kunskapsbasen svåröverskådlig:

```text
reference-project/
├── README.md
├── docs/
├── project/
└── tests/
```

## 4. Filansvar och gränser

### `00-INDEX.md`

**Huvudansvar:** Navigering och översikt.

Ska innehålla:

- kunskapsbasens syfte,
- lista över filer,
- när respektive fil används,
- rekommenderad läsordning,
- hänvisning till huvudinstruktionen,
- versionsinformation.

Ska inte innehålla:

- detaljerad speldesign,
- arkitekturregler,
- genrespecifika råd,
- duplicerade checklistor.

### `01-GPT-ROLE-AND-PRINCIPLES.md`

**Huvudansvar:** Förklara GPT:ns roll, kvalitetsmål och övergripande resonemodell.

Ska innehålla:

- kombinationen speldesign och utveckling,
- relationen mellan design, teknik och innehåll,
- principen spelbarhet före omfattning,
- hur användarens erfarenhetsprofil påverkar kommunikationen,
- hur kunskapsfiler används.

Ska inte vara enda platsen för:

- obligatoriska regler om zip-hantering,
- säkerhetsregler,
- krav på ärlig testredovisning.

Dessa måste även finnas i huvudinstruktionen.

### `02-GAME-DESIGN-FOUNDATIONS.md`

**Huvudansvar:** Genreoberoende speldesign.

Ska innehålla:

- spelarupplevelse,
- kärnloop,
- mål och feedback,
- progression,
- svårighetskurva,
- onboarding,
- scope,
- prototyper,
- playtesting,
- balans,
- skillnaden mellan simulerbart och spelkänsla.

Ska inte innehålla:

- detaljerade SpriteKit-implementationer,
- fullständiga genreprofiler,
- grafikpipeline,
- zip-releaseprocedur.

### `03-INSPIRATION-AND-DIFFERENTIATION.md`

**Huvudansvar:** Arbete med referensspel och egen identitet.

Ska innehålla:

- abstrakt referensspelsanalys,
- identifiering av önskad upplevelse,
- differentieringsmetod,
- praktisk likhetsriskkontroll,
- mall för projektdokumentet `INSPIRATION-AND-DIFFERENTIATION.md`,
- tydlig gräns mellan inspiration och kopiering.

Ska inte innehålla:

- juridiska garantier,
- genrespecifik helhetsdesign,
- teknisk implementation av spelmekanik.

### `04-TVOS-SPRITEKIT-ARCHITECTURE.md`

**Huvudansvar:** Teknisk arkitektur för Swift, SpriteKit och tvOS.

Ska innehålla:

- scen- och nodstruktur,
- spelloop och tidshantering,
- spellogik utanför `SKScene`,
- tillståndshantering,
- fysik och kollisioner,
- kameror,
- animationer,
- texture atlases,
- lokal sparning,
- delad logik mellan tvOS och macOS,
- prestanda,
- SpriteKit-lämplighetsbedömning.

Ska inte innehålla:

- detaljerad controller-UX,
- full releaseprocess,
- genrespecifika balansråd,
- bildgenereringsprompter.

### `05-CONTROLLER-AND-TV-UX.md`

**Huvudansvar:** Inmatning och användarupplevelse på TV.

Ska innehålla:

- spelkontroller,
- input mapping,
- dead zones,
- anslutning och frånkoppling,
- paus,
- lokalt multiplayerstöd,
- fokusnavigering,
- TV-läsbarhet,
- safe areas,
- textstorlek,
- soffavstånd,
- tillgänglighetsprinciper för kontroll och presentation.

Ska inte innehålla:

- allmän SpriteKit-arkitektur,
- nivådesign,
- releasepaketering,
- Game Center i version 1.0.

### `06-PROJECT-ZIP-WORKFLOW.md`

**Huvudansvar:** Arbete med uppladdade projekt och leverans av uppdaterad zip.

Ska innehålla:

- inventering,
- identifiering av sanningskälla,
- säker redigering,
- bevarande av projektstruktur,
- filstädning,
- versionshantering,
- releasepaketering,
- nedladdningsbar leverans,
- regler för saknade eller ofullständiga projektfiler.

Ska inte innehålla:

- detaljerad teststrategi,
- speldesignteori,
- SpriteKit-arkitekturmönster annat än hänvisningar.

### `07-TESTING-AND-RELEASE.md`

**Huvudansvar:** Verifiering, provspelning och releasekvalitet.

Ska innehålla:

- enhetstester,
- testbar spellogik,
- integrationstestning,
- manuella kontroller i Xcode,
- test på macOS,
- test på fysisk Apple TV,
- controller-testmatris,
- prestanda- och stabilitetskontroller,
- playtestfrågor,
- ärlig testredovisning,
- releasechecklista.

Ska inte innehålla:

- zip-kommandon och paketeringsdetaljer,
- fullständig arkitekturguide,
- genrespecifik spelbalans utöver hänvisningar.

### `08-GAME-ART-AND-ASSET-PIPELINE.md`

**Huvudansvar:** Planering, generering och integration av spelgrafik.

Ska innehålla:

- art direction,
- prototypgrafik kontra produktionsgrafik,
- assetinventering,
- pixel art-pipeline,
- högupplöst 2D-pipeline,
- tilesets,
- isometriska assets,
- sprites och sprite sheets,
- animation frames,
- pivot/origin,
- transparens,
- namngivning,
- texture atlas-integration,
- TV-läsbarhet för grafik,
- kvalitetskontroll av genererade bilder.

Ska inte innehålla:

- generell illustrationsrådgivning utan koppling till spelet,
- full SpriteKit-arkitektur,
- marknadsföringsmaterial i version 1.0.

### `genres/00-GENRE-INDEX.md`

**Huvudansvar:** Vägleda till rätt genreprofil och förklara hybridgenrer.

Ska innehålla:

- profilernas omfattning,
- val av huvud- och sekundärgenre,
- hur flera profiler kombineras,
- gemensam profilstruktur.

Ska inte duplicera profilernas innehåll.

### Genreprofilerna

**Huvudansvar:** Tillämpa gemensamma designprinciper på en specifik genre.

Varje profil ska innehålla:

- kärnupplevelse,
- typisk kärnloop,
- centrala mekaniker,
- viktigaste designrisker,
- viktigaste tekniska risker,
- minsta spelbara prototyp,
- rekommenderad utvecklingsordning,
- parametrar att justera,
- vanliga misstag,
- playtestfrågor,
- simulerbara frågor,
- tvOS-aspekter,
- SpriteKit-aspekter,
- grafikbehov,
- hänvisningar till grundfilerna.

Genreprofilerna ska inte återge generella definitioner eller fullständiga teknikguider.

## 5. Gemensam mall för kunskapsfiler

Varje kunskapsfil ska använda följande struktur när den passar ämnet:

```markdown
# Titel

## Syfte
Kort beskrivning av vad filen hjälper GPT:n att göra.

## När filen ska användas
Konkreta situationer där innehållet är relevant.

## Huvudprinciper
De viktigaste ämnesspecifika principerna.

## Rekommenderat arbetsflöde
Stegvis metod som GPT:n kan följa.

## Beslut och avvägningar
Vanliga val, konsekvenser och varningssignaler.

## Kontrollfrågor
Frågor som bara ställs när svaret påverkar resultatet väsentligt.

## Checklistor
Kort, praktiskt verifieringsunderlag.

## Vanliga misstag
Problem GPT:n ska upptäcka eller förebygga.

## Projektdokumentation
Vilka projektfiler som ska skapas eller uppdateras.

## Hänvisningar
Närliggande kunskapsfiler utan att duplicera deras innehåll.

## Avgränsning
Vad filen uttryckligen inte ansvarar för.
```

Alla rubriker behöver inte användas i varje fil. Strukturen ska anpassas utan att förlora filens tydliga ansvar.

## 6. Gemensam mall för genreprofiler

```markdown
# Genre: <namn>

## Genre och kärnupplevelse
## Vanliga varianter och hybridformer
## Kärnloop
## Centrala mekaniker
## Viktigaste designrisker
## Viktigaste tekniska risker
## Minsta spelbara prototyp
## Rekommenderad utvecklingsordning
## Parametrar att justera
## Vanliga misstag
## Playtestfrågor
## Vad som kan simuleras
## tvOS och controller
## SpriteKit
## Grafik och assets
## Hänvisningar
```

## 7. Läsordning och beroenden

### Normal generell fråga

1. `00-INDEX.md`
2. `01-GPT-ROLE-AND-PRINCIPLES.md`
3. relevant ämnesfil
4. relevant genreprofil
5. projektets egna dokument

### Ny spelidé

1. `02-GAME-DESIGN-FOUNDATIONS.md`
2. relevant genreprofil
3. `04-TVOS-SPRITEKIT-ARCHITECTURE.md`
4. `05-CONTROLLER-AND-TV-UX.md`
5. `08-GAME-ART-AND-ASSET-PIPELINE.md` vid grafikbehov

### Spel inspirerat av befintligt spel

1. `03-INSPIRATION-AND-DIFFERENTIATION.md`
2. `02-GAME-DESIGN-FOUNDATIONS.md`
3. relevant genreprofil
4. projektets `INSPIRATION-AND-DIFFERENTIATION.md`

### Teknisk implementation

1. `04-TVOS-SPRITEKIT-ARCHITECTURE.md`
2. `05-CONTROLLER-AND-TV-UX.md` vid input eller TV-UI
3. relevant genreprofil
4. `07-TESTING-AND-RELEASE.md`

### Zip-baserad förändring

1. huvudinstruktionens obligatoriska filregler
2. `06-PROJECT-ZIP-WORKFLOW.md`
3. projektets egna dokument och kod
4. relevant ämnesfil
5. `07-TESTING-AND-RELEASE.md`

### Grafikarbete

1. `08-GAME-ART-AND-ASSET-PIPELINE.md`
2. relevant genreprofil
3. `04-TVOS-SPRITEKIT-ARCHITECTURE.md` för atlas och integration
4. `05-CONTROLLER-AND-TV-UX.md` för TV-läsbarhet

## 8. Regler mot överlappning

### En princip ska ha en ägare

Varje större ämne ska ha en huvudfil. Andra filer får sammanfatta högst några meningar och därefter hänvisa vidare.

Exempel:

- kärnloop ägs av `02-GAME-DESIGN-FOUNDATIONS.md`,
- controllerinput ägs av `05-CONTROLLER-AND-TV-UX.md`,
- texture atlas-teknik ägs av `04-TVOS-SPRITEKIT-ARCHITECTURE.md`,
- assetnamngivning ägs av `08-GAME-ART-AND-ASSET-PIPELINE.md`,
- zip-städning ägs av `06-PROJECT-ZIP-WORKFLOW.md`,
- testredovisning ägs av `07-TESTING-AND-RELEASE.md` och är dessutom obligatorisk i huvudinstruktionen.

### Hänvisa i stället för att kopiera

När en fil behöver ett ämne som ägs någon annanstans ska den:

1. beskriva den lokala konsekvensen,
2. länka till huvudfilen,
3. inte återge hela checklistan eller teorin.

### Duplicering som är tillåten

Kort upprepning är tillåten när den behövs för:

- säkerhet,
- obligatorisk testärlighet,
- projektzippen som sanningskälla,
- tvOS som produktplattform,
- SpriteKit som standardspår,
- tydlig gräns mot direkt kopiering.

Dessa kärnregler ska finnas i huvudinstruktionen och kan kort återges i relevanta kunskapsfiler.

### Versionskontroll av innehåll

Vid ändring ska följande kontrolleras:

- påverkas huvudinstruktionen,
- påverkas filens huvudansvar,
- finns samma regel i en annan fil,
- behöver hänvisningar uppdateras,
- påverkas en genreprofil,
- behöver `00-INDEX.md` eller changelog uppdateras.

## 9. Kontrollmatris för filansvar

| Ämne | Huvudägare | Sekundär hänvisning |
|---|---|---|
| GPT-roll och kommunikationsnivå | `01-GPT-ROLE-AND-PRINCIPLES.md` | Huvudinstruktionen |
| Kärnloop och scope | `02-GAME-DESIGN-FOUNDATIONS.md` | Genreprofiler |
| Inspirationsspel och differentiering | `03-INSPIRATION-AND-DIFFERENTIATION.md` | Genreprofiler |
| SpriteKit-arkitektur | `04-TVOS-SPRITEKIT-ARCHITECTURE.md` | Genreprofiler |
| Controller och TV-UX | `05-CONTROLLER-AND-TV-UX.md` | Genreprofiler |
| Projektzip och filstädning | `06-PROJECT-ZIP-WORKFLOW.md` | `07-TESTING-AND-RELEASE.md` |
| Tester och releasekvalitet | `07-TESTING-AND-RELEASE.md` | Genreprofiler |
| Grafik och assetpipeline | `08-GAME-ART-AND-ASSET-PIPELINE.md` | Genreprofiler |
| Genrespecifik design | respektive genreprofil | `02-GAME-DESIGN-FOUNDATIONS.md` |
| Isometrisk specialdesign | `GENRE-ISOMETRIC-ADVENTURE.md` | Arkitektur och assetpipeline |
| Lokal multiplayer | `GENRE-LOCAL-MULTIPLAYER.md` | Controller och arkitektur |

## 10. Storlek och skrivstil

Kunskapsfiler ska:

- prioritera handlingsbara råd,
- använda korta exempel,
- undvika långa historiska bakgrunder,
- undvika upprepning av API-dokumentation,
- skilja tydligt mellan rekommendation, krav och alternativ,
- använda svenska med engelska tekniska termer där det ger precision,
- vara tillräckligt fristående för att kunna läsas separat.

Riktvärden:

- grundfil: normalt 1 500–4 000 ord,
- genreprofil: normalt 1 000–2 500 ord,
- indexfil: normalt under 1 000 ord.

Riktvärdena är inte hårda gränser. Tydlighet och täckning är viktigare än exakt längd.

## 11. Projektdokument kontra GPT-kunskap

Kunskapsbasen ska beskriva **hur** projekt dokumenteras. Den ska inte innehålla projektets faktiska designbeslut.

Projektets zip ska vid behov innehålla:

- `GAME-DESIGN.md`,
- `TECHNICAL-DESIGN.md`,
- `PROJECT-STATUS.md`,
- `INSPIRATION-AND-DIFFERENTIATION.md`,
- `ART-DIRECTION.md`,
- `ASSET-PLAN.md`,
- `PLAYTEST-NOTES.md`,
- `KNOWN-ISSUES.md`,
- `CHANGELOG.md`.

Det aktuella projektets dokument har företräde framför generella exempel i kunskapsbasen.

## 12. Definition of Done för Prompt 3

Prompt 3 är färdig när:

- den slutliga kunskapsfilstrukturen är definierad,
- varje fil har tydligt ansvar och tydlig avgränsning,
- gemensam mall finns,
- genreprofilmall finns,
- läsordning och beroenden finns,
- regler mot överlappning finns,
- kontrollmatris finns,
- tidigare kontrollfrågor utom namnfrågan är beslutade,
- nästa prompt kan skapa de tre första kunskapsfilerna utan nya strukturfrågor.
