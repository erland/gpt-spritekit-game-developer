import XCTest
@testable import ReferenceGame_macOS

final class GameWorldTests: XCTestCase {
    func testMovementUsesIntentSpeedAndDeltaTime() {
        var world = GameWorld(playerSpeed: 100)
        world.update(intent: PlayerIntent(movement: CGVector(dx: 1, dy: 0)), deltaTime: 0.5)
        XCTAssertEqual(world.playerPosition.x, 50, accuracy: 0.001)
        XCTAssertEqual(world.playerPosition.y, 0, accuracy: 0.001)
    }

    func testMovementIsClampedToBounds() {
        var world = GameWorld(bounds: .init(minX: -10, maxX: 10, minY: -5, maxY: 5), playerSpeed: 100)
        world.update(intent: PlayerIntent(movement: CGVector(dx: 1, dy: 1)), deltaTime: 1)
        XCTAssertEqual(world.playerPosition, CGPoint(x: 10, y: 5))
    }

    func testZeroDeltaTimeDoesNotMove() {
        var world = GameWorld(playerPosition: CGPoint(x: 2, y: 3))
        world.update(intent: PlayerIntent(movement: CGVector(dx: 1, dy: 1)), deltaTime: 0)
        XCTAssertEqual(world.playerPosition, CGPoint(x: 2, y: 3))
    }
}
