class State(object):
    def __init__(self):
        pass

    @property
    def name(self) -> str:
        return ''

    def enter(self, machine):
        text = machine.macropad.display_text()
        text[0].text = machine.state.name.upper()
        text.show()

    def exit(self, machine):
        pass

    def update(self, machine):
        if machine.macropad.encoder_switch:
            machine.go_to_state('')