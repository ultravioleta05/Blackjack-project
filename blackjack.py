import random
### The deck ###


suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        f'{self.rank} of {self.suit}'
     
class Deck:
    def __init__(self):
        self.deck = [Card(rank, suit) for rank in ranks for suit in suits]
        




### The game ###

class Player:
    def __init__(self):
        self.score = 0

    def hit_or_stand(self):
        move = input('hit or stand?')

    def hit(self):
        pass

    def stand(self):
        pass



        
class Dealer:
    def __init__(self, deck):
        self.deck = deck
        self.cards = []

    def initial_deal(self, player):
        # take two random cards out of the deck, add values, add to players score. Discard cards. Repeat for self
        pass

    def shuffle(self):
        random.shuffle(self.deck)



# the game #

def play_blackjack(player):
    while True:
        deck = Deck()
        dealer = Dealer(deck)
        player = Player()

        dealer.deal()

        player.hit_or_stand()
        # hit or stand?


# dealer deals two cards to each player and two to themself
# first players turn starts, is asked to hit or stand
# 


# each turn:
#   - player hits or stands
#   - if they hit, change their score. If over 21, they bust. If under 21, nothing happens. If they stand, do nothing
