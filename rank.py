from __future__ import annotations
from enum import Enum, auto

class Rank(Enum):        
    ace   = dict(numeric=1,  notation="A")
    two   = dict(numeric=2,  notation="2")
    three = dict(numeric=3,  notation="3")
    four  = dict(numeric=4,  notation="4")
    five  = dict(numeric=5,  notation="5")
    six   = dict(numeric=6,  notation="6")
    seven = dict(numeric=7,  notation="7")
    eight = dict(numeric=8,  notation="8")
    nine  = dict(numeric=9,  notation="9")
    ten   = dict(numeric=10, notation="10")
    jack  = dict(numeric=11, notation="J")
    queen = dict(numeric=12, notation="Q")
    king  = dict(numeric=13, notation="K")


    def is_next_of(self, other: Rank) -> bool:
        if self == Rank.ace and other == Rank.king:
            return True
        return self.value["numeric"] == other.value["numeric"] + 1

    def is_prev_of(self, other: Rank) -> bool:
        if self == Rank.king and other == Rank.ace:
            return True
        return self.value["numeric"] == other.value["numeric"] - 1
# 両隣を見る
# sort して card1の右隣を見る
# Rank.連続?(card1, card2)
# rank.連続?(other_rank)
#def is_連続(self, other: Rank):
#    return self.next == other or self.prev == other
