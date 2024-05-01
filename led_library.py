import time
import board
import adafruit_dotstar

DOTSTAR_DATA = board.D5
DOTSTAR_CLOCK = board.D6

dots = adafruit_dotstar.DotStar(DOTSTAR_CLOCK, DOTSTAR_DATA, 3, brightness=0.2)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def showColor(led):
   startS = time.time()
   while  time.time() - startS < 5:
    for j in range(35):
        
        rc_index = j * 5
        dots[led] = wheel(rc_index & 255)
        dots.show()
        time.sleep(0.01)

def alternate_colors(color1, color2, led):
     initiate = True
     while initiate:
        dots[led] = color1
        dots.show()
        time.sleep(0.3)
        dots[led] = color2
        dots.show()
        time.sleep(0.3)
        initiate = False

def stop_led(led):
    dots[led] = (0, 0, 0)
    dots.show()
