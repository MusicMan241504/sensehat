from sense_hat import SenseHat
import time
from datetime import datetime
from random import randint
sense = SenseHat()
bx = 0
by = 0
z = 0
while round(z) != -1:
    x, y, z = sense.get_accelerometer_raw().values()

sense.show_letter('3')
time.sleep(1)
sense.show_letter('2')
time.sleep(1)
sense.show_letter('1')
time.sleep(1)
px = randint(0,7)
py = randint(0,7)
score = 0
start = time.time()
while True:
    x, y, z = sense.get_accelerometer_raw().values()
    x = round(x,1)*2
    y = round(y,1)*2
    bx = bx + x
    by = by + y
    if bx < 0:
        bx = 0
    if bx > 7:
        bx = 7
    if by < 0:
        by = 0
    if by > 7:
        by = 7
    if round(z) == -1:
        break

    
    sense.set_pixels([[0,0,0]]*64)
    sense.set_pixel(round(bx),round(by),[255,0,0])
    sense.set_pixel(px,py,[0,255,0])


    if round(bx) == px and round(by) == py:
        score = score + 1
        if score == 10:
            msg = str(round(time.time() - start,1))
            sense.show_message(msg,scroll_speed=0.4)
            z = 0
            while round(z) != -1:
                x, y, z = sense.get_accelerometer_raw().values()
            sense.show_letter('3')
            time.sleep(1)
            sense.show_letter('2')
            time.sleep(1)
            sense.show_letter('1')
            time.sleep(1)
            score = 0
            start = time.time()
            bx = 0
            by = 0
        else:
            sense.show_letter(str(score),text_colour=[255,0,0])
            time.sleep(0.2)
        px = randint(0,7)
        py = randint(0,7)
