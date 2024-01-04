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