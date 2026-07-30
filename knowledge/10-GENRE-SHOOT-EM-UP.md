# Genre: Shoot 'em up

## Syfte

För vertikala och horisontella shooters, arena shooters och bullet-hell-varianter där projektiler, fiendevågor och positionering är centrala.

## Genre och kärnupplevelse

Spelaren ska läsa hot, hitta säkra rörelsevägar och fatta snabba beslut om position, eld och risk trots hög visuell belastning.

## Vanliga varianter och hybridformer

Klassisk scrolling, bullet hell, arena shooter, roguelite-shooter och lokal co-op.

## Kärnloop

Läs mönster → positionera → skjut eller använd specialförmåga → undvik → samla belöning → gå vidare.

## Centrala mekaniker

Analog rörelse, eld, projektilmönster, fiendevågor, mindre hitboxar, poäng/combo, power-ups och bossfaser.

## Viktigaste designrisker

Visuellt brus, otydliga telegraphs, statiska vinnande strategier, svårighet genom enbart fler projektiler och obalanserade power-ups.

## Viktigaste tekniska risker

Många noder, partiklar och kollisionskontroller, allokeringar per frame, tunneling, inputlatens och stabil bildfrekvens på Apple TV.

## Minsta spelbara prototyp

En spelare, ett vapen, tre fiendetyper, två korta vågor, en power-up och en enkel boss med två mönster.

## Rekommenderad utvecklingsordning

1. Rörelse, skjutning och pooling.
2. Belastnings- och kontrasttest.
3. Tre fiender.
4. Två vågor och boss.
5. Playtest av träffboxar och tempo.
6. Vapenvariation och progression.

## Parametrar att justera

Rörelsehastighet, dead zone, fire rate, projektilhastighet, hitbox, spawnfrekvens, hälsa, power-up-frekvens, combo och maximal projektilmängd.

## Vanliga misstag

Skapa många vapen för tidigt, samma färg för dekor och hot, hårdkodade vågor, full spriteyta som hitbox och överdrivna partiklar.

## Playtestfrågor

Är hot tydliga? Känns träffar rättvisa? Finns positionella val? Är bossattacker läsbara? Blir händerna trötta?

## Vad som kan simuleras

Skadeutfall, time-to-kill, drop rates, poängkurvor och teoretisk vågbelastning kan simuleras.

## tvOS och controller

Kalibrerad dead zone och tydlig färg-/formkodning. Hållen skjutknapp bör stödjas. Lokal co-op kräver robust spelaridentifiering.

## SpriteKit

Använd objektpooler, datadrivna vågor och begränsade kontaktmasker. Profilera noder, partiklar och draw calls på fysisk Apple TV.

## Grafik och assets

Spelarfarkost, tre fiendesilhuetter, egna/fientliga projektiler, explosion, power-up, bakgrund och HUD med hög kontrast.

## Hänvisningar

- `02-GAME-DESIGN-FOUNDATIONS.md`
- `04-TVOS-SPRITEKIT-ARCHITECTURE.md`
- `05-CONTROLLER-AND-TV-UX.md`
- `08-GAME-ASSET-REQUIREMENTS-AND-INTEGRATION.md`
