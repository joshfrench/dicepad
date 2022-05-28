import time

from state import State
from state_machine import StateMachine

class Title(State):
    @property
    def name(self):
        return 'title'

    def enter(self, machine: StateMachine):
        self.encoder = machine.macropad.encoder
        self.reset_timer()
        State.enter(self, machine)

    def exit(self, machine: StateMachine):
        self.timeout = None
        State.exit(self, machine)

    def update(self, machine: StateMachine):
        if time.monotonic() >= self.timeout:
            machine.go_to_state('')

        if self.encoder != machine.macropad.encoder:
            machine.go_to_state('chooser')

        State.update(self, machine)

    def reset_timer(self):
        self.timeout = time.monotonic() + 2