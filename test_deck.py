import unittest
from deck_of_cards import Card
from deck_of_cards import Deck


class TestDeck(unittest.TestCase):
    def test_make_card(self):
        expected = (9, 'diamonds')
        card = Card(*expected)
        actual = (card.rank, card.suit)
        self.assertEquals(expected, actual)

    def test_add_card_to_deck(self):
        card = Card(10, 'hearts')
        deck = Deck()
        deck.add(card)
        actual = deck.deck[-1]
        expected = card
        self.assertEquals(expected, actual)

    def test_make_standard_deck(self):
        deck = Deck()
        deck.make_deck()
        actual = []
        for card in deck.deck:
            actual.append((card.rank, card.suit))
        expected = [(2, 'hearts'),
                    (2, 'diamonds'),
                    (2, 'spades'),
                    (2, 'clubs'),
                    (3, 'hearts'),
                    (3, 'diamonds'),
                    (3, 'spades'),
                    (3, 'clubs'),
                    (4, 'hearts'),
                    (4, 'diamonds'),
                    (4, 'spades'),
                    (4, 'clubs'),
                    (5, 'hearts'),
                    (5, 'diamonds'),
                    (5, 'spades'),
                    (5, 'clubs'),
                    (6, 'hearts'),
                    (6, 'diamonds'),
                    (6, 'spades'),
                    (6, 'clubs'),
                    (7, 'hearts'),
                    (7, 'diamonds'),
                    (7, 'spades'),
                    (7, 'clubs'),
                    (8, 'hearts'),
                    (8, 'diamonds'),
                    (8, 'spades'),
                    (8, 'clubs'),
                    (9, 'hearts'),
                    (9, 'diamonds'),
                    (9, 'spades'),
                    (9, 'clubs'),
                    (10, 'hearts'),
                    (10, 'diamonds'),
                    (10, 'spades'),
                    (10, 'clubs'),
                    ('J', 'hearts'),
                    ('J', 'diamonds'),
                    ('J', 'spades'),
                    ('J', 'clubs'),
                    ('Q', 'hearts'),
                    ('Q', 'diamonds'),
                    ('Q', 'spades'),
                    ('Q', 'clubs'),
                    ('K', 'hearts'),
                    ('K', 'diamonds'),
                    ('K', 'spades'),
                    ('K', 'clubs'),
                    ('A', 'hearts'),
                    ('A', 'diamonds'),
                    ('A', 'spades'),
                    ('A', 'clubs')]
        self.assertEquals(actual, expected)

    def test_bad_rank(self):
        with self.assertRaises(ValueError) as context:
            Card(12, 'hearts')
        self.assertEqual(context.exception.message, "Card rank must be from \
2-10 or 'J', 'Q', 'K', 'A'")

    def test_bad_suit(self):
        with self.assertRaises(ValueError) as context:
            Card(2, 'HeArtZ')
        self.assertEqual(context.exception.message, "Card suit must be \
'hearts', 'diamonds', 'spades', or clubs'")

    def test_deck_initialize_as_52(self):
        deck = Deck()
        assert len(deck.deck) == 52
        actual = []
        for card in deck.deck:
            actual.append((card.rank, card.suit))
        expected = [(2, 'hearts'),
                    (2, 'diamonds'),
                    (2, 'spades'),
                    (2, 'clubs'),
                    (3, 'hearts'),
                    (3, 'diamonds'),
                    (3, 'spades'),
                    (3, 'clubs'),
                    (4, 'hearts'),
                    (4, 'diamonds'),
                    (4, 'spades'),
                    (4, 'clubs'),
                    (5, 'hearts'),
                    (5, 'diamonds'),
                    (5, 'spades'),
                    (5, 'clubs'),
                    (6, 'hearts'),
                    (6, 'diamonds'),
                    (6, 'spades'),
                    (6, 'clubs'),
                    (7, 'hearts'),
                    (7, 'diamonds'),
                    (7, 'spades'),
                    (7, 'clubs'),
                    (8, 'hearts'),
                    (8, 'diamonds'),
                    (8, 'spades'),
                    (8, 'clubs'),
                    (9, 'hearts'),
                    (9, 'diamonds'),
                    (9, 'spades'),
                    (9, 'clubs'),
                    (10, 'hearts'),
                    (10, 'diamonds'),
                    (10, 'spades'),
                    (10, 'clubs'),
                    ('J', 'hearts'),
                    ('J', 'diamonds'),
                    ('J', 'spades'),
                    ('J', 'clubs'),
                    ('Q', 'hearts'),
                    ('Q', 'diamonds'),
                    ('Q', 'spades'),
                    ('Q', 'clubs'),
                    ('K', 'hearts'),
                    ('K', 'diamonds'),
                    ('K', 'spades'),
                    ('K', 'clubs'),
                    ('A', 'hearts'),
                    ('A', 'diamonds'),
                    ('A', 'spades'),
                    ('A', 'clubs')]
        self.assertEquals(actual, expected)
