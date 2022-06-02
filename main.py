from tkinter import *
from tkinter import font as tkFont
from random import randrange
import random

# master = Tk()
# w = Canvas(master, width=403, height=403)
# w.pack()
# w.create_rectangle(3, 3, 103, 103, fill="gray", outline = 'black', width = 3)
# w.create_rectangle(103, 3, 203, 103, fill="gray", outline = 'black', width = 3)
# w.create_rectangle(203, 3, 303, 103, fill="gray", outline = 'black', width = 3)
# w.create_rectangle(303, 3, 403, 103, fill="gray", outline = 'black', width = 3)

#master.mainloop() 

board = ["-", "-", "-", "-",
         "-", "-", "-", "-",
         "-", "-", "-", "-",
         "-", "-", "-", "-"]



color_dictionary = {"-": "gray", "2": "white", "4": "beige", "8": "orange", "16": "darkorange", "32": "tomato", "64": "orangered",
                    "128": "khaki", "256": "gold", "512": "gold", "1024": "gold"}

button_texts = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
button_colors = ["gray", "gray", "gray", "gray", "gray", "gray", "gray", "gray", "gray", "gray", "gray", "gray", "gray", "gray", "gray", "gray"]



master = Tk()
button_font = tkFont.Font(family="Helvetica", size=20, weight= 'bold')

B = Button(master, text = button_texts[0], height = 4, width = 8, bg = button_colors[0], bd = 10, font = button_font)
B1 = Button(master, text = button_texts[1], height = 4, width = 8, bg = button_colors[1], bd = 10, font = button_font)
B2 = Button(master, text = button_texts[2], height = 4, width = 8, bg = button_colors[2], bd = 10, font = button_font)
B3 = Button(master, text = button_texts[3], height = 4, width = 8, bg = button_colors[3], bd = 10, font = button_font)
B4 = Button(master, text = button_texts[4], height = 4, width = 8, bg = button_colors[4], bd = 10, font = button_font)
B5 = Button(master, text = button_texts[5], height = 4, width = 8, bg = button_colors[5], bd = 10, font = button_font)
B6 = Button(master, text = button_texts[6], height = 4, width = 8, bg = button_colors[6], bd = 10, font = button_font)
B7 = Button(master, text = button_texts[7], height = 4, width = 8, bg = button_colors[7], bd = 10, font = button_font)
B8 = Button(master, text = button_texts[8], height = 4, width = 8, bg = button_colors[8], bd = 10, font = button_font)
B9 = Button(master, text = button_texts[9], height = 4, width = 8, bg = button_colors[9], bd = 10, font = button_font)
B10 = Button(master, text = button_texts[10], height = 4, width = 8, bg = button_colors[10], bd = 10, font = button_font)
B11 = Button(master, text = button_texts[11], height = 4, width = 8, bg = button_colors[11], bd = 10, font = button_font)
B12 = Button(master, text = button_texts[12], height = 4, width = 8, bg = button_colors[12], bd = 10, font = button_font)
B13 = Button(master, text = button_texts[13], height = 4, width = 8, bg = button_colors[13], bd = 10, font = button_font)
B14 = Button(master, text = button_texts[14], height = 4, width = 8, bg = button_colors[14], bd = 10, font = button_font)
B15 = Button(master, text = button_texts[15], height = 4, width = 8, bg = button_colors[15], bd = 10, font = button_font)

button_dict = {0: B, 1: B1, 2: B2, 3: B3, 4: B4, 5: B5, 6: B6, 7: B7, 8: B8, 9: B9, 10: B10, 11: B11, 12: B12, 13: B13, 14: B14, 15: B15}
button_dict2 = {0: B, 1: B1, 2: B2, 3: B3, 4: B4, 5: B5, 6: B6, 7: B7, 8: B8, 9: B9, 10: B10, 11: B11, 12: B12, 13: B13, 14: B14, 15: B15}


