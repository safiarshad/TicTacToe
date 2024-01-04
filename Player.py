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
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass