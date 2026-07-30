# Genre: Lokalt flerspelarspel

## Syfte

Kompletterande profil för lokal co-op, versus, party och hot-seat på Apple TV. Kombineras ofta med en annan genreprofil.

## Genre och kärnupplevelse

Spelarna ska omedelbart förstå vem de är, vad de kan göra och hur handlingar påverkar andra. Social tydlighet och rättvisa är centrala.

## Vanliga varianter och hybridformer

Gemensam co-op, lokal versus, party/minigames, hot-seat, asymmetriska roller och drop-in/drop-out.

## Kärnloop

Anslut och tilldela controller → förstå roll och mål → agera → påverka andra eller målet → få resultat → snabb omgång eller fortsättning.

## Centrala mekaniker

Controller discovery, player assignment, join/leave, identifiering, kamera, respawn, paus, disconnect och balans mellan skicklighetsnivåer.

## Viktigaste designrisker

Spelare tappar identitet, dominans utan comeback, orättvis kamera, disconnect förstör state, lång elimination och passiva co-op-spelare.

## Viktigaste tekniska risker

Flera samtidiga controllers, stabil assignment över scener, gemensam kamera/split-screen, fokuskonflikter och reconnect.

## Minsta spelbara prototyp

En arena eller kort bana för två spelare, stabil controlleranslutning, tydlig tilldelning, mål, matchslut, omstart och disconnect-test.

## Rekommenderad utvecklingsordning

1. Controller registry och player slots.
2. Join screen och identifiering.
3. Tvåspelarsprototyp.
4. Kamera, respawn och disconnect.
5. Socialt playtest.
6. Skala till fler spelare.

## Parametrar att justera

Antal spelare, spawnavstånd, invulnerability, matchlängd, poänggräns, respawntid, catch-up, kameraavstånd och disconnect timeout.

## Vanliga misstag

Identifiering enbart med färg, dold controllerassignment, test med bara en controller, multiplayer tillagt sent och lång elimination.

## Playtestfrågor

Vet alla vem de styr? Förstår nya spelare målet? Skapar reglerna samspel? Är matchlängden rätt? Är kameran rättvis?

## Vad som kan simuleras

Win rates, spawnfördelar, poängkurvor och catch-up kan simuleras; social dynamik måste observeras i grupp.

## tvOS och controller

Stöd flera `GCController`, stabil slot mapping och tydligt join/leave-flöde. Använd färg, symbol och position tillsammans.

## SpriteKit

Routa input per player slot till semantiska actions. Bevara assignment över scene transitions. Gemensam kamera bör vara egen komponent.

## Grafik och assets

Distinkta spelare, join-indikatorer, symboler, gemensam eller separat HUD, respawn-effekt och resultatvy.

## Hänvisningar

- `02-GAME-DESIGN-FOUNDATIONS.md`
- `04-TVOS-SPRITEKIT-ARCHITECTURE.md`
- `05-CONTROLLER-AND-TV-UX.md`
- `08-GAME-ART-AND-ASSET-PIPELINE.md`
