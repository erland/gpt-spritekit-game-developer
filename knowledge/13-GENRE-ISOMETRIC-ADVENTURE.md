# Genre: Isometriskt actionäventyr

## Syfte

För 2D-isometriska actionäventyr, utforskningsspel och pussel/action-hybrider med fast isometrisk projektion.

## Genre och kärnupplevelse

Spelaren ska förstå position, blockering, höjd och om objekt ligger framför eller bakom utan att perspektivet skapar onödig frustration.

## Vanliga varianter och hybridformer

Rumsbaserat äventyr, sammanhängande karta, action/pussel, infiltration/stealth och lätt RPG-progression.

## Kärnloop

Utforska → tolka hinder och interaktioner → lös strid eller pussel → få föremål/information → öppna passage → fortsätt.

## Centrala mekaniker

World/tile/screen-transformer, 4/8-riktningsrörelse, footpoint-sortering, kollisionsytor, occlusion, interaktion och höjdregler.

## Viktigaste designrisker

Otydlig stickriktning, fel depth sorting, motsägande visuell/kollisionsgeometri, inkonsekvent höjd, pixeljakt och perspektiv utan spelvärde.

## Viktigaste tekniska risker

Koordinatkonvertering, footpoint-sortering, pathfinding på logiskt rutnät, occlusion, kamera, atlasstorlek och transparens.

## Minsta spelbara prototyp

Ett område med golv, två höga objekt, passage framför/bakom, rörelse, en fiende, en interaktion, ett föremål och låst utgång.

## Rekommenderad utvecklingsordning

1. Logiskt world coordinate system.
2. World-to-screen och footpoint sorting.
3. Testområde för överlappning.
4. Interaktion och fiende.
5. Occlusion och höjd.
6. Större tileset och nivåverktyg.

## Parametrar att justera

Tile width/height, world scale, rörelseriktning, footpoint offset, z-sorteringsnyckel, kollisionspolygoner, occlusion fade och interaktionsradie.

## Vanliga misstag

Sortera på nodcentrum, använda bildtiles som world model, kollision från alfakanter, producera tileset för tidigt och blanda vinklar/ljusriktningar.

## Playtestfrågor

Är riktningen intuitiv? Förstår spelaren framför/bakom? Är interaktioner tydliga? Ser höjd konsekvent ut?

## Vad som kan simuleras

Pathfinding, räckvidd, sorteringsordning och koordinattransformer kan testas automatiskt; läsbarhet måste playtestas.

## tvOS och controller

Skärmrelativ analog input är standard. Visa riktning omedelbart och undvik precision-cursor. Överlapp kräver stark kontrast.

## SpriteKit

Separera logisk värld från projektion. Använd fasta lager plus dynamisk footpoint-sortering. Riskprototypa transparens och atlasbelastning.

## Grafik och assets

6–10 golv/edge-tiles, spelare i 4/8 riktningar, höga props, skuggor, fiende, interaktionsmarkör och effekt med gemensam vinkel/ljus.

## Hänvisningar

- `02-GAME-DESIGN-FOUNDATIONS.md`
- `04-TVOS-SPRITEKIT-ARCHITECTURE.md`
- `05-CONTROLLER-AND-TV-UX.md`
- `08-GAME-ASSET-REQUIREMENTS-AND-INTEGRATION.md`
