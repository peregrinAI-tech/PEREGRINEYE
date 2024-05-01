# filename: useLeds.py

import time
import threading
import led_library

def button_press_simulation():
    # Simulate button press for 10 seconds
    start_time = time.time()
    while time.time() - start_time < 12:
         #print(time.time() - start_time)
    #    if time.time() - start_time > 5:
            # Simulate button press
            # Start alternating colors on LED 1
            #threading.Thread(target=led_library.alternate_colors, args=((0, 0, 255), (255, 165, 0), 2)).start()
            #led_library.stop_led(1)
         if time.time() - start_time < 5:
          #led_library.showColor(0)
          #led_library.alternate_colors(34,122,1)
          threading.Thread(target=led_library.alternate_colors, args=((0, 0, 255), (255, 165, 0), 2)).start()
         else :
          led_library.stop_led(0)
          led_library.showColor(2)
    #time.sleep(0.5)
        #elif time.time() - start_time < 5:
            # Simulate button release
            # Stop LED 1
            #led_library.stop_led(1)
    #led_library.showColor(False,1)
    #led_library.showColor(False,2)
    #time.sleep(0.5)
    #led_library.showColor(False,2)
    led_library.stop_led(1)
    led_library.stop_led(2)

button_press_simulation()
exit(1)
