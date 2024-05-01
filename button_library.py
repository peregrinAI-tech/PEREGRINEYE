# filename: button_library.py
import time
import board
from digitalio import DigitalInOut, Direction, Pull

class Button:
    def __init__(self, pin=board.D17):
        self.button = DigitalInOut(pin)
        self.button.direction = Direction.INPUT
        self.button.pull = Pull.UP
        self.button_state = self.button.value

    def button_pressed(self):
        if not self.button.value and self.button_state:
            self.button_state = False
            return True
        return False

    def button_released(self):
        if self.button.value and not self.button_state:
            self.button_state = True
            return True
        return False

    def wait(self, seconds=0.01):
        time.sleep(seconds)