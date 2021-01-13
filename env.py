from sense_hat import SenseHat
sense = SenseHat()
while True:

    t = round(sense.get_temperature(),1)
    p = round(sense.get_pressure(),1)
    h = round(sense.get_humidity(),1)

    msg = "Temperature=%s, Pressure=%s, Humidity=%s" %(t,p,h)
    sense.show_message(msg,scroll_speed=0.2)
