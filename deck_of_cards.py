"""Create a deck of cards"""


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class DeckOfCards(object):
    def __init__(self):
        self.deck = []

