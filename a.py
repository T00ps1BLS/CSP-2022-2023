import turtle as trtl
import random

tr = trtl.Turtle()
tr.speed('fastest')
tr.pensize(2)
randpointx1 = random.randint(-300, 300)
randpointy1 = random.randint(-300, 300)

randpointx2 = random.randint(-300, 300)
randpointy2 = random.randint(-300, 300)
def reset():
    tr.penup()
    tr.goto(randpointx1 + ((randpointx2 - randpointx1) / 2), randpointy1 + ((randpointy2 - randpointy1) / 2))
    tr.pendown()
tr.penup()
tr.goto(randpointx1, randpointy1)
tr.pendown()
tr.goto(randpointx2, randpointy1)
tr.goto(randpointx2, randpointy2)
tr.goto(randpointx1, randpointy2)
tr.goto(randpointx1, randpointy1)

screen = trtl.Screen()
reset()
xposStart = tr.xcor()
yposStart = tr.ycor()
colors = ["red", "blue", "green", "orange", "purple", "gold"]

if randpointx1 < randpointx2:
    xlower = randpointx1
    xhigher = randpointx2
else:
    xlower = randpointx2
    xhigher = randpointx1
if randpointy1 < randpointy2:
    ylower = randpointy1
    yhigher = randpointy2
else:
    ylower = randpointy2
    yhigher = randpointy1

while True:
    for i in colors:
        xpos = tr.xcor()
        ypos = tr.ycor()
        if xpos >= xhigher or xpos <= xlower or ypos >= yhigher or ypos <= ylower:
            tr.seth(tr.towards(randpointx1 + ((randpointx2 - randpointx1) / 2), randpointy1 + ((randpointy2 - randpointy1) / 2)))
            tr.forward(6)
        tr.seth(random.randint(1, 360))
        tr.forward(random.randint(1, 10))
        colors.append(i)
        tr.pencolor(i)
        

        

screen.mainloop()
