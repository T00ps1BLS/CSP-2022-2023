# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
#-----game configuration----
wn = trtl.Screen()
cn = trtl.getcanvas()

x, y = cn.winfo_pointerxy()
#-----initialize turtle-----
tr = trtl.Turtle()
tr.penup()
#-----game functions--------
def click(x, y):
    
    if abs(tr.xcor()) - abs(x) <= 10 or abs(tr.ycor()) - abs(y) <= 10:
        print("click")

#-----events----------------
for i in range(1000):
    tr.forward(1)
tr.onclick(click)


wn.mainloop()