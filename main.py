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
menu_clicked = False

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




def add_points(num, x, y):
    global overall_cost1, overall_cost2, quality_points1, quality_points2, text_prompt
    if text_prompt == 0:
        item_prices = open(item_atr_file, 'r')
        line_num = num
        for line in item_prices:
            index = 0
            while line[index] != line_num:
                if line[index] == '\n':
                    break
                index += 1
            index += 2
            overall_cost1 += line[index]
            print(overall_cost1)
    elif text_prompt == 1:
        #
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
    



def open_menu(x, y):
    global menu_clicked
    if menu_clicked == False:
        global item_atr_file

        mntrlMAIN.goto(0, 200)
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


        with open(item_atr_file, 'a') as file:
            file.write('0,{}\n'.format(itematr0))
            file.write('1,{}\n'.format(itematr1))
            file.write('2,{}\n'.format(itematr2))
            file.write('3,{}\n'.format(itematr3))
            file.write('4,{}\n'.format(itematr4))
            file.write('5,{}\n'.format(itematr5))

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

mnit0.onclick(add_points(num=0, x=0, y=0), btn=1)
mnit1.onclick(add_points(num=1 x=0, y=0), btn=1)
mnit2.onclick(add_points(num=2, x=0, y=0), btn=1)
mnit3.onclick(add_points(num=3, x=0, y=0), btn=1)
mnit4.onclick(add_points(num=4, x=0, y=0), btn=1)
mnit5.onclick(add_points(num=5, x=0, y=0), btn=1)

wn.onkeypress(enter, 'space')
wn.listen()
wn.mainloop()
