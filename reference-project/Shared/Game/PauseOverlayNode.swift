import SpriteKit

final class PauseOverlayNode: SKNode {
    private let title = SKLabelNode(fontNamed: "Avenir Next Bold")
    private let detail = SKLabelNode(fontNamed: "Avenir Next Medium")

    override init() {
        super.init()
        zPosition = 1000

        let dimmer = SKShapeNode(rectOf: CGSize(width: 1600, height: 1000))
        dimmer.fillColor = SKColor(white: 0, alpha: 0.72)
        dimmer.strokeColor = .clear
        addChild(dimmer)

        title.text = "Paus"
        title.fontSize = 64
        title.position = CGPoint(x: 0, y: 24)
        addChild(title)

        detail.fontSize = 28
        detail.position = CGPoint(x: 0, y: -44)
        addChild(detail)
    }

    required init?(coder aDecoder: NSCoder) { fatalError("init(coder:) has not been implemented") }

    func configure(for reason: PauseReason) {
        switch reason {
        case .userRequested: detail.text = "Tryck Menu/P igen för att fortsätta"
        case .controllerDisconnected: detail.text = "Anslut en controller för att fortsätta"
        case .applicationInactive: detail.text = "Spelet fortsätter när appen blir aktiv igen"
        }
    }
}
