import CoreGraphics

#if os(macOS)
import AppKit

@MainActor
final class KeyboardInputSource: InputSource {
    private var pressedKeys = Set<UInt16>()
    private var primaryEdge = false
    private var secondaryEdge = false
    private var pauseEdge = false

    func keyDown(_ event: NSEvent) {
        let inserted = pressedKeys.insert(event.keyCode).inserted
        guard inserted else { return }

        switch event.keyCode {
        case 36, 49: primaryEdge = true       // Return, Space
        case 7: secondaryEdge = true          // X
        case 35, 53: pauseEdge = true         // P, Escape
        default: break
        }
    }

    func keyUp(_ event: NSEvent) {
        pressedKeys.remove(event.keyCode)
    }

    func currentIntent() -> PlayerIntent {
        var x: CGFloat = 0
        var y: CGFloat = 0

        if pressedKeys.contains(0) || pressedKeys.contains(123) { x -= 1 } // A, Left
        if pressedKeys.contains(2) || pressedKeys.contains(124) { x += 1 } // D, Right
        if pressedKeys.contains(13) || pressedKeys.contains(126) { y += 1 } // W, Up
        if pressedKeys.contains(1) || pressedKeys.contains(125) { y -= 1 } // S, Down

        let length = hypot(x, y)
        let movement = length > 1
            ? CGVector(dx: x / length, dy: y / length)
            : CGVector(dx: x, dy: y)

        let intent = PlayerIntent(
            movement: movement,
            primaryActionPressed: primaryEdge,
            secondaryActionPressed: secondaryEdge,
            pausePressed: pauseEdge
        )

        primaryEdge = false
        secondaryEdge = false
        pauseEdge = false
        return intent
    }
}
#else
@MainActor
final class KeyboardInputSource: InputSource {
    func currentIntent() -> PlayerIntent { .neutral }
}
#endif
