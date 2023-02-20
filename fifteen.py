from random import choice
from graph import Vertex, Graph
class Fifteen:

    # create a vector (ndarray) of tiles and the layout of tiles positions (a graph)
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size=4): 
        self.tiles = [i for i in range(1,size**2)] + [0]# change to list
        self.adj = [[1,4],[0,2,5],[1,6,3],[2,7],[0,5,8],[4,1,6,9],[5,2,7,10],[3,6,11],[4,9,12],[5,8,13,10],[6,9,11,14],[7,10,15],[8,13],[12,9,14],[13,10,15],[14,11]]

    # draw the layout with tiles
    def draw(self):
        tiles = '|'
        for tile in self.tiles:
            tile = str(tile)
            if tile == '0':
                tile = ' '
            if len(tile)==1:
                spacer = ' '
            else:
                spacer = ''
            tiles += spacer + tile + ' |' 
        print('+---+---+---+---+')
        print(tiles[:17])
        print('+---+---+---+---+')
        print(tiles[16:33])
        print('+---+---+---+---+')
        print(tiles[32:49])
        print('+---+---+---+---+')
        print(tiles[48:71])
        print('+---+---+---+---+')
        

    # return a string representation of the vector of tiles as a 2d array
    def __str__(self): 
        string = ""
        spacer = ''
        count = 0
        for i in self.tiles:
            count += 1
            i = str(i)
            if i == '0':
                i = ' '
            if len(i)==1:
                spacer = ' '
            else:
                spacer = ''
            if count == 4:
                newline = '\n'
                count = 0
            else:
                newline = ''
            string += spacer+i+' '+newline
        return string

    # exchanges tiles
    def transpose(self, i, j): #internal func, i and j are indexes
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]

    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor 
    def is_valid_move(self, move): #move is a tile value
        move_index = self.get_index(move)
        #check adjacent to see if there is a zero
        adj = self.adj[move_index]
        for i in adj:
            if 0 == self.tiles[i]:
                return True
        return False

    # returns index in the list for a specific tile
    def get_index(self, move):
        for moves in self.tiles:
            if move == self.tiles[moves]:
                return moves
                

    # update the vector of tiles
    # if the move is valid assign the vector to the return of transpose() or call transpose 
    def update(self, move): 
        if self.is_valid_move(move):
            i = self.get_index(move)
            j = self.get_index(0)
            self.transpose(i,j)
    
    # make a move by index rather than tile value, easier for graphical implementation
    def index_update(self, index):
        self.update(self.tiles[index])
    
    # shuffle tiles
    def shuffle(self, moves = 100):
        for i in range(moves):
            valid_moves = self.adj[self.get_index(0)]
            move = self.tiles[choice(valid_moves)]
            self.update(move)
        
    
    # verify if the puzzle is solved
    def is_solved(self):
        if str(self) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n':
            return True
        return False

    # verify if the puzzle is solvable (optional)
    def is_solvable(self):
        pass
        # Ran out of time. Please let me know If I can have an extension to finish this!

    # solve the puzzle
    def solve(self):
        pass
        # Ran out of time. Please let me know If I can have an extension to finish this!

if __name__ == '__main__':
    # terminal version of the game
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    '''
    game = Fifteen()    
    game.draw()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    game.solve()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    '''

    
    
    
