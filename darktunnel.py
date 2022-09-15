from math import sqrt
import turtle as trtl
import random
import math

tr = trtl.Turtle()

tr.screen.bgcolor("black")


# User Input
inIterationMax = tr.screen.numinput("Line Count", "Enter desired number of lines to be drawn (more will take longer to complete)", 50, 1, 30000)
inLineLength = tr.screen.numinput("Length Input", "Enter desired line length", 50, 1, 1000)
inLineColor = tr.screen.textinput("Line Color", "Enter desired line color")
inOctogonColor = tr.screen.textinput("Octogon Color", "Enter desired octogon color")
inSquareColor = tr.screen.textinput("Square Color", "Enter desired square color")

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

# Setup for Octogon Shape After Lines are finished being drawn (can take up to 10 minutes with over 10000 lines)
tr.speed("normal")
tr.penup()
tr.pensize(5)
tr.setpos(-150, ((300*(math.sqrt(2)))*1.5)/2)
tr.pencolor(inOctogonColor)
tr.pendown()
tr.seth(0)

# Draws Octogon Shape
while x1 !=8:
    tr.forward(300)
    tr.right(45)
    x1 += 1

# Setup for Square Shape
tr.penup()
tr.setpos(-300, 300)
tr.pencolor(inSquareColor)
tr.pendown()


# Draws Square Shape
while x2 !=4:
    tr.forward(600)
    tr.right(90)
    x2 += 1

wn = trtl.Screen()
wn.mainloop()




