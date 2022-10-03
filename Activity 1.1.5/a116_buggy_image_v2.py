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
legDirection = 360 / legCount
painter.pensize(5)
directionModifier = 0

# Draws Spider Legs
while (directionModifier < legCount):
  painter.goto(0,20)
  painter.setheading(legDirection*directionModifier)
  painter.forward(legLength)
  directionModifier += 1


painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()