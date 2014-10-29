import unittest
from deck_of_cards import Card
from deck_of_cards import Deck


class TestDeck(unittest.TestCase):
    def test_make_card(self):
        expected = ('9', 'diamonds')
        card = Card(*expected)
        actual = (card.rank, card.suit)
        self.assertEquals(expected, actual)

    def test_add_card_to_deck(self):
        card = Card('10', 'hearts')
        deck = Deck()
        deck.add(card)
        actual = deck.deck
        expected = [card]
        self.assertEquals(expected, actual)
