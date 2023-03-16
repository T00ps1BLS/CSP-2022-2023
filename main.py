import turtle as fred # Imported turtle from https://pythonturtle.org/
import random # Imported random

screen_w = 1280
screen_h = 720
backgroundimg1 = 'TACOBELL-STOREFRONT.png'
backgroundimg2 = 'KFC-STOREFRONT.png'
backgroundimg3 = 'ORDER-SCREEN.png'
employeeimg = 'EMPLOYEE.gif'
employeeimg1 = 'EMPLOYEE1.gif'
spchbbl = 'speechbubble.gif'
menu_items1= ['Taco', 'Taco', 'taco', 'tacos', 'Tacos', 'Taco with Cheese',]
bgstate = 0
select = False


wn = fred.Screen()
wn.setup(width=screen_w, height=screen_h)
wn.addshape(employeeimg)
wn.addshape(spchbbl)
emp = fred.Turtle()
emp.ht()
emp.pu()
emp.speed(0)
spb = fred.Turtle()
spb.ht()
# spb.shape(spchbbl)
spb.pu()
spb.speed(0)
spb.goto(0, -323)
mntrlMAIN = fred.Turtle()
mntrlMAIN.ht()
mntrlMAIN.pu()
mntrlMAIN.speed(0)
mntrlMAIN.turtlesize(10)


def refresh_bg():
    global bgstate 
    if bgstate == 0:
        wn.bgpic(backgroundimg1)
    elif bgstate == 1:
        wn.bgpic(backgroundimg2)
    elif bgstate == 3:
        wn.bgpic(backgroundimg3)

def click(x, y):
    global bgstate, select
    if select == False:
        if bgstate == 0:
            bgstate = 1
        elif bgstate == 1:
            bgstate = 0
        
        print(bgstate)
        refresh_bg()

def menu_turtles():
    global menu_items1
    for i in menu_items1:
        random_taco_num = random.randint(0, 5)
        index = 0
        while index != random_taco_num:
            index += 1


        

def enter():
    global select, bgstate
    select = True
    if bgstate == 0:
        wn.bgcolor('purple')
    elif bgstate == 1:
        wn.bgcolor('red')
    text_prompt = bgstate
    bgstate = 3
    refresh_bg()
    if text_prompt == 0:
        spb.write("Hey there! What can I get you today?", align='center', font=('Arial', 27, 'bold'))
        emp.shape(employeeimg)
    elif text_prompt == 1:
        spb.write(".......Hello....... *awkward silence*", align='center', font=('Arial', 27, 'bold'))
        emp.shape(employeeimg1)
    emp.st()
    mntrlMAIN.goto(-350, -50)
    

refresh_bg()
wn.onclick(click, btn=1)
wn.onkeypress(enter, 'space')
wn.listen()
wn.mainloop()
