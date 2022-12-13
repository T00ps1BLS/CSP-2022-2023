## MainFile.py


## Imports
# import turtle as trtl


## Setup
# wn = trtl.Screen()
# trObj = trtl.Turtle()
num_cats = 3
cat_num = 0
cat1 = []
cat2 = []
cat3 = []
## Functions

def new_cat():
    global num_cats, cat_num, cat1, cat2, cat3
    words_file = open("initwordlist.txt", "r")
    cat_words = []
    
    for line in words_file:
        leader_word = ""
        index = 0
        if line[index] == "\n":
            break
        while line[index] != "\n":
            if line[index] == "1" or line[index] == "2":
                break
            leader_word += line[index]
            index += 1
        cat_words.append(leader_word)
    new_list = []
    for word in cat_words:
        end = False
        new_word = ""
        if word == '':
            end = True
        if end == True:
            cat_words.pop()
        else:
            new_word += word
            new_list.append(new_word)
        
    if cat_num == 0:
        cat1 = new_list
    elif cat_num == 1:
        cat2 = new_list
    elif cat_num == 2:
        cat3 = new_list
    return cat1, cat2, cat3



## Events


print(new_cat())

# wn.mainloop()
