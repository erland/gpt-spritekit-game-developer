# Continuous Integration

Projektet innehåller `.github/workflows/ci.yml` som:

1. kör på pull requests, push till `main` och manuell start,
2. använder en GitHub-hostad macOS-runner,
3. visar Xcode-version och projektets schemes,
4. kör `ReferenceGameTests` via macOS-schemat,
5. bygger tvOS-targeten för tvOS Simulator,
6. stänger av code signing för CI-byggena.

## Första körningen

Efter att projektet lagts i roten av ett GitHub-repository:

1. pusha workflowfilen,
2. öppna repositoryts Actions-flik,
3. kör workflowt manuellt eller öppna en pull request,
4. kontrollera vilken Xcode-version `macos-latest` ger,
5. lås runner/Xcode-version först om projektet behöver reproducerbar SDK-version.

## Begränsningar

Workflowt:

- distribuerar inte appen,
- installerar inga certifikat,
- kör inte på fysisk Apple TV,
- verifierar inte fysisk controller,
- ersätter inte manuell TV-läsbarhetskontroll.

Arkivering eller distribution kräver separat och säker hantering av Apple-certifikat, provisioning profiles och App Store Connect-uppgifter.
