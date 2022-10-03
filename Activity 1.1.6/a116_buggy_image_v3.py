#   a116_buggmove_image.pmove
from configparser import LegacyInterpolation
import turtle as trtl

# instead of a descriptive name of the turtle such as painter,
# a less useful variable name painter is used
painter = trtl.Turtle()

# Draws Spider Body
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)

# Configures Spider Legs
legCount = 8
legLength = 70
legDirection = 180 / legCount
painter.pensize(5)
directionModifier = 0

# Draws Spider Legs
while (directionModifier < legCount):
  painter.goto(0,20)
  if directionModifier < 4:
    painter.setheading(-35 + (legDirection*directionModifier))
  else:
    painter.setheading(-45 + (-legDirection*directionModifier))
  painter.forward(legLength)
  directionModifier += 1

# Configure Eyes
eyeSpacing = 30
painter.pencolor("red")

# Draw Eyes
for i in range(2):
  painter.penup()
  painter.goto((eyeSpacing-(eyeSpacing*i)-15),30)
  painter.pendown()
  painter.forward(1)
  i += 1

painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()