def generate_board():
    #master = Tk()
    button_font = tkFont.Font(family='Helvetica', size=20, weight='bold')

    
    # pick 2 random squares to start out with the values 2
    index1 = randrange(16)
    index2 = randrange(16)
    if index1 == index2:
        while index2 == index1:
            index2 = randrange(16)
    
    button_dict[index1]['text'] = "2"
    button_dict[index2]['text'] = "2"

    button_dict[index1]['bg'] = "white"
    button_dict[index2]['bg'] = "white"

    board[index1] = "2"
    board[index2] = "2"

    # B = Button(master, text = button_texts[0], height = 4, width = 8, bg = button_colors[0], bd = 10, font = button_font).grid(row=0, column=0)
    # B1 = Button(master, text = button_texts[1], height = 4, width = 8, bg = button_colors[1], bd = 10, font = button_font).grid(row=0, column=1)
    # B2 = Button(master, text = button_texts[2], height = 4, width = 8, bg = button_colors[2], bd = 10, font = button_font).grid(row=0, column=2)
    # B3 = Button(master, text = button_texts[3], height = 4, width = 8, bg = button_colors[3], bd = 10, font = button_font).grid(row=0, column=3)
    # B4 = Button(master, text = button_texts[4], height = 4, width = 8, bg = button_colors[4], bd = 10, font = button_font).grid(row=1, column=0)
    # B5 = Button(master, text = button_texts[5], height = 4, width = 8, bg = button_colors[5], bd = 10, font = button_font).grid(row=1, column=1)
    # B6 = Button(master, text = button_texts[6], height = 4, width = 8, bg = button_colors[6], bd = 10, font = button_font).grid(row=1, column=2)
    # B7 = Button(master, text = button_texts[7], height = 4, width = 8, bg = button_colors[7], bd = 10, font = button_font).grid(row=1, column=3)
    # B8 = Button(master, text = button_texts[8], height = 4, width = 8, bg = button_colors[8], bd = 10, font = button_font).grid(row=2, column=0)
    # B9 = Button(master, text = button_texts[9], height = 4, width = 8, bg = button_colors[9], bd = 10, font = button_font).grid(row=2, column=1)
    # B10 = Button(master, text = button_texts[10], height = 4, width = 8, bg = button_colors[10], bd = 10, font = button_font).grid(row=2, column=2)
    # B11 = Button(master, text = button_texts[11], height = 4, width = 8, bg = button_colors[11], bd = 10, font = button_font).grid(row=2, column=3)
    # B12 = Button(master, text = button_texts[12], height = 4, width = 8, bg = button_colors[12], bd = 10, font = button_font).grid(row=3, column=0)
    # B13 = Button(master, text = button_texts[13], height = 4, width = 8, bg = button_colors[13], bd = 10, font = button_font).grid(row=3, column=1)
    # B14 = Button(master, text = button_texts[14], height = 4, width = 8, bg = button_colors[14], bd = 10, font = button_font).grid(row=3, column=2)
    # B15 = Button(master, text = button_texts[15], height = 4, width = 8, bg = button_colors[15], bd = 10, font = button_font).grid(row=3, column=3)
    
    button_dict[0].grid(row=0, column=0)
    button_dict[1].grid(row=0, column=1)
    button_dict[2].grid(row=0, column=2)
    button_dict[3].grid(row=0, column=3)
    button_dict[4].grid(row=1, column=0)
    button_dict[5].grid(row=1, column=1)
    button_dict[6].grid(row=1, column=2)
    button_dict[7].grid(row=1, column=3)
    button_dict[8].grid(row=2, column=0)
    button_dict[9].grid(row=2, column=1)
    button_dict[10].grid(row=2, column=2)
    button_dict[11].grid(row=2, column=3)
    button_dict[12].grid(row=3, column=0)
    button_dict[13].grid(row=3, column=1)
    button_dict[14].grid(row=3, column=2)
    button_dict[15].grid(row=3, column=3)
    

    #master.mainloop()


def play():
    winner = False
    generate_board()
    #while not winner:
        #master.update_idletasks()
        #master.update()

    master.bind("<Up>", up)
    master.bind("<Down>", down)
    master.bind("<Left>", left)
    master.bind("<Right>", right)
        #inp = input()
        #update(inp)

    master.mainloop()
        #master.update_idletasks()
        #master.update()



