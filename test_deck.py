import unittest
from deck_of_cards import Card


class TestDeck(unittest.TestCase):
    def test_make_card(self):
        expected = ('9', 'diamonds')
        card = Card(*expected)
        actual = (card.rank, card.suit)
        self.assertEquals(expected, actual)
