from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
c = [
[255, 0, 0],
[255, 127, 0],
[255, 255, 0],
[127, 255, 0],
[0, 255, 0],
[0, 255, 127],
[0, 255, 255],
[0, 127, 255],
[0, 0, 255],
[127, 0, 255],
[255, 0, 255],
[255, 0, 127]
]
cc = 0
while True:
    for y in range(8):
        for x in range(8):
            if cc + y + x < 12:
                ccc = cc+y+x
            else:
                ccc = cc+y+x-11
            if ccc >= 12:
                ccc = ccc-11
            sense.set_pixel(x,y,c[ccc])
    sleep(0.1)
    cc = cc + 1
    if cc == 11:
        cc = 0



