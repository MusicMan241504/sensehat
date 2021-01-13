from sense_hat import SenseHat
sense = SenseHat()
while True:
    x, y, z = sense.get_accelerometer_raw().values()
    print("x=%s, y=%s, z=%s" % (round(x,2), round(y,2), round(z,2)))
