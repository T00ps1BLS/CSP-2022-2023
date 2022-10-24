from sys import _xoptions
import turtle as trtl
import random

tr = trtl.Turtle()
tr.speed('fastest')
def reset():
    tr.penup()
    tr.goto(randpointx1 - randpointx1 / 2, randpointy2 - randpointy2 / 2)
    tr.pendown()

randpointx1 = random.randint(-300, 300)
randpointy1 = random.randint(-300, 300)
randpointx2 = random.randint(-300, 300)
randpointy2 = random.randint(-300, 300)
tr.penup()
tr.goto(randpointx1, randpointy1)
tr.pendown()
tr.goto(randpointx2, randpointy1)
tr.goto(randpointx2, randpointy2)
tr.goto(randpointx1, randpointy2)
tr.goto(randpointx1, randpointy1)

def resetArea():
    tr.clear()
    randpointx1 = random.randint(-300, 300)
    randpointy1 = random.randint(-300, 300)
    randpointx2 = random.randint(-300, 300)
    randpointy2 = random.randint(-300, 300)
    tr.penup()
    tr.goto(randpointx1, randpointy1)
    tr.pendown()
    tr.goto(randpointx2, randpointy1)
    tr.goto(randpointx2, randpointy2)
    tr.goto(randpointx1, randpointy2)
    tr.goto(randpointx1, randpointy1)
reset()
while True:
    tr.seth(random.randint(1, 360))
    tr.forward(random.randint(1, 10))
    xpos = tr.xcor()
    ypos = tr.ycor()
    if xpos >= randpointx1 or xpos <= randpointx2:
        reset()
        if ypos >= randpointy1 or xpos <= randpointy2:
            reset()

screen = trtl.Screen()



screen.mainloop()