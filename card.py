from __future__ import annotations

from rank import Rank
from suit import Suit

class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def has_same_suit(self, other: Card) -> bool:
        return self.suit == other.suit
    
    def has_same_rank(self, other: Card) -> bool:
        return self.rank == other.rank

    def __str__(self) -> str:
        return f"{self.rank.value['notation']}{self.suit.value}"
