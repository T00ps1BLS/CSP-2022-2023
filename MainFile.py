## MainFile.py


## Imports
# import turtle as trtl


## Setup
# wn = trtl.Screen()
# trObj = trtl.Turtle()
num_cats = 3
catnum = 0
cat1 = []
cat2 = []
cat3 = []
## Functions
def new_cat():
    global catnum, cat1, cat2, cat3
    words_file = open("initwordlist.txt", "r")
    cat_words = []
    index = 0
    for line in words_file:
        leader_word = ""
        if line[index] == "\n":
            break
        while line[index] != "\n":
            print(index)
            leader_word += line[index]
            index += 1
        cat_words.append(leader_word)
    
    if catnum == 1:
        cat1 = cat_words
        return cat1
    elif catnum == 2:
        cat2 = cat_words
        return cat2
    elif catnum == 3:
        cat3 = cat_words
        return cat3



## Events


print(new_cat(), catnum)

# wn.mainloop()
