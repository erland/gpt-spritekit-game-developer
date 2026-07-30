import CoreGraphics

struct GameWorld: Equatable {
    struct Bounds: Equatable {
        var minX: CGFloat
        var maxX: CGFloat
        var minY: CGFloat
        var maxY: CGFloat
    }

    private(set) var playerPosition: CGPoint
    let bounds: Bounds
    let playerSpeed: CGFloat

    init(
        playerPosition: CGPoint = .zero,
        bounds: Bounds = .init(minX: -550, maxX: 550, minY: -270, maxY: 270),
        playerSpeed: CGFloat = 520
    ) {
        self.playerPosition = playerPosition
        self.bounds = bounds
        self.playerSpeed = playerSpeed
    }

    mutating func update(intent: PlayerIntent, deltaTime: TimeInterval) {
        guard deltaTime > 0 else { return }
        playerPosition.x += intent.movement.dx * playerSpeed * deltaTime
        playerPosition.y += intent.movement.dy * playerSpeed * deltaTime
        playerPosition.x = min(max(playerPosition.x, bounds.minX), bounds.maxX)
        playerPosition.y = min(max(playerPosition.y, bounds.minY), bounds.maxY)
    }
}
