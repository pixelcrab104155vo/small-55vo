"""Small UI state helper module."""
class UIState:
    """Represents a simple UI component state."""
    def __init__(self, active=False, enabled=True, visible=True):
        self.active = active
        self.enabled = enabled
        self.visible = visible

    def toggle_active(self):
        self.active = not self.active

    def set_enabled(self, flag: bool):
        self.enabled = bool(flag)

    def toggle_visible(self):
        self.visible = not self.visible

    def __repr__(self):
        return f"UIState(active={self.active}, enabled={self.enabled}, visible={self.visible})"


if __name__ == "__main__":
    state = UIState()
    print("Initial state:", state)
    state.toggle_active()
    state.toggle_visible()
    state.set_enabled(False)
    print("After changes:", state)