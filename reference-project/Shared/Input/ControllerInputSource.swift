import CoreGraphics
import GameController

@MainActor
final class ControllerInputSource: NSObject, InputSource {
    private let notificationCenter: NotificationCenter
    private var controller: GCController?
    private var previousPrimaryPressed = false
    private var previousSecondaryPressed = false
    private var previousPausePressed = false

    private(set) var connectionSummary = "Ingen controller ansluten"
    var isControllerConnected: Bool { controller?.extendedGamepad != nil }

    init(notificationCenter: NotificationCenter = .default) {
        self.notificationCenter = notificationCenter
        super.init()

        notificationCenter.addObserver(
            self,
            selector: #selector(controllerDidConnect(_:)),
            name: .GCControllerDidConnect,
            object: nil
        )
        notificationCenter.addObserver(
            self,
            selector: #selector(controllerDidDisconnect(_:)),
            name: .GCControllerDidDisconnect,
            object: nil
        )

        GCController.startWirelessControllerDiscovery(completionHandler: nil)
        selectControllerIfNeeded()
    }

    deinit {
        notificationCenter.removeObserver(self)
    }

    func currentIntent() -> PlayerIntent {
        selectControllerIfNeeded()

        guard let gamepad = controller?.extendedGamepad else {
            resetEdges()
            return .neutral
        }

        let stick = gamepad.leftThumbstick
        let dpad = gamepad.dpad
        let rawX = abs(stick.xAxis.value) > abs(dpad.xAxis.value)
            ? stick.xAxis.value
            : dpad.xAxis.value
        let rawY = abs(stick.yAxis.value) > abs(dpad.yAxis.value)
            ? stick.yAxis.value
            : dpad.yAxis.value

        let movement = applyRadialDeadZone(
            x: CGFloat(rawX),
            y: CGFloat(rawY),
            threshold: 0.18
        )

        let primaryNow = gamepad.buttonA.isPressed
        let secondaryNow = gamepad.buttonX.isPressed
        let pauseNow = gamepad.buttonMenu.isPressed

        defer {
            previousPrimaryPressed = primaryNow
            previousSecondaryPressed = secondaryNow
            previousPausePressed = pauseNow
        }

        return PlayerIntent(
            movement: movement,
            primaryActionPressed: primaryNow && !previousPrimaryPressed,
            secondaryActionPressed: secondaryNow && !previousSecondaryPressed,
            pausePressed: pauseNow && !previousPausePressed
        )
    }

    private func applyRadialDeadZone(
        x: CGFloat,
        y: CGFloat,
        threshold: CGFloat
    ) -> CGVector {
        let magnitude = hypot(x, y)
        guard magnitude > threshold else { return .zero }

        let clampedMagnitude = min(magnitude, 1)
        let scaledMagnitude = (clampedMagnitude - threshold) / (1 - threshold)
        let directionX = x / magnitude
        let directionY = y / magnitude

        return CGVector(
            dx: directionX * scaledMagnitude,
            dy: directionY * scaledMagnitude
        )
    }

    private func selectControllerIfNeeded() {
        if controller == nil {
            controller = GCController.controllers().first(where: { $0.extendedGamepad != nil })
        }
        updateConnectionSummary()
    }

    private func updateConnectionSummary() {
        guard let controller else {
            connectionSummary = "Ingen controller ansluten"
            return
        }
        connectionSummary = controller.vendorName ?? "Controller ansluten"
    }

    private func resetEdges() {
        previousPrimaryPressed = false
        previousSecondaryPressed = false
        previousPausePressed = false
    }

    @objc private func controllerDidConnect(_ notification: Notification) {
        if controller == nil {
            controller = notification.object as? GCController
        }
        updateConnectionSummary()
    }

    @objc private func controllerDidDisconnect(_ notification: Notification) {
        guard let disconnected = notification.object as? GCController,
              disconnected === controller else { return }
        controller = nil
        resetEdges()
        selectControllerIfNeeded()
    }
}
