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

