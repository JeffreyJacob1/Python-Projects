# author: Jeffrey Jacob
# date: Nov 10, 2022
# file: board.py
# input: tictac.py driver code
# output: interactive tic tac toe board

class Board:
    def __init__(self):
        #init vars
        self.sign = " "
        self.size = 3
        self.board = {}

        #creates a dictionary with the space's names as keys and blanks as values
        for x in "123":
            for y in "ABC":
                self.board[y+x] = ' '
        
        # the winner's sign O or X
        self.winner = " "

    # this function allows the SmartAI to read the state of the board easily
    def read_board(self):
        return self.board
    # returns size of the board
    def get_size(self): 
        return self.size

    def get_winner(self):
        return self.winner
        # return the winner's sign O or X (an instance winner)  
       
    # allows spaces to be edited
    def set(self, cell, sign):
        #accounts for lowercase inputs
        cell = cell.upper()
        #adds the sign to the dictionary
        self.board[cell] = sign

    #check if space is empty
    def isempty(self, cell):
        cell = cell.upper()
        contents = self.board[cell]
        if contents == ' ':
            empty = True
        else:
            empty = False
        return empty

    # checks for any game over conditions
    def isdone(self):
        # check all game terminating conditions, if one of them is present, assign the var done to True
        # depending on conditions assign the instance var winner to O or X
        self.winner = ' '

        done = False
        # list of winning combinations
        winning_combos = [['A1','B1','C1'],['A2','B2','C2'],['A3','B3','C3'],['A1','A2','A3'],['B1','B2','B3'],['C1','C2','C3'],['A1','B2','C3'],['A3','B2','C1']]

        # checks if the winning combo is true
        def check(combo):
            a = self.board[combo[0]]
            b = self.board[combo[1]]
            c = self.board[combo[2]]
            if a==b==c!=' ':
                return True
            else:
                return False
        
        # calls on each winning combo and evaluates
        for comb in winning_combos:
            if check(comb):
                done = True
                self.winner = self.board[comb[0]]
                return done
            else:
                done = False
        # checks for tie (all spaces will be filled and no winner)
        for i in self.board.values():
            if i == ' ':
                done = False
                return done
            else:
                done = True
        return done
    
    def show(self):
        spots = self.board
        board = f"   A   B   C  \n +---+---+---+\n1| {spots['A1']} | {spots['B1']} | {spots['C1']} |\n +---+---+---+\n2| {spots['A2']} | {spots['B2']} | {spots['C2']} |\n +---+---+---+\n3| {spots['A3']} | {spots['B3']} | {spots['C3']} |\n +---+---+---+"
        print(board)
        # draw the board
