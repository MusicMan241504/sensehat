from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
count = 0
while True:
    pitch, roll, yaw = sense.get_orientation().values()
    if count == 10:
        print("pitch=%s, roll=%s, yaw=%s" % (pitch,yaw,roll))
        count = 0
    count = count + 1
