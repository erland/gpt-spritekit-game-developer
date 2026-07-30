import SpriteKit

#if os(macOS)
import AppKit
#endif

@MainActor
final class GameScene: SKScene {
    private let input: CombinedInputSource
    private var world = GameWorld()
    private var session = GameSession()

    private let worldRoot = SKNode()
    private let player = SKShapeNode(circleOfRadius: 34)
    private let statusLabel = SKLabelNode(fontNamed: "Avenir Next Medium")
    private let actionLabel = SKLabelNode(fontNamed: "Avenir Next Bold")
    private let pauseOverlay = PauseOverlayNode()

    private var previousUpdateTime: TimeInterval?
    private var controllerWasConnected = false

    init(size: CGSize, input: CombinedInputSource) {
        self.input = input
        super.init(size: size)
        scaleMode = .resizeFill
        backgroundColor = SKColor(red: 0.07, green: 0.09, blue: 0.14, alpha: 1)
    }

    required init?(coder aDecoder: NSCoder) { fatalError("init(coder:) has not been implemented") }

    override func didMove(to view: SKView) {
        anchorPoint = CGPoint(x: 0.5, y: 0.5)
        addChild(worldRoot)

        let arena = SKShapeNode(rectOf: CGSize(width: 1180, height: 620), cornerRadius: 36)
        arena.strokeColor = SKColor(white: 0.45, alpha: 1)
        arena.lineWidth = 6
        arena.fillColor = SKColor(white: 0.12, alpha: 1)
        arena.zPosition = -10
        worldRoot.addChild(arena)

        player.fillColor = SKColor(red: 0.25, green: 0.78, blue: 0.95, alpha: 1)
        player.strokeColor = .white
        player.lineWidth = 5
        worldRoot.addChild(player)

        statusLabel.fontSize = 30
        statusLabel.horizontalAlignmentMode = .left
        statusLabel.verticalAlignmentMode = .top
        statusLabel.position = CGPoint(x: -590, y: 345)
        addChild(statusLabel)

        actionLabel.fontSize = 34
        actionLabel.position = CGPoint(x: 0, y: -350)
        addChild(actionLabel)

        pauseOverlay.isHidden = true
        addChild(pauseOverlay)
        controllerWasConnected = input.controller.isControllerConnected
        synchronizePresentation()
    }

    override func update(_ currentTime: TimeInterval) {
        let deltaTime = calculateDeltaTime(currentTime)
        let intent = input.currentIntent()
        handleControllerTransition()
        handlePause(intent: intent)

        if !session.isPaused {
            world.update(intent: intent, deltaTime: deltaTime)
            showActionFeedback(for: intent)
        }
        synchronizePresentation()
    }

    private func calculateDeltaTime(_ currentTime: TimeInterval) -> TimeInterval {
        defer { previousUpdateTime = currentTime }
        guard let previousUpdateTime else { return 0 }
        return min(currentTime - previousUpdateTime, 1.0 / 15.0)
    }

    private func handlePause(intent: PlayerIntent) {
        guard intent.pausePressed else { return }
        session.toggleUserPause()
        previousUpdateTime = nil
    }

    private func handleControllerTransition() {
        let connected = input.controller.isControllerConnected
        if controllerWasConnected && !connected {
            session.pause(reason: .controllerDisconnected)
        } else if !controllerWasConnected && connected {
            session.resumeAfterExternalPause()
            previousUpdateTime = nil
        }
        controllerWasConnected = connected
    }

    private func synchronizePresentation() {
        player.position = world.playerPosition
        statusLabel.text = "Input: \(input.controller.connectionSummary)"

        switch session.state {
        case .playing:
            pauseOverlay.isHidden = true
            worldRoot.isPaused = false
        case .paused(let reason):
            pauseOverlay.configure(for: reason)
            pauseOverlay.isHidden = false
            worldRoot.isPaused = true
        }
    }

    private func showActionFeedback(for intent: PlayerIntent) {
        if intent.primaryActionPressed {
            actionLabel.text = "Primär handling"
            pulsePlayer(scale: 1.22)
        } else if intent.secondaryActionPressed {
            actionLabel.text = "Sekundär handling"
            pulsePlayer(scale: 0.82)
        }

        if actionLabel.text != nil {
            actionLabel.removeAction(forKey: "clearText")
            actionLabel.run(.sequence([.wait(forDuration: 0.8), .run { [weak self] in self?.actionLabel.text = nil }]), withKey: "clearText")
        }
    }

    private func pulsePlayer(scale: CGFloat) {
        player.removeAction(forKey: "pulse")
        player.run(.sequence([.scale(to: scale, duration: 0.08), .scale(to: 1, duration: 0.12)]), withKey: "pulse")
    }

    func applicationDidBecomeInactive() {
        session.pause(reason: .applicationInactive)
        previousUpdateTime = nil
    }

    func applicationDidBecomeActive() {
        session.resumeAfterExternalPause()
        previousUpdateTime = nil
    }

    #if os(macOS)
    override func keyDown(with event: NSEvent) { input.keyboard.keyDown(event) }
    override func keyUp(with event: NSEvent) { input.keyboard.keyUp(event) }
    #endif
}
