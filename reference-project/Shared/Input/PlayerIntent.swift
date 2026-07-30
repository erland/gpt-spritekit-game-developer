import CoreGraphics

struct PlayerIntent: Equatable {
    var movement: CGVector = .zero
    var primaryActionPressed = false
    var secondaryActionPressed = false
    var pausePressed = false

    static let neutral = PlayerIntent()
}
