#!/usr/bin/env python
from sense_hat import SenseHat
import time 
import random
sense = SenseHat()
r = (255, 0, 0)
b = (0, 0, 255)
g = (0, 255, 0)
z = (0, 0, 0)
w = (255, 255, 255)

# r = random.randint(0, 255)
# print("The random number is"), r, ("this time")

pixels = []
for i in range(0,64):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    pixels.append(random_color)

sense.set_pixels(pixels)

time.sleep(2)
sense.clear()
