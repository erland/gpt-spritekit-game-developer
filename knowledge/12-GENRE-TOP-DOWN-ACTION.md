# Genre: Top-down-action

## Syfte

För top-down action, twin-stick-inspirerade spel, dungeon action och enklare action-RPG eller stealth/action-hybrider.

## Genre och kärnupplevelse

Spelaren ska snabbt läsa avstånd, riktning, hot och säkra ytor. Rörelse och attack måste kännas samordnade.

## Vanliga varianter och hybridformer

Direkt melee/ranged action, twin-stick, dungeon rooms, stealth/action och lätt action-RPG.

## Kärnloop

Utforska eller gå in i möte → läs hot → positionera → attackera/undvik → samla belöning eller öppna väg → fortsätt.

## Centrala mekaniker

Analog rörelse, attackriktning, cooldown, hit/hurtboxes, dodge/block, fiende-AI, telegraphs, interaktion och kamera.

## Viktigaste designrisker

Inputkonflikt mellan rörelse/sikte, omringning utan utväg, dekor som skymmer hot, knappspam och progression som maskerar svag strid.

## Viktigaste tekniska risker

Stabil analog input, många agents, pathfinding, attacktiming, kamera, occlusion och navigation runt dynamiska hinder.

## Minsta spelbara prototyp

En arena med rörelse, grundattack, dodge eller defensiv handling, två fiendetyper, ett interaktivt objekt och ett mål.

## Rekommenderad utvecklingsordning

1. Rörelse och semantisk input.
2. Attackmodell och hit/hurtboxes.
3. Två fiender.
4. Kamera och arena.
5. Playtest av spacing.
6. Progression och fler rum.

## Parametrar att justera

Rörelsehastighet, attack wind-up/active/recovery, räckvidd, dodge, aggro, knockback, hit-stop, kamera och spawnbudget.

## Vanliga misstag

Träff kopplad implicit till animation, för många fiender tidigt, otydliga dekorgränser, svag kontrast och överdriven fysikstyrning.

## Playtestfrågor

Kan spelaren hålla avstånd? Är attacker läsbara? Känns träffar kraftfulla? Är interaktioner tydliga? Är arenan intressant?

## Vad som kan simuleras

DPS, cooldowns, time-to-kill, spawnmix och drops kan simuleras; spatialt beteende kräver speltest.

## tvOS och controller

En eller två sticks beroende på kontrollschema. Kontextuell interaktion och stora telegraphs är viktiga.

## SpriteKit

Använd explicita attackfaser, separata hit/hurtboxes och gameplay state utanför scenen. Undvik `SKAction` som AI-state machine.

## Grafik och assets

Spelare med idle/move/attack/hurt, två fiender, attackeffekt, arena-tiles, interaktionsikon och enkel HUD.

## Hänvisningar

- `02-GAME-DESIGN-FOUNDATIONS.md`
- `04-TVOS-SPRITEKIT-ARCHITECTURE.md`
- `05-CONTROLLER-AND-TV-UX.md`
- `08-GAME-ASSET-REQUIREMENTS-AND-INTEGRATION.md`
