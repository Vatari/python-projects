import os
import turtle

image = os.path.expanduser("/python_basics/Spaceship/starship.gif")
image.size = 10

wn = turtle.Screen()
wn.register_shape(image)
last_pressed = 'up'


def setup(col, x, y, w, s, shape):
    turtle.up()
    turtle.goto(x, y)
    turtle.width(w)
    turtle.turtlesize(s)
    turtle.color(col)
    turtle.shape(image)
    turtle.lt(90)
    turtle.down()
    wn.onkey(up, "Up")
    wn.onkey(left, "Left")
    wn.onkey(right, "Right")
    wn.onkey(back, "Down")
    wn.onkey(quitTurtles, "Escape")
    wn.listen()
    wn.mainloop()


# Event handlers
def up():
    global last_pressed
    if last_pressed == 'left':
        turtle.rt(90)
        turtle.fd(10)
    elif last_pressed == 'right':
        turtle.lt(90)
        turtle.fd(10)
    elif last_pressed == 'up':
        turtle.fd(10)
    else:
        turtle.rt(180)
        turtle.fd(10)

    last_pressed = 'up'


def left():
    global last_pressed
    if last_pressed == 'left':
        turtle.fd(10)
    elif last_pressed == 'right':
        turtle.lt(180)
        turtle.fd(10)
    elif last_pressed == 'up':
        turtle.lt(90)
        turtle.fd(10)
    else:
        turtle.rt(90)
        turtle.fd(10)

    last_pressed = 'left'


def right():
    global last_pressed
    if last_pressed == 'left':
        turtle.rt(180)
        turtle.fd(10)
    elif last_pressed == 'right':
        turtle.fd(10)
    elif last_pressed == 'up':
        turtle.rt(90)
        turtle.fd(10)
    else:
        turtle.lt(90)
        turtle.fd(10)

    last_pressed = 'right'


def back():
    global last_pressed
    if last_pressed == 'left':
        turtle.lt(90)
        turtle.fd(10)
    elif last_pressed == 'right':
        turtle.rt(90)
        turtle.fd(10)
    elif last_pressed == 'up':
        turtle.rt(180)
        turtle.fd(10)
    else:
        turtle.fd(10)

    last_pressed = 'down'


def quitTurtles():
    wn.bye()


setup("blue", -200, 200, 2, 2, image)
