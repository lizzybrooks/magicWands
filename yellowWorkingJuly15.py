# this version makes the lights stay on and it eliminates IR pulses that are below 300 -- what measurement is this?
# the IR sensor does need to get close to the flashing LED, but I think that has to do with the LED, not the IR sensor, since it works from a longer range with the projector remote

# now the questions i have are mainly design questions about how this activity will work. I have a lot of rings, but I'd need to buy strips. 
# i'm also trying to experiment with the battery. I guess I'll build one prototype using a battery charger thing that I have. Then I will experiment with that. 

import board
import pulseio
import neopixel
import time

pixel_pin = board.D2
num_pixels = 16

pulses = pulseio.PulseIn(board.A0, maxlen=20, idle_state=True)
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
    print("my code is running")
    print("lightCounter = " + str(lightCounter))
    if(lightCounter>15):
        lightCounter=0
        pixels.fill(OFF)
        pixels.show()
        
    # for p in range(0,num_pixels-1,1):
#         pixels[p] = OFF
#         pixels.show()
#         time.sleep(1)

    while len(pulses) == 0:
        pass
    # Pause while we do something with the pulses
    pulses.pause()
    
    # Print the pulses. pulses[0] is an active pulse unless the length
    # reached max length and idle pulses are recorded.
    print(pulses[0])
    if(pulses[0]> 300):
       
    
        lightCounter +=1
        if(lightCounter>num_pixels-1):
            lightCounter=0
        print("lightCounter = " + str(lightCounter))

        pixels[lightCounter] = YELLOW
        pixels.show()
        time.sleep(1)
    
    for n in range(0,len(pulses),1):
        print(pulses[n])
    time.sleep(.6)
    # Clear the rest
    pulses.clear()
    print("cleared pulses")
    print("len pulses = " + str(len(pulses)))

    # Resume with an 80 microsecond active pulse
    pulses.resume(80)
