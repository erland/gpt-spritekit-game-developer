import CoreGraphics

@MainActor
final class CombinedInputSource: InputSource {
    let controller: ControllerInputSource
    let keyboard: KeyboardInputSource

    init(
        controller: ControllerInputSource = ControllerInputSource(),
        keyboard: KeyboardInputSource = KeyboardInputSource()
    ) {
        self.controller = controller
        self.keyboard = keyboard
    }

    func currentIntent() -> PlayerIntent {
        let controllerIntent = controller.currentIntent()
        let keyboardIntent = keyboard.currentIntent()

        let combined = CGVector(
            dx: controllerIntent.movement.dx + keyboardIntent.movement.dx,
            dy: controllerIntent.movement.dy + keyboardIntent.movement.dy
        )
        let length = hypot(combined.dx, combined.dy)
        let movement = length > 1
            ? CGVector(dx: combined.dx / length, dy: combined.dy / length)
            : combined

        return PlayerIntent(
            movement: movement,
            primaryActionPressed: controllerIntent.primaryActionPressed || keyboardIntent.primaryActionPressed,
            secondaryActionPressed: controllerIntent.secondaryActionPressed || keyboardIntent.secondaryActionPressed,
            pausePressed: controllerIntent.pausePressed || keyboardIntent.pausePressed
        )
    }
}
