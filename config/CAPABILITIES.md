# Rekommenderade funktioner

## Ska aktiveras

### Webbsökning

Används för aktuell och officiell information om:

- tvOS,
- SpriteKit,
- Xcode,
- Game Controller,
- Apple-plattformarnas aktuella API:er och krav.

GPT:n ska prioritera officiell Apple-dokumentation och andra primärkällor för tekniska frågor.

### Kodtolkare och dataanalys

Kritisk funktion för:

- packa upp och skapa zip-filer,
- inventera projekt,
- ändra filer,
- generera nedladdningsbara artefakter,
- köra möjliga tester och statiska kontroller,
- simulera balans och spelsystem,
- analysera data och loggar.

### Bildgenerering

Behöver inte aktiveras för kärnrollen. GPT:n ska normalt skapa tekniska grafikbeställningar, placeholders, granskningsrapporter och SpriteKit-integration i stället för polerad spelgrafik. Aktivera endast bildgenerering om enkla koncept eller tillfälliga prototypbilder uttryckligen ska kunna skapas; använd då inte funktionen som ersättning för den separata Game Graphics Creator.

### Canvas, om tillgängligt

Kan aktiveras för längre kod- och dokumentredigering. Det är användbart men inte nödvändigt för kärnflödet.

## Ska inte konfigureras i version 1.0

### Actions

Inga externa API-actions behövs för första versionen. GitHub-, CI- eller andra integrationer kan utvärderas senare när ett verkligt behov finns.

### Appar eller externa anslutningar

Lägg inte till externa anslutningar enbart för att de finns. Projektzippen och användarens uppladdade filer ska vara den primära arbetsytan i version 1.0.

## Viktig verifiering

Efter att funktionerna aktiverats ska Förhandsvisning verifiera att GPT:n faktiskt kan:

1. ta emot en zip,
2. packa upp och inventera den,
3. skapa eller ändra filer,
4. skapa en ny zip,
5. lämna en fungerande nedladdningslänk.
