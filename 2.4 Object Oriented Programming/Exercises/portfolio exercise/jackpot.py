#class for player
# attributes(name, nationality, score)
# method: roll game(set a random number)
from random import random
class Player:

    def __init__(self, name, nationalit, score=0, value=0, turn=0):
        self.name = name
        self.country = nationality
        self.score = score
        self.value = value
        self.turn = turn

    def guess(self, value):
        self.value = value

    def __repr__(self):
        return '{} from {} has {}.'.format(self.name, self.country, self.score)


class Game:

    def __init__(self, value=0, round=1, max_round=1):
        self.value=value
        self.round=round
        self.max_round=max_round

    def roll(self):
        if self.round <= max_round:
            self.value = random.randint(1,100)
            self.round += 1
            print('Game Start. Pick a number from 1 to 100')
        else:
            print('The game is over.')

    def compare(self, player):
        try:
            assert type(player.value) == int, 'You need to put an integer'
        except AssertionError as error:
            raise

        if player.turn <= 3:

            player.turn += 1
            if self.value < player.guess:
                print('No. Try lower value.')
            elif self.value > player.guess:
                print('No. Try bigger value.')
            else:
                player.score += 1
                print('Binggo! How did you know?')
        else:
            player.turn = 0
            print('You finished 3 chances. No more chance for you.')

class StartGame:
    def __init__(self):
        print('First Player \n')
        name1 = input("What's your name? ")
        country1 = input("Where are you from? ")
        self.player1 = Player(name1, country1)

        print('Second Player \n')
        name2 = input("What's your name? ")
        country2 = input("Where are you from? ")
        self.player2 = Player(name2, country2)

        print('How many rounds you want to play?\n')
        rounds = input()
        try:
            assert rounds.isdigit(), 'You need to put an integer'
        except AssertionError as error:
            raise

        self.game = Game(max_round=int(rounds))

    def check_scores(self):
        if self.player1.score > self.player2.score:
            return 'The winner is: {}'.format(self.player1)
        elif self.player1.score < self.player2.score:
            return 'The winner is: {}'.format(self.player2)
        else:
            return 'Tie. No winners.'

    def play(self):
        self.game.roll()

        self.player1.guess()















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
