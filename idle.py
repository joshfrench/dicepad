from state import State

class Idle(State):
    @property
    def name(self):
        return ''

    def enter(self, machine):
        self.encoder = machine.macropad.encoder
        State.enter(self, machine)

    def exit(self, machine):
        self.encoder = None
        State.enter(self, machine)

    def update(self, machine):
        if self.encoder != machine.macropad.encoder:
            machine.go_to_state('title')
        State.update(self, machine)