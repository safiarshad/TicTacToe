import math 
import random 

class Player:
    def __init__(self, letter):
        # letter is 'x' or 'o'
        self.letter = letter
        
        #getting the next moves in the game as a player
        def get_move(self, game):
            pass

         
#we are going to use inheritence to create a random computer player
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        #we have to initialise a super class

        super().__init__(letter)
        #the line above calls the init in the super class whic is "Player"

    def get_move(self, game):
        return random.choice(game.avaibalbe_moves())
                      


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #We want the human to have the ability of choosing a spot based on some Input thro terminal
        valid_square = False
        val = None # bcz the user hasn't put an input yet
        while not valid_square: #simply saying while valid square is false
            square = input(self.letter + "\'s turn. Input move (0-9): ")

            """
            We are goin to check that this input is a correct value by converting it to an int
            (or we say ivalid if that's not the case).
            The return would also be invalid if the spot on the board is already taken.

            """
            try:
                val = int(square)
                if val not in game.avaibalbe_moves():
                    raise ValueError
                

