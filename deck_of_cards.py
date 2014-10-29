"""Create a standard 52 card deck"""


class Card(object):
    def __init__(self, rank, suit):
        if rank not in range(2, 11) + ['J', 'Q', 'K', 'A']:
            raise ValueError("Card rank must be from 2-10 or \
'J', 'Q', 'K', 'A'")
        if suit not in ['hearts', 'diamonds', 'spades', 'clubs']:
            raise ValueError("Card suit must be 'hearts', 'diamonds', \
'spades', or clubs'")
        self.rank = rank
        self.suit = suit


class Deck(object):
    def __init__(self):
        self.deck = []
        self.make_deck()

    def add(self, card):
        """Add a card to the deck"""
        self.deck.append(card)

    def make_deck(self):
        """Create a new deck of 52 cards"""
        self.deck = []
        ranks = range(2, 11) + ['J', 'Q', 'K', 'A']
        suits = ['hearts', 'diamonds', 'spades', 'clubs']
        for rank in ranks:
                for suit in suits:
                    self.add(Card(rank, suit))
