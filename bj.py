import random
playing = True
dealer_playing = False
suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}

class Card:
        def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit
            self.value = values[self.rank]

        def __str__(self):
            return f'{self.rank} of {self.suit}'
        
        def __repr__(self):
            return f'{self.rank} of {self.suit}'
        
class Deck:
    def __init__(self):
        self.deck = [Card(rank, suit) for rank in ranks for suit in suits]
        
    def __str__(self):
        pass
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self): ## whenever a new card is needed
        dealt_card = self.deck.pop()
        return dealt_card
    
class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.aces = 0
        self.is_playing = False
        self.busted = False
        self.stood = False
        self.blackjacked = False

    def __str__(self):
        pass

    def recieve_card(self, card):
        self.cards.append(card)
        self.score += card.value
        if card.rank == 'ace':
            self.aces += 1
        print('')


## actions / states ##

def hit(hand, deck):
    newcard = deck.deal()
    hand.recieve_card(newcard)
    print(f'{hand.name} recieved a {str(newcard)}')
    print(f"{hand.name}'s score is now {hand.score}")

def bust(hand, deck):
    playing = False

def prompt(player, dealer, deck):
    global playing
    print(f'You have {player.score}. Dealer has {dealer.score}.')
    ask = input('Would you like to hit or stand? H for hit, S for stand.')
    if ask.upper() == 'H':
        hit(player, deck)
    elif ask.upper() == 'S':
        playing = False

def dealer_turn(hand, deck):
    if hand.score == 21:
        print('Dealer hit a blackjack!')
    while hand.score < 17:
        hit(hand, deck)
    

def win(winner, loser):
    print(f"Final Score: {winner.score} to {loser.score}.")
    print(f'{winner.name} wins!')

def play():
    global playing
    playing = True
    deck = Deck()
    player = Hand()
    dealer = Hand()
    player.name = 'player'
    dealer.name = 'dealer'

    deck.shuffle()
    player.recieve_card(deck.deal())
    player.recieve_card(deck.deal())

    dealer.recieve_card(deck.deal())
    print('Your turn')

    if player.score == 21:
        playing = False
    while playing:
        prompt(player, dealer, deck)
        if player.score > 21:
            print('Player busted!')
            playing = False  
        if player.score == 21:
            print('Player hit a blackjack!')
            playing = False
    

    dealer.recieve_card(deck.deal())
    if player.score <= 21:
        dealer_turn(dealer, deck)
    if player.score > 21:
        win(dealer, player)
    elif dealer.score > 21:
        print('Dealer busted!')
        win(player, dealer)
    elif player.score > dealer.score:
        win(player, dealer)
    elif player.score < dealer.score:
        win(dealer, player)
    elif player.score == dealer.score:
        print('Tied!')
    
play()    
while True:
    again = input('Do you want to play again? y/n:')
    if again == 'y':
        play()
    else:
        break