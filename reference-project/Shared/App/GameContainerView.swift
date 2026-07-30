import SpriteKit
import SwiftUI

struct GameContainerView: View {
    @Environment(\.scenePhase) private var scenePhase
    private let scene: GameScene

    init() {
        let coordinator = SceneCoordinator()
        self.scene = coordinator.makeScene(.game, size: CGSize(width: 1280, height: 720)) as! GameScene
    }

    var body: some View {
        SpriteView(scene: scene, preferredFramesPerSecond: 60)
            .ignoresSafeArea()
            .onChange(of: scenePhase) { _, phase in
                switch phase {
                case .active: scene.applicationDidBecomeActive()
                case .inactive, .background: scene.applicationDidBecomeInactive()
                @unknown default: break
                }
            }
    }
}
