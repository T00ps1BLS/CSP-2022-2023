import turtle as fred # Imported turtle from https://pythonturtle.org/

screen_w = 1280
screen_h = 720
backgroundimg1 = 'TACOBELL-STOREFRONT.png'
backgroundimg2 = 'KFC-STOREFRONT.png'
backgroundimg3 = 'ORDER-SCREEN.png'
employeeimg = 'EMPLOYEE.gif'
spchbbl = 'speechbubble.gif'
bgstate = 0
select = False


wn = fred.Screen()
wn.setup(width=screen_w, height=screen_h)
wn.addshape(employeeimg)
wn.addshape(spchbbl)



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
        

def enter():
    global select, bgstate
    select = True
    if bgstate == 0:
        wn.bgcolor('purple')
    elif bgstate == 1:
        wn.bgcolor('red')
    bgstate = 3
    emp = fred.Turtle()
    emp.pu()
    emp.shape(employeeimg)
    spb = fred.Turtle()
    spb.speed(0)
    spb.pu()
    spb.shape(spchbbl)
    spb.turtlesize(0.5)
    spb.goto(-400, 200)
    spb.speed(0)
    spb.write("Hi! What can I get you today?", align='center', font=('Arial', 27, 'bold'))


    refresh_bg()
    

refresh_bg()
wn.onclick(click, btn=1)
wn.onkeypress(enter, 'space')
wn.listen()
wn.mainloop()