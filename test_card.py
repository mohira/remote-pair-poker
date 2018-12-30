from __future__ import annotations

import unittest
from enum import Enum, auto

from card import Card
from hand import Hand
from rank import Rank
from suit import Suit


class TestCard(unittest.TestCase):
    def test_Cardは文字列表記を持つ(self):
        with self.subTest("スペードの3の場合"):
            card = Card(Suit.spade, Rank.three)

            self.assertEqual("3S", str(card))

        with self.subTest("ハートのAの場合"):
            card = Card(Suit.heart, Rank.ace)

            self.assertEqual("AH", str(card))

    def test_Card同士は比較することができる(self):
        spade_3 = Card(Suit.spade, Rank.three)
        spade_A = Card(Suit.spade, Rank.ace)
        heart_3 = Card(Suit.heart, Rank.three)
        
        with self.subTest("Suitの比較_同一の場合"):
            self.assertTrue(spade_3.has_same_suit(spade_A))

        with self.subTest("Suitの比較_異なる場合"):
            self.assertFalse(spade_3.has_same_suit(heart_3))

        with self.subTest("Rankの比較_同一の場合"):
            self.assertTrue(spade_3.has_same_rank(heart_3))

        with self.subTest("Rankの比較_異なる場合"):
            self.assertFalse(spade_3.has_same_rank(spade_A))

if __name__ == "__main__":
    unittest.main()
