"""Create a deck of cards"""


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class Deck(object):
    def __init__(self):
        self.deck = []

    def add(self, card):
        self.deck.append(card)

    def make_deck(self):
        ranks = range(2, 11) + ['J', 'Q', 'K', 'A']
        suits = ['hearts', 'diamonds', 'spades', 'clubs']
        for rank in ranks:
                for suit in suits:
                    self.add(Card(rank, suit))
