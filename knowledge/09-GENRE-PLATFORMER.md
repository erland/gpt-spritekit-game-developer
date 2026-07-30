# Genre: 2D-plattformsspel

## Syfte

För sidscrollande plattformsspel, actionplattformare, precision platformers och puzzle-platformers där rörelse och hopp bär upp upplevelsen.

## Genre och kärnupplevelse

Spelaren ska känna direkt och förutsägbar kontroll, kunna läsa hoppavstånd och förstå varför ett försök lyckas eller misslyckas.

## Vanliga varianter och hybridformer

Klassisk linjär plattform, precision platformer, actionplattform, puzzle-platformer och utforskningsplattform.

## Kärnloop

Läs hinder → välj rörelse och hopp → genomför → landa eller misslyckas → fortsätt eller försök igen.

## Centrala mekaniker

Acceleration, inbromsning, hoppimpuls, gravitation, luftkontroll, coyote time, input buffering, markkontakt, kamera, checkpoints och snabb omstart.

## Viktigaste designrisker

Trög eller hal rörelse, svårlästa hopp, överraskningsbaserad svårighet, felaktiga kollisionsytor och för lång tid mellan misslyckande och nytt försök.

## Viktigaste tekniska risker

Stabil update-ordning, envägsplattformar, snabba rörelser, hörnfall, kamera, pixelavrundning och kontinuerlig kollisionsdetektering.

## Minsta spelbara prototyp

En figur, en testarena med 8–12 plattformar, ett rörligt hinder, en fara, en checkpoint och ett mål. Placeholdergrafik räcker.

## Rekommenderad utvecklingsordning

1. Semantisk input och testbar rörelsemodell.
2. Testarena för hopp och landning.
3. Kamera, checkpoint och fara.
4. Playtest och parameterjustering.
5. En fiende eller unik mekanik.
6. Kort vertikal slice.

## Parametrar att justera

Maxhastighet, acceleration, bromsning, hoppimpuls, gravitation, fallhastighet, coyote time, input buffer, luftkontroll och kamera-look-ahead.

## Vanliga misstag

Koppla rå input direkt till fysik, låta fysikmotorn definiera spelkänslan, skapa många banor för tidigt och använda för små visuella detaljer.

## Playtestfrågor

Kan spelaren förutsäga landningen? Känns riktningsbyten avsiktliga? Förstår spelaren misslyckanden? Är kameran hjälpsam?

## Vad som kan simuleras

Sweep-tester kan mäta hopphöjd, hoppavstånd, tid i luften, stoppsträcka och teoretisk nåbarhet, men inte game feel.

## tvOS och controller

Analog stick eller d-pad bör ge semantisk horisontell input. Primärknappen hoppar. HUD och hinder måste vara tydliga på soffavstånd.

## SpriteKit

Håll rörelsemodellen utanför `SKScene`, använd enkla kollisionsformer och tydlig update-ordning. Riskprototypa plattformskanter och snabba rörelser.

## Grafik och assets

Spelare med idle/run/jump/fall, grundtiles, fara, checkpoint, mål och enkel bakgrund. Silhuett och fotkontakt prioriteras.

## Hänvisningar

- `02-GAME-DESIGN-FOUNDATIONS.md`
- `04-TVOS-SPRITEKIT-ARCHITECTURE.md`
- `05-CONTROLLER-AND-TV-UX.md`
- `08-GAME-ASSET-REQUIREMENTS-AND-INTEGRATION.md`
