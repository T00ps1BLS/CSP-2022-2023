from math import sqrt
import turtle as trtl
import random
import math

tr = trtl.Turtle()

tr.screen.bgcolor("black")


# User Input
inIterationMax = tr.screen.numinput("Line Count", "Enter desired number of lines to be drawn (more will take longer to complete)", 50, 10, 30000)
inLineLength = tr.screen.numinput("Length Input", "Enter desired line length", 500, 100, 1000)
inLineColor = tr.screen.textinput("Line Color", "Enter desired line color")
inShapeSelection1 = int(tr.screen.textinput("Shape Selection 1", "Enter first desired shappe | Options: 1. Triangle, 2. Octogon, 3. Square, 4. Circle"))
inShapeSelection2 = int(tr.screen.textinput("Shape Selection 2", "Enter second shape desired shappe | Options:1. Triangle, 2. Octogon, 3. Square, 4. Circle"))
inShapeColor1 = tr.screen.textinput("Shape Color 1", "Enter first desired shape color")
inShapeColor2 = tr.screen.textinput("Shape Color 2", "Enter second desired shape color")


def shapePicker(x, y, z):
    if x == 1:
        tr.setpos(-150, -125)
        tr.pencolor(y)
        tr.pendown()
        tr.seth(0)
        while z != 3:
            tr.forward(300)
            tr.left(120)
            z += 1
    elif x == 2:
        tr.setpos(-150, ((300*(math.sqrt(2)))*1.5)/2)
        tr.pencolor(y)
        tr.pendown()
        tr.seth(0)
        while z != 8:
            tr.forward(300)
            tr.right(45)
            z += 1
    elif x == 3:
        tr.setpos(-300, -300)
        tr.pencolor(y)
        tr.pendown()
        tr.seth(0)
        while z != 4:
            tr.forward(600)
            tr.left(90)
            z += 1

# Counters
iteration = 0
x1 = 0
x2 = 0

# Setup for line drawing
tr.pencolor(inLineColor)
tr.speed(1000000000000000)
tr.hideturtle()


# was supposed to keep random length lines going at random angles from leaving a bounding box
# ended up just making a line that radiates out from the center and brings the turtle object back to the center after every line drawn (can easily be optimized for this purpose)
while iteration != inIterationMax:
    tr.right(random.randint(1, 1000))
    tr.forward(random.randint(1, inLineLength))
    if tr.xcor() >= inLineLength or -inLineLength:
        tr.setpos(0, 0)
    if tr.ycor() >= inLineLength or -inLineLength:
        tr.setpos(0, 0)
    
    iteration += 1

# Setup for First Shape After Lines are finished being drawn (can take up to 10 minutes with over 10000 lines)
tr.speed("normal")
tr.penup()
tr.pensize(5)



# Draws First Shape
shapePicker(inShapeSelection1, inShapeColor1, x1)

# Setup for Second Shape
tr.penup()

# Draws Second Shape
shapePicker(inShapeSelection2, inShapeColor2, x2)
# while x2 !=4:
#     tr.forward(600)
#     tr.right(90)
#     x2 += 1

wn = trtl.Screen()
wn.mainloop()
