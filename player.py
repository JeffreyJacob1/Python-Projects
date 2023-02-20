# author: Jeffrey Jacob
# date: Nov 10, 2022
# file: Player.py a Python program that implements a user driven Player class, and 3 different AI classes for the game tic tac toe
# input: tictac.py driver program, or user input for Player class
# output: Makes moves based on AI or user input

from random import choice

class Player:
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X

        #creates a list with all possible moves
        self.moves = []
        for x in "123":
            for y in "ABC":
                self.moves += [y+x]

    def get_sign(self):
        # return an instance sign
        return self.sign

    def get_name(self):
        # return an instance name
        return self.name

    def choose(self, board):
        # prompt the user to choose a cell
        # if the user enters a valid string and the cell on the board is empty, update the board
        # otherwise print a message that the input is wrong and rewrite the prompt
        # use the methods board.isempty(cell), and board.set(cell, sign)
        move_chosen = False
        while not move_chosen:
            chosen_cell = input(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n")
            chosen_cell = chosen_cell.upper()
            if chosen_cell not in self.moves:
                print("Invalid Move.")
                continue
            elif not board.isempty(chosen_cell):
                print("You did not choose correctly.")
                continue
            else:
                board.set(chosen_cell, self.sign)
                move_chosen = True

class AI(Player):
    def __init__(self, name, sign, board):
        self.name = name
        self.sign = sign
        self.moves = []
        self.scores = []
        self.moves = self._moves()
        self.other = ''

    #creates a list of all possible moves
    def _moves(self):
        moves = []
        for x in "123":
            for y in "ABC":
                moves += [y+x]
        return moves

    #chooses a random move from available spots on the board
    def choose(self, board):
        print(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        while True:
            cell = choice(self.moves)
            if board.isempty(cell):
                board.set(cell, self.sign)
                self.moves.remove(cell)
            else:
                self.moves.remove(cell)
                continue 
            break
        print(cell)

class SmartAI(AI):
    #makes a move
    def make_move(self, cell, board):
        print(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        board.set(cell, self.sign)
        print(cell)
    
    # plays a perfect game of tic tac toe
    def choose(self, board):
        #figures out opponents sign
        if self.sign =='X':
            other = 'O'
        else:
            other = 'X'
        current_board = board.read_board()
        winning_combos = [['A1','B1','C1'],['A2','B2','C2'],['A3','B3','C3'],['A1','A2','A3'],['B1','B2','B3'],['C1','C2','C3'],['A1','B2','C3'],['A3','B2','C1']]

        # checks if the combo can be a winning combo if any of the spaces are replaced with self.sign
        def check_win(combo):
                a = current_board[combo[0]]
                b = current_board[combo[1]]
                c = current_board[combo[2]]
                if self.sign==b==c:
                    return combo[0]
                elif a==self.sign==c:
                    return combo[1]
                elif a==b==self.sign:
                    return combo[2]
                else: 
                    return 1
        
        #checks if the combo will be a winning combo for the opponent if they play in any of the spaces
        def check_block(combo):
                a = current_board[combo[0]]
                b = current_board[combo[1]]
                c = current_board[combo[2]]
                if other==b==c:
                    return combo[0]
                elif a==other==c:
                    return combo[1]
                elif a==b==other:
                    return combo[2]
                else: 
                    return 1

        # while loop breaks once move is found. 
        # move rules are written in order of priority based on wikipedia article provided by proffesor
        while True:

            #checks if there is any moves that will result in a winning combo
            for comb in winning_combos:
                checker = check_win(comb)
                if checker != 1 and board.isempty(checker):
                    movemade = True
                    self.make_move(checker, board)
                    break
                else:
                    movemade = False
            if movemade:
                break
            
            # checks if there is any moves that can block an opponents winning combo
            for comb in winning_combos:
                checker = check_block(comb)
                if checker != 1 and board.isempty(checker):
                    movemade = True
                    self.make_move(checker, board)
                    break
                else:
                    movemade = False
            if movemade:
                break

            # checks for conditions that allow opponent or player to make a fork. for can be blocked or created by playing the middle space (B2)
            if board.isempty('B2'):
                if current_board['A1'] == current_board['A3'] != ' ' or current_board['A3'] == current_board['C3'] != ' ' or current_board['C1'] == current_board['C3'] != ' ' or current_board['A1'] == current_board['C1'] != ' ':
                    self.make_move('B2', board)
                    break
            
            # if opponent has control of oposing corners, plays a side space if possible
            elif not board.isempty('B2') and current_board['A1'] == current_board['C3'] == other or current_board['A3'] == current_board['C1'] == other:
                for move in ['A2','B3','C2','B1']:
                    if board.isempty(move):
                        self.make_move(move, board)
                        movemade = True
                        break
                    else:
                        movemade = False
                if movemade:
                    break

            # plays opposing corner from opponent
            if current_board['A1'] == other and board.isempty('C3'):
                self.make_move('C3', board)
                break
            elif current_board['A3'] == other and board.isempty('C1'):
                self.make_move('C1', board)
                break
            elif current_board['C3'] == other and board.isempty('A1'):
                self.make_move('A1', board)
                break
            elif current_board['C1'] == other and board.isempty('A3'):
                self.make_move('A3', board)
                break
            
            # if no other move is chosen, cycles through this list of moves and tries to play them
            starter_moves = ['A1','C1','C3','A3','A2','C2','B1','B3','B2']
            for move in starter_moves:
                if board.isempty(move):
                    movemade = True
                    self.make_move(move, board)
                    break
                else:
                    movemade = False
            if movemade == True:
                break



# MiniMax Player
class MiniMax(AI):

    # chooses a move
    def choose(self, board):
        maxscore = -10000

        # determines other players sign
        if self.sign =='X':
            self.other = 'O'
        else:
            self.other = 'X'

        # prompt for move
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")

        # iterates through all possible moves
        for move in self.moves:

            # if the move is available, plays the move and evaluates its score ((certain) win: 1, (potential for) tie: 0, (potential for) loss: -1) with MiniMax
            if board.isempty(move):
                board.set(move, self.sign)
                movescore = MiniMax.minimax(self, board, False)
                # undoes previous move so that the rest of the moves can be evaluated
                board.set(move, ' ')
                # if the move has a better score than previous, plays that move.
                if movescore > maxscore:
                    maxscore = movescore
                    best_move = move
        print(best_move)
        # plays the best move
        board.set(best_move, self.sign)

        #clears out false wins created by minimax
        board.winner = ' '
        

    def minimax(self, board, self_player):
        self.player = self_player
        # check the base conditions
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
            # is a tie
            elif board.get_winner() == ' ':
                return 0
            # self is a looser (opponent is a winner)
            else:
                return -1
        moves = self.moves
        
        # if it is minimaxes turn, returns the max score, else returns the min score.
        # this is becasuse minimax assumes both opponents play optimally and assign a score based on the result of optimal players
        score = []
        if self.player:
            # iterates through moves, plays the move, scores each move minimax, returns highest score
            for move in moves:
                if board.isempty(move):
                    board.set(move, self.sign)
                    score.append(MiniMax.minimax(self, board, not self_player))
                    board.set(move, ' ')
            return max(score)
        else:
            # iterates through moves, plays the move, scores each move with minimax, returns lowest score
            for move in moves:
                if board.isempty(move):
                    board.set(move, self.other)
                    score.append(MiniMax.minimax(self, board, not self_player))
                    board.set(move, ' ')
            return min(score)

        # essentially plays every possible game recursivly 
        # board states create new board states that branch into every possible move until end conditions are found
        # returns high score when end condition ends only in a win
        # else returns tie or loss if the move has potential to be a losing move
                    
        
        
     
        
