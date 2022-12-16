## MainFile.py

##
## Imports
##
import turtle as trtl

##
## Setup
##

wordlistfile = ""
wn = trtl.Screen()
tr = trtl.Turtle()
tr.hideturtle()
tr.penup()
wn.bgcolor("#42bff5")
correct_words = 0
incorrect_words = 0
match = False
num_cats = 3
cat1 = []
timer = 10
timer_interval = 1000
timer_up = False

##
## Functions
##

def new_cat():
    ## I originally named this function "new_cat" because I originally wanted to split parts of the text file into different lists as different categories but it ended up being too complicated 
    ## for me to do in a reasonable time so now it just takes all the words in the text file and puts them in a list.
    global num_cats, cat1 # accesses global variables in Setup
    words_file = open(wordlistfile, "r")
    cat_words = []
    
    for line in words_file: # takes every word in the text file and puts them into a temporary list (cat_words)
        leader_word = ""
        index = 0
        if line[index] == "\n":
            break
        while line[index] != "\n":
            leader_word += line[index]
            index += 1
        cat_words.append(leader_word)
        cat1 = cat_words # appends words in the temporary list and adds them to the permanent list (probably unnecessary)

def print_words():
    ## If the user's inputed word matches a word in the list, the user's word is printed on the screen and the user's correct words score goes up, and the opposite is true for if no match is
    ## found.
    global correct_words, incorrect_words, match # accesses global variables in Setup
    tr.goto(0, 240 - (35 * correct_words)) # moves the turtle down by 35 pixels every time a word is printed
    match = False
    wordIn = wn.textinput("Word Input", "Guess word:") # takes the user's input
    for word in cat1: # checks for a match
        if wordIn == word:
            match = True
    if match == True: # prints the matched word and increases correct_words score
        tr.write(wordIn, True, align="center", font=('Arial', 25, 'normal'))
        correct_words += 1
    else: # increases incorrect_words score
        incorrect_words += 1

##
## Events
##

fileIn = int(wn.textinput("Select words file", "Options: 1"))
if fileIn == 1:
    wordlistfile = "initwordlist.txt"
    tr.goto(0, 285)
    tr.write("Categories: Fruit, House, Natural Disaster", True, align="center", font=('Arial', 30, 'normal'))




new_cat()

tr.pencolor("green")
for word in cat1: ## checks every word for a match and prints correct words and increases scores accordingly
    match = False # always starts as false for each word
    print_words()


## Prints final scores
tr.pencolor("black")
tr.goto(0, 240 - (35 * (correct_words + 1)))
tr.write("Correct Words:" + str(correct_words), True, align="center", font=('Arial', 25, 'normal'))
tr.pencolor("red")
tr.goto(0, 240 - (10 + (35 * (correct_words + 2))))
tr.write("Incorrect Words:" + str(incorrect_words), True, align="center", font=('Arial', 25, 'normal'))

wn.mainloop()
