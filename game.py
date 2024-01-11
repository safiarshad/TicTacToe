from Player import HumanPlayer, RandomComputerPlayer, Player

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #this list is used to represent a 3x3 board 
        self.current_winner = None #keeps tack of the winner (in this we dont have yet so 'None')

    def print_board(self):
        #we gonna divid the list into rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: #this allows us to choose the rows like which three spaces you wanna take
            print(' |' + ' |'.join(row) + ' |')                     #first, second or last

    @staticmethod #it doesn't relate to any spicific board that's why it's static and we don't need to pass in 'self'
    def print_board_nums():
        # 0 | 1 | 2 etc (the corresponding numbers to the boxes)
        number_board = [[str(i) for i in range (j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(' |' + ' |'.join(row) + ' |')     

    def avaibalbe_moves(self):
        #returns a [] of remaining moves or boxes
        moves = []
        for (i, spot) in enumerate(self.board):  #the enumrate in here enumrtes the indexes using tuple to represent the value in the box
            # ['x', 'x', 'o']  --> [(0, 'x'), (1, 'x'), (2, 'o')]
            if spot == ' ':
                moves.append(i)
                
        return moves
        #or the below line instead of the multiple line 
        #return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_square(self):
        return len.avaibalbe_moves
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] == letter
            if self.winner(square, letter):
                self.current_winner = letter

            return True
        return False
        
    def winner(self, square, letter):
        #if 3 in a row anywhere, then winner!
        #checking the row:
        row_index = square // 3 
        row = self.board[row_index*3 : (row_index + 1) *3]
        if all([spot == letter for spot in row]):
            return True
        
        #check the column for winner
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #checking diagnaly
        #if the square is an even num that's the only way to win diagonally (0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            digonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in digonal2]):
                return True
            
        #if all fail no winner
        return False
                
    def play(game, x_Player, o_Player, print_game=True):
       
        if print_game:
            game.print_board_nums()

        letter = 'X' #Staring 
        """
        While there're empty squares in the game this should keep iterating.
        (The winner would be returned which will break the loop).
        """
        while game.empty_squares():
            #getting the move from the right player
            if letter == 'O':
                square =  o_Player.get_move(game)
            else:
                square = x_Player.get_move(game)

            if game.make_move(square, letter):
                if print_game:
                    print(letter + f"makes a move to square {square}")
                    game.print_board()
                    print('')#an empty line 

                if game.current_winner:
                    if print_game:
                        print(letter + " wins!")
                    return letter


                #after the first move, the letters should be alternate
                letter = 'O' if letter =='X' else 'X'

            if print_game:
                print("it\'s a tie!")
        

if __name__ == '__main__':
    x_Player = HumanPlayer('X')
    o_Player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_Player, o_Player, print_game=True)




            


    




