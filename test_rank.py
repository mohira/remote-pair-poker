from __future__ import annotations

import unittest
from enum import Enum, auto

from rank import Rank


class TestRank(unittest.TestCase):
    def test_次のRankかどうかを判定できる(self):
        with self.subTest("4 は 3 の次のRankである"):
            self.assertTrue(Rank.four.is_next_of(Rank.three))
            
        with self.subTest("2 は A の次のRankである"):
            self.assertTrue(Rank.two.is_next_of(Rank.ace))
            
        with self.subTest("A は K の次のRankである"):
            self.assertTrue(Rank.ace.is_next_of(Rank.king))

    def test_前のRankかどうかを判定できる(self):
        with self.subTest("3 は 4 の前のRankである"):
            self.assertTrue(Rank.three.is_prev_of(Rank.four))
            
        with self.subTest("A は 2 の前のRankである"):
            self.assertTrue(Rank.ace.is_prev_of(Rank.two))
            
        with self.subTest("K は A の前のRankである"):
            self.assertTrue(Rank.king.is_prev_of(Rank.ace))
            

if __name__ == "__main__":
    unittest.main()
