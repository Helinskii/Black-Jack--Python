import random
import sys

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
        return (f'{self.rank} of {self.suit}')

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
        for card in self.cards:
            self.value += values[card.rank]
            if card.rank == 'Ace':
                self.aces += 1

    def adjust_for_ace(self):
        if self.aces != 0:
            for _ in range(0, self.aces):
                self.value -= 10

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += 2 * self.bet

    def lose_bet(self):
        self.total -= self.bet

# Functions

# Function to take a bet
def take_bet(player_chips):
    while True:
        try:
            bet = int(input('Enter bet amount: '))
            if bet > player_chips.total:
                print(f'Amount greater than available amount.\nYou have = ${player_chips.total}\n')
                continue
        except:
            print('That is not a valid amount.\n')
            continue
        else:
            print(f'Bet amount entered = ${bet}\n')
            player_chips.bet = bet
            break

def hit(deck, hand):
    new_card = deck.deal()
    hand.add_card(new_card)
    if hand.value > 21:
        hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    answer = ''
    while answer.lower() not in ('hit', 'stand'):
        answer = input("Do you want to 'Hit' or 'Stand': ")
        if answer.lower() == 'hit':
            hit(deck, hand)
        elif answer.lower() == 'stand':
            playing = False
        else:
            print('Invalid option. (Hit / Stand)\n')

def show_some(player, dealer):
    print("Player's Hand: ")
    for cards in player.cards:
        print(cards)
    print('\n')

    print("Dealer's Hand: ")
    print("First card hidden.")
    for i in range(1, len(dealer.cards)):
        print(dealer.cards[i])
    print('\n')

def show_all(player, dealer):
    print("Player's Hand: \n")
    for cards in player.cards:
        print(cards)
    print(f"Player's total: {player.value}")
    print("Dealer's Hand: \n")
    for cards in dealer.cards:
        print(cards)
    print(f"Dealer's total: {dealer.value}")

def player_busts():
    pass

def player_wins():
    pass

def dealer_busts():
    pass

def dealer_wins():
    pass

def push():
    pass


if __name__ == '__main__':
    # Print an opening statement
    print('Welcome to the game of Black Jack!')

    # Input name
    name = input('Enter your name: ')

    # Print general instructions
    print(f'\nWell {name}, you will be starting with $100. We hope you know the rules to Black Jack.\nEnjoy the game!\n')

    # Create & shuffle the deck
    deck = Deck()
    deck.shuffle()

    # Create 'hands' for the player and the dealer
    player = Hand()
    dealer = Hand()

    # Deal two cards to each player
    for _ in range(2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())

    print(player.cards[0].rank)
    print(str(player.value) + '\n' + str(player.aces) + '\n')
    print(str(dealer.value) + '\n' + str(dealer.value) + '\n')
    sys.exit(0)

    # Initialize player's chips
    player_chips = Chips()

    # Prompt the player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
