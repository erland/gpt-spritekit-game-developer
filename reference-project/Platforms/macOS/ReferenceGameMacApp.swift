import SwiftUI

@main
struct ReferenceGameMacApp: App {
    var body: some Scene {
        WindowGroup {
            GameContainerView()
                .frame(minWidth: 960, minHeight: 540)
        }
        .windowStyle(.hiddenTitleBar)
    }
}
