from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

red = (200,0,0)
green = (0,255,0)
blank = (0,0,0)
brightred = (255,0,0)
darkred = (100,0,0)

snake = [[2,4],[3,4],[4,4]]
apples = []
direction = 'right'
score = 0
speed = 5
dead = False

def draw_snake():
    for segment in snake:
        sense.set_pixel(segment[0],segment[1],red)

def make_apple():
    new = snake[0]
    while new in snake:
        x, y = randint(0,7), randint(0,7)
        new = [x,y]
    sense.set_pixel(new[0],new[1],green)
    apples.append(new)


def wrap(pix):
    if pix[0] > 7:
        pix[0] = 0
    elif pix[0] < 0:
        pix[0] = 7
    elif pix[1] > 7:
        pix[1] = 0
    elif pix[1] < 0:
        pix[1] = 7
    return pix

def move():
    global score
    global speed
    global dead
    remove = True
    front = snake[-1]
    end = snake[0]
    new = list(front)
    
    if direction == 'right':
        new[0] = front[0] + 1
    elif direction == 'left':
        new[0] = front[0] - 1
    elif direction == 'down':
        new[1] = front[1] + 1
    elif direction == 'up':
        new[1] = front[1] - 1

    new = wrap(new)

    if new in apples:
        apples.remove(new)
        score += 1

        if score % 2 == 0:
            remove = False

            speed = speed * 0.9
    if remove:
            sense.set_pixel(end[0],end[1],blank)
            snake.remove(end)
    if new in snake:
        dead = True
    if not dead:
        snake.append(new)
        for i in range(len(snake)):
            sense.set_pixel(snake[-1-i][0],snake[-1-i][1],(255-i*10,0,0))
        sense.set_pixel(snake[-1][0],snake[-1][1],(255,50,0))
        

def tilt():
    global direction
    x, y, z = sense.get_accelerometer_raw().values()
    print(str(x) + ' ' + str(y))
    if x > 0.2:
        direction = 'right'
    if x < -0.2:
        direction = 'left'
    if y > 0.2:
        direction = 'down'
    if y < -0.2:
        direction = 'up'
    

    
def joystick_moved(event):
    global direction
    if event.direction != 'middle':
        front = snake[-1]
        new = list(front)
        if event.direction == 'right':
            new[0] = front[0] + 1
        elif event.direction == 'left':
            new[0] = front[0] - 1
        elif event.direction == 'down':
            new[1] = front[1] + 1
        elif event.direction == 'up':
            new[1] = front[1] - 1
        if new != snake[-2]:
            direction = event.direction

while True:
    #start
    snake = [[2,4],[3,4],[4,4]]
    apples = []
    direction = 'right'
    score = 0
    speed = 5
    dead = False

    sense.clear()
    event = sense.stick.wait_for_event()
    
    sense.show_letter('3',text_colour=[255,255,0])
    sleep(1)
    sense.show_letter('2',text_colour=[255,255,0])
    sleep(1)
    sense.show_letter('1',text_colour=[255,255,0])
    sleep(1)
    sense.clear()
    draw_snake()


    count = 0
    while not dead:
        if count >= speed:
            move()
        sense.stick.direction_any = joystick_moved
        if len(apples) < 3:
            make_apple()
        tilt()
        sleep(0.1)
        count += 1

    sense.show_message('You scored %d' %score,text_colour=[255,255,0])
    sleep(1)
