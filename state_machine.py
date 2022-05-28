from adafruit_macropad import MacroPad
from state import State

class StateMachine(object):

    def __init__(self, macropad: MacroPad):
        self._state = None
        self.states = {}
        self._macropad = macropad

    @property
    def state(self) -> State:
        return self._state

    @property
    def macropad(self) -> MacroPad:
        return self._macropad

    def add_state(self, state: State):
        self.states[state.name] = state

    def go_to_state(self, state_name: str):
        if self.state:
            self.state.exit(self)
        self._state = self.states[state_name]
        self.state.enter(self)

    def update(self):
        if self.state:
            self.state.update(self)