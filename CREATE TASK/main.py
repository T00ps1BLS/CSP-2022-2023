import turtle as fred # Imported turtle from https://pythonturtle.org/
import random # Imported random from https://github.com/python/cpython/blob/3.11/Lib/random.py

screen_w = 1280
screen_h = 720
backgroundimg1 = 'TACOBELL-STOREFRONT.png'
backgroundimg2 = 'KFC-STOREFRONT.png'
backgroundimg3 = 'ORDER-SCREEN.png'
employeeimg = 'EMPLOYEE.gif'
employeeimg1 = 'EMPLOYEE1.gif'
spchbbl = 'speechbubble.gif'
menu_background = 'menubackground.gif'
item_atr_file = 'itematr.txt'
menu_items1 = ['Taco', 'Taco', 'taco', 'tacos', 'Tacos', 'Taco w/ Cheese',]
menu_items2 = []
menu_prices1 = ['0.25', '0.50', '0.50', '1.00', '0.25', '1.25']
menu_prices2 = []
overall_cost1 = 0
overall_cost2 = 0
quality_points1 = 0
quality_points2 = 0
item_clicked = 0
bgstate = 0
text_prompt = 0
select = False
mnit0 = fred.Turtle()
mnit0.ht()
mnit1 = fred.Turtle()
mnit1.ht()
mnit2 = fred.Turtle()
mnit2.ht()
mnit3 = fred.Turtle()
mnit3.ht()
mnit4 = fred.Turtle()
mnit4.ht()
mnit5 = fred.Turtle()
mnit5.ht()
spawn_count = 0
menu_clicked1 = False

wn = fred.Screen()
wn.setup(width=screen_w, height=screen_h)
wn.addshape(employeeimg)
wn.addshape(employeeimg1)
wn.addshape(spchbbl)
wn.addshape(menu_background)
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
mntrlMAIN.pu()
mntrlMAIN.speed(0)
mntrlMAIN.turtlesize(10)
mntrlMAIN.hideturtle()
drw = fred.Turtle()
drw.ht()
drw.pu()
drw.pencolor('black')






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




def add_points(x, y):
    print("null")




def menu_turtles(trtl):
    global menu_items1, menu_prices1, spawn_count, text_prompt
    random_taco_num = random.randint(0, 5)
    turtleitem = ""
    turtleprice = ""
    for i in menu_items1:
        index = 0
        
        while index != random_taco_num:
            index += 1
        if index == random_taco_num:
            if text_prompt == 0:
                turtleitem = menu_items1[index]
                turtleprice = menu_prices1[index]
            elif text_prompt == 1:
                turtleitem = menu_items2[index]
                turtleprice = menu_prices2[index]


    trtl.penup()


    if spawn_count < 3:
        trtl.speed(0)
        trtl.goto(-450, (200 - (80 * spawn_count)))
        if turtleitem == 'Taco w/ Cheese':
            trtl.write('''
            {} ${}
            '''.format(turtleitem, turtleprice), align='left', font=('Arial', 27, 'bold'))
        else:
            trtl.write('''
            {} ${}
            '''.format(turtleitem, turtleprice), font=('Arial', 27, 'bold'))
    else:
        trtl.goto(50, (200 - (80 * (spawn_count - 3))))
        if turtleitem == 'Taco w/ Cheese':
            trtl.write('''
            {} ${}
            '''.format(turtleitem, turtleprice), align='center', font=('Arial', 27, 'bold'))
        else:
            trtl.write('''
            {} ${}
            '''.format(turtleitem, turtleprice), font=('Arial', 27, 'bold'))

    spawn_count += 1
    return turtleitem, turtleprice
    
def press1():
    mntrlMAIN.clear()
    mntrlMAIN.write("1", font=('Arial', 20, 'bold'))
    keypress = 1

def press2():
    mntrlMAIN.clear()
    mntrlMAIN.write("2", font=('Arial', 20, 'bold'))
    keypress = 2

def press3():
    mntrlMAIN.clear()
    mntrlMAIN.write("3", font=('Arial', 20, 'bold'))
    keypress = 3

def press4():
    mntrlMAIN.clear()
    mntrlMAIN.write("4", font=('Arial', 20, 'bold'))
    keypress = 4

def press5():
    mntrlMAIN.clear()
    mntrlMAIN.write("5", font=('Arial', 20, 'bold'))
    keypress = 5

def press6():
    mntrlMAIN.clear()
    mntrlMAIN.write("6", font=('Arial', 20, 'bold'))
    keypress = 6


def open_menu(x, y):
    global menu_clicked1
    if menu_clicked1 == False:
        global item_atr_file

        mntrlMAIN.goto(0, -250)
        mntrlMAIN.hideturtle()
        drw.speed(0)
        drw.goto(400, 400)
        drw.pensize(10)
        drw.pd()
        drw.fillcolor('#bc8e52')
        drw.begin_fill()
        drw.goto(-400, 400)
        drw.goto(-400, -40)
        drw.goto(400, -40)
        drw.goto(400, 400)
        drw.pu()
        drw.goto(0, 0)
        drw.end_fill()

        itematr0 = menu_turtles(mnit0)
        itematr1 = menu_turtles(mnit1)
        itematr2 = menu_turtles(mnit2)
        itematr3 = menu_turtles(mnit3)
        itematr4 = menu_turtles(mnit4)
        itematr5 = menu_turtles(mnit5)

        wn.onkeypress(press1, '1')
        wn.onkeypress(press2, '2')
        wn.onkeypress(press3, '3')
        wn.onkeypress(press4, '4')
        wn.onkeypress(press5, '5')
        wn.onkeypress(press6, '6')

    else:
        mnit0.clear()
        mnit1.clear()
        mnit2.clear()
        mnit3.clear()
        mnit4.clear()
        mnit5.clear()
        

def enter():
    global select, bgstate, text_prompt
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
    mntrlMAIN.st()

refresh_bg()
wn.onclick(click, btn=1)
mntrlMAIN.onclick(open_menu, btn=1)

wn.onkeypress(enter, 'space')

wn.listen()
wn.mainloop()