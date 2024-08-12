import time
import board
from digitalio import DigitalInOut, Direction, Pull

button = DigitalInOut(board.D17)
button.direction = Direction.INPUT
button.pull = Pull.UP

while True:
  if not button.value:
    print("Button pressed")
  time.sleep(0.01)
