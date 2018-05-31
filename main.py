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
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

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
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    answer = ''
    while answer.lower() not in ('hit', 'stand'):
        answer = input("Do you want to 'Hit' or 'Stand'? [Hit/Stand]: ")
        if answer.lower() == 'hit':
            hit(deck, hand)
        elif answer.lower() == 'stand':
            print('Player stands. Dealer is playing.\n')
            playing = False
        else:
            print('Invalid option. (Hit / Stand)\n')
    print('\n')

def show_some(player, dealer):
    print("Player's Hand: ")
    for cards in player.cards:
        print(cards)
    print('\n')

    print("Dealer's Hand: ")
    print("<card hidden>")
    for i in range(1, len(dealer.cards)):
        print(dealer.cards[i])
    print('\n')

def show_all(player, dealer):
    print("Player's Hand: ")
    for cards in player.cards:
        print(cards)
    print('\n')
    print(f"Player's total: {player.value}\n")

    print("Dealer's Hand: ")
    for cards in dealer.cards:
        print(cards)
    print('\n')
    print(f"Dealer's total: {dealer.value}\n")

def player_busts(chips):
    print('You have exceeded 21. You lose!\n')
    chips.lose_bet()
    player_bust = True

def player_wins(chips):
    print('You have a higher sum. You win!\n')
    chips.win_bet()

def dealer_busts(chips):
    print('Dealer has exceeded 21. You win!\n')
    chips.win_bet()

def dealer_wins(chips):
    print('Dealer has a higher sum. You lose!\n')
    chips.lose_bet()

def push():
    print("Dealer and Player tie. It's a push.\n")

if __name__ == '__main__':

    # Print an opening statement
    print('Welcome to the game of Black Jack!')

    # Input name
    name = input('Enter your name: ')

    # Print general instructions
    print(f'\nHello {name}!\nYou will be starting with $100. We hope you know the rules to Black Jack.\nEnjoy the game!\n')

    # Initialize player's chips
    player_chips = Chips()

    while True:
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

        # Prompt the player for their bet
        take_bet(player_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        while playing:
            # Prompt for player to hit or stand
            hit_or_stand(deck, player)
            # Show cards
            show_some(player, dealer)
            # If the player busts
            if player.value > 21:
                player_busts(player_chips)
                break

        # If player hasn't bust
        if player.value <= 21:
            # Play dealer's hand until dealer reaches 17
            while dealer.value < 17:
                dealer.add_card(deck.deal())

            # Show all cards as the hand is over
            show_all(player, dealer)

            # Run all scenarios
            if dealer.value > 21:
                dealer_busts(player_chips)

            elif dealer.value > player.value:
                dealer_wins(player_chips)

            elif dealer.value < player.value:
                player_wins(player_chips)

            else:
                # In case the player and the dealer have the same sum
                push()

        # Inform the player of his/her current standings
        print(f'Your current winnings are: {player_chips.total}\n')

        # If the player has '0' funds, exit game
        if player_chips.total == 0:
            print('You have no funds left. Thanks for playing!')
            break

        # Ask if the player wants to play again
        answer = '#'
        play_game = False
        while answer[0].lower() not in ('y', 'n'):
            answer = input('Do you want to play again? [Y/N]: ')
            if answer[0].lower() == 'y':
                play_game = True
            elif answer[0].lower() == 'n':
                play_game = False
            else:
                print('Invalid Entry. [Y/N]\n')

        if play_game:
            playing = True
            continue
        else:
            print('Thanks for playing.\n')
            break
