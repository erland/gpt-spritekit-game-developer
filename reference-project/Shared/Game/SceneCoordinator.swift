import SpriteKit

@MainActor
final class SceneCoordinator {
    enum SceneID { case game }

    private let input: CombinedInputSource

    init(input: CombinedInputSource = CombinedInputSource()) {
        self.input = input
    }

    func makeScene(_ id: SceneID, size: CGSize) -> SKScene {
        switch id {
        case .game:
            return GameScene(size: size, input: input)
        }
    }
}
