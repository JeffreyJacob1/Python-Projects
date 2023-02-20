# author: Jeffrey Jacob
# date: 12/1/2022
# program: 15 game
# inputs: mouse clicks
# outputs: graphical representation of the game

from tkinter import *
from fifteen import Fifteen

# initialize game mechanics
game = Fifteen()

# creates board and button layout
def game_board(gui):
    tiles = str(game).split()
    tiles.append(' ')
    global buttons 
    buttons = [addButton(gui, i) for i in range(16)]
    k = 4           
    for i in range(k):
        for j in range(k):
            buttons[i*k+j].grid(row=i+1, column=j, columnspan=1)

# updates tiles
def update_board():
    tiles = game.tiles
    for i in range(16):
        button = buttons[i]
        tile = tiles[i]
        if tile == 0:
            tile = ' '
            button.config(bg = 'white', fg = 'black')
        else:
            button.config(bg = 'black', fg='white')
        button.config(text = tile)

# returns a button class with specified perameters
def addButton(gui, value):
    return Button(gui, text=value, height=4, width=8, command = lambda: clickButton(value))

def add_menu_Button(gui, value):
    return Button(gui, text=value, height=2, width=15, bg = 'black', fg = 'white', command = lambda: click_menu_button(value))

# event handler when button is clicked sends value to game engine, updates board
def clickButton(value):
    game.index_update(value)
    update_board()
    if game.is_solved():
        winning_menu()
    game.draw()

# same as above but for the menus
def click_menu_button(value):
    if value == 'play':
        game_board(gui)
        update_board()
        gui.deiconify()
    elif value == 'exit':
        gui.destroy()
    elif value == 'shuffle and play':
        game.shuffle()
        game_board(gui)
        update_board()
        gui.deiconify()

# pop-up window when user solves the puzzle
def winning_menu():
    pop= Toplevel(gui)
    pop.geometry("200x100")
    pop.title("Congrats")
    Label(pop, text= "YOU WIN", font=('Mistral 18 bold')).pack()

# start menu pop-up window
def start_menu():
    pop= Toplevel(gui)
    pop.geometry("200x200")
    pop.title("Welcome")
    Label(pop, text= "F I F T E E N", font=('Mistral 18 bold')).pack()
    play = add_menu_Button(pop, 'play')
    shuff_play = add_menu_Button(pop, 'shuffle and play')
    exi = add_menu_Button(pop, 'exit')
    play.pack()
    shuff_play.pack()
    exi.pack()

# main calls
if __name__ == '__main__':
    gui = Tk()
    gui.title('Fifteen!')
    gui.withdraw()
    start_menu()
# update the window
    gui.mainloop()  