def up(event):
    board_check = []
    for elem in board:
        board_check.append(elem)
    count = 0
    # for every changed spot in board, change the old button text and color and the new button spot text and color
        
    while count < 3:
        i = 12

        while i >= 4:
            # 1st column spaces being free
            if board[i - 4] == "-":
                temp = board[i]
                board[i] = "-"
                board[i - 4] = temp
            
            # 1st row has a number
            if board[12 - i] != "-":
                # if number right below it is the same as the number above it, combine them, double the upper one, and make lower one empty
                if board[12 - i + 4] != "-" and board[12 - i] == board[12 - i + 4]:
                    num_version = int(board[12 - i])
                    num_version *= 2
                    board[12 - i] = str(num_version)
                    board[12 - i + 4] = "-"


            # 2nd column 
            if board[i - 3] == "-":
                temp = board[i + 1]
                board[i + 1] = "-"
                board[i - 3] = temp


            # 1st row has a number
            if board[13 - i] != "-":
                # if number right below it is the same as the number above it, combine them, double the upper one, and make lower one empty
                if board[13 - i + 4] != "-" and board[13 - i] == board[13 - i + 4]:
                    num_version = int(board[13 - i])
                    num_version *= 2
                    board[13 - i] = str(num_version)
                    board[13 - i + 4] = "-"
            


            # 3rd column
            if board[i - 2] == "-":
                temp = board[i + 2]
                board[i + 2] = "-"
                board[i - 2] = temp



            # 1st row has a number
            if board[14 - i] != "-":
                # if number right below it is the same as the number above it, combine them, double the upper one, and make lower one empty
                if board[14 - i + 4] != "-" and board[14 - i] == board[14 - i + 4]:
                    num_version = int(board[14 - i])
                    num_version *= 2
                    board[14 - i] = str(num_version)
                    board[14 - i + 4] = "-"


            
            # 4th column
            if board[i - 1] == "-":
                temp = board[i + 3]
                board[i + 3] = "-"
                board[i - 1] = temp


            
            # 1st row has a number
            if board[15 - i] != "-":
                # if number right below it is the same as the number above it, combine them, double the upper one, and make lower one empty
                if board[15 - i + 4] != "-" and board[15 - i] == board[15 - i + 4]:
                    num_version = int(board[15 - i])
                    num_version *= 2
                    board[15 - i] = str(num_version)
                    board[15 - i + 4] = "-"


            i -= 4
            
        count += 1


    if board_check == board:
        update()
    else:
        update_with_two()


def down(event):
    board_check = []
    for elem in board:
        board_check.append(elem)
    count = 0
    
    # for every changed spot in board, change the old button text and color and the new button spot text and color
        
    while count < 3:
        #i = 12
        i = 0

        while i <= 8:
            # 1st column spaces being free
            if board[i + 4] == "-":
                temp = board[i]
                board[i] = "-"
                board[i + 4] = temp
            
            # last row has a number
            if board[12 - i] != "-":
                # if number right below it is the same as the number above it, combine them, double the upper one, and make lower one empty
                if board[12 - i - 4] != "-" and board[12 - i] == board[12 - i - 4]:
                    num_version = int(board[12 - i])
                    num_version *= 2
                    board[12 - i] = str(num_version)
                    board[12 - i - 4] = "-"


            # 2nd column 
            if board[i + 5] == "-":
                temp = board[i + 1]
                board[i + 1] = "-"
                board[i + 5] = temp


            # last row has a number
            if board[13 - i] != "-":
                # if number right below it is the same as the number above it, combine them, double the upper one, and make lower one empty
                if board[13 - i - 4] != "-" and board[13 - i] == board[13 - i - 4]:
                    num_version = int(board[13 - i])
                    num_version *= 2
                    board[13 - i] = str(num_version)
                    board[13 - i - 4] = "-"
            


            # 3rd column
            if board[i + 6] == "-":
                temp = board[i + 2]
                board[i + 2] = "-"
                board[i + 6] = temp



            # last row has a number
            if board[14 - i] != "-":
                # if number right below it is the same as the number above it, combine them, double the upper one, and make lower one empty
                if board[14 - i - 4] != "-" and board[14 - i] == board[14 - i - 4]:
                    num_version = int(board[14 - i])
                    num_version *= 2
                    board[14 - i] = str(num_version)
                    board[14 - i - 4] = "-"


            
            # 4th column
            if board[i + 7] == "-":
                temp = board[i + 3]
                board[i + 3] = "-"
                board[i + 7] = temp


            
            # last row has a number
            if board[15 - i] != "-":
                # if number right below it is the same as the number above it, combine them, double the upper one, and make lower one empty
                if board[15 - i - 4] != "-" and board[15 - i] == board[15 - i - 4]:
                    num_version = int(board[15 - i])
                    num_version *= 2
                    board[15 - i] = str(num_version)
                    board[15 - i - 4] = "-"


            i += 4
            
        count += 1

    if board_check == board:
        update()
    else:
        update_with_two()




