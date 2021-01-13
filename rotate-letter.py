from sense_hat import SenseHat
sense = SenseHat()
sense.show_letter('P')
while True:
    x, y, z = sense.get_accelerometer_raw().values()
    if round(x) == -1:
        sense.set_rotation(90)
    elif round(y) == 1:
        sense.set_rotation(0)
    elif round(x) == 1:
        sense.set_rotation(270)
    elif round(y) == -1:
        sense.set_rotation(180)
