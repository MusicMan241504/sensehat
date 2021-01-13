from sense_hat import SenseHat
from random import randint
sense = SenseHat()
while True:
    sense.show_message('Hello!! I am Isaac',text_colour=[randint(100,255),randint(100,255),randint(0,100)],back_colour=[0,0,255],scroll_speed=0.1)
