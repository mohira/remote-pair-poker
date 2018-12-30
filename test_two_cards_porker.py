from __future__ import annotations

import unittest
from enum import Enum, auto

from card import Card
from hand import Hand
from rank import Rank
from suit import Suit
from two_cards import TwoCards


class TestTwoCardsPoker(unittest.TestCase):
    def test_TwoCardsは役を持つ(self):
        spade_3 = Card(Suit.spade, Rank.three)
        spade_A = Card(Suit.spade, Rank.ace)
        heart_2 = Card(Suit.heart, Rank.two)
        heart_3 = Card(Suit.heart, Rank.three)
        heart_A = Card(Suit.heart, Rank.ace)

        with self.subTest("ペア"):
            cards = TwoCards([spade_3, heart_3])

            self.assertEqual(Hand.pair, cards.hand)

        with self.subTest("フラッシュ"):
            cards = TwoCards([spade_3, spade_A])

            self.assertEqual(Hand.flush, cards.hand)

        with self.subTest("ハイカード"):
            cards = TwoCards([spade_3, heart_A])

            self.assertEqual(Hand.high_card, cards.hand)

        with self.subTest("ストレート_シンプルなケース"):
            cards = TwoCards([spade_3, heart_2])
            self.assertEqual(Hand.straight, cards.hand)

if __name__ == "__main__":
    unittest.main()
