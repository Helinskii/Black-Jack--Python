import random

# Representation of Cards
# Suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
# Ranks
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')
# Values assigned to each card
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
          'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
# Boolean to control the flow of the game
playing = True

# Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (f'{self.rank} of {self.suit}\n')

# Deck class
class Deck:
    def __init__(self):
        self.deck = [] # Start with an empty list
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.deck.append(new_card)

    def __str__(self):
        for cards in self.deck:
            print(cards.suit + ' - ' + cards.rank)
        return 'Done'

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop() # Not sure about this function

# Hand class
class Hand:
    def __init__(self):
        self.cards = [] # start with an empty list
        self.value = 0 # start with a zero value
        self.aces = 0 # to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        for card in cards:
            self.value += values[card.rank]
            if card.rank == 'Ace':
                self.aces += 1

    def adjust_for_ace(self):
        pass

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        pass

    def lose_bet(self):
        pass
