# assignment: programming assignment 2
# author: Jeffrey Jacob
# date: Oct 22
# file: Board.py prints the tic tac toe board and checks to see if a player has won
# input: accepts player choices from player class and the sign of the player (X or O) and the size of the board
# output: interactive messages



class Board:

    def __init__(self):

        self.sign = " "

        self.size = 3

        self.board = list(self.sign * self.size**2)

        self.winner = ""

    def get_size(self):

        #return the board size (an instance size)

        return self.size

    def get_winner(self):

        #return the winner (a sign X or O) (an instance winner)

        return self.winner

    def set(self,index,sign):

        #mark the cell specified by index with the sign(X or O)

        self.board[index] = sign

    def isEmpty(self, index):

        #Return true if the cell specified by the index is empty (not marked as X or O)

        if(self.board[index] == " "):

            return True

        else:

            return False

    def isdone(self):

        done = False

        #checking for 3 horizontally arranged marks

        #for i in range(0,9):
            #print('a' +self.board[i])

        if (self.board[0] == self.board[1] and self.board[1] == self.board[2] and self.board[2] in ["X", "O"]):
            self.winner = self.board[0]

            done = True

        if (self.board[3] == self.board[4] and self.board[4] == self.board[5] and self.board[5] in ["X", "O"]):
            self.winner = self.board[3]

            done = True

        if (self.board[6] == self.board[7] and self.board[7] == self.board[8] and self.board[8] in ["X", "O"]):
            self.winner = self.board[6]

            done = True

        #checking for 3 vertically arranged marks

        if (self.board[0] == self.board[3] and self.board[3] == self.board[6] and self.board[6] in ["X", "O"]):
            self.winner = self.board[0]

            done = True

        if (self.board[1] == self.board[4] and self.board[4] == self.board[7] and self.board[7] in ["X", "O"]):
            self.winner = self.board[1]

            done = True

        if (self.board[2] == self.board[5] and self.board[5] == self.board[8] and self.board[8] in ["X", "O"]):
            self.winner = self.board[2]

            done = True

        #checking for 3 vertically arranged marks

        if (self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[8] in ["X", "O"]):
            self.winner = self.board[0]

            done = True

        if (self.board[2] == self.board[4] and self.board[4] == self.board[6] and self.board[6] in ["X", "O"]):
            self.winner = self.board[2]

            done = True

        
        
        return done

    def show(self):

        ind = 0

        print(" A     B     C")

        for i in range(0, 3):

            print(" +---+---+---+\n{}|".format(i+1), end = " ")

            for j in range(0, 3):

                print("{} |".format(self.board[ind]), end = " ")

                ind = ind + 1

            print()

        print(" +---+---+---+")
