# [PLAN2 Prompt 9] Referensprojektets grund

## Levererat

- tvOS-app som primärt produktmål,
- macOS-app som officiellt utvecklings- och testmål,
- gemensam SwiftUI/SpriteKit-container,
- enkel top-down-`GameScene`,
- semantiskt `PlayerIntent`,
- controllerpolling via GameController,
- radial dead zone,
- flankdetektering för diskreta handlingar,
- anslutnings- och frånkopplingshantering,
- tangentbordsadapter på macOS.

## Medvetet uppskjutet till Prompt 10

- full pausmodell,
- scenövergångar,
- explicit app- och spellägesmaskin,
- frikopplad domänmodell,
- enhetstesttarget,
- integrationstester.

## Verifieringsstatus

Filstruktur, referenser och paketering har verifierats i arbetsmiljön. Xcode-byggning och körning måste verifieras på macOS eftersom Xcode och Apple SDK:er inte finns i denna miljö.
