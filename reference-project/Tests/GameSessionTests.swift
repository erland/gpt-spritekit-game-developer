import XCTest
@testable import ReferenceGame_macOS

final class GameSessionTests: XCTestCase {
    func testUserPauseToggles() {
        var session = GameSession()
        session.toggleUserPause()
        XCTAssertEqual(session.state, .paused(.userRequested))
        session.toggleUserPause()
        XCTAssertEqual(session.state, .playing)
    }

    func testExternalPauseCannotBeDismissedAsUserPause() {
        var session = GameSession()
        session.pause(reason: .controllerDisconnected)
        session.toggleUserPause()
        XCTAssertEqual(session.state, .paused(.controllerDisconnected))
    }

    func testExternalPauseCanResume() {
        var session = GameSession()
        session.pause(reason: .applicationInactive)
        session.resumeAfterExternalPause()
        XCTAssertEqual(session.state, .playing)
    }
}
