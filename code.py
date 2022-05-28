import time
from adafruit_macropad import MacroPad

from state_machine import StateMachine
from chooser import Chooser
from idle import Idle
from roll import Title

macropad = MacroPad()

encoder = StateMachine(macropad)
encoder.add_state(Idle())
encoder.add_state(Title())
encoder.add_state(Chooser())
encoder.go_to_state('title')

# TODO: keypad is its own state machine;
# chooser selects kp state
# kp = StateMachine(macropad)

while True:
    encoder.update()