from state import State
from state_machine import StateMachine

class Chooser(State):
    @property
    def name(self):
        return 'chooser'

    def enter(self, machine: StateMachine):
        self.encoder = machine.macropad.encoder
        State.enter(self, machine)

    def exit(self, machine):
        pass

    def update(self, machine: StateMachine):
        # TODO: get index of kp.state and +/- encoder delta
        if self.encoder != machine.macropad.encoder:
            text = machine.macropad.display_text()
            text[0].text = "Encoder: {}".format(machine.macropad.encoder - self.encoder)
            text.show()
            self._encoder = machine.macropad.encoder
        State.update(self, machine)