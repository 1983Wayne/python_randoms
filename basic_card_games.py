import random

### How many decks in a game deck, how big a starting hand is, and the game.
CRIBBAGE = [1, 7, 'Cribbage']
POKER = [1, 6, 'Poker']
BLACKJACK = [6, 2, 'BlackJack']
PLAYERS = {}

def get_game_to_play():
    game_wanted = int(input('CRIB, POKER, or 21? (1, 2, or 3) >  '))
    if game_wanted == 1:
        return CRIBBAGE
    elif game_wanted == 2:
        return POKER
    else:
        return BLACKJACK

class Deck:
    def __init__(self):
        self.cards_in_deck = []
        self.make_deck()
        self.shuffle_deck()
        
    def make_deck(self):
        for i in range(GAME[0]):
            for item in '1 2 3 4 5 6 7 8 9 10 Jack Queen King'.split():
                for j_item in 'spades hearts clubs diamonds'.split():
                    self.cards_in_deck.append('{} of {}'.format(item, j_item))
    
    def shuffle_deck(self):
        random.shuffle(self.cards_in_deck)
        
    def show_deck(self):
        for card in self.cards_in_deck:
            print(card)       
            
    def draw_card(self):
        return self.cards_in_deck.pop(random.randint(0, len(self.cards_in_deck) -1))
    
class Player:
    def __init__(self, starting_cards, deck, name):
        self.hand = []
        self.name = name
        
        for i in range(starting_cards):
            self.hand.append(deck.draw_card())
    
    def show_name(self):
        return self.name
    
    def show_hand(self):
        for i in self.hand:
            print(i)
                
    def draw_card(self, deck):
        self.hand.append(deck.draw_card())

def player_joins(name):
    PLAYERS[name] = Player(GAME[1], game_deck, name)

def player_quits(name):
    del PLAYERS[name]
    
def show_players():
    return PLAYERS

def get_hand(name):
    PLAYERS[name].show_hand()
    
GAME = get_game_to_play()
game_deck = Deck()
player_joins('Dealer')