def left(event):
    board_check = []
    for elem in board:
        board_check.append(elem)
    count = 0
    
    # for every changed spot in board, change the old button text and color and the new button spot text and color
        
    while count < 3:
        #i = 12
        i = 3
        # just like up, start i at a high value, decrement by maybe 1, and do while i >= something

        while i >=  1:
            # 1st row spaces being free
            if board[i - 1] == "-":
                temp = board[i]
                board[i] = "-"
                board[i - 1] = temp
            
            # first column has a number
            if board[3 - i] != "-":
                # if number to the right of it is the same thing, double the left one and make the right one blank
                if board[3 - i + 1] != "-" and board[3 - i] == board[3 - i + 1]:
                    num_version = int(board[3 - i])
                    num_version *= 2
                    board[3 - i] = str(num_version)
                    board[3 - i + 1] = "-"


            # 2nd row 
            if board[i + 3] == "-":
                temp = board[i + 4]
                board[i + 4] = "-"
                board[i + 3] = temp


            # first column has a number
            if board[7 - i] != "-":
                # if number to the right of it is the same thing, double the left one and make the right one blank
                if board[7 - i + 1] != "-" and board[7 - i] == board[7 - i + 1]:
                    num_version = int(board[7 - i])
                    num_version *= 2
                    board[7 - i] = str(num_version)
                    board[7 - i + 1] = "-"
            


            # 3rd row
            if board[i + 7] == "-":
                temp = board[i + 8]
                board[i + 8] = "-"
                board[i + 7] = temp



            # first column has a number
            if board[11 - i] != "-":
                # if number to the right of it is the same thing, double the left one and make the right one blank
                if board[11 - i + 1] != "-" and board[11 - i] == board[11 - i + 1]:
                    num_version = int(board[11 - i])
                    num_version *= 2
                    board[11 - i] = str(num_version)
                    board[11 - i + 1] = "-"


            
            # 4th row
            if board[i + 11] == "-":
                temp = board[i + 12]
                board[i + 12] = "-"
                board[i + 11] = temp


            
            # first column has a number
            if board[15 - i] != "-":
                # if number to the right of it is the same thing, double the left one and make the right one blank
                if board[15 - i + 1] != "-" and board[15 - i] == board[15 - i + 1]:
                    num_version = int(board[15 - i])
                    num_version *= 2
                    board[15 - i] = str(num_version)
                    board[15 - i + 1] = "-"


            i -= 1
            
        count += 1

    if board_check == board:
        update()
    else:
        update_with_two()



def right(event):
    board_check = []
    for elem in board:
        board_check.append(elem)
    count = 0
    
    # for every changed spot in board, change the old button text and color and the new button spot text and color
        
    while count < 3:
        #i = 12
        i = 0
        # just like up, start i at a high value, decrement by maybe 1, and do while i >= something

        while i <=  2:
            # 1st row spaces being free
            if board[i + 1] == "-":
                temp = board[i]
                board[i] = "-"
                board[i + 1] = temp
            
            # last column has a number
            if board[3 - i] != "-":
                # if number to the left of it is the same thing, double the right one and make the left one blank
                if board[3 - i - 1] != "-" and board[3 - i] == board[3 - i - 1]:
                    num_version = int(board[3 - i])
                    num_version *= 2
                    board[3 - i] = str(num_version)
                    board[3 - i - 1] = "-"


            # 2nd row 
            if board[i + 5] == "-":
                temp = board[i + 4]
                board[i + 4] = "-"
                board[i + 5] = temp


            # last column has a number
            if board[7 - i] != "-":
                # if number to the left of it is the same thing, double the right one and make the left one blank
                if board[7 - i - 1] != "-" and board[7 - i] == board[7 - i - 1]:
                    num_version = int(board[7 - i])
                    num_version *= 2
                    board[7 - i] = str(num_version)
                    board[7 - i - 1] = "-"
            


            # 3rd row
            if board[i + 9] == "-":
                temp = board[i + 8]
                board[i + 8] = "-"
                board[i + 9] = temp



            # last column has a number
            if board[11 - i] != "-":
                # if number to the left of it is the same thing, double the right one and make the left one blank
                if board[11 - i - 1] != "-" and board[11 - i] == board[11 - i - 1]:
                    num_version = int(board[11 - i])
                    num_version *= 2
                    board[11 - i] = str(num_version)
                    board[11 - i - 1] = "-"


            
            # 4th row
            if board[i + 13] == "-":
                temp = board[i + 12]
                board[i + 12] = "-"
                board[i + 13] = temp


            
            # last column has a number
            if board[15 - i] != "-":
                # if number to the left of it is the same thing, double the right one and make the left one blank
                if board[15 - i - 1] != "-" and board[15 - i] == board[15 - i - 1]:
                    num_version = int(board[15 - i])
                    num_version *= 2
                    board[15 - i] = str(num_version)
                    board[15 - i - 1] = "-"


            i += 1
            
        count += 1

    if board_check == board:
        update()
    else:
        update_with_two()






