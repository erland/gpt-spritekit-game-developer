# Kända begränsningar och öppna verifieringar

## Kvarstående verifiering

- Projektet har inte byggts i Xcode i den miljö där paketet skapades.
- XCTest har inte körts mot en verklig Apple SDK här.
- Controllerinput har inte verifierats med fysisk controller.
- tvOS-layout och bildfrekvens har inte verifierats på fysisk Apple TV.

## Arkitektoniska begränsningar

- `GameSession` lagrar endast en pausorsak åt gången.
- Extern paus återupptas automatiskt när orsaken försvinner.
- Controller mapping är fast och kan inte konfigureras.
- `SceneCoordinator` demonstrerar endast en spelscen.
- Projektet saknar lokal sparning trots att GPT version 1.0 ska kunna vägleda kring det.
- Referensprojektet innehåller ingen isometrisk modul; den är medvetet senarelagd.

## Inte fel i referensens nuvarande scope

- Ingen meny eller laddningsscen.
- Ingen ljudhantering.
- Ingen tilemap eller fysik.
- Ingen lokal multiplayerimplementation.
- Ingen asset catalog med produktionsgrafik.
