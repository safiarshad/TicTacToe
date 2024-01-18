import math 
import random
from typing import Self 

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
                valid_square = True
            except ValueError:
                print("Invalid suqare, Try again!")

        return val


class GeniusComPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.avaibalbe_moves()) == 9:
            square = random.choice(game.avaibalbe_moves()) #Choosing Random Square
        else:
            #get the square based on minimax algorithm
            square = self.minimax(game, self.letter)["Position"]

        return square

    def minimax(self, state, player):  #state is the state of the game, where are we at the game
        max_player = self.letter #the Player (you)
        other_player = 'O' if player == 'X' else 'X'

        #to being with, was the previous move a winner? 
        if state.current_winner == other_player:
            #it is best to return both position and score for our algorithm (minimax) to work
            return {"Position" : None,
                    "score" : 1 * (state.num_empty_square() + 1) if other_player == max_player else -1 * (
                        state.nu + 1)
                        }
        elif not state.empty_squares(): #no empty square
            return {"Position" : None,
                    "score" : 0 }
        
        if player == max_player:
            best = {"Position": None, "Score": -math.inf } #each score should maximise
            #the dic stores the "best" available moves to win
        else:
            best = {"Position": None, "Score": math.inf } #each score should minimise

        for possible_move in state.avaibalbe_moves():

            #a) make a move, and try that spot
            state.make_move(possible_move, player)

            #b) recurse using minimax to simulate a game after making that move

            #c) unde the move


            #d) update the the dicts if needed









    




