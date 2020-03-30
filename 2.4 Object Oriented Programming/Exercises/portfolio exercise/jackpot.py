#class for player
# attributes(name, nationality, score)
# method: roll game(set a random number)
from random import random
class Player:

    def __init__(self, name, nationalit, score=0, value=0):
        self.name = name
        self.country = nationality
        self.score = score
        self.value = value

    def guess(self, value):
        self.value = value

class Game:

    def __init__(self, value=0, round=1, max_round=1):
        self.value=value
        self.round=round
        self.max_round=max_round

    def roll(self):
        if self.round <= max_round:
            self.value = random.randint(1,100)
            print('Game Start. Pick a number from 1 to 100')
        else:
            print('The game is over.')


    def compare(self, player):
        try:
            assert type(player.value) == int, 'You need to put an integer'
        except AssertionError as error:
            raise

        if self.value < player.guess:
            print('No. Try lower value.')
        elif self.value > player.guess:
            print('No. Try bigger value.')
        else:
            print('Binggo! How did you know?')




#class for game
# attribute: value
# method: record score, announce score

##five rounds: player can define rounds
##make a random number beteen 1-100
##player a guess
##player b guess
  ##each player has 3 chances to guess
  ##each round player a and b take turn to guess
  ##if no one guess it right, abore the game, no one gain points, move to next round

##calculate points at the end of the 5th rounds
##announce winner
