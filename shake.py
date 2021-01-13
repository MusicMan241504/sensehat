from sense_hat import SenseHat
sense = SenseHat()
while True:
    x, y, z = sense.get_accelerometer_raw().values()
    x, y, z = abs(x), abs(y), abs(z)
    if x>1 or y>1 or z>1:
        sense.show_letter('!',text_colour=[255,0,0])
    else:
        sense.clear()
