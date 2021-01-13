from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
r = 255
g = 0
b = 0
while True:
    while g < 255:
        g = g+1
        sense.set_pixels([[r,g,b]]*64)
        sleep(0.0005)
    while r > 0:
        r = r-1
        sense.set_pixels([[r,g,b]]*64)
        sleep(0.0005)
    while b < 255:
        b = b+1
        sense.set_pixels([[r,g,b]]*64)
        sleep(0.0005)
    while g > 0:
        g = g-1
        sense.set_pixels([[r,g,b]]*64)
        sleep(0.0005)
    while r < 255:
        r = r+1
        sense.set_pixels([[r,g,b]]*64)
        sleep(0.0005)
    while b > 0:
        b = b-1
        sense.set_pixels([[r,g,b]]*64)
        sleep(0.0005)
    
    
    
    



    
sense.set_pixels([[r,g,b]]*64)
sleep(0.01)
    
