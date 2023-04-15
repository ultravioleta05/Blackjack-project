import random
### The deck ###


suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}

def the_game():
    game_over = False
    class Card:
        def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit
            self.value = values[self.rank]

        def __str__(self):
            f'{self.rank} of {self.suit}'
        
        def __repr__(self):
            f'{self.rank} of {self.suit}'
        
    class Deck:
        def __init__(self):
            self.deck = [Card(rank, suit) for rank in ranks for suit in suits]
            
        def shuffle(self):
            random.shuffle(self.deck)

        def deal(self, player):
            dealt_card = self.deck.pop()
            return dealt_card

    class Hand:
        def __init__(self):
            self.cards = []
            self.score = 0
            self.aces = 0
            self.is_playing = False
            self.stood = False
            self.busted = False
            self.blackjacked = False

        
        def hit(self, deck):
            self.add_card(deck)
            print('hit')
            print(f"{self.name}'s score is {self.score}")
            
        def stand(self):
            print('stand')
            print(f"{self.name}'s score is {self.score}")
            self.is_playing = False
            self.stood = True

        def blackjack(self):
            print(f"{self.name} hit a blackjack!")
            self.blackjacked = True
            self.is_playing = False
            self.win()

        def bust(self):
            print(f'{self.name} went bust!')
            self.is_playing = False
            self.busted = True
            game_over = True

        def player_play(self):
            move = input('type h for hit, s for stand: ')
            if move == 'h':
                self.hit(deck)
                if self.score > 21:
                    self.bust()
                if self.score == 21:
                    self.blackjack()
                if self.score < 21 and not self.stood: 
                    return self.player_play()
            if move == 's':
                self.stand()


        def dealer_play(self):
            if self.score > 21:
                self.bust()
            if self.score == 21:
                self.blackjack()
            if self.score >= 17 and self.score < 21:
                self.is_playing = False
            if self.score <= 16:
                self.hit(deck)
                self.dealer_play()

        def win(self):
            print(f"{self.name} won")
            game_over = True

        def add_card(self, deck):
            new_card = deck.deal(self)
            self.cards.append(new_card)
            self.score += new_card.value

    # the game #

    while not game_over:
        deck = Deck()
        dealer = Hand()
        player = Hand()
        player.name = 'player'
        dealer.name = 'dealer'
        # cards are shuffled and dealt
        deck.shuffle()
        dealer.add_card(deck)

        player.add_card(deck)
        player.add_card(deck)
        print(f"Your score is {player.score}. The dealer's score is {dealer.score}.")
        if player.score == 21:
            player.blackjack()
            break

        print("player's turn")
        player.is_playing = True
        player.player_play()
        if player.score < 21 and not player.stood:
            player.player_play()
        if player.score == 21:
            player.blackjack()
            game_over = True
            break
        if player.score > 21:
            player.bust()
            game_over = True
            break
        while player.is_playing and not player.stood:
            player.player_play()

        print("dealer's turn")
        deck.deal(dealer)
        dealer.dealer_play()
        game_over = True
        break


    if player.score > dealer.score and not dealer.blackjacked and not player.busted and not player.blackjacked or dealer.busted:
        player.win()
    else:
        dealer.win()

the_game()
again = input("Do you want to play again? y for yes, n for no.\
              ")
if again == 'y':
    the_game()
else:
    print('aight')