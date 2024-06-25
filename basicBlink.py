# use this to get your infrared LED blinking. it's super basic. eventually you want to build this without the trinket, just using a transistor to make a flashing light... 

import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D3)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
