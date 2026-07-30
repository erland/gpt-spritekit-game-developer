# [PLAN2 Prompt 13] Fil- och zip-funktionstest

## Syfte

Verifiera att det planerade GPT-arbetsflödet praktiskt kan:

1. ta emot och läsa en zip,
2. inventera innehållet,
3. arbeta i en separat kopia,
4. ändra befintliga filer och skapa en ny fil,
5. skapa en ny ren zip,
6. verifiera att den nya zippen är läsbar,
7. lämna en faktisk nedladdningsbar fil.

## Testmiljö

Testet kördes i den tillgängliga fil- och kodmiljön. Det verifierar den tekniska filhanteringen som GPT:n är avsedd att använda. Det verifierar inte Xcode-byggning, signering eller körning på Apple TV.

## Testfixture

`prompt-13/fixture/fixture-input.zip` innehöll:

- `README.md`
- `settings.json`

Arbetskopian ändrades genom att:

- uppdatera `settings.json` från version 1 till version 2,
- ändra `enabled` från `false` till `true`,
- lägga till en ändringsmarkering,
- komplettera `README.md`,
- skapa `TEST-RESULT.txt`.

Resultatet sparades som `prompt-13/fixture/fixture-output.zip`.

## Resultat

| Kontroll | Resultat |
|---|---|
| Källzip kunde öppnas | PASS |
| Innehållet kunde inventeras | PASS |
| Arbete skedde i separat katalog | PASS |
| Befintliga text- och JSON-filer kunde ändras | PASS |
| En ny fil kunde skapas | PASS |
| Ny zip kunde skapas | PASS |
| Ny zip klarade integritetstest med `unzip -t` | PASS |
| Input och output har separata SHA-256-värden | PASS |
| Huvudprojektets releasezip kan skapas och länkas | PASS |

## Bevisfiler

- `fixture/SHA256SUMS.txt`
- `fixture/output-inventory.txt`
- `fixture/unzip-test.txt`
- `fixture/fixture-input.zip`
- `fixture/fixture-output.zip`

## Bedömning

Fil- och zip-arbetsflödet fungerar i den tillgängliga miljön. GPT:n kan därför praktiskt hantera det avsedda mönstret: senaste zip som sanningskälla, isolerad arbetskopia, avgränsade ändringar, verifiering och ny releasezip.

## Begränsningar

Testet visar inte att alla framtida zippar kan hanteras utan problem. Särskild försiktighet krävs för:

- mycket stora arkiv,
- krypterade eller lösenordsskyddade arkiv,
- symboliska länkar och ovanliga filrättigheter,
- binära projektformat som kräver externa verktyg,
- filer med konfliktande namn eller skadade arkiv,
- Xcode-byggning som kräver macOS och installerade Apple-SDK:er.

## Slutsats

`[PLAN2 Prompt 13]` är godkänd. Nästa steg är `[PLAN2 Prompt 14]`: testpaket och preflight av GPT:ns instruktioner, kunskapsfiler och konfigurationsunderlag.
