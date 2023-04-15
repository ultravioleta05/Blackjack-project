import random
### The deck ###


suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[self.rank]

    def __str__(self):
        f'{self.rank} of {self.suit}'
     
class Deck:
    def __init__(self):
        self.deck = [Card(rank, suit) for rank in ranks for suit in suits]
        
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, player):
        dealt_card = self.deck.pop()
        player.cards.append(dealt_card)
        player.score.append(dealt_card)
        if dealt_card.rank == 'ace':
            player.aces += 1



class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.aces = 0
    
    def add_card(self, card): # card arg is the dealt_card from deck.deal
        self.cards.append(card)
        self.score += card.value







# actions #
def hit_or_stand():
    playing = True
    while playing:
        move = input('type h for hit, s for stand')
        if move == 'h':
            return hit()
        if move == 's':
            pass

def hit(deck, hand):
    new_card = deck.deal
    hand.add_card(new_card)
    


# the game #

def play_blackjack(player):
    while True:
        deck = Deck()
        dealer_hand = Hand()
        player_hand = Hand()

        # cards are shuffled and dealt
        deck.shuffle()
        deck.deal(dealer_hand)
        deck.deal(dealer_hand)
        deck.deal(player_hand)
        deck.deal(player_hand)
        
        # the player is asked if they want to hit or stand
            hit_or_stand()



# dealer deals two cards to each player and two to themself
# first players turn starts, is asked to hit or stand
# 


# each turn:
#   - player hits or stands
#   - if they hit, change their score. If over 21, they bust. If under 21, nothing happens. If they stand, do nothing
