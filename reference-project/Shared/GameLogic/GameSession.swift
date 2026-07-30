enum GameSessionState: Equatable {
    case playing
    case paused(PauseReason)
}

enum PauseReason: Equatable {
    case userRequested
    case controllerDisconnected
    case applicationInactive
}

struct GameSession: Equatable {
    private(set) var state: GameSessionState = .playing

    var isPaused: Bool {
        if case .paused = state { return true }
        return false
    }

    mutating func toggleUserPause() {
        switch state {
        case .playing:
            state = .paused(.userRequested)
        case .paused(.userRequested):
            state = .playing
        case .paused:
            break
        }
    }

    mutating func pause(reason: PauseReason) {
        state = .paused(reason)
    }

    mutating func resumeAfterExternalPause() {
        switch state {
        case .paused(.controllerDisconnected), .paused(.applicationInactive):
            state = .playing
        default:
            break
        }
    }
}
