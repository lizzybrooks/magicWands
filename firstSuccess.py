# this is still pretty buggy, but the IR sensor works and triggers a neopixel ring. 
# next step: use a neopixel strip instead of a ring, make the lights stay on, make each light a different color, figure out why you have to get so close to the flashing IR led
# it's okay, you have plenty of time

import board
import pulseio
import neopixel
import time

pixel_pin = board.D2
num_pixels = 4

pulses = pulseio.PulseIn(board.A0, maxlen=200, idle_state=True)
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)

RED = (255, 0, 0) #RGB
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 20)
PURPLE = (180, 0, 255)
OFF = (0,0,0)

lightCounter = 0


while True:
    if(lightCounter>3):
        lightCounter=0
        
    for p in range(0,num_pixels-1,1):
        pixels[p] = OFF
        pixels.show()
        time.sleep(1)

    while len(pulses) == 0:
        pass
    # Pause while we do something with the pulses
    pulses.pause()

    # Print the pulses. pulses[0] is an active pulse unless the length
    # reached max length and idle pulses are recorded.
    print("got pulse")
    lightCounter +=1
    if(lightCounter>3):
        lightCounter=0
    print(lightCounter)
    pixels[lightCounter] = BLUE
    pixels.show()
    time.sleep(1)
    # for n in range(0,len(pulses),1):
#         print(pulses[n])
    time.sleep(.6)
    # Clear the rest
    pulses.clear()
    print("cleared pulses")
    print(len(pulses))

    # Resume with an 80 microsecond active pulse
    pulses.resume(80)




