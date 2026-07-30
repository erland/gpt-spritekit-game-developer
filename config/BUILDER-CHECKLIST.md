# Checklista för GPT-byggaren

## Förberedelser

- Använd webbversionen av ChatGPT för att skapa eller redigera GPT:n.
- Skapa GPT:n med delningsnivån **Endast jag**.

## Konfiguration

- [ ] Ange namnet `SpriteKit Game Designer & Developer`.
- [ ] Klistra in beskrivningen från `GPT-CONFIGURATION.md`.
- [ ] Lägg in en egen eller genererad profilbild enligt ikonbriefen.
- [ ] Klistra in innehållet från `FINAL-INSTRUCTIONS.md` i instruktionsfältet.
- [ ] Lägg in de fyra rekommenderade samtalsstartarna.

## Kunskap

- [ ] Ladda upp de 15 filerna i `KNOWLEDGE-UPLOAD-MANIFEST.md`.
- [ ] Kontrollera att inga historiska eller dubblerade filer har laddats upp.
- [ ] Kontrollera att alla filer har behandlats utan fel.

## Funktioner

- [ ] Aktivera webbsökning.
- [ ] Aktivera Kodtolkare och dataanalys.
- [ ] Aktivera bildgenerering.
- [ ] Aktivera Canvas om det finns och bedöms användbart.
- [ ] Lägg inte till Actions i version 1.0.

## Förhandsvisning

- [ ] Testa en ny spelidé.
- [ ] Testa ett inspirationsspel.
- [ ] Testa en SpriteKit-lämplighetsbedömning.
- [ ] Testa grafik- och assetspecifikation.
- [ ] Testa att GPT:n svarar tekniskt utan onödig nybörjarförklaring.
- [ ] Testa att GPT:n redovisar osäkerhet och testbegränsningar korrekt.

## Nästa steg

Efter grundkonfigurationen ska `[PLAN2 Prompt 13]` genomföra fil- och zip-funktionstestet innan GPT:n delas eller betraktas som version 1.0.

## Storlekskontroll för rc3

- [ ] Bekräfta att hela innehållet i `FINAL-INSTRUCTIONS.md` kan klistras in.
- [ ] Instruktionen är 7 707 Unicode-tecken och ligger under gränsen 8 000.
- [ ] Exakt 16 knowledge-filer är uppladdade; inga historiska dubletter.

## Language consistency check

- Verify a Swedish request produces a Swedish chat response but English code, comments, tests and technical documentation.
- Verify explicitly requested Swedish game UI strings remain Swedish and are treated as localizable content.
