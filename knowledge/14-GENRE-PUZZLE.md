# Genre: Pusselspel

## Syfte

För gridpussel, logikspel, begränsade fysikpussel, actionpussel och miljöpussel där förståelse av regler är central.

## Genre och kärnupplevelse

Spelaren ska observera, formulera hypotes, testa och förstå resultatet. Insikt och tydliga regler prioriteras framför gissning.

## Vanliga varianter och hybridformer

Deterministiskt gridpussel, sekvens-/signalpussel, fysikpussel, actionpussel och miljöpussel.

## Kärnloop

Observera state → identifiera mål och regler → välj handling → se konsekvens → uppdatera hypotes → lös eller återställ.

## Centrala mekaniker

Tydligt mål, få handlingar, undo/restart, gradvis regelintroduktion, feedback och hints som inte ger lösningen direkt.

## Viktigaste designrisker

Saknad information, oavsiktliga triviala lösningar, lång återställning, otydligt UI, för många nya regler och övertydliga hints.

## Viktigaste tekniska risker

Deterministisk state, korrekt undo, lösbarhetskontroll, serialization, fysikdeterminism och controllerfokus på stora bräden.

## Minsta spelbara prototyp

En mekanik och 8–12 handgjorda nivåer som introducerar, varierar och kombinerar regeln. Undo och restart från början.

## Rekommenderad utvecklingsordning

1. Ren state- och handlingsmodell.
2. Undo/restart och nivådata.
3. Tre tutorialpussel.
4. Variation och kombination.
5. Playtest av förståelse.
6. Hints och progression.

## Parametrar att justera

Antal handlingar, nivåstorlek, måltrösklar, hintfördröjning, undo-regler, timingfönster och generator constraints.

## Vanliga misstag

Procedural generator för tidigt, regler i presentationen, text i stället för visuell förklaring, lång reset och fler element utan djup.

## Playtestfrågor

Förstår spelaren målet? När uppstår insikten? Är fel informativa? Finns oavsiktliga lösningar? Är progressionen jämn?

## Vad som kan simuleras

Solvers kan verifiera lösbarhet, minsta antal drag, alternativa lösningar och svårighetsproxyer.

## tvOS och controller

Tydlig fokus, få handlingar och snabb undo/restart. Brädet måste vara läsbart utan exakt pekning.

## SpriteKit

Regelmodell och nivådata utanför SpriteKit. Använd kommandon, snapshots eller inversa operationer för undo och deterministiska tester.

## Grafik och assets

Brädtiles, mål, flyttbara objekt, fokusmarkör, success/failure-feedback och stora enkla ikoner.

## Hänvisningar

- `02-GAME-DESIGN-FOUNDATIONS.md`
- `04-TVOS-SPRITEKIT-ARCHITECTURE.md`
- `05-CONTROLLER-AND-TV-UX.md`
- `08-GAME-ASSET-REQUIREMENTS-AND-INTEGRATION.md`