def update_with_two():
    new_dict = button_dict2
    
    # board done updating, now iterate through all button_texts and button_colors and then go thru button_dict with these arrays
    # to change it (use color_dictionary)
    for j, v in enumerate(board):
        button_texts[j] = v
        button_colors[j] = color_dictionary[v]
        
    #new_dict = button_dict2
    for k, w in enumerate(button_texts):
        if w == "-":
            new_dict[k]['text'] = ""
        else:
            new_dict[k]['text'] = button_texts[k]
        new_dict[k]['bg'] = button_colors[k]

    # elif inp == "a":

    # elif inp == "s":

    # elif inp == "d":


    # generate a new 2 in a random empty spot
    empty_spaces = []

    for i, v in enumerate(board):
        if v == "-":
            empty_spaces.append(i)

    new_index = random.choice(empty_spaces)
    board[new_index] = "2"

    
    new_dict[new_index]['text'] = "2"
    new_dict[new_index]['bg'] = "white"

    new_dict[0].grid(row=0, column=0)
    new_dict[1].grid(row=0, column=1)
    new_dict[2].grid(row=0, column=2)
    new_dict[3].grid(row=0, column=3)
    new_dict[4].grid(row=1, column=0)
    new_dict[5].grid(row=1, column=1)
    new_dict[6].grid(row=1, column=2)
    new_dict[7].grid(row=1, column=3)
    new_dict[8].grid(row=2, column=0)
    new_dict[9].grid(row=2, column=1)
    new_dict[10].grid(row=2, column=2)
    new_dict[11].grid(row=2, column=3)
    new_dict[12].grid(row=3, column=0)
    new_dict[13].grid(row=3, column=1)
    new_dict[14].grid(row=3, column=2)
    new_dict[15].grid(row=3, column=3)



def update():
    new_dict = button_dict2
    
    # board done updating, now iterate through all button_texts and button_colors and then go thru button_dict with these arrays
    # to change it (use color_dictionary)
    for j, v in enumerate(board):
        button_texts[j] = v
        button_colors[j] = color_dictionary[v]
        
    #new_dict = button_dict2
    for k, w in enumerate(button_texts):
        if w == "-":
            new_dict[k]['text'] = ""
        else:
            new_dict[k]['text'] = button_texts[k]
        new_dict[k]['bg'] = button_colors[k]

    # elif inp == "a":

    # elif inp == "s":

    # elif inp == "d":

    new_dict[0].grid(row=0, column=0)
    new_dict[1].grid(row=0, column=1)
    new_dict[2].grid(row=0, column=2)
    new_dict[3].grid(row=0, column=3)
    new_dict[4].grid(row=1, column=0)
    new_dict[5].grid(row=1, column=1)
    new_dict[6].grid(row=1, column=2)
    new_dict[7].grid(row=1, column=3)
    new_dict[8].grid(row=2, column=0)
    new_dict[9].grid(row=2, column=1)
    new_dict[10].grid(row=2, column=2)
    new_dict[11].grid(row=2, column=3)
    new_dict[12].grid(row=3, column=0)
    new_dict[13].grid(row=3, column=1)
    new_dict[14].grid(row=3, column=2)
    new_dict[15].grid(row=3, column=3)





play()