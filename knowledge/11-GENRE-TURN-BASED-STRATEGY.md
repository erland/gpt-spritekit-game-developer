# Genre: Turordningsbaserad strategi

## Syfte

För taktiska rutnätsspel, turbaserad resurshantering och strategispel där diskreta beslut utan realtidspress står i centrum.

## Genre och kärnupplevelse

Spelaren ska kunna förstå läget, jämföra alternativ och se konsekvenser. Meningsfulla beslut är viktigare än regelmängd.

## Vanliga varianter och hybridformer

Taktiskt rutnät, turbaserad ekonomi, kort-/förmågebaserad strategi, asymmetriska fraktioner och deterministiska pusselstrider.

## Kärnloop

Observera → formulera turmål → välj handlingar → förhandsgranska → bekräfta → motståndaren agerar → utvärdera.

## Centrala mekaniker

Turordning, handlingsbudget, position, terräng, räckvidd, enhetsroller, resurser, konsekvensförhandsvisning, AI och vinstvillkor.

## Viktigaste designrisker

Dominerande val, snöbollseffekter, för mycket dold information, långsamma turer, fuskande AI och otydligt UI.

## Viktigaste tekniska risker

Ren regelmotor, AI utan blockering, serialization, pathfinding, line of sight och controllerfokus över rutnät.

## Minsta spelbara prototyp

Liten karta, två enhetstyper per sida, en resurs eller handlingspoäng, ett mål och enkel AI. Match på 10–15 minuter.

## Rekommenderad utvecklingsordning

1. Ren Swift-modell för state och regler.
2. Kommandon och validering.
3. Litet rutnät och två enhetstyper.
4. Enkel heuristisk AI.
5. Controller-UI och förhandsgranskning.
6. Simulering och playtest.

## Parametrar att justera

Handlingspoäng, rörelsekostnad, räckvidd, skada, försvar, resursproduktion, initiativ, terrängbonus, sannolikheter och AI-vikter.

## Vanliga misstag

Regler i noder/animationer, animation som sanningskälla, många enheter för tidigt, dold kritisk information och specialregler för AI.

## Playtestfrågor

Finns flera rimliga val? Förstår spelaren resultaten? När är matchen i praktiken avgjord? Hur lång är en tur med controller?

## Vad som kan simuleras

Win rates, resurskurvor, dominant strategies, time-to-victory, enhetsvärde och slumputfall lämpar sig väl för batchsimulering.

## tvOS och controller

Snap-to-grid, snabbval och kontextmenyer minskar långa markörresor. Kritisk information ska vara läsbar utan små tabeller.

## SpriteKit

Regelmotor, state, kommandon och AI ligger utanför SpriteKit. SpriteKit presenterar kartan och animationerna. Använd reproducerbara seeds och snapshots.

## Grafik och assets

Terrängtiles, fyra enhetssprites, val-/räckviddsmarkeringar, målmarkör, fokusram och stor informationspanel.

## Hänvisningar

- `02-GAME-DESIGN-FOUNDATIONS.md`
- `04-TVOS-SPRITEKIT-ARCHITECTURE.md`
- `05-CONTROLLER-AND-TV-UX.md`
- `08-GAME-ART-AND-ASSET-PIPELINE.md`
