from math import sqrt
import turtle as trtl
import random
import math

tr = trtl.Turtle()

tr.screen.bgcolor("black")

inIterationMax = tr.screen.numinput("Line Count", "Enter desired number of lines to be drawn (more will take longer to complete)", 50, 1, 30000)
inLineLength = tr.screen.numinput("Length Input", "Enter desired line length", 50, 1, 1000)
inLineColor = tr.screen.textinput("Line Color", "Enter desired line color")
inOctogonColor = tr.screen.textinput("Octogon Color", "Enter desired octogon color")
inSquareColor = tr.screen.textinput("Square Color", "Enter desired square color")

iteration = 0
x1 = 0
x2 = 0

tr.pencolor(inLineColor)
tr.speed(1000000000000000)
tr.hideturtle()

while iteration != inIterationMax:
    tr.right(random.randint(1, 1000))
    tr.forward(random.randint(1, inLineLength))
    if tr.xcor() >= inLineLength or -inLineLength:
        tr.setpos(0, 0)
    if tr.ycor() >= inLineLength or -inLineLength:
        tr.setpos(0, 0)
    
    iteration += 1

tr.speed("normal")
tr.penup()
tr.pensize(5)
tr.setpos(-150, ((300*(math.sqrt(2)))*1.5)/2)
tr.pencolor(inOctogonColor)
tr.pendown()
tr.seth(0)

while x1 !=8:
    tr.forward(300)
    tr.right(45)
    x1 += 1

tr.penup()
tr.setpos(-300, 300)
tr.pencolor(inSquareColor)
tr.pendown()

while x2 !=4:
    tr.forward(600)
    tr.right(90)
    x2 += 1

wn = trtl.Screen()
wn.mainloop()




